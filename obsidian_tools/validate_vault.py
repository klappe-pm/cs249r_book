#!/usr/bin/env python3
"""Validate YAML, links, assets, tables, source coverage and import cleanliness."""
from __future__ import annotations
import argparse
import collections
import json
import re
import sys
import urllib.parse
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
import yaml

TICK = chr(96)
SMALL_WORDS = set("a an and as at but by for from if in into nor of on onto or over per so than the to up via vs with without yet".split())
CAPITAL_MATH = set("Alpha Beta Gamma Delta Epsilon Zeta Eta Theta Iota Kappa Lambda Mu Nu Xi Omicron Pi Rho Sigma Tau Upsilon Phi Chi Psi Omega Digamma Bbbk Box Finv Game Im Re Pr Rrightarrow Lleftarrow Vdash Vvdash Join Vert Rightarrow Leftarrow Leftrightarrow Longrightarrow Longleftarrow Longleftrightarrow Uparrow Downarrow Updownarrow Big Bigl Bigr Bigg Biggl Biggr Bmatrix Vmatrix".split())

class UniqueKeyLoader(yaml.SafeLoader):
    """Safe YAML with duplicate mapping keys rejected rather than overwritten."""
    pass

def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError("Duplicate YAML Key: " + str(key))
        result[key] = loader.construct_object(value_node, deep=deep)
    return result

UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)

class TableAudit(HTMLParser):
    """Audit retained HTML tables without relying on a browser's repairs."""
    def __init__(self):
        super().__init__()
        self.tables=[]
        self.current=None
        self.row=None
        self.errors=[]
    def handle_starttag(self,tag,attrs):
        if tag=="table":
            if self.current is not None:
                self.errors.append("Nested HTML Table")
            self.current=[]
        elif tag=="tr" and self.current is not None:
            if self.row is not None:
                self.errors.append("HTML Table Row Not Closed")
            self.row=[]
        elif tag in {"td","th"} and self.row is not None:
            attrs=dict(attrs)
            try:
                self.row.append((int(attrs.get("colspan","1")),int(attrs.get("rowspan","1"))))
            except ValueError:
                self.errors.append("Invalid HTML Cell Span")
    def handle_endtag(self,tag):
        if tag=="tr" and self.current is not None:
            if self.row is None:
                self.errors.append("HTML Table Row End Has No Start")
            else:
                self.current.append(self.row)
            self.row=None
        elif tag=="table":
            if self.current is None:
                self.errors.append("HTML Table End Has No Start")
            else:
                if self.row is not None:
                    self.errors.append("Unclosed HTML Table Row")
                self.tables.append(self.current)
            self.current=None

def frontmatter(text):
    match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
    if not match:
        return {}, text, "Missing Or Unclosed YAML Frontmatter"
    try:
        meta = yaml.load(match[1], Loader=UniqueKeyLoader)
        if not isinstance(meta, dict):
            raise ValueError("YAML Must Be A Mapping")
        return meta, text[match.end():], None
    except (yaml.YAMLError, ValueError) as error:
        return {}, text[match.end():], str(error).splitlines()[0]

def prose_lines(body, include_math=False):
    result, fence, opened, math = [], None, None, False
    for number, line in enumerate(body.splitlines(), 1):
        opening = re.match(r"^\s{0,3}([" + TICK + r"]{3,}|~{3,})(.*)$", line)
        if opening:
            marker = opening[1]
            if fence:
                if marker[0] == fence[0] and len(marker) >= len(fence) and not opening[2].strip():
                    fence = None
            else:
                fence, opened = marker, number
            continue
        if fence:
            continue
        if line.strip() == "$$":
            math = not math
            if include_math:
                result.append((number,line))
            continue
        if not math or include_math:
            result.append((number, line))
    return result, opened if fence else None, math

