---
title: Conformal Prediction
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Metrics_Calibration_Uncertainty
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Conformal prediction
taxonomy_id: mlsys.conformal-prediction
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Conformal Prediction

Constructing prediction sets from conformity scores with finite-sample coverage guarantees under stated assumptions, such as exchangeability.

## Browsing Home

[[02 Concepts/Lifecycle/Model Evaluation & Testing/Metrics, Calibration & Uncertainty Subject|Metrics, Calibration & Uncertainty]] → [[02 Concepts/Lifecycle/Model Evaluation & Testing/Model Evaluation & Testing Index|Model Evaluation & Testing]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/14 Robust AI/V2-14.05 Environmental Shifts#^sec-robust-ai-selective-prediction|V2-14.05 Environmental Shifts]] — Selective prediction. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/14_robust_ai/14_robust_ai.qmd#L1128).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Provides coverage-calibrated sets for [[02 Concepts/Lifecycle/Model Evaluation & Testing/Selective Prediction|Selective Prediction]]. **Condition:** Prediction sets inform an abstention rule; ordinary marginal coverage under exchangeability does not automatically guarantee coverage under distribution shift or conditional accuracy among accepted predictions.

- Requires a held-out calibration [[02 Concepts/Lifecycle/Model Evaluation & Testing/Evaluation Split|Evaluation Split]]. **Condition:** For split conformal methods, the calibration data are separated from score-function fitting, with the stated exchangeability assumptions required for the coverage guarantee.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
