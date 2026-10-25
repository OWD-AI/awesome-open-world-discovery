"""Build an explicit, public-only GitHub Pages artifact (no local research caches)."""
import argparse
import hashlib
import html
import json
import shutil
from functools import lru_cache
from datetime import date, datetime, timedelta
from pathlib import Path
from urllib.parse import urlsplit
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
SITE_URL = 'https://owd-ai.github.io/awesome-open-world-discovery/'


def paper_slug(url):
    return hashlib.sha256(canonical(url).encode()).hexdigest()[:16]


def canonical(url):
    parsed = urlsplit(url)
    path = parsed.path.rstrip('/')
    if parsed.hostname in ('nature.com', 'www.nature.com'):
        import re
        match = re.fullmatch(r'/articles/(s(?:41586|42256|43588)-\d{3}-\d{5}-[a-z0-9]+)(?:\.pdf)?', path)
        if match:
            return 'https://www.nature.com/articles/' + match[1]
    if parsed.hostname in ('arxiv.org', 'www.arxiv.org', 'export.arxiv.org'):
        import re
        match = re.fullmatch(r'/(?:abs|pdf|html)/((?:[A-Za-z.-]+/\d{7})|(?:\d{4}\.\d{4,5}))(?:v\d+)?(?:\.pdf)?', path)
        if match:
            return 'https://arxiv.org/abs/' + match[1]
    return 'https://' + (parsed.hostname or '') + path


def source_info(item):
    host = urlsplit(item['url']).hostname or ''
    if host.endswith('arxiv.org'): return 'arXiv', 'arXiv', 'arXiv'
    if host in ('x.com', 'twitter.com'): return 'X', 'X', '𝕏'
    if host.endswith('linkedin.com'): return 'LinkedIn', 'LinkedIn', 'in'
    if host in ('nature.com', 'www.nature.com'):
        for code, name, mark in [('s41586', 'Nature', 'N'), ('s42256', 'Nature Machine Intelligence', 'NMI'),
                                 ('s43588', 'Nature Computational Science', 'NCS')]:
            if '/articles/' + code in item['url']: return name, 'Journals', mark
    if host == 'research.google': return 'Google Research', 'Blogs', 'G'
    if host == 'deepmind.google': return 'Google DeepMind', 'Blogs', 'D'
    if host == 'huggingface.co': return 'Hugging Face', 'Hugging Face', 'HF'
    if host.endswith('microsoft.com'): return 'Microsoft Research', 'Blogs', 'MS'
    return host.removeprefix('www.'), 'Blogs' if item['kind'] == 'blog' else 'Other', '↗'


@lru_cache(maxsize=512)
def image_fingerprint(path, modified, size):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()[:10]


def preview_images(image, asset_prefix):
    images = []
    for entry in image.get('images') or ([image] if image else []):
        path = entry.get('path', '')
        local = (ROOT / path).resolve()
        if not path.startswith('assets/news/') or not local.is_relative_to(ROOT / 'assets/news') or not local.is_file():
            continue
        stat = local.stat()
        images.append({'url': asset_prefix + '/' + path.removeprefix('assets/') + '?v=' + image_fingerprint(str(local), stat.st_mtime_ns, stat.st_size),
                       'alt': entry.get('alt', ''), 'source_url': entry.get('source_url', image.get('source_url', '')),
                       'credit': image.get('credit', 'Original source authors'),
                       'width': entry.get('width', 1000), 'height': entry.get('height', 700)})
    return images


def merge_links(*groups):
    return list({(link['label'], link['url']): link for group in groups for link in group}.values())


