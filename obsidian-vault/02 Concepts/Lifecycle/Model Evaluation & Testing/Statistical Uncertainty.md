---
title: Statistical Uncertainty
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Metrics_Calibration_Uncertainty
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Statistical uncertainty
taxonomy_id: mlsys.statistical-uncertainty
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Statistical Uncertainty

Uncertainty in an estimated quantity due to finite and dependent observations.

## Browsing Home

[[02 Concepts/Lifecycle/Model Evaluation & Testing/Metrics, Calibration & Uncertainty Subject|Metrics, Calibration & Uncertainty]] → [[02 Concepts/Lifecycle/Model Evaluation & Testing/Model Evaluation & Testing Index|Model Evaluation & Testing]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Bounds the precision of conclusions from [[02 Concepts/Lifecycle/Model Evaluation & Testing/Evaluation Metrics|Evaluation Metrics]]. **Condition:** Dependence, sample selection, and repeated comparison matter.

- Bounds the ranking resolution of [[02 Concepts/Lifecycle/Model Evaluation & Testing/Pairwise Preference Evaluation|Pairwise Preference Evaluation]]. **Condition:** Holds because rankings from finite pairwise votes carry sampling error that can reorder close models.

- Limits the confidence achievable in [[02 Concepts/Qualities/Safety & Assurance/Rare Event Safety Validation|Rare Event Safety Validation]]. **Condition:** When the number of observed failures is small, confidence bounds dominate the estimate.

- Lowers, through outcome variance, [[02 Concepts/Lifecycle/Model Evaluation & Testing/Statistical Power|Statistical Power]]. **Condition:** At a fixed sample size; a noisier metric needs more units to detect the same effect.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
