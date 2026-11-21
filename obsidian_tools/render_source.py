"""Convert source-correlated published book pages into portable Obsidian Markdown.

Published HTML is used only when every explicit source section anchor survives.
It supplies executed values and rendered diagrams without executing repository code.
The import manifest records the rendered snapshot independently of the Git revision.
"""
from __future__ import annotations

from collections import Counter
from functools import lru_cache
import hashlib
import html as html_std
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import urljoin

import yaml
from lxml import html, etree


@lru_cache(maxsize=4)
def load_macros(repo_name: str) -> dict[str, str]:
    repo = Path(repo_name)
    macros = {}
    listing = subprocess.check_output(
        ['git', 'ls-tree', '-r', '--name-only', 'HEAD', 'mlsysim/mlsysim/notation/data/'], cwd=repo, text=True)
    for path in listing.splitlines():
        if path.endswith(('.yaml', '.yml')) and not path.endswith('exempt.yaml'):
            raw = subprocess.check_output(['git', 'show', 'HEAD:' + path], cwd=repo, text=True)
            doc = yaml.safe_load(raw) or {}
            for symbol in doc.get('symbols', []):
                if symbol.get('macro') and symbol.get('latex'):
                    macros[symbol['macro'].lstrip('\\')] = str(symbol['latex'])
                    for alias in symbol.get('aliases', []):
                        macros[str(alias).lstrip('\\')] = str(symbol['latex'])
    return macros


def expand_macros(text: str, macros: dict[str, str]) -> str:
    text = re.sub(r'\\Glyph(?=\{)', '', text)
    # Registry replacements contain ordinary LaTeX, and can contain another symbol.
    for _ in range(12):
        new = re.sub(r'\\([A-Za-z]+)(?![A-Za-z])', lambda m: ('{' + macros[m.group(1)] + '}') if m.group(1) in macros else m.group(0), text)
        if new == text:
            return text
        text = new
    return text


def _visible_source(text: str) -> str:
    """Remove comments and PDF-only branches while respecting executable fences."""
    text = re.sub(r'<!--.*?-->', '', text, flags=re.S)
    out=[]; stack=[]; fence=None
    for line in text.splitlines():
        f=re.match(r'^\s*(`{3,}|~{3,})',line)
        if f:
            if fence is None: fence=f.group(1)[0]
            elif f.group(1)[0]==fence: fence=None
            if all(stack): out.append(line)
            continue
        if fence is None:
            div=re.match(r'^\s*:{3,}(.*)$',line)
            if div:
                attrs=div.group(1).strip()
                if attrs:
                    hidden=bool(re.search(r'when-format\s*=\s*["\']?(?:pdf|latex)',attrs) or re.search(r'unless-format\s*=\s*["\']?html(?:["\']|\s|$)',attrs))
                    stack.append(not hidden)
                elif stack: stack.pop()
                continue
        if all(stack): out.append(line)
    return '\n'.join(out)


def source_heading_ids(text: str) -> list[str]:
    ids=[]; fence=None
    for line in _visible_source(text).splitlines():
        f=re.match(r'^\s*(`{3,}|~{3,})',line)
        if f:
            if fence is None: fence=f.group(1)[0]
            elif f.group(1)[0]==fence: fence=None
            continue
        if fence is None and re.match(r'^#{1,6}\s',line):
            m=re.search(r'\{#([^\s}]+)',line)
            if m: ids.append(m.group(1))
    return ids


def _sanitize_html_tooltips(raw: str) -> str:
    # Quarto occasionally interpolates resolved <a> cross-references directly
    # into a lightbox title attribute without HTML escaping its quotes. Remove
    # that redundant tooltip before parsing; the real figcaption remains intact.
    pattern = r'(<a\b[^>]*\bclass="[^"]*\blightbox\b[^"]*"[^>]*?)\s+title="(?:(?!</figure>|<section).)*?"(?=>\s*<img\b)'
    return re.sub(pattern,r'\1',raw,flags=re.S)