def payload(resources, categories, updates, asset_prefix):
    media_path = ROOT / 'data/update-media.json'
    media = json.loads(media_path.read_text(encoding='utf-8')) if media_path.exists() else {}
    reviews = json.loads((ROOT / 'data/paper-reviews.json').read_text(encoding='utf-8'))['reviews']
    end = date.fromisoformat(updates['window_end'])
    start = end - timedelta(days=updates['window_days'] - 1)
    works = []
    byurl = {}
    for resource in resources:
        links = [{'label': l['label'], 'url': l['url']} for l in resource['links']]
        paper = next((l['url'] for l in links if l['label'] == 'Paper'), links[0]['url'])
        pub = resource.get('publication', {})
        authors = resource.get('display_authors', resource['authors'])
        review = reviews.get(resource['id'], {})
        description = review.get('method', '')
        if not description:
            description = 'Research resource covering ' + ', '.join(tag.replace('-', ' ') for tag in resource['tags']) + '.'
        works.append({'id': resource['id'], 'slug': paper_slug(paper), 'title': resource['title'], 'category': resource['category'], 'year': resource['year'],
                      'venue': pub.get('venue', 'Research project'), 'authors': ', '.join(authors[:3]) + (' et al.' if len(authors) > 3 else ''),
                      'summary': description, 'discovery_use': review.get('discovery_use', ''), 'url': paper, 'links': links})
        for link in links:
            byurl[canonical(link['url'])] = links
    news = []
    for item in sorted(updates['items'], key=lambda r: (r['published_at'], r['title']), reverse=True):
        if item.get('review_status') != 'approved' or not start <= date.fromisoformat(item['published_at'][:10]) <= end:
            continue
        source, group, mark = source_info(item)
        image = media.get(canonical(item['url']), {})
        links = merge_links(byurl.get(canonical(item['url']), []), item.get('links', []))
        if not links:
            links = [{'label': 'Paper' if item['kind'] == 'paper' else 'Model' if item['kind'] == 'model' else 'Read post', 'url': item['url']}]
        if image.get('related_url'):
            links = merge_links(links, [{'label': 'Related paper' if image.get('kind') == 'related-figure' else image.get('related_label', 'Related source'), 'url': image['related_url']}])
        images = preview_images(image, asset_prefix)
        news.append({'title': item['title'], 'summary': item['summary'], 'url': item['url'],
                     'kind': item['kind'],
                     'slug': paper_slug(item['url']),
                     'content_label': item.get('content_label') or {'paper': 'Paper', 'x': 'Social post', 'linkedin': 'Social post', 'blog': 'Blog', 'model': 'Model release'}[item['kind']],
                     'published_at': item['published_at'][:10], 'source': source, 'source_group': group, 'source_mark': mark,
                     'links': links, 'image': images[0]['url'] if images else '', 'images': images,
                     'image_alt': images[0]['alt'] if images else '', 'image_kind': image.get('kind', ''),
                     'image_label': image.get('image_label') or ('Related paper figure' if image.get('kind') == 'related-figure' else 'Post images' if item['kind'] in ('x', 'linkedin') else 'Source figures' if image.get('kind') == 'source-image' else 'Publisher cover' if image.get('kind') == 'blog' else 'Paper figure' if image.get('kind') == 'figure' else 'Paper preview')})
    return {'categories': categories, 'updates': news, 'works': sorted(works, key=lambda r: (-r['year'], r['title']))}


def resource_links(links):
    return ''.join(f'<a href="{html.escape(link["url"], quote=True)}" target="_blank" rel="noopener noreferrer">{html.escape(link["label"])} ↗</a>' for link in links)


def paper_pages(works, updates):
    pages = {}
    for item in [*updates.get('paper_pages', []), *updates['items']]:
        if item.get('kind') != 'paper' or item.get('review_status') != 'approved':
            continue
        slug = paper_slug(item['url'])
        pages[slug] = {'slug': slug, 'title': item['title'], 'summary': item['summary'],
                       'year': int(item['published_at'][:4]), 'venue': source_info(item)[0],
                       'links': merge_links([{'label': 'Paper', 'url': item['url']}], item.get('links', [])), 'url': item['url']}
    # Catalog admission enriches the same page rather than moving its conversation.
    for item in works:
        old = pages.get(item['slug'], {})
        pages[item['slug']] = {**item, 'links': merge_links(item.get('links', []), old.get('links', []))}
    return pages


