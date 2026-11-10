---
title: User Feedback Collection
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Drift_Feedback_Loops_Retraining
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: User feedback collection
taxonomy_id: mlsys.user-feedback
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# User Feedback Collection

Capturing explicit signals such as ratings and corrections and implicit signals such as clicks, edits, and abandonment, for use as labels or quality signals.

## Browsing Home

[[02 Concepts/Lifecycle/MLOps & Operations/Drift, Feedback Loops & Retraining Subject|Drift, Feedback Loops & Retraining]] → [[02 Concepts/Lifecycle/MLOps & Operations/MLOps & Operations Index|MLOps & Operations]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Attaches signals to records in [[02 Concepts/Lifecycle/MLOps & Operations/Prediction Logging|Prediction Logging]]. **Condition:** Feedback is joined to the prediction that elicited it.

- Supplies labels for [[02 Concepts/Lifecycle/MLOps & Operations/Retraining|Retraining]]. **Condition:** Feedback is filtered for noise and position or exposure bias.

- Can drive [[02 Concepts/Lifecycle/MLOps & Operations/Deployment Feedback Loop|Deployment Feedback Loop]]. **Condition:** Feedback is gathered only on outputs the model chose to show.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: explicit feedback; implicit feedback.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
