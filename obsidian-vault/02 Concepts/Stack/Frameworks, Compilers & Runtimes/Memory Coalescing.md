---
title: Memory Coalescing
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Kernel_GPU_Programming_Model
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Memory coalescing
taxonomy_id: mlsys.memory-coalescing
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Memory Coalescing

Combining memory requests from threads in a warp into fewer global-memory transactions, reducing wasted memory traffic.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Kernel & GPU Programming Model Subject|Kernel & GPU Programming Model]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Helps determine achieved [[02 Concepts/Stack/Hardware & Accelerators/Memory Bandwidth|Memory Bandwidth]]. **Condition:** For global-memory accesses by a warp, coalescing reduces wasted transactions; achieved bandwidth also depends on the workload and hardware.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: coalesced access.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
