---
title: Profiling
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Profiling_Utilization
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Profiling
taxonomy_id: mlsys.profiling
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Profiling

Measuring execution to attribute time, work, stalls, and resource use.

## Browsing Home

[[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Profiling & Utilization Subject|Profiling & Utilization]] → [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Performance, Efficiency & Benchmarking Index|Performance, Efficiency & Benchmarking]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Estimates realized [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Resource Utilization|Resource Utilization]]. **Condition:** Instrumentation and measurement boundaries affect interpretation.

- Measures observed [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Execution Time|Execution Time]]. **Condition:** Measurement boundaries, instrumentation, and workload determine the observation; a sample is not a universal time bound.

- Supplies evidence for [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Bottleneck Analysis|Bottleneck Analysis]]. **Condition:** When the profile covers the same workload, configuration, and execution boundary as the bottleneck claim.

- Records [[02 Concepts/Foundations/Quantitative System Models/Operator Execution Trace|Operator Execution Trace]]. **Condition:** Operator dependencies are captured along with timings.

- Records per-tensor and per-phase allocations that make up [[02 Concepts/Foundations/Workloads & Requirements/Memory Footprint|Memory Footprint]]. **Condition:** When the profiler tracks allocations over a training step rather than only peak usage.

- Exposes the slow ranks behind [[02 Concepts/Stack/Parallelism & Distributed Execution/Stragglers|Stragglers]]. **Condition:** When per-rank step and collective times are recorded and compared.

- Reads stall and throughput causes from [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Hardware Performance Counters|Hardware Performance Counters]]. **Condition:** When the profiler collects counters in addition to timestamps; collection can perturb execution and on some accelerators serializes it.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
