"""Checks public export boundaries and safe research data rendering."""
import json
import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path

import build_site
from build import CATEGORIES, load


class SiteTests(unittest.TestCase):
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
        reviewed = {'slug': slug, 'title': 'Reviewed paper', 'summary': 'Full-text-reviewed contribution.'}
        self.assertEqual(build_site.paper_pages([reviewed], updates)[slug], reviewed)

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
