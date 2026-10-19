"""Generate the English awesome list and benchmark index using the standard library."""
import argparse
import hashlib
import html
import json
from datetime import date, timedelta
from itertools import groupby
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = {
    'foundations': 'Discovery Foundations',
    'causality': 'Discovery Representations',
    'sci_methods': 'Discovery Reasoning',
    'learning': 'Discovery Training',
    'adaptation': 'Continual Discovery',
    'systems': 'Discovery Systems',
    'open_ended': 'Open-Ended Discovery',
    'benchmarks': 'Discovery Evaluation',
}
CATEGORY_GUIDE = {
    'foundations': ('📚', 'What constitutes a discovery?'),
    'causality': ('🧩', 'What representations enable discovery?'),
    'sci_methods': ('🔬', 'How should agents formulate and test hypotheses?'),
    'learning': ('🧠', 'How can we train agents to discover?'),
    'adaptation': ('🔄', 'How can agents learn from ongoing investigations?'),
    'systems': ('🛠️', 'How can we build reliable discovery systems?'),
    'open_ended': ('🌱', 'How can agents expand the scope of discovery?'),
    'benchmarks': ('📊', 'How can we measure progress in discovery?'),
}
RELATED = [
    ('Awesome LLM Scientific Discovery', 'https://github.com/HKUST-KnowComp/Awesome-LLM-Scientific-Discovery', 'Scientific-method and autonomy taxonomy'),
    ('Awesome Open-Ended AI', 'https://github.com/jennyzzt/awesome-open-ended', 'Open-ended learning, environment generation and evolution'),
    ('Awesome Self-Improving Agents', 'https://github.com/selfimproving-agent/Awesome-Self-Improving-Agents', 'Foundation-model versus scaffolding improvement'),
    ('Awesome AI Scientist', 'https://github.com/ResearAI/Awesome-AI-Scientist', 'Research lifecycle and scientific agent systems'),
    ('Awesome AI Scientists', 'https://github.com/tsinghua-fib-lab/Awesome-AI-Scientists', 'Functional roles, collaboration and research domains'),
    ('Awesome Test-Time LLMs', 'https://github.com/Dereck0602/Awesome_Test_Time_LLMs', 'Earlier test-time computing literature; supplement recent papers'),
    ('Awesome LLM Causal Reasoning', 'https://github.com/chendl02/Awesome-LLM-Causal-Reasoning', 'Language models and causal reasoning'),
    ('Awesome Causal Discovery', 'https://github.com/Ewillingfly/AwesomeCausalDiscovery', 'Broader causal-discovery methods'),
]
PROFILE_GROUPS = {
    'simulated': 'Simulated Worlds and Digital Twins',
    'analysis': 'Fixed-Data Scientific Analysis',
    'computational': 'Executable Computational Research',
    'recorded': 'Recorded Experimental Outcomes',
    'physical': 'Live Physical Experiments',
    'proposed': 'Proposed Physical Backends',
}
FEEDBACK_LABELS = {
    'synthetic-rules': 'Synthetic rules',
    'probabilistic-model': 'Probabilistic model',
    'scientific-simulator': 'Scientific simulator',
    'synthetic-scm': 'Synthetic SCM',
    'synthetic-data': 'Synthetic data',
    'real-data': 'Real data',
    'executed-computation': 'Executed programs + evaluators',
    'real-experiment-records': 'Recorded experiments',
    'scientific-datasets-and-hidden-verifiers': 'Scientific data + verifiers',
    'new-physical-measurements': 'Physical measurements',
    'digital-twin': 'Digital twin',
    'planned-physical-backend': 'Planned physical backend',
}
INTERACTION_LABELS = {
    'interactive-simulator': 'Interactive simulator',
    'task-demonstrations': 'Task demonstrations',
    'fixed-data-analysis': 'Data analysis',
    'fixed-data-code-execution': 'Analysis + code',
    'finite-pool-query': 'Finite-pool queries',
    'offline-data': 'Offline data',
    'remote-device-jobs': 'Remote device jobs',
    'fixed-data-tool-execution': 'Analysis + tools',
    'budgeted-pool-jobs': 'Budgeted pool queries',
    'budgeted-simulator-jobs': 'Budgeted simulator',
    'proposed-device-jobs': 'Proposed device jobs',
    'human-mediated-lab': 'Human-mediated laboratory',
    'computational-experimentation': 'Computational experiments',
}
STATUS_LABELS = {
    'public-code': 'Code',
    'public-data-code': 'Data + code',
    'public-data': 'Data',
    'paper-described': 'Paper-described',
    'preprint-described': 'Preprint-described',
    'source-reported-tooling': 'Reported tooling',
    'access-required-author-reported': 'Access required',
    'early-project-author-reported': 'Early project',
    'contract-only': 'Contract only',
}


