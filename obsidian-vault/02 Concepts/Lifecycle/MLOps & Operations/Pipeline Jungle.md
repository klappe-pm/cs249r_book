---
title: Pipeline Jungle
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/ML_Platforms_Teams_Technical_Debt
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Pipeline jungle
taxonomy_id: mlsys.pipeline-jungle
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Pipeline Jungle

Data preparation grown incrementally into a tangle of scrapes, joins, and intermediate outputs that is hard to test, trace, and change.

## Browsing Home

[[02 Concepts/Lifecycle/MLOps & Operations/ML Platforms, Teams & Technical Debt Subject|ML Platforms, Teams & Technical Debt]] → [[02 Concepts/Lifecycle/MLOps & Operations/MLOps & Operations Index|MLOps & Operations]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is a form of [[02 Concepts/Lifecycle/MLOps & Operations/ML Technical Debt|ML Technical Debt]]. **Condition:** Data preparation evolves without holistic redesign.

- Impedes end-to-end [[02 Concepts/Lifecycle/Model Evaluation & Testing/Integration Testing|Integration Testing]]. **Condition:** Failures can only be detected by expensive end-to-end tests.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
