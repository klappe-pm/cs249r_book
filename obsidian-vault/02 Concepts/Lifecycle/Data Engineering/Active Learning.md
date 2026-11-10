---
title: Active Learning
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Data_Collection_Labeling
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Active learning
taxonomy_id: mlsys.active-learning
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Active Learning

Selecting which unlabeled examples to annotate next according to their expected value to the model.

## Browsing Home

[[02 Concepts/Lifecycle/Data Engineering/Data Collection & Labeling Subject|Data Collection & Labeling]] → [[02 Concepts/Lifecycle/Data Engineering/Data Engineering Index|Data Engineering]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Biases sampling in [[02 Concepts/Lifecycle/Data Engineering/Data Acquisition and Sampling|Data Acquisition and Sampling]]. **Condition:** The selected examples depend on the current model, so the labeled set is not a random sample of the deployment population.

- Is label-acquisition [[02 Concepts/Lifecycle/Data Engineering/Data Selection|Data Selection]]. **Condition:** Applies when the cost being allocated is annotation effort.

- Selects examples to label from [[02 Concepts/Lifecycle/Model Evaluation & Testing/Predictive Uncertainty Estimation|Predictive Uncertainty Estimation]]. **Condition:** For uncertainty-sampling acquisition functions.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
