---
title: Training Serving Skew
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Leakage_Training_Serving_Skew
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Training-serving skew
taxonomy_id: mlsys.train-serve-skew
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Training Serving Skew

A mismatch between the data transformations or feature semantics used in training and serving.

## Browsing Home

[[02 Concepts/Lifecycle/Data Engineering/Leakage & Training Serving Skew Subject|Leakage & Training Serving Skew]] → [[02 Concepts/Lifecycle/Data Engineering/Data Engineering Index|Data Engineering]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/01 Foundations/04 Data Engineering/V1-04.08 Data Processing#^sec-data-engineering-ensuring-trainingserving-consistency-c683|V1-04.08 Data Processing]] — Training-serving parity. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/04_data_engineering/04_data_engineering.qmd#L3440).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Can degrade deployed [[02 Concepts/Lifecycle/Model Evaluation & Testing/Generalization|Generalization]]. **Condition:** A deployed pipeline may compute different inputs from those used in development.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