def load():
    resources = json.loads((ROOT / 'data/resources.json').read_text(encoding='utf-8'))
    benchmarks = json.loads((ROOT / 'data/benchmarks.json').read_text(encoding='utf-8'))
    return resources, benchmarks


def anchor(name):
    return f'<a id="{name}"></a>'


def profile_group(profile):
    if profile['status'] == 'contract-only':
        return 'proposed'
    if profile['new_physical_experiments'] is True:
        return 'physical'
    if profile['feedback'] == 'real-experiment-records':
        return 'recorded'
    if profile['feedback'] in {'synthetic-rules', 'probabilistic-model', 'scientific-simulator', 'synthetic-scm', 'digital-twin'}:
        return 'simulated'
    if profile.get('evaluation_family') == 'computational-research':
        return 'computational'
    return 'analysis'


def extlinks(resource):
    labels = {'Official blog': 'Blog', 'HF Dataset': 'HF Dataset', 'Related list': 'List'}
    return ' · '.join(f"[{labels.get(link['label'], link['label'])}]({link['url']})" for link in resource['links'])


def publication_label(resource):
    p = resource['publication']
    suffix = ' (preprint)' if p['type'] == 'preprint' else ' (chapter)' if p['type'] == 'book-chapter' else ''
    return f"{p['venue']} {p['year']}{suffix}"


def publication_link(resource):
    return f"[{publication_label(resource)}]({resource['publication']['source_url']})"


def attribution(resource, full=False):
    authors = resource.get('display_authors', resource['authors'])
    author_text = ', '.join(authors if full or len(authors) <= 4 else authors[:1])
    if not full and len(authors) > 4:
        author_text += ' et al.'
    institutions = resource['institutions']
    visible = institutions if full or len(institutions) <= 3 else institutions[:3]
    institution_text = '; '.join(visible)
    if len(visible) < len(institutions):
        institution_text += f"; +{len(institutions) - len(visible)} institutions"
    return author_text + (' · ' + institution_text if institution_text and institution_text != author_text else '')


def recent_updates():
    data = json.loads((ROOT / 'data/updates.json').read_text(encoding='utf-8'))
    end = date.fromisoformat(data['window_end'])
    start = end - timedelta(days=data['window_days'] - 1)
    items = [item for item in data['items'] if item.get('review_status') == 'approved'
             and start <= date.fromisoformat(item['published_at'][:10]) <= end]
    return data, sorted(items, key=lambda item: (item['published_at'], item['title']), reverse=True)


def updates_markdown():
    data, items = recent_updates()
    papers = [item for item in items if item['kind'] == 'paper'][:10]
    out = [anchor('updates'), '', '## 📰 Latest Papers', '',
           '**[Explore the research observatory →](https://owd-ai.github.io/awesome-open-world-discovery/#updates)**', '',
           f"The latest 10 source-checked papers from our daily monitor · Updated {data['updated_at'][:10]}.", '',
           "Visit the website for summaries, figures, today's updates, and the full research library.", '']
    if not papers:
        return out + ['No source-checked papers are available for this interval.', '']
    out += ['| Date | Paper |', '| --- | --- |']
    for item in papers:
        title = item['title'].replace('|', '\\|').replace('\n', ' ')
        out.append(f"| {item['published_at'][:10]} | [{title}]({item['url']}) |")
    out.append('')
    return out


