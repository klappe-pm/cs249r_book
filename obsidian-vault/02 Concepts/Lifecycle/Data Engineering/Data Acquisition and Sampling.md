---
title: Data Acquisition and Sampling
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Data_Collection_Labeling
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Data acquisition and sampling
taxonomy_id: mlsys.data-acquisition
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Data Acquisition and Sampling

The observation and selection process that determines which examples and populations enter a dataset.

## Browsing Home

[[02 Concepts/Lifecycle/Data Engineering/Data Collection & Labeling Subject|Data Collection & Labeling]] → [[02 Concepts/Lifecycle/Data Engineering/Data Engineering Index|Data Engineering]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Determines the observed population for [[02 Concepts/Lifecycle/Model Evaluation & Testing/Evaluation Split|Evaluation Split]]. **Condition:** Selection and missing outcomes can change the population to which an estimate applies.

- Sampling bias can cause [[02 Concepts/Lifecycle/MLOps & Operations/Distribution Shift|Distribution Shift]]. **Condition:** Holds when the collected population differs from the deployment population.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
