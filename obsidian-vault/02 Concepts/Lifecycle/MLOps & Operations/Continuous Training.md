---
title: Continuous Training
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Drift_Feedback_Loops_Retraining
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Continuous training
taxonomy_id: mlsys.continuous-training
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Continuous Training

An automated pipeline that retrains, validates, and proposes models on a schedule or when triggered by data or performance signals.

## Browsing Home

[[02 Concepts/Lifecycle/MLOps & Operations/Drift, Feedback Loops & Retraining Subject|Drift, Feedback Loops & Retraining]] → [[02 Concepts/Lifecycle/MLOps & Operations/MLOps & Operations Index|MLOps & Operations]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Automates [[02 Concepts/Lifecycle/MLOps & Operations/Retraining|Retraining]]. **Condition:** Holds when data validation and release gates are automated so retrained models can be promoted without manual steps.

- Is a defining capability of higher levels of [[02 Concepts/Lifecycle/MLOps & Operations/MLOps Maturity|MLOps Maturity]]. **Condition:** Holds for maturity models that define levels by degree of pipeline automation.

- Validates incoming data before each run of [[02 Concepts/Lifecycle/Data Engineering/Data Validation|Data Validation]]. **Condition:** When the pipeline is automated end to end, so a schema or distribution failure must stop retraining rather than a person.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: CT.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