def updates_html():
    from build_site import render
    data, benchmarks = load()
    return render(data['resources'], benchmarks, CATEGORIES, inline=True)


def readme(data, benchmarks):
    resources = data['resources']
    counts = {category: sum(r['category'] == category for r in resources) for category in CATEGORIES}
    out = [
        '<p align="center">',
        f'  <img src="assets/owd-mark.svg?v={hashlib.sha256((ROOT / "assets/owd-mark.svg").read_bytes()).hexdigest()[:10]}" width="72" height="72" alt="Open World Discovery: exploring beyond a known boundary">',
        '</p>', '',
        '<h1 align="center">Awesome Open World Discovery</h1>', '',
        '<p align="center">',
        '  <strong>Acquire evidence. Discover mechanisms. Learn to discover.</strong><br>',
        '  A curated research guide to discovery agents, learning methods, and evaluation.',
        '</p>', '',
        '<p align="center">',
        '  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>',
        f'  <a href="#contents"><img src="https://img.shields.io/badge/works-{len(resources)}-2563eb?style=flat-square" alt="{len(resources)} curated works"></a>',
        f'  <a href="docs/benchmarks.md"><img src="https://img.shields.io/badge/environment_profiles-{len(benchmarks["profiles"])}-0f766e?style=flat-square" alt="{len(benchmarks["profiles"])} environment profiles"></a>',
        '  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/contributions-welcome-7c3aed?style=flat-square" alt="Contributions welcome"></a>',
        '</p>', '',
        '<p align="center">',
        '  <a href="https://owd-ai.github.io/awesome-open-world-discovery/">Research observatory ↗</a> · <a href="#what-is-owd">What is OWD?</a> · <a href="#why-owd">Why this focus?</a> · <a href="#updates">Latest papers</a> · <a href="#contents">Browse the list</a> · <a href="CONTRIBUTING.md">Contribute</a>',
        '</p>', '',
        f"<p align=\"center\"><sub>Literature checked through {data['updated']} · Papers, author blogs, code, and benchmarks</sub></p>", '',
        anchor('what-is-owd'), '', '## 🧭 What is Open World Discovery?', '',
        '> **Our working definition:** Open World Discovery connects research on how agents acquire, construct, and revise knowledge through exploration and learning in incompletely understood or changing worlds. This broad agenda brings together discovering unknowns, developing verifiable and reusable knowledge, and improving the ability to discover.', '',
        'The central loop connects **hypotheses, informative actions, evidence, and revision**. Its outputs should be checked against independent observations, interventions, or executable/formal verifiers. Learning to discover asks how experience improves this loop across investigations.', '',
        '![A discovery agent sends experiments to a partially known world, revises its hypotheses using returned evidence, and can expand its knowledge boundary. A separate learning loop improves discovery across investigations.](assets/open-world-discovery.png)', '',
        '[View the diagram at full size](assets/open-world-discovery.png)', '',
        '**What makes the world open?** The current model or problem formulation may be incomplete: evidence can call for a different mechanism, a new variable, or a revised question. Openness is relative to what the agent is given and allowed to change. Bounded discovery tasks help study individual components; see the [scope guide](docs/taxonomy.md#positioning).', '',
        anchor('why-owd'), '', '### Why Open World Discovery?', '',
        anchor('related-directions'), '',
        'Discovery involves deciding what to investigate, gathering evidence, testing explanations, and carrying knowledge into future investigations. Representations, reasoning, training, and agent systems each contribute to this process.', '',
        '**We use Open World Discovery as a shared research agenda connecting these contributions.** It brings together work on learning from unknowns, generating and validating discoveries, and improving discovery capabilities over time. By organizing methods, systems, and evaluation around common questions, this list aims to help researchers understand how individual advances can support the discovery process as a whole. See [the research scope and connections to related fields](docs/taxonomy.md#positioning).', '',
        '**Download the catalog:** [BibTeX](references.bib) · [JSON](data/resources.json)', '',
    ]
    out += updates_markdown()
    out += [anchor('contents'), '', '## 🗂️ Contents', '',
        '| Topic | Research question | Works |',
        '| --- | --- | ---: |',
    ]
    for category, title in CATEGORIES.items():
        icon, question = CATEGORY_GUIDE[category]
        out.append(f'| {icon} [{title}](#{category}) | {question} | {counts[category]} |')
    out += ['', '[🔗 Related lists](#related) · [🤝 Contributing](#contributing)', '',
            'Each work appears once under its primary contribution; see the [classification guide](docs/taxonomy.md#categories) for category scopes. Entries are grouped by publication year, newest first. Each work keeps its paper, code, project, and dataset links together, followed by authors and paper-time affiliations. Full attribution is recorded in the [catalog data](data/resources.json).', '']
    for category, title in CATEGORIES.items():
        icon, question = CATEGORY_GUIDE[category]
        out += [anchor(category), '', f'## {icon} {title}', '', f'*{question}*', '']
        if category == 'benchmarks':
            out += ['For environment types, physical experiment access, and training interfaces, see the [benchmark guide](docs/benchmarks.md).', '']
        entries = sorted((r for r in resources if r['category'] == category), key=lambda r: (-r['year'], r['title'].lower()))
        for year, group in groupby(entries, key=lambda r: r['year']):
            out += [f'### {year}', '']
            for resource in group:
                medium = ' <sup>blog</sup>' if resource['kind'] == 'blog' else ' <sup>project</sup>' if resource['kind'] == 'project' else ''
                venue = f" · *{publication_link(resource)}*" if resource['kind'] == 'paper' else ''
                out += [f"- {anchor(resource['id'])}**{resource['title']}**{medium}{venue} · {extlinks(resource)}<br>", f"  {attribution(resource)}"]
            out.append('')
        out += ['[↑ Contents](#contents)', '']
    out += [anchor('related'), '', '## 🔗 Related Lists', '']
    out.extend(f'- [{name}]({url}) — {description}.' for name, url, description in RELATED)
    out += [
        '', anchor('contributing'), '', '## 🤝 Contributing', '',
        'Suggestions and corrections are welcome. Prefer primary papers and author explanations; merge related artifacts into one entry. See the [contribution guide](CONTRIBUTING.md).', '',
    ]
    return '\n'.join(out)


