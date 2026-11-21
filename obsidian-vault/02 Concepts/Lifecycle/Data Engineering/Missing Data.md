---
title: Missing Data
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Data_Validation_Feature_Engineering
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Missing data
taxonomy_id: mlsys.missing-data
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Missing Data

Absent observations whose pattern and treatment can change learned behavior.

## Browsing Home

[[02 Concepts/Lifecycle/Data Engineering/Data Validation & Feature Engineering Subject|Data Validation & Feature Engineering]] → [[02 Concepts/Lifecycle/Data Engineering/Data Engineering Index|Data Engineering]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Forces imputation and indicator decisions in [[02 Concepts/Lifecycle/Data Engineering/Feature Engineering|Feature Engineering]]. **Condition:** Treatment must preserve the meaning and availability of inputs.

- Can cause [[02 Concepts/Lifecycle/Data Engineering/Training Serving Skew|Training Serving Skew]]. **Condition:** Holds when missingness patterns or imputation differ between offline data and live requests.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
