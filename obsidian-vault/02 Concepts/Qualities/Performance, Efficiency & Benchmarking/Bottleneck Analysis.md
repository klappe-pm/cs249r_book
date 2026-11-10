---
title: Bottleneck Analysis
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Profiling_Utilization
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Bottleneck analysis
taxonomy_id: mlsys.bottleneck-analysis
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Bottleneck Analysis

Identifying the resource or stage, such as compute, memory bandwidth, I/O, or communication, whose capacity limits end-to-end throughput or latency for a workload.

## Browsing Home

[[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Profiling & Utilization Subject|Profiling & Utilization]] → [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Performance, Efficiency & Benchmarking Index|Performance, Efficiency & Benchmarking]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Uses [[02 Concepts/Foundations/Quantitative System Models/Roofline Bound|Roofline Bound]]. **Condition:** When the candidate bottleneck is a kernel's compute or memory-bandwidth bound rather than I/O, scheduling, or communication.

- Identifies the operating [[02 Concepts/Foundations/Quantitative System Models/Compute Bound vs. Memory Bound|Compute Bound vs. Memory Bound]]. **Condition:** When per-kernel time, FLOPs, and bytes are measured, so each kernel can be placed relative to the ridge point.

- Locates the limiting software layer with [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Cross Stack Profiling|Cross Stack Profiling]]. **Condition:** When the bottleneck lies in host code or framework overhead rather than in a single kernel.

- Places a kernel on the roofline using measured bytes and operations from [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Hardware Performance Counters|Hardware Performance Counters]]. **Condition:** When measured rather than estimated arithmetic intensity is needed.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: optimization prioritization; optimization planning.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
