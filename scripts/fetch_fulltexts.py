"""Cache primary-source full texts locally and record acquisition evidence.

Downloading and text extraction do not mark a paper as read. Human/agent review
notes are maintained separately. Cached PDFs and extracted text are gitignored.
"""
import argparse
import concurrent.futures
import hashlib
import json
import re
import subprocess
import threading
import time
import urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / '.local/fulltexts'
MANIFEST = ROOT / 'data/fulltext-manifest.json'
LOCK = threading.Lock()
NEXT_HOST = {}


def request(url):
    host = urlsplit(url).hostname
    with LOCK:
        slot = max(time.monotonic(), NEXT_HOST.get(host, 0))
        NEXT_HOST[host] = slot + (3.2 if host == 'arxiv.org' else 1)
    time.sleep(max(0, slot - time.monotonic()))
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (compatible; ResearchBibliography/1.0)'})
    with urllib.request.urlopen(req, timeout=35) as response:
        body = response.read(70_000_001)
        if len(body) > 70_000_000:
            raise ValueError('Download exceeds 70 MB bound')
        return body, response.url, response.headers.get('Content-Type', '')


class Metadata(HTMLParser):
    def __init__(self):
        super().__init__()
        self.meta = {}
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'meta':
            name = attrs.get('name', attrs.get('property', '')).lower()
            if name and attrs.get('content'):
                self.meta.setdefault(name, []).append(attrs['content'])


def candidates(resource):
    urls = [link['url'] for link in resource['links']]
    found = []
    for url in urls:
        if re.search(r'\.pdf(?:$|\?)', url):
            found.append(url)
        match = re.search(r'arxiv.org/(?:abs|html|pdf)/(.+?)(?:\.pdf)?$', url)
        if match:
            found.append('https://arxiv.org/pdf/' + match[1])
        if 'proceedings.mlr.press/' in url and url.endswith('.html'):
            found.append(url[:-5] + '/' + url.rsplit('/', 1)[1][:-5] + '.pdf')
        if 'jmlr.org/papers/v15/peters14a.html' in url:
            found.append('https://jmlr.org/papers/volume15/peters14a/peters14a.pdf')
        if 'jmlr.org/papers/v21/17-123.html' in url:
            found.append('https://jmlr.org/papers/volume21/17-123/17-123.pdf')
        if any(host in url for host in ['proceedings.neurips.cc/', 'proceedings.iclr.cc/']) and '/hash/' in url:
            found.append(url.replace('/hash/', '/file/').replace('-Abstract', '-Paper').replace('.html', '.pdf'))
        if 'nature.com/articles/' in url and not url.endswith('.pdf'):
            found.append(url + '.pdf')
    return list(dict.fromkeys(found))


