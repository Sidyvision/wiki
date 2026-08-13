import os, re, json, html
HERE = os.path.dirname(os.path.abspath(__file__))

ROOT = os.path.expanduser("~/depot-lecture")
INCLUDE_TOP = ["rd", "doctrinal", "hermeneutique"]
EXCLUDE_DIRS = {"assets-instrument"}
EXCLUDE_SLUGS = {"CLAUDE"}

def parse_frontmatter(text):
    m = re.match(r'^---\n(.*?)\n---\n(.*)$', text, re.DOTALL)
    if not m:
        return {}, text
    fm_raw, body = m.group(1), m.group(2)
    fm = {}
    for line in fm_raw.splitlines():
        mm = re.match(r'^(\w[\w_]*):\s*(.*)$', line)
        if mm:
            key, val = mm.group(1), mm.group(2).strip()
            if key not in fm:
                fm[key] = val.strip('"').strip("'")
    return fm, body

def inline_fmt(s):
    # order matters: bold before italic, wikilinks last (targets may contain other chars)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<!\*)\*([^*\n]+?)\*(?!\*)', r'<em>\1</em>', s)
    s = re.sub(r'`([^`]+?)`', r'<code>\1</code>', s)
    s = re.sub(r'\[\[([^\]]+?)\]\]', lambda m: '<wl target="%s"></wl>' % html.escape(m.group(1), quote=True), s)
    return s

def md_to_html(body):
    lines = body.split('\n')
    out = []
    para = []
    list_buf = []
    quote_buf = []

    def flush_para():
        if para:
            out.append('<p>' + ' '.join(inline_fmt(l) for l in para) + '</p>')
            para.clear()
    def flush_list():
        if list_buf:
            out.append('<ul>' + ''.join('<li>'+inline_fmt(l)+'</li>' for l in list_buf) + '</ul>')
            list_buf.clear()
    def flush_quote():
        if quote_buf:
            out.append('<blockquote>' + ' '.join(inline_fmt(l) for l in quote_buf) + '</blockquote>')
            quote_buf.clear()
    def flush_all():
        flush_para(); flush_list(); flush_quote()

    for raw in lines:
        line = html.escape(raw, quote=False)
        stripped = line.strip()
        if stripped == '':
            flush_all()
            continue
        hm = re.match(r'^(#{1,6})\s+(.*)$', stripped)
        if hm:
            flush_all()
            level = min(len(hm.group(1)) + 1, 6)
            out.append('<h%d>%s</h%d>' % (level, inline_fmt(hm.group(2)), level))
            continue
        qm = re.match(r'^&gt;\s?(.*)$', stripped)
        if qm:
            flush_para(); flush_list()
            quote_buf.append(qm.group(1))
            continue
        lm = re.match(r'^[-*]\s+(.*)$', stripped)
        if lm:
            flush_para(); flush_quote()
            list_buf.append(lm.group(1))
            continue
        flush_list(); flush_quote()
        para.append(stripped)
    flush_all()
    return '\n'.join(out)

entries_by_dir = {}
slug_index = {}  # slug -> (dirKey, idx, title)

for top in INCLUDE_TOP:
    topdir = os.path.join(ROOT, top)
    if not os.path.isdir(topdir):
        continue
    for dirpath, dirnames, filenames in os.walk(topdir):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS and not d.startswith('.')]
        rel = os.path.relpath(dirpath, ROOT)
        md_files = sorted(f for f in filenames if f.endswith('.md'))
        if not md_files:
            continue
        entries = []
        for f in md_files:
            slug = f[:-3]
            if slug in EXCLUDE_SLUGS:
                continue
            fp = os.path.join(dirpath, f)
            try:
                with open(fp, 'r', encoding='utf-8', errors='replace') as fh:
                    text = fh.read()
            except Exception:
                continue
            fm, body = parse_frontmatter(text)
            title = fm.get('title') or slug
            ftype = fm.get('type', '')
            status = fm.get('status', '')
            bodyHtml = md_to_html(body.strip())
            idx = len(entries)
            entries.append({
                "slug": slug, "title": title, "type": ftype, "status": status,
                "bodyHtml": bodyHtml
            })
            if slug not in slug_index:
                slug_index[slug] = (rel, idx, title)
        if entries:
            entries_by_dir[rel] = entries

# second pass: resolve <wl target="..."> into links or missing spans
def resolve_wl(m):
    target = html.unescape(m.group(1))
    last = target.rsplit('/', 1)[-1]
    hit = slug_index.get(last)
    if hit:
        dirKey, idx, title = hit
        return '<a class="xlink" data-dir="%s" data-idx="%d">%s</a>' % (
            html.escape(dirKey, quote=True), idx, html.escape(title))
    return '<span class="xlink-missing">%s</span>' % html.escape(last)

wl_re = re.compile(r'<wl target="([^"]*)"></wl>')
total_chars = 0
for dirKey, entries in entries_by_dir.items():
    for e in entries:
        e['bodyHtml'] = wl_re.sub(resolve_wl, e['bodyHtml'])
        total_chars += len(e['bodyHtml'])

print("dirs:", len(entries_by_dir), "total entries:", sum(len(v) for v in entries_by_dir.values()))
print("total bodyHtml chars:", total_chars)

with open(os.path.join(HERE, 'library-full.json'), 'w', encoding='utf-8') as f:
    json.dump(entries_by_dir, f, ensure_ascii=False)

print("bytes:", os.path.getsize(os.path.join(HERE, 'library-full.json')))
