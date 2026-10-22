"""Cache first-page paper previews and first-party blog cover images for the news feed."""
import argparse
import hashlib
import io
import json
import re
import time
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit

from build_site import ROOT, canonical


class Metadata(HTMLParser):
    def __init__(self):
        super().__init__()
        self.image = ''

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'meta' and attrs.get('property', attrs.get('name')) == 'og:image':
            self.image = attrs.get('content', '')


def fetch(url, limit=25_000_000):
    import gzip
    req = urllib.request.Request(url, headers={'User-Agent': 'OWDResearchMonitor/1.0 (paper preview cache)', 'Accept-Encoding': 'identity'})
    with urllib.request.urlopen(req, timeout=40) as response:
        body = response.read(limit + 1)
        if len(body) > limit:
            raise ValueError('Media exceeds size bound')
        if body.startswith(b'\x1f\x8b'):
            with gzip.GzipFile(fileobj=io.BytesIO(body)) as decoded:
                body = decoded.read(limit + 1)
            if len(body) > limit:
                raise ValueError('Decoded media exceeds size bound')
        return body


def acquire(paper_cache=None):
    import fitz
    from PIL import Image
    path = ROOT / 'data/update-media.json'
    media = json.loads(path.read_text(encoding='utf-8')) if path.exists() else {}
    updates = json.loads((ROOT / 'data/updates.json').read_text(encoding='utf-8'))
    manifest = json.loads((ROOT / 'data/fulltext-manifest.json').read_text(encoding='utf-8'))['papers']
    cached = {canonical(row['landing_url']): ROOT / row['local_pdf'] for row in manifest if row.get('landing_url')}
    local = ROOT / '.local/news-media'
    local.mkdir(parents=True, exist_ok=True)
    assets = ROOT / 'assets/news'
    assets.mkdir(parents=True, exist_ok=True)
    errors = []
    added = 0
    for item in updates['items']:
        if item.get('review_status') != 'approved':
            continue
        url = canonical(item['url'])
        if url in media and (ROOT / media[url]['path']).exists() and (media[url].get('kind') == 'blog' or media[url].get('preview_version') == 3):
            continue
        host = urlsplit(url).hostname
        key = hashlib.sha256(url.encode()).hexdigest()[:16]
        output = assets / (key + '.webp')
        try:
            if host == 'arxiv.org':
                pdf_url = url.replace('/abs/', '/pdf/')
                candidates=[cached.get(url),Path(paper_cache)/key/'paper.pdf' if paper_cache else None]
                pdf=next((candidate for candidate in candidates if candidate and candidate.is_file()),local/(key+'.pdf'))
                if not pdf.exists():
                    pdf.write_bytes(fetch(pdf_url,limit=80_000_000))
                    time.sleep(3.2)
                with fitz.open(pdf) as doc:
                    page = doc[0]
                    clip = page.rect
                    page_number = 1
                    kind = 'paper'
                    for n in range(min(5, len(doc))):
                        candidate = doc[n]
                        captions = [block for block in candidate.get_text('blocks')
                                    if re.match(r'^\s*(?:Figure|Fig\.?)\s*1\b', block[4], flags=re.I)]
                        if not captions:
                            continue
                        caption = captions[0]
                        regions = [drawing['rect'] for drawing in candidate.get_drawings()]
                        for image_info in candidate.get_images(full=True):
                            regions.extend(candidate.get_image_rects(image_info[0]))
                        regions = [r for r in regions if r.get_area() > 8 and r.height > 5
                                   and r.get_area() < candidate.rect.get_area() * .75
                                   and max(25, caption[1] - 430) <= r.y0 and r.y1 <= caption[1] + 3
                                   and r.x0 >= caption[0] - 25 and r.x1 <= caption[2] + 25]
                        if not regions:
                            continue
                        bounds = fitz.Rect(regions[0])
                        for region in regions[1:]: bounds |= region
                        if bounds.width < 120 or bounds.height < 70:
                            continue
                        page = candidate
                        clip = fitz.Rect(bounds.x0 - 10, bounds.y0 - 10, bounds.x1 + 10, min(bounds.y1 + 10, caption[1])) & page.rect
                        page_number = n + 1
                        kind = 'figure'
                        break
                    pixmap = page.get_pixmap(matrix=fitz.Matrix(1000 / clip.width, 1000 / clip.width), clip=clip, alpha=False)
                    image = Image.frombytes('RGB', (pixmap.width, pixmap.height), pixmap.samples)
                    image.thumbnail((1000, 1000))
                    image.save(output, 'WEBP', quality=78)
                media[url] = {'path': output.relative_to(ROOT).as_posix(), 'kind': kind,
                              'alt': ('Figure 1 from ' if kind == 'figure' else 'First-page preview of ') + item['title'], 'source_url': pdf_url,
                              'pdf_page': page_number, 'pdf_clip': list(clip), 'preview_version': 3,
                              'credit': 'Original paper authors; figure or first-page preview with direct paper attribution.'}
            elif host in ('research.google', 'deepmind.google'):
                meta = Metadata()
                meta.feed(fetch(url).decode('utf-8', errors='replace'))
                image_url = urljoin(url, meta.image)
                image_host = urlsplit(image_url).hostname or ''
                if not meta.image or not (image_host.endswith(('.google', '.google.com', '.googleapis.com', '.gstatic.com', '.googleusercontent.com', '.googleblog.com')) or image_host == 'research.google'):
                    raise ValueError('No allowlisted first-party cover image')
                with Image.open(io.BytesIO(fetch(image_url))) as image:
                    image.thumbnail((900, 600))
                    image.convert('RGB').save(output, 'WEBP', quality=80)
                media[url] = {'path': output.relative_to(ROOT).as_posix(), 'kind': 'blog',
                              'alt': 'Publisher cover image for ' + item['title'], 'source_url': image_url,
                              'credit': 'Publisher cover image; attribution and article link appear on the card.'}
            else:
                continue
            added += 1
            print('Cached preview:', item['title'][:70], flush=True)
        except Exception as exc:
            errors.append({'url': url, 'error': str(exc)[:250]})
            print('Preview unavailable:', url, str(exc)[:100], flush=True)
    path.write_text(json.dumps(media, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
    (local / 'last-run.json').write_text(json.dumps({'added': added, 'cached': len(media), 'errors': errors}, indent=2), encoding='utf-8')
    print(f'{len(media)} previews available; {len(errors)} unavailable (source marks are used instead).')


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--paper-cache',type=Path,help='Optional local reviewed-PDF cache; PDFs are never copied into public assets.')
    acquire(parser.parse_args().paper_cache)
