---
title: Precision, Recall, and ROC Analysis
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Metrics_Calibration_Uncertainty
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Precision, recall, and ROC analysis
taxonomy_id: mlsys.precision-recall
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Precision, Recall, and ROC Analysis

Classifier metrics that separate the two error types, false positives and false negatives, and the curves (ROC, precision-recall) that show how a decision threshold trades them, which matter whenever classes are imbalanced or the two errors cost differently.

## Browsing Home

[[02 Concepts/Lifecycle/Model Evaluation & Testing/Metrics, Calibration & Uncertainty Subject|Metrics, Calibration & Uncertainty]] → [[02 Concepts/Lifecycle/Model Evaluation & Testing/Model Evaluation & Testing Index|Model Evaluation & Testing]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is the two-error-type family of [[02 Concepts/Lifecycle/Model Evaluation & Testing/Evaluation Metrics|Evaluation Metrics]]. **Condition:** For classification or detection tasks where false positives and false negatives carry different costs.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: F1 score; ROC curve; AUC; precision-recall curve.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
