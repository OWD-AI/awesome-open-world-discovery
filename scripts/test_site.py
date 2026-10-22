"""Checks public export boundaries and safe research data rendering."""
import json
import tempfile
import unittest
from unittest.mock import patch
from html.parser import HTMLParser
from pathlib import Path

import build_site
from build import CATEGORIES, load


class SiteTests(unittest.TestCase):
    def test_model_release_displays_official_artifacts_without_becoming_a_paper(self):
        resources, _ = load()
        links=[{'label':'Model','url':'https://huggingface.co/RecursiveSI/flint'},
               {'label':'Code','url':'https://github.com/recursive-oss/rec'}]
        updates={'window_end':'2026-10-21','window_days':30,'items':[{
            'title':'Recursive Flint','summary':'A developer-reported automated research model release.',
            'url':links[0]['url'],'kind':'model','published_at':'2026-10-21',
            'review_status':'approved','links':links}]}
        card=build_site.payload(resources['resources'],CATEGORIES,updates,'assets')['updates'][0]
        self.assertEqual(card['links'],links)
        self.assertEqual(card['content_label'],'Model release')
        self.assertNotIn('Discuss',build_site.initial_cards([card]))

    def test_related_paper_and_discussion_keep_separate_content_and_dates(self):
        resources, _ = load()
        updates = {'window_end': '2026-10-19', 'window_days': 30, 'items': [
            {'title': 'DiscoveryRSI paper', 'summary': 'Introduces the discovery method and benchmark.',
             'url': 'https://arxiv.org/abs/2610.23839', 'kind': 'paper', 'published_at': '2026-10-16', 'review_status': 'approved'},
            {'title': 'WITNESS alongside DiscoveryRSI', 'summary': 'Discusses related hypothesis-testing environments.',
             'url': 'https://x.com/quietnning/status/2112233429245063201', 'kind': 'x', 'content_label': 'Research discussion',
             'published_at': '2026-10-19', 'review_status': 'approved'},
        ]}
        cards = build_site.payload(resources['resources'], CATEGORIES, updates, 'assets')['updates']
        related = [item for item in cards if 'DiscoveryRSI' in item['title']]
        self.assertEqual(len(related), 2)
        by_source = {item['source']: item for item in related}
        self.assertEqual(by_source['arXiv']['content_label'], 'Paper')
        self.assertEqual(by_source['X']['content_label'], 'Research discussion')
        self.assertNotEqual(by_source['X']['summary'], by_source['arXiv']['summary'])
        self.assertNotEqual(by_source['X']['published_at'], by_source['arXiv']['published_at'])

    def test_only_approved_in_window_news_is_exported(self):
        resources, _ = load()
        rows = [{'title': '</script><script>alert(1)</script>', 'summary': 'Example',
                 'url': 'https://arxiv.org/abs/2610.99999', 'kind': 'paper',
                 'published_at': day, 'review_status': state}
                for day, state in [('2026-09-19', 'approved'), ('2026-10-20', 'approved'),
                                   ('2026-10-19', 'candidate'), ('2026-10-19', 'approved')]]
        updates = {'window_end': '2026-10-19', 'window_days': 30, 'items': rows}
        data = build_site.payload(resources['resources'], CATEGORIES, updates, 'assets')
        self.assertEqual(len(data['updates']), 1)
        markup = build_site.initial_cards(data['updates'])
        self.assertNotIn('<script>', markup)
        self.assertIn('&lt;script&gt;', markup)
        self.assertEqual(data['updates'][0]['source'], 'arXiv')
        self.assertTrue(all(len(item['summary']) > 25 for item in data['works']))

    def test_public_artifact_contains_no_raw_documents_or_private_cache(self):
        with tempfile.TemporaryDirectory() as folder:
            build_site.build(Path(folder))
            names = {p.relative_to(folder).as_posix() for p in Path(folder).rglob('*') if p.is_file()}
            allowed = {'index.html', 'site.css', 'site.js', '.nojekyll', 'README.md',
                       'updates/index.html', 'library/index.html', 'about/index.html',
                       'assets/owd-mark.svg', 'assets/owd-mark.png', 'assets/favicon.ico', 'assets/open-world-discovery-web.png'}
            resources, _ = load()
            updates = json.loads((build_site.ROOT / 'data/updates.json').read_text(encoding='utf-8'))
            data = build_site.payload(resources['resources'], CATEGORIES, updates, 'assets')
            for row in data['updates']:
                for image in row['images']:
                    self.assertIn(image['url'].split('?', 1)[0], names, 'Gallery image missing from public artifact')
            slugs = set(build_site.paper_pages(data['works'], updates))
            allowed |= {f'papers/{slug}/index.html' for slug in slugs}
            self.assertTrue(all(n in allowed or (n.startswith('assets/news/') and n.endswith('.webp')) for n in names))
            self.assertFalse(any('.local' in n or n.endswith(('.pdf', '.txt', '.bib', '.json')) for n in names))
            page = (Path(folder) / 'index.html').read_text(encoding='utf-8')
            self.assertNotIn('@@', page)
            self.assertNotIn('local_pdf', page)
            self.assertNotIn('watchlist', page)
            self.assertNotIn('News screening verifies sources and publication dates.', page)
            self.assertIn('Figure 1 from', page)
            self.assertIn('class="framework-figure"', page)
            self.assertIn('open-world-discovery-web.png?v=', page)
            for route in ('updates', 'library', 'about'):
                route_page = (Path(folder) / route / 'index.html').read_text(encoding='utf-8')
                self.assertNotIn('@@', route_page)
                self.assertIn(f'data-page="{route}"', route_page)
                self.assertIn('../site.js?v=', route_page)
                self.assertIn('../site.css?v=', route_page)
            for slug in slugs:
                detail = (Path(folder) / 'papers' / slug / 'index.html').read_text(encoding='utf-8')
                self.assertNotIn('@@', detail)
                self.assertIn('data-mapping="pathname"', detail)
                self.assertIn('data-reactions-enabled="1"', detail)
                self.assertIn('../../site.css?v=', detail)
                self.assertIn('id="discussion"', detail)

    def test_paper_discussion_identity_ignores_arxiv_versions(self):
        self.assertEqual(build_site.paper_slug('https://arxiv.org/abs/2610.23839'),
                         build_site.paper_slug('https://arxiv.org/pdf/2610.23839v2.pdf'))
        for variant in ['https://arxiv.org/pdf/2610.23839.pdf', 'https://export.arxiv.org/html/2610.23839v2']:
            self.assertEqual(build_site.paper_slug('https://arxiv.org/abs/2610.23839'), build_site.paper_slug(variant))
        self.assertEqual(build_site.paper_slug('https://arxiv.org/abs/math/0406077'),
                         build_site.paper_slug('https://arxiv.org/pdf/math/0406077v2.pdf'))

    def test_expired_news_keeps_its_page_and_catalog_admission_keeps_its_identity(self):
        item = {'title': 'Earlier paper', 'summary': 'An older source-checked research announcement.',
                'kind': 'paper', 'review_status': 'approved', 'published_at': '2025-01-01',
                'url': 'https://arxiv.org/abs/2501.99999'}
        updates = {'items': [], 'paper_pages': [item]}
        slug = build_site.paper_slug(item['url'])
        self.assertEqual(build_site.paper_pages([], updates)[slug]['title'], item['title'])
        reviewed = {'slug': slug, 'title': 'Reviewed paper', 'summary': 'Full-text-reviewed contribution.',
                    'links': [{'label': 'Paper', 'url': item['url']}]}
        self.assertEqual(build_site.paper_pages([reviewed], updates)[slug], reviewed)

    def test_paper_detail_keeps_reviewed_code_links_after_catalog_admission(self):
        item = {'title': 'Paper', 'summary': 'A reviewed paper.', 'kind': 'paper', 'review_status': 'approved',
                'published_at': '2026-10-21', 'url': 'https://arxiv.org/abs/2610.99999',
                'links': [{'label': 'Code', 'url': 'https://github.com/lab/method'}]}
        slug = build_site.paper_slug(item['url'])
        catalog = {'slug': slug, 'title': 'Catalog paper', 'links': [{'label': 'Paper', 'url': item['url']}]}
        page = build_site.paper_pages([catalog], {'items': [item]})[slug]
        self.assertIn(item['links'][0], page['links'])
        self.assertEqual(len(page['links']), 2)

    def test_missing_preview_does_not_break_build_and_related_figure_is_labeled(self):
        self.assertEqual(build_site.preview_images({'path': 'assets/news/missing.webp'}, 'assets'), [])
        self.assertEqual(build_site.preview_images({'path': '../references.bib'}, 'assets'), [])
        resources, _ = load()
        updates = {'window_end': '2026-10-19', 'window_days': 30, 'items': [{
            'url': 'https://x.com/quietnning/status/2112233429245063201', 'title': 'Research discussion',
            'summary': 'A discussion distinct from its related paper.', 'kind': 'x',
            'review_status': 'approved', 'published_at': '2026-10-19'}]}
        row = build_site.payload(resources['resources'], CATEGORIES, updates, 'assets')['updates'][0]
        self.assertEqual(row['image_label'], 'Related paper figure')
        self.assertTrue(row['images'])
        html = build_site.initial_cards([row])
        self.assertIn('data-gallery=', html)
        self.assertIn('Related paper figure', html)

    def test_reviewed_image_derivative_checks_hash_and_strips_local_paths(self):
        import hashlib
        from PIL import Image
        import fetch_update_media as media
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            original = root / 'private' / 'photo.png'
            original.parent.mkdir()
            Image.new('RGBA', (300, 200), (50, 100, 150, 150)).save(original)
            assets = root / 'assets' / 'news'; assets.mkdir(parents=True)
            photo = {'path': str(original), 'sha256': hashlib.sha256(original.read_bytes()).hexdigest(),
                     'source_url': 'https://pbs.twimg.com/media/source.png', 'alt': 'A chart', 'index': 1}
            with patch.object(media, 'ROOT', root):
                result = media.cache_reviewed_images({'url': 'https://x.com/lab/status/123'}, {'images': [photo]}, assets)
                self.assertNotIn('private', json.dumps(result))
                self.assertTrue((root / result['path']).is_file())
                self.assertEqual(result['images'][0]['source_url'], photo['source_url'])
                photo['sha256'] = 'stale'
                with self.assertRaisesRegex(ValueError, 'hash mismatch'):
                    media.cache_reviewed_images({'url': 'https://x.com/lab/status/123'}, {'images': [photo]}, assets)

    def test_subpage_links_resolve_under_a_project_site(self):
        class Links(HTMLParser):
            def __init__(self):
                super().__init__()
                self.links = []
            def handle_starttag(self, tag, attrs):
                self.links.extend(value for key, value in attrs if key in ('href', 'src') and value)
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            build_site.build(root)
            for page in root.rglob('*.html'):
                parser = Links()
                parser.feed(page.read_text(encoding='utf-8'))
                for link in parser.links:
                    if link.startswith(('https://', 'http://', '#')):
                        continue
                    path = link.split('?', 1)[0].split('#', 1)[0]
                    target = (page.parent / path).resolve()
                    self.assertTrue(target.is_relative_to(root), link)
                    self.assertTrue(target.is_file() or (target / 'index.html').is_file(), f'{page.name}: {link}')
            library = (root / 'library/index.html').read_text(encoding='utf-8')
            resources, _ = load()
            self.assertEqual(library.count('class="work-row"'), len(resources['resources']))
            self.assertNotIn('Read full description', library)


if __name__ == '__main__': unittest.main()
