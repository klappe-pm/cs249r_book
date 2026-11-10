---
title: Asynchronous Data Movement
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Kernel_GPU_Programming_Model
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Asynchronous data movement
taxonomy_id: mlsys.async-data-movement
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Asynchronous Data Movement

Transferring data into on-chip memory while independent computation proceeds, with explicit synchronization on the transfer's completion; hardware copy engines and producer-consumer warp roles are its implementations.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Kernel & GPU Programming Model Subject|Kernel & GPU Programming Model]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Applies within a device the idea of [[02 Concepts/Stack/Parallelism & Distributed Execution/Communication Overlap|Communication Overlap]]. **Condition:** Loads into on-chip memory proceed while matrix units compute on the previous tile.

- Stages operands into [[02 Concepts/Stack/Hardware & Accelerators/On Chip SRAM and Scratchpads|On Chip SRAM and Scratchpads]]. **Condition:** Bulk copies land in shared memory while compute proceeds on the previous buffer.

- Raises matrix-engine [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Resource Utilization|Resource Utilization]]. **Condition:** The kernel would otherwise stall its matrix units waiting on loads.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: TMA.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
