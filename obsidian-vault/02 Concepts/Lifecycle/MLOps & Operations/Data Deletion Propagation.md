---
title: Data Deletion Propagation
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Model_Retirement
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Data deletion propagation
taxonomy_id: mlsys.deletion-propagation
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Data Deletion Propagation

Carrying a deletion request through every copy and derivative of the data, including datasets, features, caches, replicas, backups, and models trained on it.

## Browsing Home

[[02 Concepts/Lifecycle/MLOps & Operations/Model Retirement Subject|Model Retirement]] → [[02 Concepts/Lifecycle/MLOps & Operations/MLOps & Operations Index|MLOps & Operations]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Extends to models through [[02 Concepts/Qualities/Security & Privacy/Machine Unlearning|Machine Unlearning]]. **Condition:** Deleted data has already been used for training.

- Locates copies through [[02 Concepts/Lifecycle/Data Engineering/Data Lineage|Data Lineage]]. **Condition:** Derived datasets and features record their sources.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: right to erasure; deletion requests.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
