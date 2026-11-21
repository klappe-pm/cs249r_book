---
title: Retraining
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Drift_Feedback_Loops_Retraining
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Retraining
taxonomy_id: mlsys.retraining
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Retraining

Training a replacement version of a deployed model on updated or revised data, with timing and data chosen to balance staleness against training and validation cost.

## Browsing Home

[[02 Concepts/Lifecycle/MLOps & Operations/Drift, Feedback Loops & Retraining Subject|Drift, Feedback Loops & Retraining]] → [[02 Concepts/Lifecycle/MLOps & Operations/MLOps & Operations Index|MLOps & Operations]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Mitigates, when triggered by, [[02 Concepts/Lifecycle/MLOps & Operations/Distribution Shift|Distribution Shift]]. **Condition:** A response requires diagnosis and evidence; not every detected shift warrants retraining.

- Mitigates, given fresh labels, [[02 Concepts/Lifecycle/MLOps & Operations/Concept Drift|Concept Drift]]. **Condition:** Holds because input monitoring alone cannot reveal changed input-target relations; updated outcomes are needed.

- Yields a replacement [[02 Concepts/Foundations/Models & Architectures/Model Artifact|Model Artifact]]. **Condition:** After the retrained model passes validation and is versioned for release.

- Is triggered by [[02 Concepts/Lifecycle/MLOps & Operations/Drift Detection|Drift Detection]]. **Condition:** When a detected shift is diagnosed as harmful rather than benign; drift alone is a signal to investigate, not proof of degraded quality.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: retraining trigger; retraining cadence.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
