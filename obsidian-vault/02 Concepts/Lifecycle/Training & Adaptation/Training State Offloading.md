---
title: Training State Offloading
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Training_Memory_State
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Training-state offloading
taxonomy_id: mlsys.memory-offloading
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Training State Offloading

Moving optimizer state, parameters, or activations from accelerator memory to host memory or storage between uses.

## Browsing Home

[[02 Concepts/Lifecycle/Training & Adaptation/Training Memory & State Subject|Training Memory & State]] → [[02 Concepts/Lifecycle/Training & Adaptation/Training & Adaptation Index|Training & Adaptation]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Reduces the accelerator-resident footprint of [[02 Concepts/Lifecycle/Training & Adaptation/Training State|Training State]]. **Condition:** Benefit depends on host-device bandwidth and how well transfers overlap with compute.

- Spills optimizer state, parameters, or activations into [[02 Concepts/Stack/Hardware & Accelerators/Host Memory Tier|Host Memory Tier]]. **Condition:** When per-device memory cannot hold the full training state.

## Themes

- [[03 Themes/Memory and Bandwidth|Memory and Bandwidth]]

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
