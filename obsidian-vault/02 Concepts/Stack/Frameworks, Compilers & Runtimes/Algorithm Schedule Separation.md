---
title: Algorithm Schedule Separation
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/ML_Compilers_Kernel_Optimization
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Algorithm-schedule separation
taxonomy_id: mlsys.schedule-separation
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Algorithm Schedule Separation

A compiler design in which what an operator computes is written once and how it runs, meaning loop order, tiling, vectorization, unrolling, memory placement, and parallel mapping, is a separate composable schedule, so the same algorithm can be retargeted and tuned without changing its semantics.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/ML Compilers & Kernel Optimization Subject|ML Compilers & Kernel Optimization]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Names, as a schedule primitive, [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Tiling|Tiling]]. **Condition:** When tile sizes and loop order are schedule choices rather than part of the algorithm's definition.

- Exposes the search space explored by [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Kernel Autotuning|Kernel Autotuning]]. **Condition:** When schedule parameters are enumerable and the algorithm is fixed, so candidate implementations differ only in schedule.

- Applies schedule transformations to the loop-level [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/ML Compiler IR|ML Compiler IR]]. **Condition:** When the compiler lowers the algorithm to a loop nest that schedule primitives rewrite.

- Selects, as a schedule primitive, [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Software Pipelining|Software Pipelining]]. **Condition:** When pipelining stages are chosen by the schedule rather than written by hand in the kernel.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: scheduling language; schedule primitives; compute-schedule split; Halide-style scheduling.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
