---
title: KV Cache Eviction
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/LLM_Generative_Inference
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: KV-cache eviction
taxonomy_id: mlsys.kv-cache-eviction
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# KV Cache Eviction

Retaining only a selected subset of cached key-value entries, chosen by attention scores, recency, or learned importance, to bound KV memory during long generation.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/LLM & Generative Inference Subject|LLM & Generative Inference]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Reduces the KV portion of [[02 Concepts/Foundations/Workloads & Requirements/Memory Footprint|Memory Footprint]]. **Condition:** Generation is long enough that cached keys and values dominate accelerator memory.

- Competes as a KV-compression option with [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/KV Cache Quantization|KV Cache Quantization]]. **Condition:** Both target KV memory; they can also be combined.

- Selects entries using scores from [[02 Concepts/Foundations/Models & Architectures/Attention|Attention]]. **Condition:** Importance is estimated from accumulated or recent attention weights.

- Bounds the resident size of [[02 Concepts/Lifecycle/Deployment & Serving/KV Cache|KV Cache]]. **Condition:** When the evicted entries receive little attention, so quality holds.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: KV token eviction; KV-cache sparsification; heavy-hitter retention; attention sink retention; sink-aware KV eviction.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