def benchmark_doc(resources, data):
    by_id = {resource['id']: resource for resource in resources}
    out = [
        '# Benchmarks and Environments', '',
        '[← Main list](../README.md) · [Structured profiles](../data/benchmarks.json)', '',
        f"**{len(data['profiles'])} usage profiles** · Updated **{data['updated']}**", '',
        'Compare environments by feedback source and interaction. Each row describes a usage mode; a single project can appear in several groups. Expand the notes below each table for sources, limitations, and training interfaces.', '',
        'Availability is source-reported; implementations have not been independently reproduced here.', '',
        'Laboratory demonstrations are included for comparison with benchmark environments. They are labeled as demonstrations and do not imply a standardized public benchmark or open device access.', '',
        anchor('contents'), '', '## Contents', '',
    ]
    out.extend(f'- [{title}](#{group})' for group, title in PROFILE_GROUPS.items())
    out.append('')
    for group, title in PROFILE_GROUPS.items():
        out += [anchor(group), '', f'## {title}', '']
        if group == 'simulated':
            out += ['Feedback is generated by rules, probabilistic models, or simulators. These modes do not collect new physical measurements.', '']
        elif group == 'analysis':
            out += ['Agents analyze fixed real or synthetic datasets. Code and tool execution do not collect new physical measurements.', '']
        elif group == 'computational':
            out += ['Agents run, train, modify or replicate computational experiments. Feedback comes from executed programs and task evaluators; the underlying tasks can use real data, synthetic data or no dataset. These modes do not collect new physical measurements.', '']
        elif group == 'recorded':
            out += ['Queries or analyses use measurements already collected. This does not create new physical measurements outside the recorded pool.', '']
        elif group == 'physical':
            out += ['New measurements come from a physical device. Access, throughput, preparation, and reset conditions must be established separately.', '']
        elif group == 'proposed':
            out += ['Interface contracts and planned integrations are listed separately from demonstrated live execution.', '']
        profiles = [profile for profile in data['profiles'] if profile_group(profile) == group]
        out += ['| Environment / Track | Feedback | Interaction | Availability |', '| --- | --- | --- | --- |']
        for profile in profiles:
            out.append(f"| [{profile['name']}](#{profile['id']}) | {FEEDBACK_LABELS[profile['feedback']]} | {INTERACTION_LABELS[profile['interaction']]} | {STATUS_LABELS[profile['status']]} |")
        out.append('')
        for profile in profiles:
            resource = by_id[profile['resource_id']]
            physical = 'Yes' if profile['new_physical_experiments'] is True else 'No' if profile['new_physical_experiments'] is False else 'Unverified'
            out += [
                anchor(profile['id']), '', '<details>', f"<summary>{profile['name']} — details</summary>", '',
                f"[Work](../README.md#{resource['id']}) · [Source]({profile['evidence']})", '',
                f"**Focus:** {profile['focus']}", '',
                '**Openness:** ' + ', '.join(f'`{tag}`' for tag in profile['openness']), '',
                f"**New physical measurements:** {physical}", '',
                f"**Limits:** {profile['limits']}", '',
                '| Training Interface | Source-Reported Support |', '| --- | --- |',
                f"| Reward / evaluator | {profile['training']['reward']} |",
                f"| Reset | {profile['training']['reset']} |",
                f"| Branching | {profile['training']['branching']} |", '',
                '</details>', '',
            ]
        out += ['[↑ Contents](#contents)', '']
    return '\n'.join(out)