def _restore_source_headings(raw: str, source: str) -> tuple[str,list[str],list[str]]:
    """Restore headings omitted by the website filter without dropping rendered data.

    A missing heading is restored only when the first substantive paragraph after
    that heading matches the published paragraph, or when the next authored child
    heading is present. This is a structure repair, never an invented numeric value.
    """
    tree=html.fromstring(raw)
    mains=tree.xpath('//main[@id="quarto-document-content"]')
    if not mains:return raw,[],source_heading_ids(source)
    main=mains[0]
    text=_visible_source(source)
    text=re.sub(r'(?ms)^(`{3,}|~{3,}).*?^\1\s*$', '',text)
    matches=list(re.finditer(r'(?m)^(#{1,6})\s+(.+?)\s*\{#([^\s}]+)[^}]*\}\s*$',text))
    present=set(tree.xpath('//@id')); restored=[]; unresolved=[]
    def words(s):
        s=re.sub(r'\\[A-Za-z]+',' ',s)
        return re.findall(r'[a-z]{3,}',s.lower())
    paragraphs=main.xpath('.//p')
    for i,m in enumerate(matches):
        ident=m.group(3)
        if ident in present:continue
        stop=matches[i+1].start() if i+1<len(matches) else len(text)
        following=text[m.end():stop]
        candidates=[p.strip() for p in re.split(r'\n\s*\n',following) if len(p.strip())>70 and not p.lstrip().startswith(('!','|','{{','\\'))]
        target=None
        if candidates:
            sw=words(candidates[0])[:14]
            if len(sw)>=5:
                for para in paragraphs:
                    pw=words(para.text_content())[:14]
                    common=0
                    for a,b in zip(sw,pw):
                        if a!=b:break
                        common+=1
                    if common>=min(7,len(sw)):
                        target=para;break
        if target is None and i+1<len(matches):
            # Missing structural parent followed directly by an existing child.
            nxt=matches[i+1]
            if len(nxt.group(1))>len(m.group(1)) and nxt.group(3) in present:
                xs=main.xpath('.//*[@id=$id]',id=nxt.group(3))
                if xs: target=xs[0]
        if target is None:
            unresolved.append(ident);continue
        heading=etree.Element('h'+str(len(m.group(1))))
        heading.set('id',ident);heading.set('data-anchor-id',ident)
        heading.text=re.sub(r'[*_`$]','',m.group(2))
        target.addprevious(heading)
        present.add(ident);restored.append(ident)
    return html.tostring(tree,encoding='unicode'),restored,unresolved


def _plain_inline(nodes: list) -> str:
    out = []
    for n in nodes:
        if not isinstance(n, dict):
            continue
        t, c = n.get('t'), n.get('c')
        if t == 'Str': out.append(c)
        elif t in ('Space', 'SoftBreak', 'LineBreak'): out.append(' ')
        elif t in ('Code', 'Math'): out.append(c[-1])
        elif isinstance(c, list):
            if t in ('Span', 'Link', 'Image'): out.append(_plain_inline(c[1]))
            else: out.append(_plain_inline(c))
    return ''.join(out)


def _pandoc(value: str, fmt: str) -> dict:
    p = subprocess.run(['pandoc', '-f', fmt, '-t', 'json'], input=value, text=True, capture_output=True)
    if p.returncode:
        raise RuntimeError(p.stderr.strip())
    return json.loads(p.stdout)


def _write_ast(ast: dict) -> str:
    p = subprocess.run(['pandoc', '-f', 'json', '-t', 'gfm+tex_math_dollars', '--wrap=none'],
                       input=json.dumps(ast), text=True, capture_output=True)
    if p.returncode:
        raise RuntimeError(p.stderr.strip())
    return p.stdout


def _drop(el):
    # lxml drop_tree retains tail text, whereas parent.remove would lose it.
    if el.getparent() is not None:
        el.drop_tree()


