---
title: Class Rebalancing
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Data_Collection_Labeling
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Class rebalancing
taxonomy_id: mlsys.rebalancing
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Class Rebalancing

Changing per-class sampling rates, synthesizing minority examples, or weighting the loss so rare classes contribute adequately to training.

## Browsing Home

[[02 Concepts/Lifecycle/Data Engineering/Data Collection & Labeling Subject|Data Collection & Labeling]] → [[02 Concepts/Lifecycle/Data Engineering/Data Engineering Index|Data Engineering]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Compensates for [[02 Concepts/Lifecycle/Data Engineering/Class Imbalance|Class Imbalance]]. **Condition:** Resampling or weighting is applied to training data only.

- Shifts predicted probabilities away from true base rates, degrading [[02 Concepts/Lifecycle/Model Evaluation & Testing/Probability Calibration|Probability Calibration]]. **Condition:** When posteriors track the altered training prior, deployment retains a different prior under stable class-conditional distributions, and no prior correction is applied.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: oversampling; undersampling; class weighting; SMOTE.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
