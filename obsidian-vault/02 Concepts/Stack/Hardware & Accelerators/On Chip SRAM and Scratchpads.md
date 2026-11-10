---
title: On Chip SRAM and Scratchpads
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Memory_Hierarchy_Bandwidth
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: On-chip SRAM and scratchpads
taxonomy_id: mlsys.on-chip-sram
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# On Chip SRAM and Scratchpads

Small, fast on-die storage, such as caches, shared memory, and register files, used to stage reused operands near compute units.

## Browsing Home

[[02 Concepts/Stack/Hardware & Accelerators/Memory Hierarchy & Bandwidth Subject|Memory Hierarchy & Bandwidth]] → [[02 Concepts/Stack/Hardware & Accelerators/Hardware & Accelerators Index|Hardware & Accelerators]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Bounds tile size for [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Tiling|Tiling]]. **Condition:** Tiles must fit in on-chip storage for reuse to occur.

- Bounds [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Occupancy and Latency Hiding|Occupancy and Latency Hiding]]. **Condition:** Shared memory and registers per block limit how many warps can be resident.

- Is the fastest managed level of [[02 Concepts/Stack/Hardware & Accelerators/Memory Hierarchy|Memory Hierarchy]]. **Condition:** The platform exposes caches, shared memory, or scratchpads near compute.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