def _html_ast(raw: str, url: str, macros: dict[str, str]) -> tuple[dict, list[str]]:
    # Supplement registry symbols with historical macros used by this snapshot.
    # Read balanced braces because definitions contain nested LaTeX arguments.
    macros = dict(macros)
    for match in re.finditer(r'\\(?:newcommand|renewcommand)\{\\([A-Za-z]+)\}\s*\{', raw):
        start = match.end(); pos = start; depth = 1
        while pos < len(raw) and depth:
            if raw[pos] == '{' and (pos == 0 or raw[pos-1] != '\\'): depth += 1
            elif raw[pos] == '}' and (pos == 0 or raw[pos-1] != '\\'): depth -= 1
            pos += 1
        if depth == 0:
            macros.setdefault(match.group(1), html_std.unescape(raw[start:pos-1]))
    tree = html.fromstring(raw)
    mains = tree.xpath('//main[@id="quarto-document-content"]') or tree.xpath('//main')
    if not mains:
        raise ValueError('Published response has no book article')
    main = mains[0]
    anchors = []
    removable = ('quarto-title-block', 'chapter-concept-map', 'code-copy-button', 'anchorjs-link',
                 'header-section-number', 'quarto-appendix-bibtex', 'quarto-title-meta', 'quarto-other-links')
    for el in list(main.iter()):
        if not isinstance(el.tag, str):
            continue
        classes = el.get('class', '').split()
        if el.tag in ('script', 'style', 'iframe', 'nav', 'button') or any(x in classes for x in removable):
            _drop(el)
    # Margin citations and footnotes otherwise interrupt prose, tables and figure
    # captions in a linear Markdown document. Gather them into linked endmatter.
    for label, selector in (
        ('Source References', './/*[contains(concat(" ",normalize-space(@class)," ")," csl-entry ")]'),
        ('Footnotes', './/*[@id]'),
    ):
        chosen = []
        seen = set()
        for el in list(main.xpath(selector)):
            ident = el.get('id', '')
            if label == 'Footnotes' and not re.fullmatch(r'fn[0-9]+', ident): continue
            if not ident: continue
            tail = el.tail
            parent = el.getparent()
            if parent is None: continue
            # remove() retains the element itself for the new endmatter section.
            if tail:
                previous = el.getprevious()
                if previous is not None: previous.tail = (previous.tail or '') + tail
                else: parent.text = (parent.text or '') + tail
            el.tail = None
            parent.remove(el)
            if ident not in seen:
                chosen.append(el); seen.add(ident)
        if chosen:
            section = etree.SubElement(main, 'section')
            section.set('id', label.lower().replace(' ', '-'))
            heading = etree.SubElement(section, 'h2'); heading.text = label
            for el in chosen: section.append(el)
    # Give headings their authored section identifiers instead of generated label IDs.
    for el in main.xpath('.//*[self::h1 or self::h2 or self::h3 or self::h4 or self::h5 or self::h6]'):
        parent = el.getparent()
        ident = el.get('data-anchor-id') or el.get('id') or (parent.get('id') if parent is not None and parent.tag == 'section' else '')
        if ident:
            el.set('id', ident)
            anchors.append(ident)
            if parent is not None and parent.get('id') == ident:
                parent.attrib.pop('id', None)
    used = set(anchors)
    # Every referenceable float, equation, citation and note gets a stable marker.
    # Header anchors remain {#id} until the vault builder creates its final note paths.
    for el in list(main.iter()):
        if not isinstance(el.tag, str): continue
        ident = el.get('id', '')
        if ident.startswith('fnref'):
            el.attrib.pop('id', None)
            continue
        if not ident or el.tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            continue
        if ident in used:
            el.attrib.pop('id', None)
            continue
        if '-caption-' not in ident and ident.startswith(('fig-', 'tbl-', 'eq-', 'ref-', 'fn', 'pri-', 'def-', 'exm-', 'exmp-', 'thm-', 'cor-', 'lem-', 'lst-', 'alg-', 'sol-', 'callout-')):
            parent = el.getparent()
            if parent is not None:
                # Marker is placed outside the table, not inside a cell or colgroup.
                host = el
                while host.getparent() is not None and host.getparent().tag in ('p', 'table', 'tbody', 'thead', 'tr', 'td', 'th', 'figure'):
                    host = host.getparent()
                marker = etree.Element('p')
                marker.text = 'OBSIDIANBLOCK' + ident + 'ENDBLOCK'
                host.addnext(marker)
                used.add(ident); anchors.append(ident)
        el.attrib.pop('id', None)
    for el in main.xpath('.//a[@href]'):
        href = el.get('href', '')
        if el.get('role') == 'doc-backlink' or '#fnref' in href:
            _drop(el)
        elif el.xpath('.//img'):
            el.drop_tag()
        elif href:
            el.set('href', urljoin(url, href))
    for el in main.xpath('.//a[@title] | .//img[@title]'):
        el.attrib.pop('title', None)
    for el in main.xpath('.//img[@src]'):
        el.set('src', urljoin(url, el.get('src')))
        for key in ('srcset', 'loading', 'width', 'height', 'class', 'style'):
            el.attrib.pop(key, None)
    # Some HTML contains SVG diagram elements; preserve them as portable data SVG.
    # Main importer recognizes data URLs and writes the assets locally.
    import base64
    for el in main.xpath('.//*[local-name()="svg"]'):
        svg = etree.tostring(el, encoding='utf-8')
        img = etree.Element('img')
        img.set('src', 'data:image/svg+xml;base64,' + base64.b64encode(svg).decode())
        img.set('alt', el.get('aria-label', 'Diagram'))
        el.getparent().replace(el, img)
    # HTML details/summary are ordinary visible callout content in Obsidian.
    for el in main.xpath('.//details | .//summary'):
        el.tag = 'div' if el.tag == 'details' else 'p'
    ast = _pandoc(html.tostring(main, encoding='unicode'), 'html')
    ast['blocks'] = _clean_blocks(ast['blocks'], macros, url)
    return ast, anchors


