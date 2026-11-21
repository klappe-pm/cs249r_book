---
title: Memory Hierarchy
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Memory_Hierarchy_Bandwidth
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Memory hierarchy
taxonomy_id: mlsys.memory-hierarchy
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Memory Hierarchy

Arrangement of storage levels and transfer paths with differing capacity, latency, bandwidth, access control, and management mechanisms. The available levels depend on the platform.

## Browsing Home

[[02 Concepts/Stack/Hardware & Accelerators/Memory Hierarchy & Bandwidth Subject|Memory Hierarchy & Bandwidth]] → [[02 Concepts/Stack/Hardware & Accelerators/Hardware & Accelerators Index|Hardware & Accelerators]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.07 Performance Bounds#^sec-hardware-acceleration-calculating-memory-bandwidth-bounds-7fc0|V1-11.07 Performance Bounds]] — Memory bandwidth. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/11_hw_acceleration/11_hw_acceleration.qmd#L3735).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Provides storage levels for [[02 Concepts/Foundations/Quantitative System Models/Data Locality|Data Locality]]. **Condition:** The algorithm, placement, and implementation determine which levels actually serve an access; effective rates depend on contention and access pattern.

## Themes

- [[03 Themes/Memory and Bandwidth|Memory and Bandwidth]]

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
