---
title: Memory Wall
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Memory_Hierarchy_Bandwidth
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Memory wall
taxonomy_id: mlsys.memory-wall
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Memory Wall

The widening gap between processor arithmetic throughput and memory bandwidth or latency, which makes data movement the limiting factor.

## Browsing Home

[[02 Concepts/Stack/Hardware & Accelerators/Memory Hierarchy & Bandwidth Subject|Memory Hierarchy & Bandwidth]] → [[02 Concepts/Stack/Hardware & Accelerators/Hardware & Accelerators Index|Hardware & Accelerators]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Shifts workloads toward the memory-bound side of [[02 Concepts/Foundations/Quantitative System Models/Compute Bound vs. Memory Bound|Compute Bound vs. Memory Bound]]. **Condition:** Peak arithmetic throughput grows faster than memory bandwidth across hardware generations.

- Depresses [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Model FLOPS Utilization|Model FLOPS Utilization]]. **Condition:** Memory-bound phases such as decode cannot feed the arithmetic units at peak rate.

- Moves to higher intensity the [[02 Concepts/Foundations/Quantitative System Models/Ridge Point|Ridge Point]]. **Condition:** Peak compute grows faster than bandwidth across hardware generations.

## Themes

- [[03 Themes/Memory and Bandwidth|Memory and Bandwidth]]

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
