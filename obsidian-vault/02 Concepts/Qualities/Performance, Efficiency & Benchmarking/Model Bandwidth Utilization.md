---
title: Model Bandwidth Utilization
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Profiling_Utilization
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Model bandwidth utilization
taxonomy_id: mlsys.model-bandwidth-utilization
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Model Bandwidth Utilization

Model-required bytes of weights and KV cache per decoding step divided by step time and by the aggregate peak memory bandwidth of the participating devices, the memory-bound counterpart of model FLOPs utilization, stated for a given batch and cache configuration.

## Browsing Home

[[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Profiling & Utilization Subject|Profiling & Utilization]] → [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Performance, Efficiency & Benchmarking Index|Performance, Efficiency & Benchmarking]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is the memory-bound counterpart of [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Model FLOPS Utilization|Model FLOPS Utilization]]. **Condition:** When one primary efficiency indicator is chosen for a stated bottleneck; both ratios can be reported for the same workload, and the bound regime says which one explains the ceiling.

- Divides bytes per token by the measured [[02 Concepts/Lifecycle/Deployment & Serving/Time per Output Token|Time per Output Token]]. **Condition:** When achieved bandwidth is estimated from weight and KV-cache bytes over time per output token rather than from hardware counters.

- Reports, as an achieved fraction of aggregate peak bandwidth, the decode-phase [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Resource Utilization|Resource Utilization]]. **Condition:** When the phase is memory-bound, so model-required bytes per step rather than FLOPs set the ceiling; physical traffic beyond model-required bytes is excluded.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: MBU.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