def outputs():
    data, benchmarks = load()
    result = {'README.md': readme(data, benchmarks), 'docs/benchmarks.md': benchmark_doc(data['resources'], benchmarks), 'docs/updates.html': updates_html()}
    bib = []
    for resource in data['resources']:
        if resource['kind'] == 'paper':
            paper = next(link['url'] for link in resource['links'] if link['label'] == 'Paper')
            authors = ' and '.join(resource.get('display_authors', resource['authors']))
            pub=resource['publication']
            kind={'conference':'inproceedings','workshop':'inproceedings','journal':'article','book-chapter':'incollection'}.get(pub['type'],'misc')
            fields=dict(title='{'+pub.get('title',resource['title'])+'}',author=authors,year=pub['year'],url=pub['source_url'])
            if pub['type']=='journal':fields['journal']=pub.get('journal',pub['venue'])
            elif pub['type'] in {'conference','workshop','book-chapter'}:fields['booktitle']=pub.get('booktitle',pub['venue'])
            else:fields['howpublished']='arXiv preprint'
            for field in ['doi','volume','number','pages','publisher']:
                if pub.get(field):fields[field]=pub[field]
            fields['note']='Catalog attribution follows the consulted version; verify final publisher author list and citation details.'
            if pub.get('note'):fields['note']+=' '+pub['note']
            bib.append('@'+kind+'{'+resource['id']+',\n'+',\n'.join('  '+key+' = {'+str(value)+'}' for key,value in fields.items())+'\n}')
    result['references.bib'] = '\n\n'.join(bib) + '\n'
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    stale = []
    for name, text in outputs().items():
        path = ROOT / name
        if args.check:
            if not path.exists() or path.read_text(encoding='utf-8') != text:
                stale.append(name)
        else:
            with path.open('w', encoding='utf-8', newline='\n') as file:
                file.write(text)
    if stale:
        raise SystemExit('Stale generated views: ' + ', '.join(stale))
    print('Generated views are current.' if args.check else 'Built catalog, benchmark guide, website preview, and BibTeX.')
