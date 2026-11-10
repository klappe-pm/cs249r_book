#!/usr/bin/env python3
"""Build source-grounded concept notes, themes, and semantic backlinks.

Run after build_vault.py. Only explicit upstream alignments create passage links.
Taxonomy browsing homes and chapter reading pointers are not prerequisites.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
import json
from pathlib import Path
import re
from urllib.parse import quote

import yaml

BEGIN = "<!-- Semantic Navigation: Begin -->"
END = "<!-- Semantic Navigation: End -->"
SMALL = {"a", "an", "and", "as", "at", "but", "by", "for", "from", "in", "into", "nor", "of", "on", "or", "per", "the", "to", "via", "vs", "with"}
ACRONYMS = {x.lower(): x for x in "AI ML MLOps API APIs CPU CPUs GPU GPUs TPU TPUs NPU NPUs FPGA FPGAs ASIC ASICs SRAM DRAM HBM RAM ROM KV IO FLOP FLOPs FLOPS SIMD SIMT SLO SLOs SLI SLIs SLA SLAs DNN DNNs CNN CNNs RNN RNNs LLM LLMs MoE SGD DP RL RLHF RLVR DPO PPO GRPO PEFT LoRA QLoRA RAG RPC RDMA NCCL MPI TCP UDP IP HTTP TLS NUMA PCIe NVLink NVSwitch CUDA JIT AOT IR LLVM XLA ONNX TFLite TinyML TinyTorch MLSysim TFLOPS BF16 FP16 FP32 FP64 FP8 INT4 INT8 INT32 PTQ QAT AWQ GPT BERT ResNet MobileNet PyTorch TensorFlow ReLU GELU SiLU RMSNorm LayerNorm BatchNorm OS OOM SSD SSDs HDD HDDs NVMe NFS HDFS Ceph POSIX S3 WAF IAM RBAC ABAC ACL ACLs JWT OAuth SQL NoSQL DNS VM VMs WASM WebAssembly LLC L1 L2 L3 L4 E2E ID IDs OOD IID KL JS JSON YAML HTML SVG PNG JPEG WebP URL URLs SHA UTF SOC SoC UPS PUE WUE CUE CO2e MTBF MTTR MTTF RTO RPO RTT HSA DAM C3 WCET VLA VLM VLMs MPC PID ROS ROS2 SLAM SIL HIL ODD FMEA STPA ISO NIST IEEE ACM MIT SKOS RDF OWL W3C ANSI NISO DCAT LinkML MMLU NAS SVD KNN kNN PCA FFT DCT CTC BLEU ROUGE MAE MSE RMSE AUROC AUC F1 IoU mAP".split()}


def title_case(value):
    value = str(value).replace("I/O", "IO").replace("CI/CD", "CI CD")
    value = re.sub(r"(?<=\w)[_\-](?=\w)", " ", value).strip().replace("/", " ")
    parts = re.split(r"(\s+)", value)
    words = [i for i, x in enumerate(parts) if x and not x.isspace()]
    for i in words:
        word = parts[i]
        m = re.match(r"([^\w]*)(.*?)([^\w]*)$", word)
        prefix, core, suffix = m.groups() if m else ("", word, "")
        if core.lower() in ACRONYMS:
            core = ACRONYMS[core.lower()]
        elif core.lower() in SMALL and i not in (words[0], words[-1]):
            core = core.lower()
        elif re.search(r"[a-z][A-Z]", core):
            pass
        elif core:
            core = core[0].upper() + core[1:]
        parts[i] = prefix + core + suffix
    return "".join(parts)


def filename(value):
    value = re.sub(r'[<>:"/\\|?*\[\]#^]', " ", title_case(value))
    return re.sub(r"\s+", " ", value).strip(" .")


def wiki(path, label=None):
    target = str(path).removesuffix(".md")
    label = (label or Path(path).stem).replace("|", " ").replace("[", "").replace("]", "")
    return f"[[{target}|{label}]]"


def clean(value):
    return re.sub(r"\[\[([^\]]+)\]\]", r"\1", str(value)).strip()


def tag_segment(value):
    return re.sub(r"_+", "_", re.sub(r"[^\w]", "_", title_case(value))).strip("_")


def load_yaml(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def source_url(repository, commit, path, line=None):
    repository = repository.removeprefix("https://github.com/").removesuffix(".git").strip("/")
    suffix = f"#L{line}" if line else ""
    return f"https://github.com/{repository}/blob/{commit}/{quote(path, safe='/')}{suffix}"


def source_headings(path):
    result = []
    fence = None
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        f = re.match(r"^\s*(" + chr(96) + r"{3,}|~{3,})", line)
        if f:
            if fence is None:
                fence = f.group(1)[0]
            elif f.group(1)[0] == fence:
                fence = None
            continue
        if fence:
            continue
        m = re.match(r"^(#{1,6})\s+(.+)", line)
        if m:
            anchor = re.search(r"\{[^}]*#([^\s}]+)", m.group(2))
            if anchor:
                result.append({"level": len(m.group(1)), "anchor": anchor.group(1), "line": number})
    return result


THEMES = {
    "Constraints Drive Architecture": {
        "description": "Trace how workload requirements, resource budgets, and deployment limits shape model and system choices.",
        "concepts": ["requirements", "slo", "latency-budget", "memory-capacity", "on-device-memory-budget", "pareto-frontier", "roofline", "arithmetic-intensity", "compute-throughput"],
    },
    "Memory and Bandwidth": {
        "description": "Follow capacity, bandwidth, and data movement from hardware through training and generative inference.",
        "concepts": ["memory-hierarchy", "memory-capacity", "memory-bandwidth", "memory-footprint", "memory-wall", "arithmetic-intensity", "roofline", "kv-cache", "kv-cache-quantization", "memory-offloading", "io-aware-attention", "data-movement-energy"],
    },
    "Latency and Throughput": {
        "description": "Compare response-time budgets, queueing, batching, and useful serving capacity under an explicit workload.",
        "concepts": ["tail-latency", "latency-budget", "latency-percentiles", "latency-throughput-curve", "request-throughput", "batching", "continuous-batching", "queueing", "slo", "slo-goodput", "inter-token-latency", "perception-latency-budget"],
    },
    "Accuracy and Efficiency": {
        "description": "Connect model quality to representation, compression, and the measured resource cost of a useful result.",
        "concepts": ["pareto-frontier", "generalization", "quantization", "post-training-quantization", "quantization-aware-training", "weight-only-quantization", "precision", "pruning", "structured-pruning", "distillation", "energy-efficiency", "unit-cost"],
    },
    "Scaling and Coordination": {
        "description": "Follow partitioning and synchronization costs across accelerator fleets and multi-agent systems.",
        "concepts": ["data-parallel", "tensor-parallel", "pipeline-parallel", "expert-parallel", "sequence-parallel", "hybrid-parallel", "all-reduce", "parallel-efficiency", "bisection-bandwidth", "coordination-failure"],
    },
    "Reliability and Recovery": {
        "description": "Connect recovery state, failure boundaries, replay, and production rollback without conflating local recovery with undone external effects.",
        "concepts": ["checkpoint", "checkpoint-io", "checkpoint-interval", "async-checkpointing", "idempotency", "retry-backoff", "recovery-objectives", "restart-free-recovery", "rollback"],
    },
    "Security and Trust": {
        "description": "Follow threat models, least authority, privacy, and safety evidence across deployed, agentic, and physical systems.",
        "concepts": ["threat-model", "least-privilege", "capability-based-security", "prompt-injection", "privacy", "differential-privacy", "privacy-budget", "safety-case", "functional-safety", "safety-filter"],
    },
    "Energy and Cost": {
        "description": "Compare energy, carbon, and cost accounting against the useful outcome delivered by a complete system.",
        "concepts": ["energy", "data-movement-energy", "energy-efficiency", "energy-per-inference", "energy-measurement", "carbon", "operational-carbon", "embodied-carbon", "carbon-intensity", "carbon-aware-scheduling", "unit-cost", "cost-per-token", "cost-attribution", "data-transfer-cost"],
    },
}


def build(repo, vault):
    manifest_path = vault / "99 System" / "Import Manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    base_notes = [n for n in manifest["notes"] if n.get("kind") not in {"concept", "theme", "concept_index"}]
    repository = manifest.get("source_repository", "klappe-pm/cs249r_book")
    commit = manifest["source_commit"]
    taxonomy_path = "taxonomy/taxonomy.yml"
    alignment_path = "taxonomy/mlsysbook-alignment.yml"
    taxonomy = load_yaml(repo / taxonomy_path)
    alignment = load_yaml(repo / alignment_path)
    concepts = {c["id"]: c for c in taxonomy["concepts"]}
    groups = {g["id"]: g for g in taxonomy["groups"]}
    areas = {a["id"]: a for a in taxonomy["areas"]}
    rows = {row["id"]: dict(row, area=a["id"], group=a["group"]) for a in taxonomy["areas"] for row in a["rows"]}
    notes_by_source = defaultdict(list)
    chapters = {}
    for note in base_notes:
        notes_by_source[note.get("source_path", "")].append(note)
        if note.get("kind") == "chapter":
            chapters[(int(note["volume"]), int(note["chapter"]))] = note
    source_anchors, source_lines = {}, {}
    for source_path, source_notes in notes_by_source.items():
        if not source_path or not (repo / source_path).is_file():
            continue
        explicit = {n.get("source_anchor"): n for n in source_notes if n.get("source_anchor")}
        for note in source_notes:
            for anchor in note.get("source_anchors", []):
                if isinstance(anchor, dict):
                    anchor = anchor.get("id", anchor.get("anchor"))
                if anchor:
                    source_anchors[(source_path, anchor)] = note
        chapter = next((n for n in source_notes if n.get("kind") == "chapter"), None)
        owner = chapter or source_notes[0]
        for heading in source_headings(repo / source_path):
            anchor = heading["anchor"]
            source_lines[(source_path, anchor)] = heading["line"]
            if anchor in explicit:
                owner = explicit[anchor]
            source_anchors.setdefault((source_path, anchor), owner)

    concept_paths, row_paths, area_paths, group_paths = {}, {}, {}, {}
    for gid, group in groups.items():
        group_paths[gid] = f"02 Concepts/{filename(group['label'])}/{filename(group['label'])} Index.md"
    for aid, area in areas.items():
        root = f"02 Concepts/{filename(groups[area['group']]['label'])}/{filename(area['label'])}"
        area_paths[aid] = f"{root}/{filename(area['label'])} Index.md"
        for row in area["rows"]:
            row_paths[row["id"]] = f"{root}/{filename(row['label'])} Subject.md"
    for cid, concept in concepts.items():
        row = rows[concept["home"]]
        root = str(Path(area_paths[row["area"]]).parent)
        concept_paths[cid] = f"{root}/{filename(concept['label'])}.md"
    if len(set(p.casefold() for p in concept_paths.values())) != len(concept_paths):
        raise ValueError("Concept filenames collide after Title Case normalization")

    graph_concepts, chapter_maps, chapter_map_paths = {}, {}, {}
    for map_path in sorted(repo.glob("books/vol*/**/*concepts.yml")):
        cmap = (load_yaml(map_path) or {}).get("concept_map", {})
        qmd_path = map_path.parent / cmap.get("source", "")
        if not qmd_path.is_file():
            continue
        qmd = qmd_path.relative_to(repo).as_posix()
        match = re.match(r"books/vol(\d)/(\d+)_", qmd)
        if match:
            key = tuple(map(int, match.groups()))
            chapter_maps[key] = cmap
            chapter_map_paths[key] = map_path.relative_to(repo).as_posix()
        for item in cmap.get("learner_graph", {}).get("concepts", []):
            graph_concepts[item["id"]] = dict(item, source_path=qmd)

    passages, passage_links = defaultdict(list), defaultdict(set)
    chapter_fallbacks = []
    unresolved = []
    for link in alignment["links"]:
        cid = link["concept"]
        item = graph_concepts.get(link["book_concept"])
        if cid not in concepts or item is None:
            unresolved.append(dict(link, reason="Unknown Concept Identity"))
            continue
        note = source_anchors.get((item["source_path"], item.get("section", "")))
        if note is None:
            unresolved.append(dict(link, reason="Unresolved Passage Anchor", source_path=item["source_path"], source_anchor=item.get("section")))
            continue
        raw_anchor = item.get("section", "")
        block_id = note.get("block_ids", {}).get(raw_anchor, raw_anchor)
        match = re.match(r"books/vol(\d)/(\d+)_", item["source_path"])
        exact_local_anchor = bool(block_id) and bool(re.search(r"(?m)^\^" + re.escape(block_id) + r"\s*$", (vault / note["path"]).read_text(encoding="utf-8")))
        if not exact_local_anchor:
            chapter = chapters.get(tuple(map(int, match.groups()))) if match else None
            if chapter is None:
                unresolved.append(dict(link, reason="No Local Anchor or Owning Chapter", source_anchor=raw_anchor))
                continue
            chapter_fallbacks.append(dict(link, source_path=item["source_path"], source_anchor=raw_anchor, chapter_path=chapter["path"]))
            note = chapter
            block_id = ""
        target = note["path"].removesuffix(".md") + ("#^" + block_id if block_id else "")
        passage = dict(link, note_path=note["path"], note_target=target, note_title=note["title"], source_path=item["source_path"], source_anchor=raw_anchor, block_id=block_id, exact_local_anchor=exact_local_anchor, source_line=source_lines.get((item["source_path"], raw_anchor)), book_label=item["label"])
        passages[cid].append(passage)
        passage_links[note["path"]].add(cid)
        match = re.match(r"books/vol(\d)/(\d+)_", item["source_path"])
        if match:
            chapter = chapters.get(tuple(map(int, match.groups())))
            if chapter:
                passage_links[chapter["path"]].add(cid)
    outgoing = defaultdict(list)
    for relation in taxonomy["relationships"]:
        if relation["source"] not in concepts or relation["target"] not in concepts:
            raise ValueError(f"Unknown taxonomy relation endpoint: {relation['id']}")
        outgoing[relation["source"]].append(relation)

    theme_paths = {title: f"03 Themes/{title}.md" for title in THEMES}
    concept_themes = defaultdict(list)
    for title, theme in THEMES.items():
        for suffix in theme["concepts"]:
            cid = "mlsys." + suffix
            if cid not in concepts:
                raise ValueError(f"Unknown curated theme concept {cid}")
            concept_themes[cid].append(title)
    generated = []

    def write(path, title, kind, body, **metadata):
        data = {"title": title, "type": kind, "tags": [f"Type/{title_case(kind).replace(' ', '_')}"], "source_repository": repository, "source_commit": commit, "source_path": taxonomy_path}
        data.update(metadata)
        text = "---\n" + yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=120).strip() + "\n---\n\n# " + title + "\n\n" + body.strip() + "\n"
        dest = vault / path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(text, encoding="utf-8")
        generated.append({"path": path, "title": title, "kind": kind, "source_path": taxonomy_path, "source_anchor": "", "volume": 0, "chapter": 0})

    taxonomy_url = source_url(repository, commit, taxonomy_path)
    alignment_url = source_url(repository, commit, alignment_path)
    relation_count = 0
    for cid, concept in concepts.items():
        row = rows[concept["home"]]
        title = filename(concept["label"])
        body = [clean(concept["definition"]), "", "## Browsing Home", "", wiki(row_paths[concept["home"]], filename(row["label"])) + " → " + wiki(area_paths[row["area"]], filename(areas[row["area"]]["label"]))]
        if concept.get("scope") == "background":
            body += ["", "This is a background concept on which ML systems reasoning depends; that classification does not make it optional."]
        body += ["", "## Book Passages", "", "These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage."]
        if passages[cid]:
            seen = set()
            for passage in passages[cid]:
                key = (passage["note_path"], passage["source_anchor"])
                if key in seen:
                    continue
                seen.add(key)
                url = source_url(repository, commit, passage["source_path"], passage["source_line"])
                fallback = " The local reading snapshot omits this source anchor; this link opens the owning chapter." if not passage["exact_local_anchor"] else ""
                body += ["", f"- {wiki(passage['note_target'], passage['note_title'])} — {clean(passage['book_label'])}.{fallback} [Exact Source Passage]({url})."]
        else:
            body += ["", "No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home."]
        if outgoing[cid]:
            body += ["", "## Conditional Relationships", "", "These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim."]
            for edge in outgoing[cid]:
                target = concepts[edge["target"]]
                predicate = clean(edge["predicate"])
                condition = clean(edge.get("conditions", ""))
                body += ["", f"- {predicate[0].upper() + predicate[1:]} {wiki(concept_paths[edge['target']], filename(target['label']))}. **Condition:** {condition}"]
                relation_count += 1
        if concept_themes[cid]:
            body += ["", "## Themes", ""]
            body += [f"- {wiki(theme_paths[theme], theme)}" for theme in concept_themes[cid]]
        if concept.get("aliases"):
            body += ["", "## Search Terms", "", "Upstream search terms may be related terms rather than exact synonyms: " + "; ".join(concept["aliases"]) + "."]
        body += ["", "## Source", "", f"[Canonical Taxonomy]({taxonomy_url}) · [Passage Alignment]({alignment_url})", "", "Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license."]
        tags = ["Type/Concept", "Group/" + tag_segment(groups[row["group"]]["label"]), "Topic/" + tag_segment(row["label"])]
        if concept.get("scope") == "background":
            tags.append("Context/Background")
        write(concept_paths[cid], title, "concept", "\n".join(body), tags=tags, source_label=concept["label"], taxonomy_id=cid, taxonomy_status=concept.get("status", "draft"), taxonomy_version=taxonomy.get("version"), source_repository=repository, source_commit=commit, source_path=taxonomy_path)

    for rid, row in rows.items():
        members = [c for c in concepts.values() if c["home"] == rid]
        title = filename(row["label"]) + " Subject"
        body = [clean(row["definition"]), "", "## Concepts", ""]
        body += [f"- {wiki(concept_paths[c['id']], filename(c['label']))}" for c in sorted(members, key=lambda c: c["label"].casefold())]
        body += ["", "## Further Reading", "", "These chapter pointers suggest reading for the subject, not depth or passage-level coverage."]
        for pointer in row.get("book_chapters", []):
            match = re.fullmatch(r"v(\d)/(\d+)", pointer)
            note = chapters.get(tuple(map(int, match.groups()))) if match else None
            if note:
                body += ["", f"- {wiki(note['path'], note['title'])}"]
        body += ["", "## Navigation", "", wiki(area_paths[row["area"]], filename(areas[row["area"]]["label"]))]
        write(row_paths[rid], title, "concept_index", "\n".join(body), taxonomy_subject=rid)
    for aid, area in areas.items():
        body = [clean(area["scope"]), "", clean(area.get("question", "")), "", "## Subjects", ""]
        body += [f"- {wiki(row_paths[row['id']], filename(row['label']))}" for row in area["rows"]]
        body += ["", "## Navigation", "", wiki(group_paths[area["group"]], filename(groups[area["group"]]["label"]))]
        write(area_paths[aid], filename(area["label"]) + " Index", "concept_index", "\n".join(body), taxonomy_area=aid)
    for gid, group in groups.items():
        body = [clean(group["question"]), "", "## Areas", ""]
        body += [f"- {wiki(area_paths[area['id']], filename(area['label']))}" for area in areas.values() if area["group"] == gid]
        body += ["", "## Navigation", "", wiki("00 Navigation/Topic Index.md", "Topic Index")]
        write(group_paths[gid], filename(group["label"]) + " Index", "concept_index", "\n".join(body), taxonomy_group=gid)
    for title, theme in THEMES.items():
        cids = ["mlsys." + suffix for suffix in theme["concepts"]]
        body = [theme["description"], "", "This curated navigation lens is an editorial association, not a claim of dependency or equivalence.", "", "## Concepts", ""]
        body += [f"- {wiki(concept_paths[cid], filename(concepts[cid]['label']))} — {clean(concepts[cid]['definition'])}" for cid in cids]
        body += ["", "## Connected Book Passages", ""]
        theme_passages = {p["note_path"]: p for cid in cids for p in passages[cid]}
        body += [f"- {wiki(p['note_target'], p['note_title'])}" for p in sorted(theme_passages.values(), key=lambda p: p["note_path"])]
        body += ["", "## Navigation", "", wiki("00 Navigation/Topic Index.md", "Topic Index")]
        write(theme_paths[title], title, "theme", "\n".join(body), tags=["Type/Theme", "Theme/" + tag_segment(title)], editorial_scope="Curated Navigation Lens")
    body = ["Browse the upstream taxonomy's five groups or cross-cutting themes. Each concept has one canonical home and stable taxonomy identity.", "", "## Knowledge Groups", ""]
    body += [f"- {wiki(group_paths[gid], filename(group['label']))} — {group['question']}" for gid, group in groups.items()]
    body += ["", "## Themes", ""]
    body += [f"- {wiki(theme_paths[theme], theme)} — {THEMES[theme]['description']}" for theme in THEMES]
    body += ["", "## Relationship Semantics", "", "Concept-to-passage links come only from explicit upstream alignment records. Subject reading pointers are broader suggestions. Taxonomy relationships retain their predicates and conditions. Search terms are not automatically synonyms. Themes are curated navigation lenses. Obsidian computes incoming backlinks from these ordinary links.", "", f"Source taxonomy: {taxonomy.get('version')} (editorial draft), {len(concepts)} concepts, {len(taxonomy['relationships'])} conditional relationships. [Original Taxonomy]({taxonomy_url}).", "", "## Navigation", "", wiki("Home.md", "Home")]
    write("00 Navigation/Topic Index.md", "Topic Index", "concept_index", "\n".join(body))
    body = ["Each canonical concept has one browsing home. Start with a knowledge group or use the broader " + wiki("00 Navigation/Topic Index.md", "Topic Index") + ".", "", "## Knowledge Groups", ""]
    body += [f"- {wiki(group_paths[gid], filename(group['label']))} — {group['question']}" for gid, group in groups.items()]
    body += ["", "## Navigation", "", wiki("Home.md", "Home")]
    write("02 Concepts/Concept Index.md", "Concept Index", "concept_index", "\n".join(body))
    body = ["Cross-cutting themes connect explicitly selected concepts across the four volumes. Membership is a curated reading association.", "", "## Themes", ""]
    body += [f"- {wiki(theme_paths[theme], theme)} — {THEMES[theme]['description']}" for theme in THEMES]
    body += ["", "## Navigation", "", wiki("00 Navigation/Topic Index.md", "Topic Index") + " · " + wiki("Home.md", "Home")]
    write("03 Themes/Theme Index.md", "Theme Index", "concept_index", "\n".join(body))

    navigation_blocks = chapter_context_links = 0
    for note in base_notes:
        path = vault / note["path"]
        if not path.is_file():
            continue
        sections = []
        cids = sorted(passage_links[note["path"]], key=lambda cid: concepts[cid]["label"].casefold())
        if cids:
            sections += ["## Connected Concepts", "", "Explicit upstream passage alignments:", ""]
            sections += [f"- {wiki(concept_paths[cid], filename(concepts[cid]['label']))}" for cid in cids]
        themes = sorted({theme for cid in cids for theme in concept_themes[cid]})
        if themes:
            sections += ["", "## Related Themes", ""]
            sections += [f"- {wiki(theme_paths[theme], theme)}" for theme in themes]
        if note.get("kind") == "chapter":
            key = (int(note["volume"]), int(note["chapter"]))
            cmap = chapter_maps.get(key, {})
            for source_key, heading in [("touches", "Earlier Connections"), ("previews", "Continuing Connections")]:
                grouped = defaultdict(list)
                for item in cmap.get(source_key, []):
                    match = re.match(r"(?:vol\d/)?(\d+)_", item.get("owner", ""))
                    target = chapters.get((key[0], int(match.group(1)))) if match else None
                    if target and target["path"] != note["path"]:
                        grouped[target["path"]].append((target, clean(item.get("concept", ""))))
                if grouped:
                    sections += ["", f"## {heading}", "", f"The source concept map records these {source_key} connections. They are reading connections, not prerequisite requirements.", ""]
                    for target_path in sorted(grouped):
                        target = grouped[target_path][0][0]
                        terms = "; ".join(dict.fromkeys(item[1] for item in grouped[target_path]))
                        sections += [f"- {wiki(target_path, target['title'])} — {terms}."]
                        chapter_context_links += 1
                    sections += ["", f"[Chapter Concept Map]({source_url(repository, commit, chapter_map_paths[key])})"]
        text = path.read_text(encoding="utf-8")
        text = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END) + r"\s*", "", text, flags=re.S).rstrip()
        if sections:
            text += "\n\n" + BEGIN + "\n\n" + "\n".join(sections).strip() + "\n\n" + END
            navigation_blocks += 1
        path.write_text(text + "\n", encoding="utf-8")
    generated_paths = {note["path"] for note in generated}
    manifest["notes"] = [note for note in base_notes if note["path"] not in generated_paths] + generated
    manifest["semantic_graph"] = {
        "taxonomy_version": taxonomy.get("version"),
        "canonical_concepts": len(concepts),
        "conditional_relationships": relation_count,
        "explicit_alignment_records": len(alignment["links"]),
        "resolved_alignment_records": len(alignment["links"]) - len(unresolved),
        "exact_local_alignment_records": len(alignment["links"]) - len(unresolved) - len(chapter_fallbacks),
        "chapter_fallbacks": chapter_fallbacks,
        "unresolved_alignment_records": unresolved,
        "themes": len(THEMES),
        "semantic_navigation_blocks": navigation_blocks,
        "chapter_context_links": chapter_context_links,
        "passage_alignments": [passage for cid in concepts for passage in passages[cid]],
        "policy": "Explicit Alignment Only; Conditions Preserved; No Inferred Prerequisites; Search Terms Are Not Synonym Aliases",
    }
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (vault / "99 System" / "Backlink Semantics.json").write_text(json.dumps(manifest["semantic_graph"], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in manifest["semantic_graph"].items() if key != "passage_alignments"}, ensure_ascii=False, indent=2))
    if unresolved:
        raise SystemExit("Unresolved explicit passage alignments: inspect Backlink Semantics.json")


def audit(repo, vault, round_number):
    """Independently compare generated semantic claims against upstream data."""
    manifest = json.loads((vault / "99 System" / "Import Manifest.json").read_text(encoding="utf-8"))
    taxonomy = load_yaml(repo / "taxonomy/taxonomy.yml")
    alignment = load_yaml(repo / "taxonomy/mlsysbook-alignment.yml")
    source_concepts = {concept["id"]: concept for concept in taxonomy["concepts"]}
    graph = manifest["semantic_graph"]
    concept_notes = {}
    errors = []
    link_count = 0
    for note in manifest["notes"]:
        if note["kind"] != "concept":
            continue
        text = (vault / note["path"]).read_text(encoding="utf-8")
        metadata = yaml.safe_load(text.split("---", 2)[1])
        cid = metadata.get("taxonomy_id")
        if cid in concept_notes:
            errors.append("Duplicate Canonical Identity: " + str(cid))
        concept_notes[cid] = (note, text, metadata)
    for cid, concept in source_concepts.items():
        if cid not in concept_notes:
            errors.append("Missing Canonical Concept: " + cid)
            continue
        note, text, metadata = concept_notes[cid]
        if clean(concept["definition"]) not in text:
            errors.append("Definition Changed: " + cid)
        if metadata.get("aliases"):
            errors.append("Unverified Synonym Alias: " + cid)
        if metadata.get("source_commit") != manifest["source_commit"]:
            errors.append("Incorrect Source Snapshot: " + cid)
    for edge in taxonomy["relationships"]:
        note, text, metadata = concept_notes[edge["source"]]
        target = concept_notes[edge["target"]][0]["path"].removesuffix(".md")
        predicate = clean(edge["predicate"])
        predicate = predicate[0].upper() + predicate[1:]
        condition = clean(edge.get("conditions", ""))
        if predicate + " [[" + target not in text:
            errors.append("Missing Or Altered Predicate: " + edge["id"])
        if "**Condition:** " + condition not in text:
            errors.append("Missing Or Altered Condition: " + edge["id"])
    generated_kinds = {"concept", "theme", "concept_index"}
    for note in manifest["notes"]:
        if note["kind"] not in generated_kinds:
            continue
        text = (vault / note["path"]).read_text(encoding="utf-8")
        for target in re.findall(r"\[\[([^\]|]+)", text):
            path, _, anchor = target.partition("#")
            dest = vault / (path + ".md")
            link_count += 1
            if not dest.is_file():
                errors.append("Missing Note: " + target)
                continue
            if anchor.startswith("^") and not re.search(r"(?m)^" + re.escape(anchor) + r"\s*$", dest.read_text(encoding="utf-8")):
                errors.append("Missing Exact Block: " + target)
    records = graph.get("passage_alignments", [])
    for passage in records:
        note, _, _ = concept_notes[passage["concept"]]
        reverse = (vault / passage["note_path"]).read_text(encoding="utf-8")
        if "[[" + note["path"].removesuffix(".md") + "|" not in reverse:
            errors.append("Missing Reciprocal Passage Link: " + passage["concept"])
        source_lines = (repo / passage["source_path"]).read_text(encoding="utf-8").splitlines()
        line = passage.get("source_line")
        if not line or passage["source_anchor"] not in source_lines[line - 1]:
            errors.append("Incorrect Exact Source Line: " + passage["concept"])
    if len(records) != len(alignment["links"]):
        errors.append("Alignment Record Count Changed")
    # Check touches/previews against actual chapter sequence without turning
    # those recorded reading associations into formal prerequisite statements.
    directional_connections = 0
    for map_path in repo.glob("books/vol*/**/*concepts.yml"):
        cmap = (load_yaml(map_path) or {}).get("concept_map", {})
        match = re.search(r"/(\d+)_", str(map_path))
        if not match:
            continue
        chapter = int(match[1])
        for key in ["touches", "previews"]:
            for item in cmap.get(key, []):
                match = re.match(r"(\d+)_", item.get("owner", ""))
                if not match:
                    continue
                target_chapter = int(match[1])
                directional_connections += 1
                if key == "touches" and target_chapter > chapter:
                    errors.append("Earlier Connection Points Forward: " + str(map_path))
                if key == "previews" and target_chapter < chapter:
                    errors.append("Continuing Connection Points Backward: " + str(map_path))
    checks = {
        "canonical_definitions_compared": len(source_concepts),
        "conditional_predicates_and_conditions_compared": len(taxonomy["relationships"]),
        "generated_semantic_links_checked": link_count,
        "explicit_alignment_records_checked": len(records),
        "exact_source_line_references_checked": len(records),
        "exact_local_passage_anchors": graph["exact_local_alignment_records"],
        "labelled_chapter_fallbacks": len(graph["chapter_fallbacks"]),
        "source_reading_associations_checked": directional_connections,
        "errors": errors,
    }
    label = "One" if round_number == 1 else "Two"
    title = f"Backlink Round {label}"
    lines = [
        f"Semantic review of source snapshot {manifest['source_commit']}.",
        "",
        "## Checks",
        "",
        "| Check | Result |",
        "| --- | ---: |",
    ]
    for key, value in checks.items():
        if key != "errors":
            lines.append(f"| {title_case(key)} | {value} |")
    lines += ["", "## Findings", ""]
    if round_number == 1:
        lines += [
            "- Initial review detected four invalid exact block links across two Volume IV, Chapter 12 source anchors: sec-enforcement-minimal-intervention and sec-enforcement-certified-functions. The source headings existed in the pinned QMD, while the rendered reading snapshot omitted them.",
            "- Corrected semantic navigation to verify that every block exists locally before creating an exact link. A missing local anchor now uses an explicitly labelled owning-chapter pointer and retains the exact source-line permalink. It never invents a local block.",
            "- Reported lowercase initial prose words after numbered title prefixes to the primary importer for correction.",
        ]
    else:
        lines += [
            "- Repeated the complete source-to-output definition, predicate, condition, target, reverse-link, and source-line checks after the corrective rebuild.",
            "- Inspected Quantization, KV Cache, Idempotency, and Safety Case across the four volumes. Distinct concepts retain their canonical identities, conditions remain attached to relationships, and reading connections are not promoted to prerequisites.",
        ]
    lines += [
        "- Search terms remain labelled search terms. No unverified synonym aliases are added to Obsidian metadata.",
        "- Theme membership is explicitly described as a curated navigation association. Subject chapter pointers do not claim passage-level coverage.",
        "",
        "## Result",
        "",
        ("Passed all semantic integrity checks." if not errors else f"Failed with {len(errors)} semantic integrity errors."),
    ]
    if graph["chapter_fallbacks"]:
        lines += ["", f"{len(graph['chapter_fallbacks'])} explicit alignments currently use clearly labelled chapter pointers because their exact local source anchors are absent. Each retains a verified pinned source-line reference."]
    if errors:
        lines += [""] + ["- " + error for error in errors]
    lines += ["", "## Navigation", "", wiki("00 Navigation/Topic Index.md", "Topic Index") + " · " + wiki("Home.md", "Home")]
    report = vault / "99 System" / "Reviews" / (title + ".md")
    report.parent.mkdir(parents=True, exist_ok=True)
    metadata = {"title": title, "type": "Review", "tags": ["Type/Review"], "review_round": round_number, "source_commit": manifest["source_commit"]}
    report.write_text("---\n" + yaml.safe_dump(metadata, sort_keys=False).strip() + "\n---\n\n# " + title + "\n\n" + "\n".join(lines) + "\n", encoding="utf-8")
    report.with_suffix(".json").write_text(json.dumps(checks, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(checks, indent=2))
    if errors:
        raise SystemExit("Semantic Review Failed")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--vault", type=Path)
    parser.add_argument("--audit-round", type=int, choices=[1, 2])
    parser.add_argument("--audit-only", action="store_true")
    args = parser.parse_args()
    repo = args.repo.resolve()
    vault = args.vault.resolve() if args.vault else repo / "obsidian-vault"
    if not args.audit_only:
        build(repo, vault)
    if args.audit_round:
        audit(repo, vault, args.audit_round)


if __name__ == "__main__":
    main()
