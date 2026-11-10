#!/usr/bin/env python3
"""Import the four-volume ML Systems curriculum as a reproducible Obsidian vault."""
from __future__ import annotations
import argparse, collections, concurrent.futures, hashlib, html, json, os, re, subprocess, sys
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse
import yaml

ROOT = Path(__file__).resolve().parents[1]
VOLUMES = {1:'Volume I - Foundations', 2:'Volume II - Scaling', 3:'Volume III - Agentic Systems', 4:'Volume IV - Physical AI'}
STATUSES = {1:'Released', 2:'Preview', 3:'In Development', 4:'In Development'}
PARTS = {
 1:['Foundations','Development','Optimization','Deployment'],
 2:['The Fleet','Distributed ML','The Fleet in Production','The Responsible Fleet'],
 3:['The Model','Agent Memory','Tool Use','The Agent Runtime','Learning from Trajectories','Agents at Scale','Synthesis'],
 4:['Machine Anatomy','Teaching the Machine','Running the Machine','Governing the Machine'],
}
SMALL = {'a','an','and','as','at','but','by','for','from','in','into','nor','of','on','or','per','the','to','via','vs','with','without'}
CASES = {'ml':'ML','ai':'AI','nn':'NN','gpu':'GPU','gpus':'GPUs','cpu':'CPU','cpus':'CPUs','tpu':'TPU','tpus':'TPUs','llm':'LLM','llms':'LLMs','mlops':'MLOps','pytorch':'PyTorch','tensorflow':'TensorFlow','kv':'KV','cnn':'CNN','cnns':'CNNs','rnn':'RNN','rnns':'RNNs','api':'API','apis':'APIs','ram':'RAM','sram':'SRAM','dram':'DRAM','hbm':'HBM','cuda':'CUDA','int8':'INT8','int4':'INT4','fp16':'FP16','fp32':'FP32','bf16':'BF16','rlvr':'RLVR','slo':'SLO','slos':'SLOs','simd':'SIMD','simt':'SIMT','tinyml':'TinyML','tinytorch':'TinyTorch','mlsysim':'MLSysim','mlperf':'MLPerf','json':'JSON','yaml':'YAML','dag':'DAG','rag':'RAG','lora':'LoRA','qlora':'QLoRA','dpo':'DPO','ppo':'PPO','rlhf':'RLHF','iot':'IoT','i/o':'I/O','tcp':'TCP','ip':'IP','rdma':'RDMA','nccl':'NCCL','ddp':'DDP','fsdp':'FSDP','p2p':'P2P','cpu-gpu':'CPU-GPU'}

def title_case(value):
    value = html.unescape(re.sub(r'\s*\{(?:#[^}]+|\.[^}]+)\}\s*$', '', value)).strip()
    value = re.sub(r'\bC\^([23])',lambda m:'C'+m[1].translate(str.maketrans('23','²³')),value)
    value = re.sub(r'([A-Za-z])\$\s*(?:\^\{?)?([0-9])\}?\s*\$',lambda m:m[1]+m[2].translate(str.maketrans('0123456789','⁰¹²³⁴⁵⁶⁷⁸⁹')),value)
    prefix=re.match(r'^((?:V[1-4](?:-\d{2}(?:\.\d{2})?)?)|\d{2})\s+(.+)$',value)
    if prefix: return prefix[1]+' '+title_case(prefix[2])
    mathematics=[]
    def protect_math(match):
        mathematics.append(match[0])
        return 'MATHOPAQUE'+str(len(mathematics)-1)+'TOKEN'
    value=re.sub(r'(?<!\\)\$(?!\$)(.+?)(?<!\\)\$',protect_math,value)
    value = re.sub(r'[`*_]', '', value)
    words=value.split()
    out=[]
    for i,word in enumerate(words):
        low=word.lower()
        if low in CASES: word=CASES[low]
        elif low in SMALL and i and i != len(words)-1: word=low
        elif re.search(r'[a-z][A-Z]',word) or (word.isupper() and len(word)>1): pass
        else:
            word=re.sub(r'(^|[-–—/(“‘])([a-z])',lambda m:m[1]+m[2].upper(),word)
        out.append(word)
    result=' '.join(out)
    for i,math in enumerate(mathematics): result=result.replace('MATHOPAQUE'+str(i)+'TOKEN',math)
    return result

