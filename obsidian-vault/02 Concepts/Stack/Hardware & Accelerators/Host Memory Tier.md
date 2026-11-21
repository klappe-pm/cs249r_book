---
title: Host Memory Tier
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Memory_Hierarchy_Bandwidth
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Host memory tier
taxonomy_id: mlsys.host-memory
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Host Memory Tier

Memory directly managed by the host processor and used for input staging or offloaded model state, whose capacity and accelerator access costs depend on the platform's memory and interconnect design.

## Browsing Home

[[02 Concepts/Stack/Hardware & Accelerators/Memory Hierarchy & Bandwidth Subject|Memory Hierarchy & Bandwidth]] → [[02 Concepts/Stack/Hardware & Accelerators/Hardware & Accelerators Index|Hardware & Accelerators]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is the capacity tier above device memory in [[02 Concepts/Stack/Hardware & Accelerators/Memory Hierarchy|Memory Hierarchy]]. **Condition:** When the accelerator is attached to a host that has its own DRAM.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: host DRAM; system memory; DDR memory; CPU memory.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