def _readable_link_label(nodes: list, macros: dict) -> list:
    """Wiki aliases are plain labels; write mathematical names as readable glyphs."""
    greek = {'alpha':'α','beta':'β','gamma':'γ','delta':'δ','Delta':'Δ',
             'tau':'τ','theta':'θ','lambda':'λ','mu':'μ','sigma':'σ',
             'rho':'ρ','eta':'η','epsilon':'ε','pi':'π','kappa':'κ'}
    result=[]
    for n in nodes:
        t,c=n.get('t'),n.get('c')
        if t == 'Math':
            text=c[1]
        elif t == 'Str' and re.search(r'\\[A-Za-z]+',c):
            text=c
        elif t in ('Emph','Strong','Superscript','Subscript','SmallCaps'):
            result.extend(_readable_link_label(c,macros));continue
        else:
            result.append(n);continue
        text=expand_macros(text,macros)
        text=re.sub(r'\\([A-Za-z]+)',lambda m:greek.get(m.group(1),m.group(1) if m.group(1) not in ('text','mathrm','mathbf','mathcal','mathbb') else ''),text)
        text=text.replace('^3','³').replace('^2','²')
        text=re.sub(r'[{}$]','',text)
        result.append({'t':'Str','c':text})
    return result


def _clean_inline(nodes: list, macros: dict, url: str) -> list:
    result = []
    for n in nodes:
        t, c = n.get('t'), n.get('c')
        if t == 'Span':
            classes = c[0][1]
            if 'math' in classes:
                tex = _plain_inline(c[1]).strip()
                tex = re.sub(r'^\\[\[(]|\\[\])]$', '', tex)
                tex = re.sub(r'^\\\[|\\\]$', '', tex)
                tex = re.sub(r'^\\\(|\\\)$', '', tex)
                result.append({'t': 'Math', 'c': [{'t': 'DisplayMath' if 'display' in classes else 'InlineMath'}, expand_macros(tex, macros)]})
            else:
                result.extend(_clean_inline(c[1], macros, url))
            continue
        if t == 'RawInline':
            if c[0] == 'html':
                # Drop decorative HTML spans; raw text exists as other nodes.
                continue
            if c[0] == 'tex':
                txt = c[1]
                if txt.startswith(('\\index{', '\\noindent', '\\chapterminitoc')):
                    continue
            result.append(n); continue
        if t in ('Emph', 'Strong', 'Strikeout', 'Superscript', 'Subscript', 'SmallCaps'):
            n['c'] = _clean_inline(c, macros, url)
        elif t in ('Link', 'Image'):
            n['c'][0] = ['', [], []]
            n['c'][1] = _clean_inline(c[1], macros, url)
            n['c'][2][1] = ''
            if t == 'Link':
                n['c'][1] = _readable_link_label(n['c'][1], macros)
            if t == 'Link' and '#fn' in c[2][0]:
                n['c'][1] = [{'t':'Str','c':_plain_inline(n['c'][1])}]
            if t == 'Link':
                n['c'][2][0] = urljoin(url, c[2][0]) if url else c[2][0]
        elif t == 'Math':
            n['c'][1] = expand_macros(c[1], macros)
        elif t == 'Note':
            n['c'] = _clean_blocks(c, macros, url)
        elif t == 'Cite':
            # Keep source citation keys for primary bibliography link resolution.
            n = {'t': 'Str', 'c': '; '.join('@' + x['citationId'] for x in c[0])}
        result.append(n)
    return result


