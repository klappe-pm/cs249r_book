---
title: V3-05 KV Cache Management
type: Chapter
volume: 3
chapter: 5
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol3/05_kv_cache/05_kv_cache.qmd
source_anchor: sec-vol3-kv-cache
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_3
rendered_source_url: https://mlsysbook.ai/vol3/05_kv_cache/05_kv_cache.html
---

# V3-05 KV Cache Management

[[Home|Home]] · [[01 Books/Volume III - Agentic Systems/Volume 3 Overview|Volume Overview]]

^sec-vol3-kv-cache

[Lecture slides](https://mlsysbook.ai/slides/vol3.html#ch-05) for this chapter

![[90 Assets/Volume III/05 KV Cache/Cover Virtual Memory Blueprint Labeled 4d81ece1ec.webp]]

*Blueprint cover illustration for the KV Cache Management chapter.*

## Chapter Sections

- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05.01 Purpose|V3-05.01 Purpose]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05.02 Attention State as a Serving Resource|V3-05.02 Attention State as a Serving Resource]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05.03 The Footprint of Retained Attention State|V3-05.03 The Footprint of Retained Attention State]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05.04 Memory Fragmentation|V3-05.04 Memory Fragmentation]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05.05 Paged KV Allocation|V3-05.05 Paged KV Allocation]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05.06 Prefix Caching Across Turns|V3-05.06 Prefix Caching Across Turns]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05.07 Chunked Prefill Scheduling|V3-05.07 Chunked Prefill Scheduling]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05.08 Paused-State Policies|V3-05.08 Paused-State Policies]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05.09 Capacity for Agent Workloads|V3-05.09 Capacity for Agent Workloads]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05.10 Fallacies and Pitfalls|V3-05.10 Fallacies and Pitfalls]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05.11 Summary|V3-05.11 Summary]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05.12 Historical Perspective and Further Reading|V3-05.12 Historical Perspective and Further Reading]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05.13 Exercises|V3-05.13 Exercises]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05.14 Source References|V3-05.14 Source References]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05.15 Footnotes|V3-05.15 Footnotes]]

Next: [[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05.01 Purpose|V3-05.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/05_kv_cache/05_kv_cache.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol3/05_kv_cache/05_kv_cache.html#sec-vol3-kv-cache). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Lifecycle/Deployment & Serving/KV Cache|KV Cache]]
- [[02 Concepts/Lifecycle/Deployment & Serving/KV Cache Offloading and Tiering|KV Cache Offloading and Tiering]]
- [[02 Concepts/Lifecycle/Deployment & Serving/Prefix Caching|Prefix Caching]]

## Related Themes

- [[03 Themes/Memory and Bandwidth|Memory and Bandwidth]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume III - Agentic Systems/00 Introduction/01 Introduction/V3-01 Introduction|V3-01 Introduction]] — Tool-wait problem; Invariant closure; Cost per accepted task; Lighthouse workloads.
- [[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02 The Foundation Model|V3-02 The Foundation Model]] — Output-bound call latency; Quadratic resend and prefix reuse.
- [[01 Books/Volume III - Agentic Systems/01 The Model/03 Test-Time Compute/V3-03 Test-Time Compute|V3-03 Test-Time Compute]] — Allocation axes.
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04 Context Engineering|V3-04 Context Engineering]] — Change-rate ordering; Context invalidation; Working-set partition.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/05_kv_cache/kv_cache_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/06 Long-Term Memory/V3-06 Long-Term Memory|V3-06 Long-Term Memory]] — Record roles.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10 The Agent Harness|V3-10 The Agent Harness]] — Supervised waiting.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11 Durable Execution|V3-11 Durable Execution]] — Trajectory log.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/05_kv_cache/kv_cache_concepts.yml)

<!-- Semantic Navigation: End -->