def acquire(resource, previous):
    rid = resource['id']
    pdf = CACHE / (rid + '.pdf')
    text = CACHE / (rid + '.txt')
    landing = CACHE / (rid + '.landing.html')
    record = dict(previous or {}, id=rid, title=resource['title'], checked_at=datetime.now(timezone.utc).isoformat(timespec='seconds'))
    errors = []
    if not pdf.exists():
        pinned = [record.get('version_url'), record.get('source_url')]
        for url in dict.fromkeys([url for url in pinned if url] + candidates(resource)):
            try:
                body, resolved, content_type = request(url)
                if not body.lstrip().startswith(b'%PDF-'):
                    raise ValueError('Response is not a PDF: ' + content_type)
                reader = PdfReader(__import__('io').BytesIO(body))
                if not reader.pages:
                    raise ValueError('PDF contains no pages')
                pdf.write_bytes(body)
                record.update(source_url=url, resolved_url=resolved)
                break
            except Exception as exc:
                errors.append({'url': url, 'error': type(exc).__name__ + ': ' + str(exc)[:250]})
    if pdf.exists():
        try:
            reader = PdfReader(pdf)
            if not text.exists():
                subprocess.run(['pdftotext', '-layout', '-enc', 'UTF-8', str(pdf), str(text)], check=True, capture_output=True)
            links = set()
            for page in reader.pages:
                for ref in page.get('/Annots', []):
                    annotation = ref.get_object()
                    action = annotation.get('/A', {})
                    if hasattr(action, 'get_object'):
                        action = action.get_object()
                    uri = action.get('/URI')
                    if uri and str(uri).startswith('http'):
                        links.add(str(uri))
            content = text.read_text(encoding='utf-8')
            version = re.search(r'arXiv:((?:[a-z-]+/)?[0-9.]+v[0-9]+)', content[:20000])
            if version:
                record.update(version_id=version[1], version_url='https://arxiv.org/pdf/' + version[1])
            record.update(status='fulltext-downloaded', pages=len(reader.pages), bytes=pdf.stat().st_size,
                          sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(), characters=len(content),
                          local_pdf=str(pdf.relative_to(ROOT)).replace('\\', '/'),
                          local_text=str(text.relative_to(ROOT)).replace('\\', '/'),
                          pdf_metadata={str(k):str(v) for k,v in (reader.metadata or {}).items()},
                          outbound_links=sorted(links))
        except Exception as exc:
            record.update(status='extraction-failed', error=str(exc))
    else:
        record['status'] = 'download-unavailable'
    primary = next(link['url'] for link in resource['links'] if link['label'] == 'Paper')
    match = re.search(r'arxiv.org/(?:html|abs|pdf)/(.+)', primary)
    landing_url = 'https://arxiv.org/abs/' + match[1] if match else primary
    if not primary.endswith('.pdf'):
        try:
            if not landing.exists():
                body, _, _ = request(landing_url)
                landing.write_bytes(body)
            parser = Metadata()
            parser.feed(landing.read_text(encoding='utf-8', errors='replace'))
            record['landing_metadata'] = parser.meta
            record['landing_url'] = landing_url
        except Exception as exc:
            errors.append({'url': landing_url, 'error': type(exc).__name__ + ': ' + str(exc)[:250]})
    record['acquisition_errors'] = errors
    # Keep extracted bibliography and outbound references in the local cache;
    # the tracked manifest contains acquisition evidence, not a paper-text dump.
    metadata_path = CACHE / (rid + '.metadata.json')
    metadata_path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
    for key in ['pdf_metadata', 'landing_metadata', 'outbound_links']:
        record.pop(key, None)
    print(json.dumps({'id':rid,'status':record['status'],'pages':record.get('pages'),'errors':len(errors)}), flush=True)
    return record


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ids', nargs='*')
    parser.add_argument('--workers', type=int, default=3)
    parser.add_argument('--catalog', default='data/resources.json')
    parser.add_argument('--manifest', default='data/fulltext-manifest.json')
    args = parser.parse_args()
    catalog_path = (ROOT / args.catalog).resolve()
    MANIFEST = (ROOT / args.manifest).resolve()
    if not catalog_path.is_relative_to(ROOT) or not MANIFEST.is_relative_to(ROOT):
        raise ValueError('Catalog and manifest must stay within the repository')
    CACHE.mkdir(parents=True, exist_ok=True)
    data = json.loads(catalog_path.read_text(encoding='utf-8'))
    old = json.loads(MANIFEST.read_text(encoding='utf-8')) if MANIFEST.exists() else {'papers': []}
    previous = {item['id']: item for item in old['papers']}
    selected = [item for item in data['resources'] if item['kind'] == 'paper' and (not args.ids or item['id'] in args.ids)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, min(args.workers, 4))) as pool:
        tasks = {pool.submit(acquire, item, previous.get(item['id'])):item['id'] for item in selected}
        for task in concurrent.futures.as_completed(tasks):
            record = task.result()
            previous[record['id']] = record
            report = {'scope': 'Acquisition and extraction evidence only; not a claim of reading or reproduction.',
                      'papers': [previous[item['id']] for item in data['resources'] if item['id'] in previous]}
            MANIFEST.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
