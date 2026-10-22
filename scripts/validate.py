"""Validate catalog structure, usage-mode semantics, generated views and local links."""
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit,unquote
from build import ROOT,CATEGORIES,load,outputs

def require(ok,message):
    if not ok:
        raise ValueError(message)

data,bench=load()
resources=data['resources']
byid={r['id']:r for r in resources}
require(len(byid)==len(resources),'Duplicate resource IDs')
primary_urls=[]
for r in resources:
    require(bool(re.fullmatch(r'[a-z0-9-]+',r['id'])),f"Invalid ID: {r['id']}")
    require(r['category'] in CATEGORIES,f"Unknown category: {r['id']}")
    require(r['kind'] in {'paper','blog','project'},f"Unknown kind: {r['id']}")
    require(r['relevance'] in {'core','enabling','adjacent'},f"Unknown relevance: {r['id']}")
    require(isinstance(r['year'],int) and 1900<=r['year']<=2026,f"Invalid year: {r['id']}")
    require(r.get('authors') and all(isinstance(name,str) and name.strip() for name in r['authors']),f"Missing authors: {r['id']}")
    require(isinstance(r.get('institutions'),list) and all(isinstance(name,str) and name.strip() for name in r['institutions']),f"Invalid affiliations: {r['id']}")
    require(all(r.get('attribution_sources',{}).get(key,'').startswith('https://') for key in ['authors','affiliations']),f"Missing attribution evidence: {r['id']}")
    require('summary' not in r,f"Obsolete one-sentence summary: {r['id']}")
    require(r['links'] and r['tags'],f"Missing links/tags: {r['id']}")
    require(len({x['url'] for x in r['links']})==len(r['links']),f"Duplicate work link: {r['id']}")
    require(r['review'].get('date') and r['review'].get('scope'),f"Missing review scope: {r['id']}")
    for link in r['links']:
        u=urlsplit(link['url'])
        require(u.scheme=='https' and bool(u.netloc),f"Invalid source URL: {r['id']}")
        if link['label'].startswith('HF'):
            require(u.netloc=='huggingface.co',f"Invalid Hugging Face host: {r['id']}")
            if 'Dataset' in link['label']:
                require(u.path.startswith('/datasets/'),f"Model mislabeled as dataset: {r['id']}")
            elif 'Collection' in link['label']:
                require(u.path.startswith('/collections/'),f"Invalid collection: {r['id']}")
            else:
                require(not any(u.path.startswith(prefix) for prefix in ['/datasets/','/papers/','/collections/','/spaces/']),f"Non-model mislabeled as model or adapter: {r['id']}")
    if r['kind']=='paper':
        require(any(x['label']=='Paper' for x in r['links']),f"Missing paper source: {r['id']}")
    primary_urls.append(r['links'][0]['url'])
require(len(set(primary_urls))==len(primary_urls),'Duplicate primary source across works')
require(set(r['category'] for r in resources)==set(CATEGORIES),'Empty category')
reviews=json.loads((ROOT/'data/paper-reviews.json').read_text(encoding='utf-8'))['reviews']
manifest=json.loads((ROOT/'data/fulltext-manifest.json').read_text(encoding='utf-8'))['papers']
acquired={record['id']:record for record in manifest}
paper_ids={r['id'] for r in resources if r['kind']=='paper'}
publication_types={'conference','journal','workshop','book-chapter','preprint'}
def publication_ok(rid,p):
    require(p.get('type') in publication_types,f'Invalid publication type: {rid}')
    require(type(p.get('year')) is int and 1900<=p['year']<=2026,f'Invalid publication year: {rid}')
    require(all(isinstance(p.get(k),str) and p[k].strip() for k in ['venue','evidence','checked_at']),f'Incomplete publication evidence: {rid}')
    require(urlsplit(p.get('source_url','')).scheme=='https' and bool(urlsplit(p.get('source_url','')).netloc),f'Invalid publication source: {rid}')
    require(p.get('verification') in {'primary-source-verified','author-reported-acceptance','preprint-only-verified'},f'Invalid publication verification: {rid}')
    require((p['type']=='preprint')==(p['verification']=='preprint-only-verified'),f'Preprint verification mismatch: {rid}')
    require(p.get('online_year',p['year'])<=p['year'],f'Invalid online/issue year: {rid}')