def thumbnail(item):
    esc = html.escape
    fallback = f'<div class="update-thumb source-thumb" aria-hidden="true"><strong>{esc(item["source_mark"])}</strong><span>{esc(item["source"])}</span></div>'
    if not item['image']:
        return fallback
    kind = 'paper-preview' if item['image_kind'] == 'paper' else ''
    count = len(item.get('images', [])) or 1
    badge = f'<span class="image-count">1 / {count}</span>' if count > 1 else ''
    return (f'<figure class="update-media"><a class="update-thumb {kind}" data-gallery="{esc(item["slug"], quote=True)}" '
            f'href="{esc(item["image"], quote=True)}" target="_blank" rel="noopener noreferrer" aria-label="View images: {esc(item["title"], quote=True)}">'
            f'<img src="{esc(item["image"], quote=True)}" alt="{esc(item["image_alt"], quote=True)}" loading="lazy" width="400" height="268">{badge}'
            f'<span class="image-expand" aria-hidden="true">⤢</span></a><figcaption>{esc(item["image_label"])}</figcaption></figure>')


def initial_cards(items, papers_url=''):
    esc = html.escape
    output = []
    previous = None
    for item in items:
        day = item['published_at']
        if day != previous:
            if previous is not None:
                output.append('</section>')
            label = date.fromisoformat(day).strftime('%b %d, %Y').replace(' 0', ' ')
            count = sum(row['published_at'] == day for row in items)
            output.append(f'<section class="date-group" aria-label="{label}"><h3 class="date-heading"><time datetime="{day}">{label}</time><span>{count} {"update" if count == 1 else "updates"}</span></h3>')
            previous = day
        visual = thumbnail(item)
        discussion = f'<a class="discussion-link" href="{esc(papers_url + item["slug"] + "/#discussion", quote=True)}">Discuss ↗</a>' if papers_url and item['kind'] == 'paper' else ''
        output.append(f'<article class="update-row">{visual}<div class="update-body"><div class="item-meta"><span class="source-name">{esc(item["source"])}</span><span class="content-type kind-{esc(item["kind"])}">{esc(item["content_label"])}</span><time datetime="{day}">{label}</time></div><h3><a href="{esc(item["url"], quote=True)}" target="_blank" rel="noopener noreferrer">{esc(item["title"])}</a></h3><p class="item-description">{esc(item["summary"])}</p><div class="resource-links">{resource_links(item["links"])}{discussion}</div></div></article>')
    if output:
        output.append('</section>')
    return ''.join(output)


def initial_works(items, categories, library_url, papers_url):
    esc = html.escape
    output = []
    for item in items:
        extra = f'<details class="work-details"><summary>Discovery relevance</summary><p>{esc(item["discovery_use"])}</p></details>' if item['discovery_use'] else ''
        detail_url = esc(papers_url + item['slug'] + '/', quote=True)
        output.append(f'<article class="work-row" id="{esc(item["id"], quote=True)}"><div class="work-meta"><span class="work-year">{item["year"]}</span><span>{esc(item["venue"])}</span><a class="work-theme" href="{esc(library_url, quote=True)}?theme={esc(item["category"], quote=True)}">{esc(categories[item["category"]])}</a></div><h2><a href="{detail_url}">{esc(item["title"])}</a></h2><p class="work-authors">{esc(item["authors"])}</p><p class="item-description">{esc(item["summary"])}</p>{extra}<div class="resource-links">{resource_links(item["links"])}<a class="discussion-link" href="{detail_url}#discussion">Discuss ↗</a></div></article>')
    return ''.join(output)


def asset_url(prefix, name):
    fingerprint = hashlib.sha256((ROOT / 'assets' / name).read_bytes()).hexdigest()[:10]
    return f'{prefix}/{name}?v={fingerprint}'


