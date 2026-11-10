---
title: KV Cache Offloading and Tiering
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/LLM_Generative_Inference
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: KV-cache offloading and tiering
taxonomy_id: mlsys.kv-cache-offload
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# KV Cache Offloading and Tiering

Moving KV-cache blocks from accelerator memory to host memory or SSD and reloading them on reuse, extending cache capacity at transfer bandwidth and latency cost.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/LLM & Generative Inference Subject|LLM & Generative Inference]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05.08 Paused-State Policies#^sec-vol3-kv-cache-keep-move-drop|V3-05.08 Paused-State Policies]] — Paused-state residency. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/05_kv_cache/05_kv_cache.qmd#L943).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Increases the capacity and hit rate of [[02 Concepts/Lifecycle/Deployment & Serving/Prefix Caching|Prefix Caching]]. **Condition:** Pays off when reload time from host or SSD is shorter than recomputing the prefix's prefill.

- Is a kind of [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Storage Tiering and Caching|Storage Tiering and Caching]]. **Condition:** Applies when KV blocks move between accelerator memory, host memory, and SSD by reuse likelihood.

- Moves cold blocks out of accelerator memory, shrinking the resident part of [[02 Concepts/Lifecycle/Deployment & Serving/KV Cache|KV Cache]]. **Condition:** When transfer bandwidth to host memory or storage can bring blocks back before they are needed.

- Keeps evicted KV blocks in [[02 Concepts/Stack/Hardware & Accelerators/Host Memory Tier|Host Memory Tier]]. **Condition:** When blocks are likely to be reused and host memory is cheaper than device memory.

- Keeps cold entries recoverable instead of discarding them as in [[02 Concepts/Lifecycle/Deployment & Serving/KV Cache Eviction|KV Cache Eviction]]. **Condition:** Both bound resident KV memory; offload spends transfer bandwidth to preserve exactness, eviction spends quality to avoid transfers; they can be combined.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: KV offload; KV tiering.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
