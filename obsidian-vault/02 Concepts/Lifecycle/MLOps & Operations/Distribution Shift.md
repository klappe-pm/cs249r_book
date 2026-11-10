---
title: Distribution Shift
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Drift_Feedback_Loops_Retraining
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Distribution shift
taxonomy_id: mlsys.distribution-shift
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Distribution Shift

A difference between development and deployment data-generating distributions.

## Browsing Home

[[02 Concepts/Lifecycle/MLOps & Operations/Drift, Feedback Loops & Retraining Subject|Drift, Feedback Loops & Retraining]] → [[02 Concepts/Lifecycle/MLOps & Operations/MLOps & Operations Index|MLOps & Operations]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/04 Deployment/14 ML Operations/V1-14.06 Production Monitoring#^sec-ml-operations-model-infrastructure-monitoring-3988|V1-14.06 Production Monitoring]] — Distribution shift. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/14_ml_ops/14_ml_ops.qmd#L1793).

- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/14 Robust AI/V2-14.05 Environmental Shifts#^sec-robust-ai-distribution-shift-concept-drift-55e2|V2-14.05 Environmental Shifts]] — Distribution shift. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/14_robust_ai/14_robust_ai.qmd#L365).

- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05.03 Mechanics of Endogenous Covariate Shift#^sec-data-covariate-shift|V4-05.03 Mechanics of Endogenous Covariate Shift]] — Endogenous covariate shift. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/05_data/05_data.qmd#L89).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Can degrade [[02 Concepts/Lifecycle/Model Evaluation & Testing/Probability Calibration|Probability Calibration]]. **Condition:** Calibration measured on one distribution need not hold after a shift.

- Feeds, in closed loop, the growth of [[02 Concepts/Lifecycle/Training & Adaptation/Compounding Error in Sequential Decisions|Compounding Error in Sequential Decisions]]. **Condition:** When the shift is the policy-induced change in visited states, so each off-distribution state raises the next per-step error.

- Bounds what can be learned in [[02 Concepts/Lifecycle/Training & Adaptation/Offline Reinforcement Learning|Offline Reinforcement Learning]]. **Condition:** The learned policy visits states the dataset does not cover.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: dataset shift; covariate shift; label shift.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
