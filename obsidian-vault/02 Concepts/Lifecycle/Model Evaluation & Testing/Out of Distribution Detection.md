---
title: Out of Distribution Detection
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Metrics_Calibration_Uncertainty
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Out-of-distribution detection
taxonomy_id: mlsys.ood-detection
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Out of Distribution Detection

Flagging individual inputs that differ from the training distribution so the system can abstain, defer, or fall back instead of trusting the prediction.

## Browsing Home

[[02 Concepts/Lifecycle/Model Evaluation & Testing/Metrics, Calibration & Uncertainty Subject|Metrics, Calibration & Uncertainty]] → [[02 Concepts/Lifecycle/Model Evaluation & Testing/Model Evaluation & Testing Index|Model Evaluation & Testing]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Flags individual inputs affected by [[02 Concepts/Lifecycle/MLOps & Operations/Distribution Shift|Distribution Shift]]. **Condition:** Inputs fall outside the training distribution.

- Supplies abstention signals to [[02 Concepts/Lifecycle/Model Evaluation & Testing/Selective Prediction|Selective Prediction]]. **Condition:** The system may defer uncertain inputs.

- Thresholds epistemic signals from [[02 Concepts/Lifecycle/Model Evaluation & Testing/Predictive Uncertainty Estimation|Predictive Uncertainty Estimation]]. **Condition:** When uncertainty rises on inputs far from the training data; raw softmax confidence is often overconfident there.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: OOD detection; novelty detection.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