def safe_name(value):
    value=title_case(value)
    value=re.sub(r'[<>:"/\\|?*\[\]#^]', ' ', value)
    value=re.sub(r'\s+', ' ', value).strip(' .')
    return value[:155].rstrip() or 'Overview'

def wiki(path, label=None, anchor=None):
    target=str(path).removesuffix('.md')
    if anchor: target += '#^'+anchor
    return '[['+target+'|'+(label or Path(path).stem)+']]'

def frontmatter(meta):
    return '---\n'+yaml.safe_dump(meta,allow_unicode=True,sort_keys=False,width=1000).strip()+'\n---\n\n'

def clean_table_line(line):
    """Preserve math and link aliases without creating extra Markdown columns."""
    if not line.lstrip().startswith('|'): return line
    def math(match):
        value=match[1].replace(r'\|',r'\Vert ')
        value=re.sub(r'(?<!\\)\|',lambda _:r'\vert ',value)
        return '$'+value+'$'
    line=re.sub(r'(?<!\\)\$(?!\$)(.+?)(?<!\\)\$',math,line)
    return re.sub(r'\[\[[^\]\n]+\]\]',lambda m:re.sub(r'(?<!\\)\|',r'\\|',m[0]),line)

def plain_note(vault,path,title,body,kind='Index',**extra):
    dest=vault/path; dest.parent.mkdir(parents=True,exist_ok=True)
    meta={'title':title,'type':kind,'tags':['Type/'+kind.replace(' ','_')],**extra}
    dest.write_text(clean_markdown(frontmatter(meta)+'# '+title+'\n\n'+body.strip()+'\n'),encoding='utf-8')

def outside_fences_lines(body):
    fence=None
    for line in body.splitlines(keepends=True):
        match=re.match(r'^\s*(`{3,}|~{3,})',line)
        inside=fence is not None
        if match:
            if fence is None: fence=match[1][0]
            elif match[1][0]==fence: fence=None
            yield line,True
        else: yield line,inside

def clean_markdown(text):
    lines=[]; blanks=0
    for line,code in outside_fences_lines(text):
        value=line.rstrip('\n')
        if not code:
            hard_break=value.endswith('  ') and bool(value.strip())
            value=value.rstrip() + ('\\' if hard_break else '')
            blanks=blanks+1 if not value else 0
            if blanks>1: continue
        else: blanks=0
        lines.append(value)
    return '\n'.join(lines).rstrip()+'\n'

def unescape_anchor(value):
    return re.sub(r'\\([^\w\s])',r'\1',value)

def block_markers(body):
    result=[]; math=False
    for line,code in outside_fences_lines(body):
        if code: continue
        if line.strip()=='$$': math=not math; continue
        if not math and (m:=re.match(r'^\^(\S+)[ \t]*$',line.strip('\n'))):
            result.append(unescape_anchor(m[1]))
    return list(dict.fromkeys(result))

def normalize_blocks(body,mapping):
    result=[]; math=False
    for line,code in outside_fences_lines(body):
        if not code and line.strip()=='$$': math=not math
        m=None if code or math else re.match(r'^\^(\S+)[ \t]*\n?$',line)
        if m and unescape_anchor(m[1]) in mapping:
            line='^'+mapping[unescape_anchor(m[1])]+'\n\n'
        result.append(line)
    return ''.join(result)

def canonicalize_headings(body):
    lines=[]
    for line,code in outside_fences_lines(body):
        if not code and (m:=re.match(r'^(#{1,6})\s+(.+?)\s*\n?$',line)):
            text=m[2]; a=re.search(r'\s*\{#([^ }]+)[^}]*\}\s*$',text)
            ident=a[1] if a else None
            text=re.sub(r'\s*\{[^}]*\}\s*$','',text)
            line=m[1]+' '+title_case(text)+((' {#'+ident+'}') if ident else '')+'\n'
        lines.append(line)
    return ''.join(lines)

