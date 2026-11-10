---
title: Data Leakage
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Leakage_Training_Serving_Skew
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Data leakage
taxonomy_id: mlsys.leakage
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Data Leakage

Information unavailable at the intended prediction boundary entering development or evaluation.

## Browsing Home

[[02 Concepts/Lifecycle/Data Engineering/Leakage & Training Serving Skew Subject|Leakage & Training Serving Skew]] → [[02 Concepts/Lifecycle/Data Engineering/Data Engineering Index|Data Engineering]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/01 Foundations/04 Data Engineering/V1-04.02 Data as Code#^sec-data-engineering-data-engineering-dataset-compilation-0496|V1-04.02 Data as Code]] — Data leakage. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/04_data_engineering/04_data_engineering.qmd#L67).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Can invalidate [[02 Concepts/Lifecycle/Model Evaluation & Testing/Evaluation Metrics|Evaluation Metrics]]. **Condition:** When evaluation uses information unavailable at the intended prediction boundary.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