def framework_figure(asset_prefix, about_url):
    image = html.escape(asset_url(asset_prefix, 'open-world-discovery-web.png'), quote=True)
    return f'<figure class="framework-figure"><a href="{image}" target="_blank" rel="noopener noreferrer" aria-label="View the Open World Discovery framework at full size"><img src="{image}" width="1774" height="887" fetchpriority="high" alt="Our discovery framework: an agent experiments in a partially known world, gathers evidence, revises its hypotheses, expands its knowledge, and learns to discover."></a><figcaption><span>Our discovery framework</span><a href="{html.escape(about_url, quote=True)}">Explore the idea <span aria-hidden="true">↗</span></a></figcaption></figure>'


def feed_context(updates):
    """Describe the published feed, independently of catalog size or an in-progress run."""
    refreshed = datetime.fromisoformat(updates['updated_at'].replace('Z', '+00:00'))
    if refreshed.tzinfo is None:
        raise ValueError('Feed refresh timestamp must include its timezone')
    refreshed = refreshed.astimezone(ZoneInfo('America/New_York'))
    start = date.fromisoformat(updates['window_start'])
    end = date.fromisoformat(updates['window_end'])
    def label(day, year=False):
        return day.strftime('%b') + f' {day.day}' + (f', {day.year}' if year else '')
    refresh_label = label(refreshed, True) + refreshed.strftime(' · %H:%M %Z')
    return (f'<p class="feed-context" aria-label="Published feed information">'
            f'<span>Feed refreshed <time datetime="{refreshed.isoformat(timespec="seconds")}">{refresh_label}</time></span> '
            f'<span>Publication window <time datetime="{start.isoformat()}">{label(start, start.year != end.year)}</time>'
            f' – <time datetime="{end.isoformat()}">{label(end, True)}</time></span></p>')