def split_document(doc):
    body=canonicalize_headings(doc['body'])
    footnotes={}
    def keep_footnote(m):
        footnotes[m[1]]=m[0].strip(); return ''
    body=re.sub(r'(?m)^\[\^([^\]]+)\]:[^\n]*(?:\n(?:[ \t]{2,}[^\n]*|(?=\n[ \t]{2,})[^\n]*))*',keep_footnote,body)
    chunks=[]; current=[]; label=doc['title']; anchor=''; h1=True
    for line,code in outside_fences_lines(body):
        match=None if code else re.match(r'^(#{1,2})\s+(.+?)\s*$',line)
        if match:
            text=re.sub(r'\s*\{[^}]*\}\s*$','',match[2]).strip()
            aid=re.search(r'\{#([^ }]+)',match[2]); aid=aid[1] if aid else ''
            if match[1]=='#' and h1:
                label=text; anchor=aid; h1=False
                if aid: current.append('^'+aid+'\n\n')
                continue
            if match[1]=='##' and doc['kind']=='chapter':
                chunks.append({'label':label,'anchor':anchor,'body':''.join(current)})
                current=[]; label=text; anchor=aid
                if aid: current.append('^'+aid+'\n\n')
                continue
        current.append(line)
    chunks.append({'label':label,'anchor':anchor,'body':''.join(current)})
    # Preserve header anchors as Obsidian block references; nested headings remain readable.
    for c in chunks:
        cited=list(dict.fromkeys(re.findall(r'\[\^([^\]]+)\]',c['body'])))
        if cited: c['body']+='\n\n'+'\n\n'.join(footnotes[k] for k in cited if k in footnotes)+'\n'
        c['body']=re.sub(r'(?m)^(#{1,6} .+?)[ \t]*\{#([^ }]+)[^}]*\}[ \t]*$',r'\1\n\n^\2\n',c['body'])
        c['anchors']=block_markers(c['body'])
        if c['anchor'] and c['anchor'] not in c['anchors']: c['anchors'].insert(0,c['anchor'])
    return chunks

def inventory(repo):
    docs=[]
    for v in range(1,5):
        conf=yaml.safe_load((repo/f'books/config/_quarto-pdf-vol{v}.yml').read_text())
        items=conf['book']['chapters']+conf['book'].get('appendices',[])
        part_index=0; part='00 Introduction'
        for source in items:
            if not isinstance(source,str) or source=='index.qmd': continue
            p=repo/'books'/source
            if not p.exists(): raise FileNotFoundError(p)
            m=re.search(r'/([0-9]{2})_[^/]+/[^/]+\.qmd$',str(p))
            chapter=int(m[1]) if m else 0
            kind='chapter' if chapter else 'part' if '/parts/' in source else 'reference' if ('/backmatter/' in source or '/appendices/' in source) else 'frontmatter'
            if kind=='part':
                part_index+=1; part=f'{part_index:02d} {PARTS[v][part_index-1]}'
            if kind=='chapter':
                folder=f'01 Books/{VOLUMES[v]}/{part}'
            elif kind=='part': folder=f'01 Books/{VOLUMES[v]}/{part}'
            elif kind=='reference': folder=f'05 Reference/{VOLUMES[v]}'
            else: folder=f'01 Books/{VOLUMES[v]}/Frontmatter'
            docs.append({'source_path':p.relative_to(repo).as_posix(),'source':p,'kind':kind,'volume':v,'chapter':chapter,'part':part,'folder':folder})
    return docs

