---
title: Device Heterogeneity
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/On_Device_Edge_Deployment
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Device heterogeneity
taxonomy_id: mlsys.device-heterogeneity
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Device Heterogeneity

Variation in hardware, operating system, and runtime capability across a deployed device fleet that a single model release must accommodate.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/On Device & Edge Deployment Subject|On Device & Edge Deployment]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Multiplies targets and effort for [[02 Concepts/Lifecycle/Deployment & Serving/Model Conversion|Model Conversion]]. **Condition:** Holds when devices differ in supported operators, precision, or accelerators.

- Shifts the best split in [[02 Concepts/Lifecycle/Deployment & Serving/Device Cloud Partitioning|Device Cloud Partitioning]]. **Condition:** Holds because device speed and network differ widely across the fleet.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
