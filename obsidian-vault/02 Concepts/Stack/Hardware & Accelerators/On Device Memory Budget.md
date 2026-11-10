---
title: On Device Memory Budget
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Edge_Embedded_Hardware
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: On-device memory budget
taxonomy_id: mlsys.on-device-memory-budget
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# On Device Memory Budget

The flash and SRAM limits that bound a deployed model's stored weights and peak activation memory on embedded hardware.

## Browsing Home

[[02 Concepts/Stack/Hardware & Accelerators/Edge & Embedded Hardware Subject|Edge & Embedded Hardware]] → [[02 Concepts/Stack/Hardware & Accelerators/Hardware & Accelerators Index|Hardware & Accelerators]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Bounds [[02 Concepts/Lifecycle/Training & Adaptation/On Device Training|On Device Training]]. **Condition:** Training must fit weights, activations, and update state in on-chip memory.

- Bounds the resolution and extent of the [[02 Concepts/System Types/Embodied & Physical Systems/mAP Representation|mAP Representation]]. **Condition:** When the map lives in onboard memory beside the perception and policy models.

## Themes

- [[03 Themes/Constraints Drive Architecture|Constraints Drive Architecture]]

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: app memory limit; mobile memory budget.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