def _walk_table(value, macros, url):
    if isinstance(value, dict):
        if value.get('t') in ('Plain','Para'):
            value['c'] = _clean_inline(value['c'], macros, url)
        elif value.get('t') == 'Div':
            value['c'][0] = ['', [], []]
        else:
            for k,v in list(value.items()): value[k] = _walk_table(v, macros, url)
    elif isinstance(value, list):
        value = [_walk_table(x, macros, url) for x in value]
    return value


def _clean_blocks(blocks: list, macros: dict, url: str) -> list:
    result = []
    for n in blocks:
        t, c = n.get('t'), n.get('c')
        if t == 'Div':
            result.extend(_clean_blocks(c[1], macros, url)); continue
        if t == 'RawBlock':
            # Site layout and PDF presentation commands are irrelevant in Obsidian.
            continue
        if t == 'Header':
            ident = c[1][0]
            inline = _clean_inline(c[2], macros, url)
            if ident:
                inline += [{'t':'Space'},{'t':'Str','c':'{#' + ident + '}'}]
            n['c'] = [c[0], ['', [], []], inline]
        elif t in ('Para','Plain'):
            n['c'] = _clean_inline(c, macros, url)
        elif t in ('BulletList',):
            n['c'] = [_clean_blocks(item, macros, url) for item in c]
        elif t == 'OrderedList':
            n['c'][1] = [_clean_blocks(item, macros, url) for item in c[1]]
        elif t == 'DefinitionList':
            n['c'] = [[_clean_inline(term, macros, url), [_clean_blocks(defn, macros, url) for defn in definitions]] for term,definitions in c]
        elif t == 'BlockQuote':
            n['c'] = _clean_blocks(c, macros, url)
        elif t == 'CodeBlock':
            # HTML sourceCode chunks contain learner-visible code only.
            classes = c[0][1]
            n['c'][0] = ['', [x for x in classes if x not in ('sourceCode', 'cell-code')][:1], []]
        elif t == 'Table':
            n = _walk_table(n, macros, url)
            n['c'][0] = ['', [], []]
        elif t == 'Figure':
            ident, caption, inner = c
            result.extend(_clean_blocks(inner, macros, url))
            if caption and caption[1]:
                result.extend(_clean_blocks(caption[1], macros, url))
            continue
        result.append(n)
    return result


def _fetch_html(url: str, repo: Path) -> str:
    cache = repo / '.git' / 'obsidian-render-cache'
    cache.mkdir(exist_ok=True)
    path = cache / (hashlib.sha256(url.encode()).hexdigest() + '.html')
    if path.exists(): return path.read_text()
    run = subprocess.run(['curl','--fail','--location','--silent','--show-error','--max-time','45',url], capture_output=True)
    if run.returncode:
        raise RuntimeError(run.stderr.decode(errors='replace').strip())
    raw = run.stdout.decode('utf-8')
    if 'quarto-document-content' not in raw:
        raise ValueError('Not a rendered book article')
    path.write_text(raw)
    return raw


