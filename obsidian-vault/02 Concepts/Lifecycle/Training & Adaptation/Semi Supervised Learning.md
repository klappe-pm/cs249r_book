---
title: Semi Supervised Learning
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Learning_Paradigms
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Semi-supervised learning
taxonomy_id: mlsys.semi-supervised-learning
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Semi Supervised Learning

Learning from a small labeled set together with a large unlabeled one, typically by training on confident model predictions for unlabeled examples or by enforcing consistent predictions under perturbation, which lowers labeling cost but can reinforce the model's own early mistakes.

## Browsing Home

[[02 Concepts/Lifecycle/Training & Adaptation/Learning Paradigms Subject|Learning Paradigms]] → [[02 Concepts/Lifecycle/Training & Adaptation/Training & Adaptation Index|Training & Adaptation]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Trains on labeled and pseudo-labeled examples with [[02 Concepts/Lifecycle/Training & Adaptation/Supervised Learning|Supervised Learning]]. **Condition:** After unlabeled examples receive model-assigned targets.

- Derives extra labels from the model itself rather than from heuristics as in [[02 Concepts/Lifecycle/Data Engineering/Weak Supervision|Weak Supervision]]. **Condition:** Both reduce manual labeling; semi-supervision needs a labeled seed and a model confident enough to self-label.

- Keeps only confident pseudo-labels through [[02 Concepts/Lifecycle/Model Evaluation & Testing/Selective Prediction|Selective Prediction]]. **Condition:** When a confidence threshold decides which unlabeled examples enter training.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: pseudo-labeling; self-training; consistency regularization.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
