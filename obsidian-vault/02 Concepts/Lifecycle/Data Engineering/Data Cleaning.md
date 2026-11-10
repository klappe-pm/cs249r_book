---
title: Data Cleaning
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Data_Validation_Feature_Engineering
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Data cleaning
taxonomy_id: mlsys.data-cleaning
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Data Cleaning

Detecting and correcting erroneous, inconsistent, duplicated, or outlying records with rules, statistics, or learned repair models before the data is used for training.

## Browsing Home

[[02 Concepts/Lifecycle/Data Engineering/Data Validation & Feature Engineering Subject|Data Validation & Feature Engineering]] → [[02 Concepts/Lifecycle/Data Engineering/Data Engineering Index|Data Engineering]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Repairs violations found by [[02 Concepts/Lifecycle/Data Engineering/Data Validation|Data Validation]]. **Condition:** Validation rules or statistics flag the records to repair.

- Imputes or removes [[02 Concepts/Lifecycle/Data Engineering/Missing Data|Missing Data]]. **Condition:** The missingness mechanism is understood well enough to choose a treatment.

- Raises [[02 Concepts/Lifecycle/Data Engineering/Data Quality|Data Quality]]. **Condition:** Repairs are validated and do not introduce label leakage.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: data cleansing; data repair.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