def _prose_coverage(source: str, tree) -> float:
    # Compare long ordinary prose paragraphs, ignoring code, math and generated values.
    text = re.sub(r'(?ms)^(`{3,}|~{3,}).*?^\1\s*$', '', source)
    paragraphs = [p for p in re.split(r'\n\s*\n', text) if len(p)>200 and not re.match(r'\s*(?:#|\||:::|\\)',p)]
    source_words = Counter(re.findall(r'[A-Za-z]{4,}', '\n'.join(paragraphs).lower()))
    html_words = Counter(re.findall(r'[A-Za-z]{4,}', ' '.join(tree.xpath('//main//text()')).lower()))
    if not source_words: return 1.0
    return sum((source_words & html_words).values()) / sum(source_words.values())


def _finalize(ast: dict) -> str:
    body = _write_ast(ast)
    body = re.sub(r'\\\{#([^\s}]+)\\\}', r'{#\1}', body)
    body = re.sub(r'OBSIDIANBLOCK([^\s]+?)ENDBLOCK', lambda m:'^'+m.group(1), body)
    # Obsidian expects display equations to occupy their own Markdown block.
    # Keep fenced code unchanged and downgrade display math inside table cells.
    pieces = re.split(r'(?ms)(^(?:`{3,}|~{3,})[^\n]*\n.*?^(?:`{3,}|~{3,})\s*$)', body)
    rebuilt = []
    for piece in pieces:
        if piece is None: continue
        if re.match(r'^(`{3,}|~{3,})', piece):
            # Captured bare fence delimiters are discarded by using the complete
            # segment list below; they are not content blocks.
            rebuilt.append(piece); continue
        lines = []
        for line in piece.splitlines(keepends=True):
            if line.lstrip().startswith('|'): line = line.replace('$$', '$')
            lines.append(line)
        piece = ''.join(lines)
        piece = re.sub(r'\$\$(.*?)\$\$', lambda m:'\n\n$$\n'+m.group(1).strip()+'\n$$\n\n', piece, flags=re.S)
        rebuilt.append(piece)
    # Do not use the capturing split's nested fence group in output.
    body = ''.join(rebuilt)
    # Pandoc's GFM writer may escape block marker carets and @ citation keys.
    body = body.replace('\\^','^')
    return re.sub(r'\n{3,}', '\n\n', body).strip() + '\n'


def render_document(source_path: Path, repo: Path) -> dict:
    source_path, repo = Path(source_path), Path(repo)
    if not source_path.is_absolute(): source_path = repo / source_path
    text = _expand_includes(source_path.read_text(encoding='utf-8'),source_path,repo)
    relative = source_path.relative_to(repo).as_posix()
    url = 'https://mlsysbook.ai/' + relative.removeprefix('books/').removesuffix('.qmd') + '.html'
    macros = load_macros(str(repo))
    warnings = []
    try:
        raw = _fetch_html(url, repo)
        original_html_sha256 = hashlib.sha256(raw.encode()).hexdigest()
        raw, restored, still_missing = _restore_source_headings(_sanitize_html_tooltips(raw), text)
        tree = html.fromstring(raw)
        authored_ids = source_heading_ids(text)
        ids = set(tree.xpath('//@id'))
        missing = sorted(set(authored_ids) - ids)
        coverage = _prose_coverage(text, tree)
        if missing or coverage < .84:
            raise ValueError(f'Published snapshot differs: {len(missing)} absent source headings; prose coverage {coverage:.3f}; missing {missing[:5]}')
        ast, anchors = _html_ast(raw, url, macros)
        title = next((_plain_inline(b['c'][2]) for b in ast['blocks'] if b.get('t')=='Header' and b['c'][0]==1), source_path.stem)
        title = re.sub(r'\s*\{#[^}]+\}', '', title).strip()
        return {'body':_finalize(ast), 'title':title, 'anchors':anchors,
                'source_mode':'Source-Correlated Published HTML' if not restored else 'Published HTML With Restored Source Headings', 'rendered_source_url':url,
                'restored_source_headings':restored,
                'rendered_sha256':original_html_sha256,
                'prose_coverage':round(coverage,4), 'warnings':warnings}
    except Exception as e:
        warnings.append(str(e))
        return _render_qmd(text, relative, repo, macros, warnings, url)