for rid in paper_ids:
    r=byid[rid];p=r.get('publication',{})
    publication_ok(rid,p)
    require(r['year']==p['year'],f'Ordering/publication year mismatch: {rid}')
    require(type(r.get('first_public_year')) is int and 1900<=r['first_public_year']<=r['year'],f'Invalid first public year: {rid}')
    require(r['publication_status']==('preprint' if p['type']=='preprint' else 'published'),f'Publication status mismatch: {rid}')
publication_dois=[byid[rid]['publication']['doi'].lower() for rid in paper_ids if byid[rid]['publication'].get('doi')]
require(len(publication_dois)==len(set(publication_dois)),'Duplicate final-publication DOI across included works')
require(set(reviews)==paper_ids,'Paper/review coverage mismatch')
require(set(acquired)==paper_ids,'Paper/download coverage mismatch')
media=json.loads((ROOT/'data/update-media.json').read_text(encoding='utf-8'))
for media_url,preview in media.items():
    require(media_url.startswith('https://') and preview['source_url'].startswith('https://'),'Invalid preview source URL')
    media_path=ROOT/preview['path']
    require(preview['path'].startswith('assets/news/') and '..' not in preview['path'].split('/') and media_path.suffix=='.webp' and media_path.is_file(),'Invalid generated preview path')
    require(preview['kind'] in {'paper','figure','related-figure','blog','source-image','related-source'} and preview.get('alt') and preview.get('credit'),'Missing preview attribution')
    signature=media_path.read_bytes()[:12]
    require(signature[:4]==b'RIFF' and signature[8:12]==b'WEBP','Invalid WebP preview')
    for image in preview.get('images', []):
        require(set(image) <= {'path','alt','source_url','width','height','source_index'},'Private image-review fields cannot be exported')
        require(image.get('alt') and image.get('source_url','').startswith('https://'),'Missing gallery attribution')
        relative=Path(image['path'])
        require(relative.as_posix().startswith('assets/news/') and '..' not in relative.parts and relative.suffix=='.webp' and (ROOT/relative).is_file(),'Invalid gallery image path')
        require(0 < image.get('width',0) <= 1600 and 0 < image.get('height',0) <= 1200,'Invalid gallery image dimensions')
    if preview['kind']=='related-source':
        require(preview.get('related_url','').startswith('https://') and preview.get('image_label'),'Unlabeled related-source image')
updates=json.loads((ROOT/'data/updates.json').read_text(encoding='utf-8'))
from datetime import date,timedelta
end=date.fromisoformat(updates['window_end']);start=end-timedelta(days=updates['window_days']-1)
require(updates['window_start']==start.isoformat(),'Incorrect news window')
news_urls=set()
for item in updates['items']:
    require(item['review_status']=='approved' and item['date_evidence'].strip(),'Unverified news item')
    require(start<=date.fromisoformat(item['published_at'][:10])<=end,'News item outside rolling window')
    require(item['kind'] in {'paper','x','linkedin','blog','model'},'Invalid news type')
    for link in item.get('links', []):
        parsed=urlsplit(link['url'])
        require(parsed.scheme=='https' and bool(parsed.hostname) and not parsed.username and not parsed.password,
                'Invalid news artifact URL')
        require(link['label'] in {'Paper','Dataset','Model','Code','Project','Announcement'},'Invalid news artifact label')
    require(urlsplit(item['url']).scheme=='https' and item['url'] not in news_urls,'Invalid or duplicate news URL')
    news_urls.add(item['url'])
from build_site import paper_slug
archived=updates.get('paper_pages',[])
require(isinstance(archived,list),'Invalid permanent paper-page archive')
archived_slugs=set()
for item in archived:
    require(item['kind']=='paper' and item['review_status']=='approved','Unverified paper-page archive item')
    require(urlsplit(item['url']).scheme=='https' and bool(urlsplit(item['url']).netloc),'Invalid archived paper URL')
    require(date.fromisoformat(item['published_at'][:10])<=end,'Future archived paper')
    require(all(item.get(key,'').strip() for key in ['title','summary','date_evidence']),'Incomplete archived paper')
    slug=paper_slug(item['url'])
    require(slug not in archived_slugs,'Duplicate archived paper')
    archived_slugs.add(slug)
