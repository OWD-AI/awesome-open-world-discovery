# Contributing

We welcome relevant papers, official projects, datasets, models, and corrections. See the [scope and category guide](docs/taxonomy.md) before suggesting a resource.

## Add or update a work

Edit `data/resources.json`. Keep one entry per work, combining its paper, official code, project, model, and dataset links. Preserve stable IDs and choose a category by the primary contribution. Record authors, paper-time affiliations, publication venue and year, and supporting primary sources. Distinguish preprints, workshops, conferences, and journal publications; submission alone is not acceptance evidence.

For papers, download the full text and inspect relevant body or technical sections before admission. Record the method, evidence, relevance, limitations, consulted pages, and classification rationale in `data/paper-reviews.json`. Record the downloaded version, page count, and SHA-256 in `data/fulltext-manifest.json`. Downloading a PDF does not establish review completion or independent reproduction. PDFs and extracted text stay in the ignored `.local/fulltexts/` cache. The optional acquisition helper requires `pypdf` and Poppler's `pdftotext`:

```bash
python scripts/fetch_fulltexts.py --ids WORK_ID
```

Verify that artifacts belong to the work. Label model weights, adapters, datasets, and collections separately; a cited base model or a Hugging Face paper page is not an author-released checkpoint. Missing links mean unverified availability, not proof that no artifact exists.

For benchmarks, also update `data/benchmarks.json`. Distinguish simulations, recorded data, executed computation, and new physical measurements. Describe allowed interactions, evaluation, reward, reset and branching support, access requirements, and limitations. Mark unknown or proposed capabilities explicitly.

Search candidates, screening logs, link-check reports, and other intermediate curation files belong in ignored local storage, rather than the public catalog. Never commit credentials, personal watchlists, or private documents.

## Build and validate

```bash
python scripts/build.py
python scripts/validate.py
python scripts/build.py --check
python scripts/test_site.py
```

The build uses Python's standard library to generate `README.md`, `references.bib`, `docs/benchmarks.md`, and the local website preview `docs/updates.html`. Change generated content through its JSON sources or `scripts/build.py`. Optional URL checks write to `.local/link-check.json`:

```bash
python scripts/check_links.py
```

## Website and daily updates

The [research observatory](https://owd-ai.github.io/awesome-open-world-discovery/) shows today's publications, a rolling 30-day feed, and a searchable library. `data/updates.json` contains source-checked news with original publication dates; admission to this feed does not automatically admit a paper to the reviewed catalog. README shows only the latest ten papers and links to the website. Today uses America/New_York.

Edit website templates in `site/`. Build the public artifact with `python scripts/build_site.py`; `.github/workflows/pages.yml` validates and deploys it on main-branch source or data pushes. No second website repository is required. The daily monitor lives separately and pushes feed updates as `gary23ai`. `scripts/publish_site.py --redeploy` can request a manual Pages deployment.

The homepage introduces the framework and shows date-grouped updates. `/updates/`, `/library/`, and `/about/` have separate layouts. Library searches, themes, years, and sorting are shareable through URL parameters. Content uses ordinary page scrolling and progressive loading; keep mobile theme filters collapsible. `docs/updates.html` remains a self-contained local homepage preview with links to the public subpages.

Each work has a `/papers/` detail page with a stable slug derived from its canonical source URL. arXiv version URLs resolve to the same identity, and a news paper keeps that identity when admitted to the catalog. Preserve these URLs to preserve their discussions. The detail page uses giscus with GitHub Discussions, strict pathname mapping, and reactions enabled. Visitors sign in with GitHub; these are account-based comments and reactions, not anonymous IP-limited votes. No custom backend or authentication secrets are required. The giscus GitHub App must be installed on this repository with metadata read and Discussions read/write permissions. Moderate conversations through GitHub. `giscus.json` limits embedding to the public website origin; local previews do not load live comments.

`data/updates.json` keeps permanent, source-checked paper metadata in `paper_pages`, maintained by the daily monitor, so discussion pages survive expiry from the rolling news window. This archive does not admit papers into the reviewed library or contain downloaded full texts. Preserve it when editing the feed.

`scripts/fetch_update_media.py` uses PyMuPDF and Pillow to cache paper previews and first-party covers in `assets/news/`. Attribution and image provenance are recorded in `data/update-media.json`. Inspect changed previews; unavailable images fall back to source marks.

The local monitor continuously reviews queued candidates between periodic source searches. An included paper enters the Library only after complete author and paper-time institution attribution is matched to the reviewed PDF and any benchmark usage profile is supplied. Admission updates `resources.json`, `paper-reviews.json`, and `fulltext-manifest.json` together, plus `benchmarks.json` when applicable. Source checks and catalog admission have separate requirements; incomplete evidence stays pending. Existing catalog entries are preserved, and papers are deduplicated by canonical source URL.

Journal recall covers Nature, Nature Machine Intelligence and Nature Computational Science through official RSS and focused publisher searches. Use the same discovery-relevance criteria as for other venues. Record verified journal publication metadata separately from the exact downloaded version used for body review; do not conflate preprint results or affiliations with a later journal version. Historical additions belong in the Library and retain their original publication dates.

The canonical logo is `assets/owd-mark.svg`; export its PNG and favicon with ImageMagick. The white-background variant is `assets/owd-mark-light.svg` with a matching PNG. The README framework is `assets/open-world-discovery.png`; the website uses its transparent sibling `assets/open-world-discovery-web.png`. Keep the discovery point centered in the ring opening and check both desktop and narrow layouts after visual changes.