def render(resources, benchmarks, categories, inline=False, page='home', paper=None):
    from build import CATEGORY_GUIDE
    if page not in ('home', 'updates', 'library', 'about', 'paper'):
        raise ValueError('Unknown website page')
    updates = json.loads((ROOT / 'data/updates.json').read_text(encoding='utf-8'))
    base = SITE_URL if inline else './' if page == 'home' else '../../' if page == 'paper' else '../'
    asset_prefix = '../assets' if inline else base + 'assets'
    paths = {'home': base, **{name: base + name + '/' for name in ('updates', 'library', 'about')}}
    paths['papers'] = base + 'papers/'
    data = payload(resources, categories, updates, asset_prefix)
    data['paths'] = paths
    data['questions'] = {key: CATEGORY_GUIDE[key][1] for key in categories}
    counts = {key: sum(item['category'] == key for item in resources) for key in categories}
    esc = html.escape
    theme_links = ''.join(f'<a href="{esc(paths["library"], quote=True)}?theme={key}">{esc(title)}<span>{counts[key]}</span></a>' for key, title in categories.items())
    theme_buttons = f'<button type="button" data-theme="all" aria-pressed="true">All themes<span>{len(resources)}</span></button>' + ''.join(f'<button type="button" data-theme="{key}" aria-pressed="false">{esc(title)}<span>{counts[key]}</span></button>' for key, title in categories.items())
    questions = ''.join(f'<a class="question-card" href="{esc(paths["library"], quote=True)}?theme={key}"><span class="question-number">0{index}</span><h3>{esc(title)}</h3><p>{esc(data["questions"][key])}</p><span>{counts[key]} works ↗</span></a>' for index, (key, title) in enumerate(categories.items(), 1))
    intro = '''<section class="hero"><div class="hero-copy"><p class="eyebrow"><span class="live-dot"></span> EXPLORE BEYOND WHAT WE KNOW</p><h1>Open World<br>Discovery<span class="heading-dot">.</span></h1><p class="hero-description">Connecting research on agents that explore unknowns, build verifiable knowledge, and learn to discover.</p><div class="hero-actions"><a class="primary-link" href="#updates">Latest research <span aria-hidden="true">↓</span></a><a class="text-link" href="@@LIBRARY@@">Browse the library ↗</a></div></div>@@FRAMEWORK@@</section>''' if page == 'home' else ''
    content = (ROOT / 'site' / (('updates' if page == 'home' else page) + '.html')).read_text(encoding='utf-8')
    footnote = '<section class="home-about"><div><h2>One connected discovery process.</h2><p>Representations, reasoning, training, systems, and evaluation contribute to a shared question: how can agents make verifiable discoveries and become better discoverers?</p></div><a class="text-link" href="@@ABOUT@@">What is Open World Discovery? ↗</a></section>' if page == 'home' else ''
    template = (ROOT / 'site/index.html').read_text(encoding='utf-8').replace('@@INTRO@@', intro).replace('@@CONTENT@@', content).replace('@@FOOTNOTE@@', footnote)
    titles = {'home': 'Open World Discovery — Research Observatory', 'updates': 'Latest updates — Open World Discovery', 'library': 'Research library — Open World Discovery', 'about': 'About — Open World Discovery'}
    public_data = data if page not in ('about', 'paper') else {key: data[key] for key in ('paths', 'categories', 'questions')}
    paper_values = {}
    if page == 'paper':
        if not paper:
            raise ValueError('Paper page requires a work')
        titles['paper'] = paper['title'] + ' — Open World Discovery'
        reviews = json.loads((ROOT / 'data/paper-reviews.json').read_text(encoding='utf-8'))['reviews']
        review = reviews.get(paper.get('id'), {})
        notes = '<section><h2>What this work does</h2><p>' + esc(paper['summary']) + '</p></section>'
        for key, heading in [('discovery_use', 'Connection to discovery'), ('evidence', 'Evidence'), ('limits', 'Scope and limitations')]:
            value = review.get(key, '')
            if value:
                notes += f'<section><h2>{heading}</h2><p>{esc(value)}</p></section>'
        paper_values = {
            '@@PAPER_TITLE@@': esc(paper['title']),
            '@@PAPER_META@@': f'<span>{paper.get("year", paper.get("published_at", "")[:4])}</span><span>{esc(paper.get("venue", paper.get("source", "Research")))}</span>',
            '@@PAPER_AUTHORS@@': '<p class="paper-authors">' + esc(paper['authors']) + '</p>' if paper.get('authors') else '',
            '@@PAPER_LINKS@@': resource_links(paper['links']), '@@PAPER_NOTES@@': notes,
            '@@GISCUS@@': '<script src="https://giscus.app/client.js" data-repo="OWD-AI/awesome-open-world-discovery" data-repo-id="R_kgDOVMtQmw" data-category="Announcements" data-category-id="DIC_kwDOVMtQm84DJE0u" data-mapping="pathname" data-strict="1" data-reactions-enabled="1" data-emit-metadata="0" data-input-position="top" data-theme="light" data-lang="en" loading="lazy" crossorigin="anonymous" async></script>',
        }
    replacements = {
        '@@PAGE@@': page, '@@TITLE@@': esc(titles[page]),
        '@@CANONICAL@@': SITE_URL + ('papers/' + paper['slug'] + '/' if page == 'paper' else page + '/' if page != 'home' else ''),
        '@@MARK@@': asset_url(asset_prefix, 'owd-mark.svg'),
        '@@MARK_PNG@@': asset_url(asset_prefix, 'owd-mark.png'),
        '@@FAVICON@@': asset_url(asset_prefix, 'favicon.ico'),
        '@@STYLE@@': '<style>' + (ROOT / 'site/site.css').read_text(encoding='utf-8') + '</style>' if inline else '<link rel="stylesheet" href="' + base + 'site.css?v=' + hashlib.sha256((ROOT / 'site/site.css').read_bytes()).hexdigest()[:10] + '">',
        '@@SCRIPT@@': '<script>' + (ROOT / 'site/site.js').read_text(encoding='utf-8') + '</script>' if inline else '<script src="' + base + 'site.js?v=' + hashlib.sha256((ROOT / 'site/site.js').read_bytes()).hexdigest()[:10] + '" defer></script>',
        '@@UPDATED@@': esc(updates['updated_at'][:10]),
        '@@FEED_CONTEXT@@': feed_context(updates),
        '@@NEWS_COUNT@@': str(len(data['updates'])), '@@WORK_COUNT@@': str(len(resources)), '@@THEME_COUNT@@': str(len(categories)),
        '@@TODAY_COUNT@@': str(sum(item['published_at'] == datetime.now(ZoneInfo('America/New_York')).date().isoformat() for item in data['updates'])),
        '@@HEADING_TAG@@': 'h2' if page == 'home' else 'h1',
        '@@THEME_LINKS@@': theme_links, '@@THEME_BUTTONS@@': theme_buttons, '@@QUESTIONS@@': questions,
        '@@YEARS@@': ''.join(f'<option value="{year}">{year}</option>' for year in sorted({item['year'] for item in resources}, reverse=True)),
        '@@INITIAL_CARDS@@': initial_cards(data['updates'][:8] if page == 'home' else data['updates'], paths['papers']) if page in ('home', 'updates') else '',
        '@@INITIAL_WORKS@@': initial_works(data['works'], categories, paths['library'], paths['papers']) if page == 'library' else '',
        '@@FRAMEWORK@@': framework_figure(asset_prefix, paths['about']),
        '@@DATA@@': json.dumps(public_data, ensure_ascii=False, separators=(',', ':')).replace('&', '\\u0026').replace('<', '\\u003c').replace('>', '\\u003e'),
        **{'@@' + key.upper() + '@@': esc(value, quote=True) for key, value in paths.items()},
        **{'@@' + key.upper() + '_ACTIVE@@': 'aria-current="page"' if page == key else '' for key in ('updates', 'library', 'about')},
        **paper_values,
    }
    # Substitute once: research text cannot introduce new template instructions.
    import re
    return re.sub(r'@@[A-Z_]+@@', lambda match: replacements[match[0]], template)


