(() => {
  'use strict';
  const data = JSON.parse(document.getElementById('research-data').textContent);
  const page = document.body.dataset.page;
  const library = page === 'library';
  const legacy = {library: data.paths.library, today: data.paths.updates + '?period=today', about: data.paths.about};
  if (page === 'home' && Object.hasOwn(legacy, location.hash.slice(1))) {
    location.replace(legacy[location.hash.slice(1)]);
    return;
  }
  if (page === 'about' || page === 'paper') return;

  const search = document.getElementById('search');
  const cards = document.getElementById('cards');
  const results = document.getElementById('results');
  const more = document.getElementById('load-more');
  const params = new URLSearchParams(location.search);
  const today = new Intl.DateTimeFormat('sv-SE', {timeZone:'America/New_York',year:'numeric',month:'2-digit',day:'2-digit'}).format(new Date());
  const batch = library ? 20 : page === 'home' ? 8 : 12;
  const groups = ['All', ...new Set(data.updates.map(item => item.source_group))];
  let period = params.get('period') === 'today' ? 'today' : 'updates';
  let source = groups.includes(params.get('source')) ? params.get('source') : 'All';
  let theme = Object.hasOwn(data.categories, params.get('theme')) ? params.get('theme') : 'all';
  let year = data.works.some(item => String(item.year) === params.get('year')) ? params.get('year') : 'all';
  let sort = ['oldest','title'].includes(params.get('sort')) ? params.get('sort') : 'newest';
  let limit = batch;
  search.value = params.get('q') || '';
  const esc = value => String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const dateLabel = value => new Date(value.slice(0,10) + 'T12:00:00Z').toLocaleDateString('en-US', {month:'short',day:'numeric',year:'numeric',timeZone:'UTC'});
  const safeURL = value => { try { const url = new URL(value, location.href); return ['http:','https:'].includes(url.protocol) ? esc(value) : '#'; } catch { return '#'; } };
  const links = items => items.map(link => `<a href="${safeURL(link.url)}" target="_blank" rel="noopener noreferrer">${esc(link.label)} ↗</a>`).join('');
  function updateRow(item) {
    const actualImage = item.image && item.image_kind !== 'related-figure';
    const visual = actualImage ? `<a class="update-thumb ${item.image_kind === 'blog' ? 'blog-thumb' : item.image_kind === 'paper' ? 'paper-preview' : ''}" href="${safeURL(item.url)}" target="_blank" rel="noopener noreferrer" aria-label="Open ${esc(item.title)}"><img src="${safeURL(item.image)}" alt="${esc(item.image_alt)}" loading="lazy" width="304" height="210"></a>` : `<div class="update-thumb source-thumb" aria-hidden="true"><strong>${esc(item.source_mark)}</strong><span>${esc(item.source)}</span></div>`;
    const discussion = item.kind === 'paper' ? `<a class="discussion-link" href="${safeURL(data.paths.papers + item.slug + '/#discussion')}">Discuss ↗</a>` : '';
    return `<article class="update-row">${visual}<div class="update-body"><div class="item-meta"><span class="source-name">${esc(item.source)}</span><span class="content-type kind-${esc(item.kind)}">${esc(item.content_label)}</span><time datetime="${esc(item.published_at)}">${dateLabel(item.published_at)}</time></div><h3><a href="${safeURL(item.url)}" target="_blank" rel="noopener noreferrer">${esc(item.title)}</a></h3><p class="item-description">${esc(item.summary)}</p><div class="resource-links">${links(item.links)}${discussion}</div></div></article>`;
  }
  function workRow(item) {
    const extra = item.discovery_use ? `<details class="work-details"><summary>Discovery relevance</summary><p>${esc(item.discovery_use)}</p></details>` : '';
    const detailURL = data.paths.papers + item.slug + '/';
    return `<article class="work-row" id="${esc(item.id)}"><div class="work-meta"><span class="work-year">${item.year}</span><span>${esc(item.venue)}</span><a class="work-theme" href="${safeURL(data.paths.library + '?theme=' + encodeURIComponent(item.category))}">${esc(data.categories[item.category])}</a></div><h2><a href="${safeURL(detailURL)}">${esc(item.title)}</a></h2><p class="work-authors">${esc(item.authors)}</p><p class="item-description">${esc(item.summary)}</p>${extra}<div class="resource-links">${links(item.links)}<a class="discussion-link" href="${safeURL(detailURL + '#discussion')}">Discuss ↗</a></div></article>`;
  }
  function timeline(rows) {
    let previous = '';
    return rows.map((item, index) => {
      const start = item.published_at !== previous;
      previous = item.published_at;
      const count = rows.filter(row => row.published_at === previous).length;
      return (start ? `${index ? '</section>' : ''}<section class="date-group" aria-label="${dateLabel(previous)}"><h3 class="date-heading"><time datetime="${esc(previous)}">${dateLabel(previous)}</time><span>${count} ${count === 1 ? 'update' : 'updates'}</span></h3>` : '') + updateRow(item) + (index === rows.length - 1 ? '</section>' : '');
    }).join('');
  }
  function updateAddress() {
    const next = new URL(location.href);
    next.search = '';
    const values = library ? {q:search.value.trim(),theme:theme === 'all' ? '' : theme,year:year === 'all' ? '' : year,sort:sort === 'newest' ? '' : sort} : {q:search.value.trim(),period:period === 'today' ? period : '',source:source === 'All' ? '' : source};
    Object.entries(values).forEach(([key,value]) => { if (value) next.searchParams.set(key,value); });
    history.replaceState(null, '', next);
  }
  function render() {
    const query = search.value.trim().toLocaleLowerCase();
    let rows = (library ? data.works : data.updates).filter(item =>
      (library || period !== 'today' || item.published_at === today) &&
      (library || source === 'All' || item.source_group === source) &&
      (!library || theme === 'all' || item.category === theme) &&
      (!library || year === 'all' || String(item.year) === year) &&
      (!query || [item.title,item.summary,item.discovery_use,item.authors,item.source,item.content_label,item.venue,data.categories[item.category]].join(' ').toLocaleLowerCase().includes(query)));
    if (library) rows.sort(sort === 'title' ? (a,b) => a.title.localeCompare(b.title) : (a,b) => (sort === 'oldest' ? a.year-b.year : b.year-a.year) || a.title.localeCompare(b.title));
    const visible = rows.slice(0,limit);
    cards.innerHTML = library ? visible.map(workRow).join('') : timeline(visible);
    document.getElementById('empty').hidden = rows.length > 0;
    document.getElementById('empty').textContent = !library && period === 'today' && !query && source === 'All' ? 'No publications today yet. Explore the last 30 days for recent research.' : `No ${library ? 'works' : 'updates'} match these filters. Try another keyword.`;
    document.getElementById('result-count').textContent = `${rows.length} ${library ? rows.length === 1 ? 'work' : 'works' : rows.length === 1 ? 'update' : 'updates'}`;
    more.hidden = rows.length <= limit;
    more.innerHTML = `Load more ${library ? 'works' : 'updates'} <span aria-hidden="true">↓</span><span class="remaining-count">${rows.length - visible.length} remaining</span>`;
    if (library) {
      document.querySelectorAll('[data-theme]').forEach(button => button.setAttribute('aria-pressed',String(button.dataset.theme === theme)));
      document.getElementById('theme-question').textContent = data.questions[theme] || 'Eight research questions. One connected discovery process.';
    } else {
      document.querySelectorAll('[data-period]').forEach(button => { const active = button.dataset.period === period; button.setAttribute('aria-selected',String(active)); button.tabIndex = active ? 0 : -1; });
      document.getElementById('filters').querySelectorAll('button').forEach(button => button.setAttribute('aria-pressed',String(button.dataset.source === source)));
      results.setAttribute('aria-labelledby','tab-' + period);
    }
  }
  function changed() { limit = batch; updateAddress(); render(); }
  if (library) {
    const years = document.getElementById('year'), order = document.getElementById('sort');
    years.value = year; order.value = sort;
    years.addEventListener('change', () => { year = years.value; changed(); });
    order.addEventListener('change', () => { sort = order.value; changed(); });
    document.querySelectorAll('[data-theme]').forEach(button => button.addEventListener('click', () => { theme = button.dataset.theme; changed(); }));
  } else {
    document.getElementById('today-count').textContent = data.updates.filter(item => item.published_at === today).length;
    groups.forEach(group => { const button = document.createElement('button'); button.type = 'button'; button.textContent = group; button.dataset.source = group; button.addEventListener('click', () => { source = group; changed(); }); document.getElementById('filters').appendChild(button); });
    document.querySelectorAll('[data-period]').forEach(button => {
      button.addEventListener('click', () => { period = button.dataset.period; changed(); });
      button.addEventListener('keydown', event => { if (['ArrowLeft','ArrowRight','Home','End'].includes(event.key)) { event.preventDefault(); period = event.key === 'Home' ? 'updates' : event.key === 'End' ? 'today' : period === 'today' ? 'updates' : 'today'; changed(); document.getElementById('tab-' + period).focus(); } });
    });
  }
  search.addEventListener('input', changed);
  more.addEventListener('click', () => { const before = cards.querySelectorAll('article').length; limit += batch; render(); const firstNew = cards.querySelectorAll('article')[before]; if (firstNew) { const link = firstNew.querySelector(library ? 'h2 a' : 'h3 a'); if (link) link.focus({preventScroll:true}); } });
  if (matchMedia('(max-width:600px)').matches) document.querySelectorAll('.theme-panel').forEach(panel => panel.open = false);
  render();
})();
