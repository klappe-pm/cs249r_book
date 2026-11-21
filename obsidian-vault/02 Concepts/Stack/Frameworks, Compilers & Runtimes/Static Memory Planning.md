---
title: Static Memory Planning
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/ML_Compilers_Kernel_Optimization
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Static memory planning
taxonomy_id: mlsys.memory-planning
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Static Memory Planning

Compile-time assignment of tensor buffers to memory with lifetime-based reuse, reducing peak memory and runtime allocation.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/ML Compilers & Kernel Optimization Subject|ML Compilers & Kernel Optimization]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Reduces peak [[02 Concepts/Foundations/Workloads & Requirements/Memory Footprint|Memory Footprint]]. **Condition:** Tensor lifetimes are known at compile time.

- Is a pass within [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Graph Compilation|Graph Compilation]]. **Condition:** Static shapes let the compiler compute tensor lifetimes ahead of execution.

- Is an alternative to [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Caching Memory Allocator|Caching Memory Allocator]]. **Condition:** Both manage device buffers; static planning needs known lifetimes, caching allocation handles dynamic shapes.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
