---
title: Deployment Feedback Loop
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Drift_Feedback_Loops_Retraining
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Deployment feedback loop
taxonomy_id: mlsys.feedback-loop
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Deployment Feedback Loop

A deployed system's outputs changing the data or behavior encountered by future learning or evaluation.

## Browsing Home

[[02 Concepts/Lifecycle/MLOps & Operations/Drift, Feedback Loops & Retraining Subject|Drift, Feedback Loops & Retraining]] → [[02 Concepts/Lifecycle/MLOps & Operations/MLOps & Operations Index|MLOps & Operations]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/04 Deployment/15 Responsible Engineering/V1-15.04 Responsible Engineering Across the Lifecycle#^sec-responsible-engineering-monitoring-incident-response-54f4|V1-15.04 Responsible Engineering Across the Lifecycle]] — Bias feedback. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/15_responsible_engr/15_responsible_engr.qmd#L1689).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Can degrade [[02 Concepts/Lifecycle/Data Engineering/Data Quality|Data Quality]]. **Condition:** Deployed decisions can alter which labels and examples are subsequently observed.

- Shared retraining data can cause [[02 Concepts/Lifecycle/Model Evaluation & Testing/Experiment Interference|Experiment Interference]]. **Condition:** Holds when control and treatment models learn from logs that both arms influenced.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
