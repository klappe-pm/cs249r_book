---
title: Advanced Accelerator Packaging
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Accelerator_Architecture
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Advanced accelerator packaging
taxonomy_id: mlsys.advanced-accelerator-packaging
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Advanced Accelerator Packaging

Integrating compute and memory dies through chiplets, interposers, or three-dimensional bonding to trade local bandwidth and manufacturing flexibility against power-delivery and heat-removal constraints.

## Browsing Home

[[02 Concepts/Stack/Hardware & Accelerators/Accelerator Architecture Subject|Accelerator Architecture]] → [[02 Concepts/Stack/Hardware & Accelerators/Hardware & Accelerators Index|Hardware & Accelerators]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Uses closely integrated stacked memory [[02 Concepts/Stack/Hardware & Accelerators/High Bandwidth Memory|High Bandwidth Memory]]. **Condition:** When a compute package connects processor dies to HBM stacks through dense package-level interfaces.

- Determines package heat paths and thermal coupling [[02 Concepts/Stack/Hardware & Accelerators/Thermal Behavior and Throttling|Thermal Behavior and Throttling]]. **Condition:** When die placement, stacking, and bonding geometry constrain heat removal.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: chiplet integration; multi-die package; heterogeneous die integration; 2.5D interposer; die-to-die interconnect.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
