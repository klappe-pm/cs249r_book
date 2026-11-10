---
title: Label Shift Estimation and Prior Correction
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Drift_Feedback_Loops_Retraining
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Label-shift estimation and prior correction
taxonomy_id: mlsys.label-shift-estimation
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Label Shift Estimation and Prior Correction

Estimating deployment class priors from unlabeled predictions under stable class-conditional input distributions and adjusting weights or probabilities to reduce errors from the changed priors.

## Browsing Home

[[02 Concepts/Lifecycle/MLOps & Operations/Drift, Feedback Loops & Retraining Subject|Drift, Feedback Loops & Retraining]] → [[02 Concepts/Lifecycle/MLOps & Operations/MLOps & Operations Index|MLOps & Operations]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Corrects, without new labels, the label-shift form of [[02 Concepts/Lifecycle/MLOps & Operations/Distribution Shift|Distribution Shift]]. **Condition:** When class priors change but class-conditional input distributions do not; it does not address covariate or concept drift.

- Adjusts posteriors by Bayes' rule and so depends on [[02 Concepts/Lifecycle/Model Evaluation & Testing/Probability Calibration|Probability Calibration]]. **Condition:** When predicted probabilities are re-weighted by the ratio of new to old priors; miscalibrated scores give wrong corrections.

- Is a label-free alternative, for prior changes, to [[02 Concepts/Lifecycle/MLOps & Operations/Retraining|Retraining]]. **Condition:** When the shift is confined to class priors and fresh labels are unavailable or delayed.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: BBSE; black-box shift estimation; prior shift correction; EM prior adjustment; class-prior re-estimation; class-prior adaptation.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
