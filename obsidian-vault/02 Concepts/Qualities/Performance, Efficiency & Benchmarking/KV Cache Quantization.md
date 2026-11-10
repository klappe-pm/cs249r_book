---
title: KV Cache Quantization
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Model_Compression
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: KV-cache quantization
taxonomy_id: mlsys.kv-cache-quantization
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# KV Cache Quantization

Storing attention keys and values at reduced precision, often with per-channel keys and per-token values, to raise batch size or context length under fixed memory.

## Browsing Home

[[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Model Compression Subject|Model Compression]] → [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Performance, Efficiency & Benchmarking Index|Performance, Efficiency & Benchmarking]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Shrinks [[02 Concepts/Lifecycle/Deployment & Serving/KV Cache|KV Cache]]. **Condition:** Capacity gains translate into throughput only when serving is KV-memory-bound and attention kernels read the quantized format directly.

- Reduces [[02 Concepts/Lifecycle/Deployment & Serving/Time per Output Token|Time per Output Token]]. **Condition:** When long-context decoding time is dominated by reading the KV cache from memory.

- Raises the feasible batch size of [[02 Concepts/Lifecycle/Deployment & Serving/Request Batching|Request Batching]]. **Condition:** When serving is KV-memory-bound, so freed capacity admits more concurrent sequences.

## Themes

- [[03 Themes/Memory and Bandwidth|Memory and Bandwidth]]

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: KV quantization.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
