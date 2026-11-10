---
title: CI CD for ML
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Versioning_Rollout_Rollback
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: CI/CD for ML
taxonomy_id: mlsys.ml-ci-cd
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# CI CD for ML

Automated building, testing, and deployment of ML code, data checks, and model artifacts on each change.

## Browsing Home

[[02 Concepts/Lifecycle/MLOps & Operations/Versioning, Rollout & Rollback Subject|Versioning, Rollout & Rollback]] → [[02 Concepts/Lifecycle/MLOps & Operations/MLOps & Operations Index|MLOps & Operations]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Automates [[02 Concepts/Lifecycle/MLOps & Operations/Release Gate|Release Gate]]. **Condition:** Holds when gate criteria are machine-checkable; some require human review.

- Runs [[02 Concepts/Lifecycle/Model Evaluation & Testing/Integration Testing|Integration Testing]]. **Condition:** Applies on each change to code, data checks, or model artifacts.

- Marks higher levels of [[02 Concepts/Lifecycle/MLOps & Operations/MLOps Maturity|MLOps Maturity]]. **Condition:** Holds for maturity models in which automated pipeline delivery defines the top level.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