require({paper_slug(item['url']) for item in updates['items'] if item['kind']=='paper'}<=archived_slugs,'News paper missing permanent page record')
for rid in paper_ids:
    note=reviews[rid]
    record=acquired[rid]
    require(record['status']=='fulltext-downloaded',f"Full text unavailable: {rid}")
    require(record['pages']>0 and record['characters']>1000 and re.fullmatch('[0-9a-f]{64}',record['sha256']),f"Missing acquisition evidence: {rid}")
    require(note['consulted_pdf_pages'] and all(type(page) is int and 1<=page<=record['pages'] for page in note['consulted_pdf_pages']),f"Invalid reviewed page reference: {rid}")
    require(note['sections'] and all(note.get(key,'').strip() for key in ['method','evidence','discovery_use','limits']),f"Incomplete body-review record: {rid}")
    require(byid[rid]['institutions']==note['institutions'],f"Affiliation mismatch: {rid}")
    require(byid[rid]['review'].get('fulltext_status')=='body-sections-reviewed',f"Missing review status: {rid}")
    classification=note.get('classification_review',{})
    require(classification.get('category')==byid[rid]['category'],f"Stale classification: {rid}")
    require(classification.get('pdf_sha256')==record['sha256'],f"Classification/full-text version mismatch: {rid}")
    require(classification.get('evidence_pages')==note['consulted_pdf_pages'] and classification.get('rationale','').strip(),f"Incomplete classification evidence: {rid}")
    for key in ['local_pdf','local_text']:
        target=(ROOT/record[key]).resolve()
        require(target.is_relative_to(ROOT/'.local/fulltexts'),f"Cache path escapes full-text directory: {rid}")
profile_ids=set()
for p in bench['profiles']:
    require(p['id'] not in profile_ids,f"Duplicate profile: {p['id']}")
    profile_ids.add(p['id'])
    require(p['resource_id'] in byid,f"Unknown benchmark work: {p['id']}")
    require(p['new_physical_experiments'] is None or type(p['new_physical_experiments']) is bool,f"Invalid physical execution flag: {p['id']}")
    if p['new_physical_experiments'] is True:
        require(p['feedback']=='new-physical-measurements',f"Unsupported real-execution label: {p['id']}")
    if p['status']=='contract-only':
        require(p['new_physical_experiments'] is None,f"Contract mislabeled as demonstrated execution: {p['id']}")
    require(all(isinstance(p[k],str) and p[k].strip() for k in ['limits','focus']),f"Missing English card: {p['id']}")
    require(set(p['training'])=={'reward','reset','branching'},f"Incomplete training card: {p['id']}")
require({r['id'] for r in resources if r['category']=='benchmarks'} <= {p['resource_id'] for p in bench['profiles']},'Benchmark resource missing a usage profile')
for name,text in outputs().items():
    require((ROOT/name).read_text(encoding='utf-8')==text,f"Stale generated output: {name}")
for path in ROOT.rglob('*.md'):
    if any(part in path.parts for part in ['.git','.qa','.local']):
        continue
    text=path.read_text(encoding='utf-8')
    require('\ufffd' not in text,f"Replacement glyph in {path.name}")
    for target in re.findall(r'\]\(([^)]+)\)',text):
        if target.startswith(('https://','http://','mailto:')):
            continue
        filename,_,fragment=target.partition('#')
        dest=(path.parent/unquote(filename)).resolve() if filename else path
        require(dest.is_relative_to(ROOT),f"Local link escapes repository: {target}")
        require(dest.is_file(),f"Broken local link in {path.name}: {target}")
        if fragment and dest.suffix=='.md':
            desttext=dest.read_text(encoding='utf-8')
            require(f'id="{fragment}"' in desttext,f"Missing explicit anchor: {target}")
print(json.dumps({'status':'passed','resources':len(resources),'categories':len(CATEGORIES),'benchmark_profiles':len(profile_ids),'paper_entries':len(paper_ids)},indent=2))