def build(repo,vault,workers=8):
    from render_source import render_document
    from media_import import import_media, prune_unused_generated_assets
    vault.mkdir(parents=True,exist_ok=True)
    (vault/'.gitattributes').write_text('# Preserve byte-identical imported SVG path data and provenance hashes.\n*.svg -whitespace\n')
    previous={}
    old_manifest=vault/'99 System/Import Manifest.json'
    if old_manifest.exists():
        previous=json.loads(old_manifest.read_text())
        for old in previous.get('notes',[]):
            if str(old.get('source_path','')).startswith('books/'):
                dest=vault/old['path']
                if dest.exists(): dest.unlink()
    source_commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=repo,text=True).strip()
    docs=inventory(repo)
    print(f'Rendering {len(docs)} Source Documents',flush=True)
    def render(d):
        result=render_document(d['source'],repo)
        d.update(result)
        d['title']=title_case(d.get('title') or d['source'].stem.replace('_',' '))
        d['chunks']=split_document(d)
        return d
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        for i,d in enumerate(pool.map(render,docs),1):
            if i%10==0 or i==len(docs): print(f'Rendered {i}/{len(docs)}',flush=True)
    notes=[]; used=set()
    for doc in docs:
        v=doc['volume']; ch=doc['chapter']; prefix=f'V{v}-{ch:02d}' if ch else f'V{v}'
        chaptertitle=safe_name(f'{prefix} {doc["title"]}')
        doc['chapter_title']=chaptertitle
        folder=doc['folder']+(f'/{ch:02d} {safe_name(doc["title"])}' if ch else '')
        for i,chunk in enumerate(doc['chunks']):
            kind=doc['kind'] if i==0 else 'section'
            name=chaptertitle if i==0 else safe_name(f'{prefix}.{i:02d} {chunk["label"]}')
            p=f'{folder}/{name}.md'
            if p.casefold() in used:
                name=safe_name(name+' '+Path(doc['source_path']).stem.replace('_',' ')); p=f'{folder}/{name}.md'
            if p.casefold() in used: raise ValueError('Duplicate note path '+p)
            used.add(p.casefold())
            block_ids={a: a if re.fullmatch(r'[A-Za-z0-9-]+',a) else re.sub(r'[^A-Za-z0-9-]+','-',a).strip('-')+'-'+hashlib.sha1(a.encode()).hexdigest()[:8] for a in chunk['anchors']}
            chunk['body']=normalize_blocks(chunk['body'],block_ids)
            record={'block_ids':block_ids,'path':p,'title':name,'source_path':doc['source_path'],'source_anchor':chunk['anchor'],'source_anchors':chunk['anchors'],'kind':kind,'volume':v,'chapter':ch,'part':doc['part'],'source_mode':doc.get('source_mode','qmd'),'rendered_source_url':doc.get('rendered_source_url'),'body':chunk['body'],'document':doc}
            notes.append(record)
        doc['note_records']=[n for n in notes if n['source_path']==doc['source_path']]
        doc['overview_path']=doc['note_records'][0]['path']
    # Media URLs can be shared among sections, but all imports receive complete source context.
    print('Importing Images',flush=True)
    media=import_media(notes,repo,vault,source_commit)
    manifest={'schema_version':1,'source_repository':'https://github.com/klappe-pm/cs249r_book','upstream_repository':'https://github.com/harvard-edge/cs249r_book','source_commit':source_commit,'notes':[], 'documents':[], 'media':media}
    # Build exact scoped source-anchor map before any rewriting.
    by_source=collections.defaultdict(list); by_anchor=collections.defaultdict(list)
    for n in notes:
        by_source[n['source_path']].append(n)
        for aid in n['source_anchors']:
            by_anchor[aid.lower()].append((n,n['block_ids'].get(aid,aid)))
    doc_lookup={d['source_path']:d for d in docs}
    unresolved=[]
    def resolve_anchor(anchor,record,source_hint=None):
        key=unquote(anchor).lstrip('^').lower()
        candidates=by_anchor.get(key,[])
        if source_hint:
            exact=[x for x in candidates if x[0]['source_path']==source_hint]
            if exact: candidates=exact
        same=[x for x in candidates if x[0]['source_path']==record['source_path']]
        if same: candidates=same
        else:
            same=[x for x in candidates if x[0]['volume']==record['volume']]
            if same: candidates=same
        if len(candidates)==1: return candidates[0]
        return None
    def source_url(record,anchor=''):
        return f'https://github.com/klappe-pm/cs249r_book/blob/{source_commit}/{record["source_path"]}'+('#'+anchor if anchor else '')
    def rewrite_text(text,record):
        # A Markdown link whose book page is imported becomes an exact vault reference.
        def link(m):
            label,target=m[1],m[2].strip('<>')
            if any(x in label for x in ['Computed Value In Source','View Rendered','Source Reference','Image Source','Original Source']): return m[0]
            if label.startswith('!') or target.startswith(('mailto:','data:')): return m[0]
            absolute=urljoin(record['document'].get('rendered_source_url') or 'https://mlsysbook.ai/'+record['source_path'].removeprefix('books/').replace('.qmd','.html'),target)
            parsed=urlparse(absolute); anchor=parsed.fragment
            hint=None
            if 'mlsysbook.ai' in parsed.netloc:
                hint='books/'+unquote(parsed.path).lstrip('/').replace('.html','.qmd')
                # Older deployments nest the volume slug twice.
                if hint not in doc_lookup:
                    mt=re.search(r'(vol[1-4]/.+\.qmd)$',hint)
                    if mt: hint='books/'+mt[1]
            elif not urlparse(target).scheme:
                hint=os.path.normpath(str(Path(record['source_path']).parent/target.split('#')[0])).replace('\\','/')
            if anchor and (target.startswith('#') or 'mlsysbook.ai' in parsed.netloc or (hint and hint in doc_lookup)):
                resolved=resolve_anchor(anchor,record,hint)
                if resolved:
                    clean_label=re.sub(r'<[^>]*>|[\[\]|]','',label)
                    if re.fullmatch(r'fn\d+',anchor): clean_label=clean_label.translate(str.maketrans('0123456789','⁰¹²³⁴⁵⁶⁷⁸⁹'))
                    return wiki(resolved[0]['path'],clean_label,resolved[1])
            if hint in doc_lookup and not anchor:
                return wiki(doc_lookup[hint]['overview_path'],re.sub(r'<[^>]*>|[\[\]|]','',label))
            # Preserve a reachable explicit source link for references absent in this revision.
            if target.startswith('#'):
                unresolved.append({'note':record['path'],'target':target,'fallback':absolute})
                return f'[{label}]({absolute})'
            return m[0]
        text=''.join(line if code else re.sub(r'(?<!!)\[([^\[\]\n]+)\]\((<[^>]+>|[^)\s]+)\)',link,line) for line,code in outside_fences_lines(text))
        def xref(m):
            token=m[1].rstrip('.:,;'); suffix=m[1][len(token):]; resolved=resolve_anchor(token,record)
            if resolved:
                n,aid=resolved
                label=token.split('-',1)[0].title()+' — '+n['title']
                return wiki(n['path'],label,aid)+suffix
            unresolved.append({'note':record['path'],'target':'@'+token,'fallback':source_url(record)})
            return '[Source Reference: '+token+']('+source_url(record)+')'
        text=''.join(line if code else re.sub(r'(?<![\w/])@((?:sec|fig|tbl|eq|lst|exm|exmp|thm|def|lem|prp|cnj|cor|alg|tip|wrn|nt|imp|cau|exr)-[A-Za-z0-9_.:-]+)',xref,line,flags=re.I) for line,code in outside_fences_lines(text))
        return text
    for record in notes:
        doc=record['document']; v=record['volume']; ch=record['chapter']
        body=''
        nav=[wiki('Home.md','Home'),wiki(f'01 Books/{VOLUMES[v]}/Volume {v} Overview.md','Volume Overview')]
        if record['kind']=='section': nav.append(wiki(doc['overview_path'],doc['chapter_title']))
        body+=' · '.join(nav)+'\n\n'
        body+=record['body'].strip()+'\n'
        if record['kind']=='chapter':
            sections=[n for n in doc['note_records'] if n['kind']=='section']
            if sections:
                body+='\n## Chapter Sections\n\n'+'\n'.join('- '+wiki(n['path'],n['title']) for n in sections)+'\n'
        seq=doc['note_records']; idx=seq.index(record)
        nearby=[]
        if idx: nearby.append('Previous: '+wiki(seq[idx-1]['path']))
        if idx+1<len(seq): nearby.append('Next: '+wiki(seq[idx+1]['path']))
        if nearby: body+='\n'+' · '.join(nearby)+'\n'
        body=rewrite_text(body,record)
        # Wiki aliases require escaped pipes inside Markdown table cells.
        body='\n'.join(clean_table_line(line) for line in body.split('\n'))
        body+='\n## Source\n\n'
        body+='[Repository Source]('+source_url(record)+') · [Original License](https://github.com/klappe-pm/cs249r_book/blob/'+source_commit+'/LICENSE.md)\n'
        if doc.get('rendered_source_url'):
            body+='\n[Rendered Reading Snapshot]('+doc['rendered_source_url']+('#'+record['source_anchor'] if record['source_anchor'] else '')+'). Rendering provenance is recorded in the import manifest.\n'
        meta={'title':record['title'],'type':record['kind'].title(),'volume':v,'chapter':ch,'publication_status':STATUSES[v],'source_repository':manifest['source_repository'],'source_commit':source_commit,'source_path':record['source_path'],'source_anchor':record['source_anchor'],'source_mode':record['source_mode'],'tags':['Type/'+record['kind'].title(),'Book/Volume_'+str(v)]}
        if doc.get('rendered_source_url'): meta['rendered_source_url']=doc['rendered_source_url']
        dest=vault/record['path']; dest.parent.mkdir(parents=True,exist_ok=True)
        dest.write_text(clean_markdown(frontmatter(meta)+'# '+record['title']+'\n\n'+body.strip()+'\n'),encoding='utf-8')
        manifest['notes'].append({k:record[k] for k in ['path','title','source_path','source_anchor','source_anchors','block_ids','kind','volume','chapter','part','source_mode','rendered_source_url']})
    for doc in docs:
        manifest['documents'].append({k:doc.get(k) for k in ['source_path','title','kind','volume','chapter','source_mode','rendered_source_url','warnings','rendered_sha256','prose_coverage','restored_source_headings','fidelity']})
    manifest['unresolved_references']=unresolved
    create_navigation(repo,vault,docs,manifest)
    repair_preserved_links(vault,previous,manifest)
    prune_unused_generated_assets(vault)
    path=vault/'99 System/Import Manifest.json'; path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print(f'Imported {len(notes)} Book Notes; {len(unresolved)} References Use Explicit Source Fallbacks',flush=True)
    return manifest