def plain(value):
    value = re.sub(r"\[\[([^]|]+)\|([^]]+)\]\]", r"\2", value)
    value = re.sub(r"\[\[([^]]+)\]\]", r"\1", value)
    value = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", value)
    value = re.sub(r"\$[^$]*\$|"+TICK+r"[^"+TICK+r"]*"+TICK+r"|<[^>]+>|\{[^}]*\}", "", value)
    return re.sub(r"[*_~]", "", value).strip()

def slug(value):
    return re.sub(r"[^\w\- ]", "", plain(value).lower()).replace(" ", "-")

def lower_words(value):
    # Numbers still occupy title positions: "Principles 1 and 13" does not end
    # with the conjunction, even though its last alphabetic token is "and".
    words = re.findall(r"[A-Za-z0-9][A-Za-z0-9’'_-]*", plain(value))
    return [word for i, word in enumerate(words)
            if not any(c.isdigit() for c in word)
            and not any(c.isupper() for c in word[1:])
            and not (len(word)==1 and ("@"+word) in value)
            and word[0].islower()
            and (word.lower() not in SMALL_WORDS or i in (0,len(words)-1))]

def cells(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|") and not line.endswith("\\|"):
        line = line[:-1]
    return re.split(r"(?<!\\)\|", line)

def reader_heading_ids(body):
    """Independently collect authored headings visible in the HTML reading path."""
    body=re.sub(r"<!--.*?-->","",body,flags=re.S)
    visible=[True]
    fence=None
    found=set()
    for line in body.splitlines():
        marker=re.match(r"^\s{0,3}(["+TICK+r"]{3,}|~{3,})(.*)$",line)
        if marker:
            if fence:
                if marker[1][0]==fence[0] and len(marker[1])>=len(fence) and not marker[2].strip():
                    fence=None
            else:
                fence=marker[1]
            continue
        if fence:
            continue
        div=re.match(r"^\s*:{3,}(.*)$",line)
        if div:
            attrs=div[1].strip()
            if attrs:
                when=re.search(r"when-format\s*=\s*[\"']?([\w-]+)",attrs)
                unless=re.search(r"unless-format\s*=\s*[\"']?([\w-]+)",attrs)
                keep=not ((when and when[1] in {"pdf","latex"}) or (unless and unless[1]=="html"))
                visible.append(visible[-1] and keep)
            elif len(visible)>1:
                visible.pop()
            continue
        if visible[-1] and re.match(r"^#{1,6}\s+",line):
            ident=re.search(r"\{#([^\s}]+)",line)
            if ident:
                found.add(ident[1])
    return found

def verify(vault):
    vault = vault.resolve()
    issues, counts, notes, metadata, headings, blocks = [], collections.Counter(), {}, {}, {}, {}
    def add(code, path, message, line=None, severity="error"):
        issues.append(dict(severity=severity, code=code, path=str(path), line=line, message=message))
    for path in sorted(vault.rglob("*.md")):
        rel = path.relative_to(vault).as_posix()
        counts["notes"] += 1
        text = path.read_text(encoding="utf-8")
        meta, body, error = frontmatter(text)
        notes[rel], metadata[rel] = body, meta
        if error:
            add("yaml",rel,error)
        if not text.endswith("\n"):
            add("newline",rel,"Missing Final Newline")
        if "title" in meta and not isinstance(meta["title"],str):
            add("yaml_title",rel,"Title Must Be A String")
        if lower_words(path.stem):
            add("filename_case",rel,"Filename Is Not Title Case: "+", ".join(lower_words(path.stem)))
        for key in ["tags","aliases"]:
            if key in meta and (not isinstance(meta[key],list) or any(not isinstance(v,str) for v in meta[key])):
                add("yaml_list",rel,key+" Must Be A List Of Strings")
        if isinstance(meta.get("tags"),list) and any(re.search(r"\s|#",str(tag)) for tag in meta["tags"]):
            add("yaml_tags",rel,"Tags Cannot Contain Whitespace Or #")
        if "source_commit" in meta and not re.fullmatch(r"[0-9a-f]{40}",str(meta["source_commit"])):
            add("yaml_commit",rel,"Expected Full Source Commit SHA")
        lines, fence, math = prose_lines(body)
        if fence:
            add("code_fence",rel,"Unclosed Code Fence",fence)
        if math:
            add("display_math",rel,"Unclosed Display Math")
        prose="\n".join(line for _,line in lines)
        code_free="\n".join(line for _,line in prose_lines(body,include_math=True)[0])
        code_free=re.sub(TICK+r"+[^"+TICK+r"\n]*"+TICK+r"+","",code_free)
        local_macros=set(re.findall(r"\\(?:newcommand|renewcommand|def)\s*\{?\\([A-Za-z]+)",code_free))
        unknown_macros=set(re.findall(r"\\([A-Z][A-Za-z]{2,})(?![A-Za-z])",code_free))-CAPITAL_MATH-local_macros
        if unknown_macros:
            add("unexpanded_macro",rel,"Unexpanded Math Or Link-Label Commands: "+", ".join(sorted(unknown_macros)))
        html_tables=TableAudit()
        html_tables.feed(prose)
        if html_tables.current is not None:
            add("html_table",rel,"Unclosed HTML Table")
        counts["html_tables"]+=len(html_tables.tables)
        for message in html_tables.errors:
            add("html_table",rel,message)
        for table in html_tables.tables:
            spans={}
            widths=[]
            for row in table:
                occupied={i for i,n in spans.items() if n>0}
                spans={i:n-1 for i,n in spans.items() if n>1}
                column=0
                for colspan,rowspan in row:
                    while column in occupied:
                        column+=1
                    for i in range(column,column+colspan):
                        occupied.add(i)
                        if rowspan>1:
                            spans[i]=rowspan-1
                    column+=colspan
                widths.append(max(occupied,default=-1)+1)
            if len(set(widths))>1:
                add("html_table_columns",rel,"Inconsistent HTML Table Widths: "+str(widths))
        for table_text in re.findall(r"<table\b.*?</table>",prose,re.S|re.I):
            if "[[" in table_text:
                add("html_table_markdown",rel,"Wiki Links Inside Raw HTML Tables Do Not Render As Links")
        defined_footnotes=re.findall(r"(?m)^\[\^([^]\n]+)\]:",prose)
        referenced_footnotes=set(re.findall(r"\[\^([^]\n]+)\](?!:)",prose))
        for ident in referenced_footnotes-set(defined_footnotes):
            add("missing_footnote",rel,"Missing Local Footnote Definition: "+ident)
        for ident,frequency in collections.Counter(defined_footnotes).items():
            if frequency>1:
                add("duplicate_footnote",rel,"Duplicate Footnote Definition: "+ident)
        placeholders=prose.count("Computed Value In Source")
        if placeholders:
            counts["computed_value_placeholders"]+=placeholders
            add("computed_placeholder",rel,f"{placeholders} Computed Values Require The External Source",severity="warning")
        float_fallbacks=prose.count("View Rendered Figure Or Table")
        if float_fallbacks:
            counts["float_fallbacks"]+=float_fallbacks
            add("float_fallback",rel,f"{float_fallbacks} Generated Figures Or Tables Require The External Source",severity="warning")
        hs = [re.match(r"^#{1,6}\s+(.+?)(?:\s+#+)?$",line)[1] for _,line in lines if re.match(r"^#{1,6}\s+",line)]
        headings[rel] = {plain(h) for h in hs}
        # Actual blocks are prose anchors; display-math exponents such as ^2
        # must never be mistaken for Obsidian IDs.
        ids = re.findall(r"(?m)(?:^|[ \t])\^([A-Za-z0-9-]+)[ \t]*$",prose)
        blocks[rel] = set(ids)
        for ident, freq in collections.Counter(ids).items():
            if freq>1:
                add("duplicate_block",rel,"Duplicate Block ID: "+ident)
        h1s = [plain(line[2:].strip()) for _,line in lines if line.startswith("# ")]
        if not h1s:
            add("h1",rel,"Missing H1 Title")
        elif len(h1s)>1:
            add("h1",rel,"Multiple H1 Titles",severity="warning")
        elif "title" in meta and h1s[0] != plain(str(meta["title"])):
            add("title_mismatch",rel,"YAML Title And H1 Differ")
        for number,line in lines:
            without_inline_code=re.sub(TICK+r"+[^"+TICK+r"\n]*"+TICK+r"+","",line)
            if line.lstrip().startswith("^") and not re.fullmatch(r"\s*\^[A-Za-z0-9-]+\s*",line):
                add("invalid_block",rel,"Block IDs Permit Only Letters, Digits, And Hyphens",number)
            if "$$" in line and line.strip()!="$$":
                add("inline_display_math",rel,"Display Math Delimiters Must Be On Separate Lines",number)
            hm=re.match(r"^#{1,6}\s+(.+)$",line)
            if hm and lower_words(hm[1]):
                add("heading_case",rel,"Heading Is Not Title Case: "+", ".join(lower_words(hm[1])),number)
            if re.match(r"^\s*:::",line):
                add("quarto_div",rel,"Unconverted Quarto Div",number)
            if re.search(r"(?<![\w/])@(?:[Ss]ec|fig|tbl|eq|exm|lst|lem|thm|def|prp)-[\w-]+",without_inline_code):
                add("quarto_reference",rel,"Unresolved Quarto Cross-Reference",number)
            if re.search(r"\[[^]\n]*@[A-Za-z][\w.-]+",without_inline_code):
                add("unresolved_citation",rel,"Unresolved Bibliographic Citation",number)
            if re.search(r"\{\{[<%]|\{[.#][\w-]+(?:[ =][^}]*)?\}",line):
                add("quarto_attribute",rel,"Unconverted Quarto Attribute Or Shortcode",number)
            if re.search(r"\\(?:chapterminitoc|noindent|newpage|clearpage|begin\{(?:figure|tikzpicture|marginfigure))",line):
                add("latex_layout",rel,"Raw LaTeX Layout Command",number)
            if re.search(r"!\[[^]]*\]\(https?://",line):
                add("remote_image",rel,"Remote Image Is Not Available Offline",number)
            if "](" in line and re.search(r"<a\s+href",line):
                add("malformed_link_title",rel,"Nested HTML Anchor In Markdown Link Metadata",number)
        table=[]
        for number,line in lines+[(0,"")]:
            if line.strip().startswith("|"):
                table.append((number,line))
            else:
                if len(table)>=2 and re.fullmatch(r"[\s|:\-]+",table[1][1]):
                    counts["tables"]+=1
                    width=len(cells(table[0][1]))
                    for n,row in table[1:]:
                        if len(cells(row))!=width:
                            add("table_columns",rel,f"Expected {width} Cells, Found {len(cells(row))}",n)
                        if re.search(r"\[\[[^\]]*(?<!\\)\|",row):
                            add("table_wikilink",rel,"Unescaped Wiki Alias Pipe In Table",n)
                table=[]
    stems=collections.defaultdict(list)
    for rel in notes:
        stems[Path(rel).stem].append(rel)
    for name, paths in stems.items():
        if len(paths)>1:
            add("duplicate_basename",paths[0],"Ambiguous Basename: "+name,severity="warning")
    def resolve(target,source):
        target=urllib.parse.unquote(target).strip()
        if not target:
            return source
        # Dots in note titles (V1-10.02) are not filename extensions.
        for direct in [target,target+".md"]:
            for candidate in [direct.lstrip("/"),(Path(source).parent/direct).as_posix()]:
                if candidate in notes or (vault/candidate).is_file():
                    return candidate
        name=Path(target).name.removesuffix(".md")
        if "/" not in target and len(stems.get(name,[]))==1:
            return stems[name][0]
        return None
    media=set()
    for rel,body in notes.items():
        lines,_,_=prose_lines(body)
        source="\n".join(line for _,line in lines)
        source=re.sub(TICK+r"+[^"+TICK+r"\n]*"+TICK+r"+","",source)
        source+="\n"+str(metadata[rel])
        for match in re.finditer(r"(!?)\[\[([^]\n]+)\]\]",source):
            counts["wikilinks"]+=1
            target=match[2].replace("\\|","|").split("|",1)[0]
            target,_,fragment=target.partition("#")
            found=resolve(target,rel)
            if not found:
                add("broken_wikilink",rel,"Missing Target: "+target)
                continue
            if fragment and found in notes:
                if fragment.startswith("^") and fragment[1:] not in blocks[found]:
                    add("broken_block",rel,"Missing Block: "+found+"#"+fragment)
                elif not fragment.startswith("^") and fragment not in headings[found]:
                    add("broken_heading",rel,"Missing Heading: "+found+"#"+fragment)
            if match[1] and found not in notes:
                counts["image_embeds"]+=1
                media.add(found)
        for match in re.finditer(r"(!?)\[[^]\n]*\]\((<[^>]+>|[^\s)]+)(?:\s+\"[^\"]*\")?\)",source):
            target=match[2].strip("<>")
            if re.match(r"(?:https?://|mailto:|data:)",target):
                counts["external_links"]+=1
                continue
            target,_,fragment=urllib.parse.unquote(target).partition("#")
            found=resolve(target,rel)
            if not found:
                add("broken_markdown_link",rel,"Missing Local Target: "+target)
                continue
            if fragment and found in notes and fragment not in {slug(h) for h in headings[found]}|headings[found]|blocks[found]:
                add("broken_markdown_heading",rel,"Missing Markdown Anchor: "+found+"#"+fragment)
            if match[1] and found not in notes:
                counts["image_embeds"]+=1
                media.add(found)
    for rel in sorted(media):
        path=vault/rel
        try:
            if not path.stat().st_size:
                raise ValueError("Empty Asset")
            if path.suffix.lower()==".svg":
                root=ET.parse(path).getroot()
                if root.tag.split("}")[-1]!="svg":
                    raise ValueError("Not An SVG Document")
                for element in root.iter():
                    if element.tag.split("}")[-1] in {"image","use"}:
                        for key,value in element.attrib.items():
                            if key.split("}")[-1] in {"href","src"} and not value.startswith(("#","data:")):
                                raise ValueError("SVG Depends On An External Image Or Glyph: "+value)
                for resource in re.findall(r"url\([\"']?([^\"')]+)",path.read_text()):
                    if not resource.startswith(("#","data:")):
                        raise ValueError("SVG Depends On An External CSS Resource: "+resource)
            elif path.suffix.lower() in {".png",".webp",".jpg",".jpeg",".gif",".bmp",".tiff"}:
                from PIL import Image
                with Image.open(path) as img:
                    img.verify()
        except Exception as error:
            add("invalid_media",rel,str(error))
    counts["unique_media"]=len(media)
    manifest_path=vault/"99 System/Import Manifest.json"
    if manifest_path.exists():
        try:
            manifest=json.loads(manifest_path.read_text())
            entries=manifest["notes"]
            counts["source_notes"]=len(entries)
            chapters=set()
            for entry in entries:
                rel=entry["path"]
                if rel not in notes:
                    add("manifest_note",rel,"Manifest Note Is Missing")
                    continue
                if entry.get("source_path"):
                    for key in ["source_path","source_commit"]:
                        expected=entry.get(key,manifest.get(key))
                        if expected is not None and metadata[rel].get(key)!=expected:
                            add("manifest_metadata",rel,key+" Does Not Match Manifest")
                anchor=entry.get("source_anchor")
                anchor=entry.get("block_ids",{}).get(anchor,anchor)
                if anchor and anchor not in blocks[rel]:
                    add("manifest_anchor",rel,"Original Source Anchor Is Missing: "+anchor)
                if entry.get("kind")=="chapter":
                    chapters.add(entry["source_path"])
                if metadata[rel].get("title")!=entry.get("title"):
                    add("manifest_title",rel,"Title Does Not Match Manifest")
            # A clean graph cannot compensate for omitted source sections. Check
            # every authored heading ID against real emitted anchors, not only
            # records claiming to preserve those IDs.
            by_source=collections.defaultdict(list)
            for entry in entries:
                if entry.get("source_path","").endswith(".qmd"):
                    by_source[entry["source_path"]].append(entry)
            for source, source_entries in by_source.items():
                source_path=vault.parent/source
                if not source_path.exists():
                    continue
                _,source_body,_=frontmatter(source_path.read_text())
                required=reader_heading_ids(source_body)
                available=set()
                for entry in source_entries:
                    mapping=entry.get("block_ids",{})
                    actual=blocks.get(entry["path"],set())
                    for ident in entry.get("source_anchors",[]):
                        if mapping.get(ident,ident) in actual:
                            available.add(ident)
                counts["source_heading_ids"]+=len(required)
                counts["imported_source_heading_ids"]+=len(required&available)
                missing=required-available
                if missing:
                    add("source_heading_coverage",source,f"{len(missing)} Authored Headings Missing: "+", ".join(sorted(missing)[:8]))
            counts["chapters"]=len(chapters)
            if len(chapters)!=71:
                add("chapter_coverage","99 System/Import Manifest.json",f"Expected 71 Main Chapters, Found {len(chapters)}")
        except (ValueError,KeyError,TypeError) as error:
            add("manifest_schema","99 System/Import Manifest.json",str(error))
    else:
        add("manifest","99 System/Import Manifest.json","Missing Import Manifest")
    counts["errors"]=sum(i["severity"]=="error" for i in issues)
    counts["warnings"]=sum(i["severity"]=="warning" for i in issues)
    return dict(counts=dict(counts),findings=issues)

def write_report(path,result,title):
    path.parent.mkdir(parents=True,exist_ok=True)
    body=["---",f"title: {title}","tags:","- Type/Review","---","",f"# {title}","","## Scope","","This review checks YAML, Title Case headings, chapter coverage, Markdown tables, local images, and exact page, heading, and block references. Literal code examples are excluded from prose checks.","","## Results","","| Check | Count |","| --- | ---: |"]
    def count_label(key):
        return key.replace('_',' ').title().replace('Html','HTML').replace(' Ids',' IDs').replace('Wikilinks','Wiki Links')
    body += [f"| {count_label(key)} | {value} |" for key,value in result["counts"].items()]
    body += ["","## Findings",""]
    if result["findings"]:
        grouped=collections.defaultdict(list)
        for issue in result["findings"]:
            grouped[(issue['severity'],issue['code'])].append(issue)
        for (severity,code),items in sorted(grouped.items()):
            body += [f"### {code.replace('_',' ').title()}","",f"{len(items)} {severity} findings. Representative examples:",""]
            for issue in items[:3]:
                where=issue["path"]+(f":{issue['line']}" if issue.get("line") else "")
                body.append(f"- {TICK}{where}{TICK} — {issue['message']}")
            body.append("")
    else:
        body.append("No structural findings remain in the generated vault.")
    body += ["","## Limits","","Structural checks establish link, metadata, table, and asset integrity. Semantic relationship validity and visual rendering require separate review. Source-generated assets without saved image files are tracked by the importer.",""]
    path.write_text("\n".join(body))

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("vault",type=Path,nargs="?",default=Path(__file__).resolve().parent.parent/"obsidian-vault")
    parser.add_argument("--report",type=Path)
    parser.add_argument("--title",default="Validation Review")
    parser.add_argument("--json",type=Path)
    args=parser.parse_args()
    result=verify(args.vault)
    if args.report:
        write_report(args.report,result,args.title)
    if args.json:
        args.json.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result["counts"],indent=2))
    codes=collections.Counter(i["code"] for i in result["findings"])
    if codes:
        print("Finding Categories:",dict(codes))
        for issue in result["findings"][:30]:
            print(f"{issue['severity']}: {issue['path']}:{issue.get('line') or ''}: {issue['message']}")
    return bool(result["counts"].get("errors"))

if __name__=="__main__":
    sys.exit(main())
