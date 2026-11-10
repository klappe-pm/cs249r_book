---
title: Kernel Autotuning
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/ML_Compilers_Kernel_Optimization
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Kernel autotuning
taxonomy_id: mlsys.autotuning
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Kernel Autotuning

Searching kernel schedule parameters, such as tile sizes and loop orders, by measurement or learned cost models to find fast implementations for a target.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/ML Compilers & Kernel Optimization Subject|ML Compilers & Kernel Optimization]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Selects parameters for [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Tiling|Tiling]]. **Condition:** The schedule space is large and performance is hard to predict analytically.

- Measures candidates with [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Profiling|Profiling]]. **Condition:** Candidate schedules are compiled and timed on the target, or a cost model is trained from such measurements.

- Is a search stage within [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Graph Compilation|Graph Compilation]]. **Condition:** The compiler exposes a schedule space whose performance is hard to predict analytically.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
