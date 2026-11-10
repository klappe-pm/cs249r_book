---
title: Performance Measurement Variability
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/System_Benchmarking
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Performance measurement variability
taxonomy_id: mlsys.measurement-variability
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Performance Measurement Variability

Run-to-run variation in measured time and throughput from warm-up, asynchronous execution, clock and thermal state, and contention, handled by synchronizing, repeating runs, and reporting spread.

## Browsing Home

[[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/System Benchmarking Subject|System Benchmarking]] → [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Performance, Efficiency & Benchmarking Index|Performance, Efficiency & Benchmarking]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Limits the precision of [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Benchmark Protocol|Benchmark Protocol]]. **Condition:** Differences between systems are comparable to run-to-run spread.

- Confounds [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Profiling|Profiling]]. **Condition:** Asynchronous kernels are timed without synchronization or warm-up.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: benchmark noise; warm-up effects; timing variance.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