def build(destination):
    from build import CATEGORIES, load
    resources, benchmarks = load()
    destination.mkdir(parents=True, exist_ok=True)
    for page in ('home', 'updates', 'library', 'about'):
        folder = destination if page == 'home' else destination / page
        folder.mkdir(exist_ok=True)
        (folder / 'index.html').write_text(render(resources['resources'], benchmarks, CATEGORIES, page=page), encoding='utf-8', newline='\n')
    updates = json.loads((ROOT / 'data/updates.json').read_text(encoding='utf-8'))
    catalog = payload(resources['resources'], CATEGORIES, updates, 'assets')
    # A canonical source URL gives papers a stable discussion, even after catalog admission.
    papers = paper_pages(catalog['works'], updates)
    for item in papers.values():
        folder = destination / 'papers' / item['slug']
        folder.mkdir(parents=True, exist_ok=True)
        (folder / 'index.html').write_text(render(resources['resources'], benchmarks, CATEGORIES, page='paper', paper=item), encoding='utf-8', newline='\n')
    for name in ('site.css', 'site.js'):
        shutil.copyfile(ROOT / 'site' / name, destination / name)
    (destination / '.nojekyll').touch()
    (destination / 'assets').mkdir(exist_ok=True)
    for name in ('owd-mark.svg', 'owd-mark.png', 'favicon.ico', 'open-world-discovery-web.png'):
        shutil.copyfile(ROOT / 'assets' / name, destination / 'assets' / name)
    media = json.loads((ROOT / 'data/update-media.json').read_text(encoding='utf-8'))
    image_paths = {image['path'] for entry in media.values() for image in [entry, *entry.get('images', [])]}
    for path in image_paths:
        source = (ROOT / path).resolve()
        if not path.startswith('assets/news/') or not source.is_relative_to(ROOT / 'assets/news') or source.suffix != '.webp' or not source.is_file():
            continue
        target = destination / path
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
    (destination / 'README.md').write_text('# Open World Discovery\n\nPublic website artifact generated from the research catalog.\n\n' + SITE_URL + '\n', encoding='utf-8', newline='\n')
    return destination


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / '_site')
    args = parser.parse_args()
    print('Built public website:', build(args.output.resolve()))