def _expand_includes(text: str, source: Path, repo: Path, depth: int = 0) -> str:
    if depth > 8: return text
    def sub(match):
        target = match.group(1).strip().strip('"\'')
        path = (source.parent / target).resolve()
        try: path.relative_to(repo.resolve())
        except ValueError: return match.group(0)
        if not path.is_file(): return match.group(0)
        return _expand_includes(path.read_text(),path,repo,depth+1)
    return re.sub(r'\{\{<\s*include\s+([^>]+?)\s*>\}\}',sub,text)


def _render_qmd(text: str, relative: str, repo: Path, macros: dict, warnings: list, url: str) -> dict:
    # Conservative fallback retains reader-visible code and source prose. It does
    # not execute cells or invent computed numeric values.
    if text.startswith('---\n'):
        text = text.split('\n---',1)[1].lstrip('-\n')
    text = re.sub(r'(?m)^(`{3,}|~{3,})\{(python|r|julia|bash)\}\s*$',r'\1{.\2}',text)
    ast = _pandoc(text, 'markdown+fenced_divs+tex_math_dollars+raw_tex+citations')
    incomplete = []
    def filt(blocks):
        out=[]
        for n in blocks:
            t,c=n.get('t'),n.get('c')
            if t=='Div':
                kv=dict(c[0][2]); classes=c[0][1]
                if kv.get('when-format') in ('pdf','latex','html:js') or kv.get('unless-format')=='html': continue
                ident=c[0][0]
                out.extend(filt(c[1]))
                if kv.get('fig-cap'):
                    caption_ast=_pandoc(kv['fig-cap'],'markdown+tex_math_dollars')['blocks']
                    out.extend(caption_ast)
                if ident:out.append({'t':'Para','c':[{'t':'Str','c':'OBSIDIANBLOCK'+ident+'ENDBLOCK'}]})
                continue
            if t=='CodeBlock':
                attrs,code=c
                if 'tikz' in attrs[1] or (re.search(r'^#\|\s*echo:\s*false',code,re.M)):
                    label=re.search(r'^#\|\s*label:\s*(\S+)',code,re.M)
                    if label and label.group(1).startswith(('fig-','tbl-')):
                        ident=label.group(1)
                        out.append({'t':'Para','c':[{'t':'Str','c':'OBSIDIANBLOCK'+ident+'ENDBLOCK'}]})
                        out.append({'t':'Para','c':[{'t':'Link','c':[['',[],[]],[{'t':'Str','c':'View Rendered Figure Or Table'}],[url+'#'+ident,'']]}]})
                        incomplete.append(ident)
                    continue
            out.append(n)
        return out
    ast['blocks']=filt(ast['blocks'])
    ast['blocks']=_clean_blocks(ast['blocks'],macros,'')
    title=next((_plain_inline(b['c'][2]) for b in ast['blocks'] if b.get('t')=='Header' and b['c'][0]==1),Path(relative).stem)
    body=_finalize(ast)
    dynamic=re.findall(r'`\{python\}\s+([^`]+)`',body)
    if dynamic:
        body=re.sub(r'`\{python\}\s+([^`]+)`',lambda m:'[Computed Value In Source]('+url+')',body)
        warnings.append(f'{len(dynamic)} dynamic values require original rendered source')
    body=re.sub(r'\\index\{[^}]*\}','',body)
    body=re.sub(r'\\(?:noindent|chapterminitoc|newpage|clearpage)\b','',body)
    body=re.sub(r'\\ref\{([^}]+)\}',r'@\1',body)
    # Relative media remains relative to source_path; importer resolves it via Git.
    return {'body':body,'title':re.sub(r'\s*\{#[^}]+\}','',title).strip(),
            'anchors':source_heading_ids(text),'source_mode':'Repository QMD',
            'rendered_source_url':url,'prose_coverage':None,'warnings':warnings,
            'unrendered_floats':incomplete,'dynamic_values':dynamic}


if __name__ == '__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('--repo',default='.')
    a=p.parse_args();r=render_document(Path(a.source),Path(a.repo).resolve())
    print(json.dumps({k:v for k,v in r.items() if k!='body'},indent=2))
    Path('/tmp/obsidian-render-sample.md').write_text(r['body'])
