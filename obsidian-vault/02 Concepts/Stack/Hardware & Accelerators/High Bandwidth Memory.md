---
title: High Bandwidth Memory
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Memory_Hierarchy_Bandwidth
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: High-bandwidth memory
taxonomy_id: mlsys.hbm
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# High Bandwidth Memory

Stacked DRAM placed beside the processor on an interposer, providing very high bandwidth with limited capacity per stack.

## Browsing Home

[[02 Concepts/Stack/Hardware & Accelerators/Memory Hierarchy & Bandwidth Subject|Memory Hierarchy & Bandwidth]] → [[02 Concepts/Stack/Hardware & Accelerators/Hardware & Accelerators Index|Hardware & Accelerators]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Provides high [[02 Concepts/Stack/Hardware & Accelerators/Memory Bandwidth|Memory Bandwidth]]. **Condition:** Data resides in device memory rather than host memory.

- Is the device-memory level of [[02 Concepts/Stack/Hardware & Accelerators/Memory Hierarchy|Memory Hierarchy]]. **Condition:** The accelerator uses stacked DRAM as off-chip device memory.

- Sets device [[02 Concepts/Stack/Hardware & Accelerators/Memory Capacity|Memory Capacity]]. **Condition:** Stack count and stack height fix the capacity attached to each accelerator.

- Narrows, without closing, [[02 Concepts/Stack/Hardware & Accelerators/Memory Wall|Memory Wall]]. **Condition:** Stacking and wide interfaces raise bandwidth, though compute still grows faster across generations.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: HBM.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