def repair_preserved_links(vault,previous,current):
    # Follow stable source identity when a generated title changes; retain progress and prose.
    keys=lambda n:(n.get('source_path'),n.get('source_anchor'),n.get('kind'),'' if n.get('source_anchor') else n.get('title','').casefold())
    current_by_key={keys(n):n for n in current.get('notes',[])}
    mapping={}
    for old in previous.get('notes',[]):
        new=current_by_key.get(keys(old))
        if new and new['path']!=old['path']:
            mapping[old['path'].removesuffix('.md')]=new['path'].removesuffix('.md')
    generated={n['path'] for n in current.get('notes',[])}
    targets={n['path'].removesuffix('.md').casefold():n['path'].removesuffix('.md') for n in current.get('notes',[])}
    for p in vault.rglob('*.md'):
        if p.relative_to(vault).as_posix() in generated or '/Reviews/' in p.as_posix(): continue
        text=p.read_text()
        for old,new in mapping.items():
            text=text.replace('[['+old+'|','[['+new+'|').replace('[['+old+'#','[['+new+'#').replace('[['+old+']]','[['+new+']]')
        text=re.sub(r'\[\[([^\]|#]+)([|#]|\]\])',lambda m:'[['+targets.get(m[1].casefold(),m[1])+m[2],text)
        p.write_text(text)

