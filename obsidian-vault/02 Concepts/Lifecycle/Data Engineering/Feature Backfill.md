---
title: Feature Backfill
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Data_Pipelines_Storage_Formats
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Feature backfill
taxonomy_id: mlsys.feature-backfill
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Feature Backfill

Recomputing a feature's historical values under a new or corrected definition so training data matches what serving will produce.

## Browsing Home

[[02 Concepts/Lifecycle/Data Engineering/Data Pipelines & Storage Formats Subject|Data Pipelines & Storage Formats]] → [[02 Concepts/Lifecycle/Data Engineering/Data Engineering Index|Data Engineering]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Must preserve [[02 Concepts/Lifecycle/Data Engineering/Point in Time Correctness|Point in Time Correctness]]. **Condition:** Backfilled values must be computed only from data available at each historical timestamp.

- Realigns history to reduce [[02 Concepts/Lifecycle/Data Engineering/Training Serving Skew|Training Serving Skew]]. **Condition:** Holds when the backfill uses the same definition that serving computes.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
