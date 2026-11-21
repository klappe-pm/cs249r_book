---
title: Training Diagnostics
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/ML_Testing_Debugging
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Training diagnostics
taxonomy_id: mlsys.training-diagnostics
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Training Diagnostics

Checks such as overfitting a tiny batch, reading learning curves, and tracking gradient and activation statistics that localize bugs in training code, data, and configuration.

## Browsing Home

[[02 Concepts/Lifecycle/Model Evaluation & Testing/ML Testing & Debugging Subject|ML Testing & Debugging]] → [[02 Concepts/Lifecycle/Model Evaluation & Testing/Model Evaluation & Testing Index|Model Evaluation & Testing]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Reveals [[02 Concepts/Lifecycle/Training & Adaptation/Training Instability|Training Instability]]. **Condition:** Gradient and loss statistics are logged at step granularity.

- Reads plots from [[02 Concepts/Lifecycle/Model Evaluation & Testing/Model and Prediction Visualization|Model and Prediction Visualization]]. **Condition:** Learning curves and activation statistics are recorded during training.

- Reveals, through diverging training and validation curves, [[02 Concepts/Lifecycle/Training & Adaptation/Overfitting|Overfitting]]. **Condition:** When validation metrics are logged alongside training loss at step granularity.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: overfit-one-batch test; learning-curve diagnosis.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