def create_navigation(repo,vault,docs,manifest):
    home='A connected reading and study vault for *Machine Learning Systems* by Vijay Janapa Reddi and contributors.\n\n'
    home+='## Start Here\n\n'+ '\n'.join('- '+wiki(p) for p in ['00 Navigation/Book Contents.md','00 Navigation/Topic Index.md','00 Navigation/Learning Paths.md','00 Navigation/Reading Progress.md','99 System/Vault Guide.md'])+'\n\n## The Four Volumes\n\n'
    contents=[]
    for v in range(1,5):
        path=f'01 Books/{VOLUMES[v]}/Volume {v} Overview.md'; title=f'Volume {v} Overview'
        home+='- '+wiki(path,VOLUMES[v])+f' — {STATUSES[v]}\n'
        body=f'Publication status: **{STATUSES[v]}**.\n\n'
        groups=collections.OrderedDict()
        for doc in docs:
            if doc['volume']==v:
                group='Reference' if doc['kind']=='reference' else 'Frontmatter' if doc['kind']=='frontmatter' else doc['part']
                groups.setdefault(group,[]).append(doc)
        contents.append('## '+VOLUMES[v]+'\n\n'+wiki(path)+'\n')
        for group,items in groups.items():
            body+='## '+title_case(group)+'\n\n'
            body+='\n'.join('- '+wiki(d['overview_path'],d['chapter_title']) for d in items)+'\n\n'
            if group not in ('Reference','Frontmatter'):
                partpath=f'01 Books/{VOLUMES[v]}/{group}/V{v} {safe_name(group)} Index.md'
                plain_note(vault,partpath,f'V{v} {safe_name(group)} Index','\n'.join('- '+wiki(d['overview_path']) for d in items),volume=v)
        plain_note(vault,path,title,body,volume=v,publication_status=STATUSES[v])
    home+='\n## Explore and Practice\n\n'+ '\n'.join('- '+wiki(p) for p in ['02 Concepts/Concept Index.md','03 Themes/Theme Index.md','04 Practice/Practice Index.md','05 Reference/Reference Index.md','06 My Notes/My Notes Index.md'])
    if (vault/'99 System/Reviews/Review Index.md').exists(): home+='\n\n## Review Evidence\n\n'+wiki('99 System/Reviews/Review Index.md','Completed Review Rounds and Validation Evidence')
    plain_note(vault,'Home.md','Home',home)
    plain_note(vault,'00 Navigation/Book Contents.md','Book Contents','\n\n'.join(contents))
    plain_note(vault,'00 Navigation/Topic Index.md','Topic Index','Explore '+wiki('02 Concepts/Concept Index.md')+' and '+wiki('03 Themes/Theme Index.md')+'. Concepts have one canonical home; themes connect related passages across volumes.')
    reading='Track progress here; this file is preserved when the importer runs again.\n\n'
    reading+='\n'.join('- [ ] '+wiki(d['overview_path'],d['chapter_title']) for d in docs if d['kind']=='chapter')
    if not (vault/'00 Navigation/Reading Progress.md').exists(): plain_note(vault,'00 Navigation/Reading Progress.md','Reading Progress',reading)
    routes={
     'Foundations to Production':[(1,1),(1,3),(1,4),(1,5),(1,8),(1,10),(1,11),(1,12),(1,13),(1,14),(1,15)],
     'Distributed Training':[(1,8),(1,11),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),(2,9)],
     'Agent Systems':[(1,13),(2,10),(3,2),(3,4),(3,5),(3,6),(3,7),(3,8),(3,9),(3,10),(3,11),(3,12),(3,13),(3,14)],
     'Physical AI':[(1,2),(1,10),(2,11),(4,1),(4,2),(4,3),(4,4),(4,5),(4,7),(4,8),(4,11),(4,12),(4,15),(4,17)]}
    routebody='Suggested reading sequences curated for this vault. They are navigation suggestions, not claims that every preceding chapter is a prerequisite.\n\n'
    for title,seq in routes.items():
        routebody+='## '+title+'\n\n'
        for v,ch in seq:
            d=next((d for d in docs if d['volume']==v and d['chapter']==ch),None)
            if d: routebody+='1. '+wiki(d['overview_path'],d['chapter_title'])+'\n'
        routebody+='\n'
    plain_note(vault,'00 Navigation/Learning Paths.md','Learning Paths',routebody)
    practices={'TinyTorch':('tinytorch','Build a small ML framework and connect implementation work to the textbook.'),'Labs':('labs','Work through the companion exercises and notebooks.'),'Hardware Kits':('kits','Apply concepts to physical devices and their deployment constraints.'),'MLSysim':('mlsysim','Explore quantitative system models and tradeoffs.')}
    pb=[]
    for title,(source,desc) in practices.items():
        p=f'04 Practice/{title}/{title} Practice.md'; pb.append('- '+wiki(p))
        body=desc+'\n\nThese are companion entry points. Executable notebooks and implementation code remain in the linked source.\n\n[Companion Source](https://github.com/klappe-pm/cs249r_book/tree/'+manifest['source_commit']+'/'+source+')\n\n## Related Reading\n\n'
        recommended={'TinyTorch':[(1,5),(1,6),(1,7),(1,8)],'Labs':[(1,8),(1,12),(2,9),(3,13)],'Hardware Kits':[(1,2),(1,10),(2,11),(4,2),(4,4)],'MLSysim':[(1,1),(1,11),(2,2),(2,3),(2,9)]}[title]
        for v,ch in recommended:
            d=next(d for d in docs if d['volume']==v and d['chapter']==ch)
            body+='- '+wiki(d['overview_path'],d['chapter_title'])+'\n'
        body+='\n## Experiment Notes\n\nRecord the task, expected result, measured result, and related reading in '+wiki('06 My Notes/Experiments/Experiment Log.md')+'.'
        plain_note(vault,p,title+' Practice',body,'Practice')
    plain_note(vault,'04 Practice/Practice Index.md','Practice Index','\n'.join(pb))
    refs=[d for d in docs if d['kind']=='reference']
    plain_note(vault,'05 Reference/Reference Index.md','Reference Index','\n'.join('- '+wiki(d['overview_path'],d['chapter_title']) for d in refs)+'\n\n'+wiki('05 Reference/Bibliography/Bibliography Sources.md'))
    bibdir=vault/'05 Reference/Bibliography'; bibdir.mkdir(parents=True,exist_ok=True)
    bib=subprocess.check_output(['git','show','HEAD:bibs/references.bib'],cwd=repo); (bibdir/'Book References.bib').write_bytes(bib)
    plain_note(vault,'05 Reference/Bibliography/Bibliography Sources.md','Bibliography Sources','The original BibTeX database is included as `Book References.bib`. Inline citation targets are preserved from the rendered source or point to the imported volume reference notes.\n\n[Repository Bibliography](https://github.com/klappe-pm/cs249r_book/blob/'+manifest['source_commit']+'/books/references.bib)')
    for sub,title in [('Inbox','Inbox'),('Questions','Open Questions'),('Experiments','Experiment Log')]:
        p=f'06 My Notes/{sub}/{title}.md'
        if not (vault/p).exists(): plain_note(vault,p,title,'Add your notes here. Link book passages and concepts using `[[Note Name]]`.','Personal')
    plain_note(vault,'06 My Notes/My Notes Index.md','My Notes Index','\n'.join('- '+wiki(p) for p in ['06 My Notes/Inbox/Inbox.md','06 My Notes/Questions/Open Questions.md','06 My Notes/Experiments/Experiment Log.md']))
    guide='''Open this `obsidian-vault` folder as a vault in Obsidian. Start at [[Home]]. Core links, backlinks, tags, search, and Graph View work without community plugins.

## Reading Structure

Books retain volume and part order. Chapter overview notes link to section notes; each section links back to its chapter. Source headings and original identifiers are retained as exact Obsidian block references. Titles and prose headings use Title Case, preserving technical acronyms.

## Concepts and Themes

Canonical concept notes use the repository taxonomy and retain its draft status, stable identifiers, and relationship conditions. Related passages are not assertions of prerequisite order or complete coverage. Theme notes are curated reading lenses. Obsidian computes backlinks from the explicit links in these notes.

## Tables, Images, and Mathematics

Tables use Markdown pipe tables or HTML tables for structures that require merged cells. Images are imported locally under `90 Assets`. Source-specific LaTeX notation is expanded or supplied as MathJax-compatible definitions. The import manifest records image provenance, rendering mode, and explicit fallbacks for content that cannot be represented faithfully.

## Rebuilding

Run `python obsidian_tools/build_vault.py`, then `python obsidian_tools/link_vault.py --repo .`, then `python obsidian_tools/validate_vault.py` from the repository root. Rebuilding replaces generated notes; personal notes and reading progress are preserved. Source and rendering snapshots are recorded separately, because a published rendering can differ from the pinned repository commit.

## Naming and Tags

File names and headings use Title Case. Source identifiers keep their original machine-readable spelling for stable references. Tags use slash-separated namespaces and underscores where spaces would otherwise be required.
'''
    plain_note(vault,'99 System/Vault Guide.md','Vault Guide',guide)
    licensebody=(repo/'LICENSE.md').read_text()
    attribution='Source: *Machine Learning Systems*, Vijay Janapa Reddi and contributors.\n\nRepository snapshot: `'+manifest['source_commit']+'`.\n\n[Upstream Repository](https://github.com/harvard-edge/cs249r_book) · [Fork](https://github.com/klappe-pm/cs249r_book)\n\n## Original License Notice\n\n'+licensebody+'\n\n## Taxonomy\n\nTaxonomy definitions and relationships carry CC BY 4.0 as stated in the source taxonomy documentation. Book text carries its own component license. Imported source, editorial navigation, and personal notes retain separate provenance.'
    plain_note(vault,'99 System/Sources and Attribution.md','Sources and Attribution',attribution,'Reference')
    plain_note(vault,'99 System/Templates/Study Note Template.md','Study Note Template','## Question\n\n## Explanation\n\n## Evidence\n\n## Related Reading\n\n## Next Experiment','Template')
    configs={'app.json':{'newLinkFormat':'absolute','useMarkdownLinks':False,'attachmentFolderPath':'90 Assets','alwaysUpdateLinks':True,'showLineNumber':True,'spellcheck':True},'appearance.json':{'baseFontSize':17},'core-plugins.json':['file-explorer','global-search','switcher','graph','backlink','outgoing-link','tag-pane','page-preview','templates','note-composer','outline','word-count','bookmarks'],'templates.json':{'folder':'99 System/Templates'},'graph.json':{'collapse-filter':False,'search':'-path:"90 Assets" -path:"99 System"','showTags':True,'showAttachments':False}}
    (vault/'.obsidian').mkdir(exist_ok=True)
    for file,data in configs.items():
        p=vault/'.obsidian'/file
        if not p.exists(): p.write_text(json.dumps(data,indent=2)+'\n')

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--repo',type=Path,default=ROOT);ap.add_argument('--vault',type=Path);ap.add_argument('--workers',type=int,default=8)
    args=ap.parse_args(); build(args.repo.resolve(),args.vault or args.repo/'obsidian-vault',args.workers)
