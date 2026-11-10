---
title: Data Augmentation
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Data_Selection_Curation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Data augmentation
taxonomy_id: mlsys.data-augmentation
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Data Augmentation

Creating additional training examples by applying label-preserving transformations to existing ones.

## Browsing Home

[[02 Concepts/Lifecycle/Data Engineering/Data Selection & Curation Subject|Data Selection & Curation]] → [[02 Concepts/Lifecycle/Data Engineering/Data Engineering Index|Data Engineering]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Can improve [[02 Concepts/Lifecycle/Model Evaluation & Testing/Generalization|Generalization]]. **Condition:** The transformations must preserve labels and reflect invariances present at deployment.

- Acts as a form of [[02 Concepts/Lifecycle/Training & Adaptation/Regularization|Regularization]]. **Condition:** Holds when transformations are label-preserving.

- Can reduce sensitivity to [[02 Concepts/Lifecycle/MLOps & Operations/Distribution Shift|Distribution Shift]]. **Condition:** Holds only for shifts that the chosen transformations actually model.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
