---
title: Production Readiness Assessment
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/ML_Testing_Debugging
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Production-readiness assessment
taxonomy_id: mlsys.production-readiness
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Production Readiness Assessment

A structured rubric of data, model, infrastructure, and monitoring tests used to judge whether an ML system is ready to operate.

## Browsing Home

[[02 Concepts/Lifecycle/Model Evaluation & Testing/ML Testing & Debugging Subject|ML Testing & Debugging]] → [[02 Concepts/Lifecycle/Model Evaluation & Testing/Model Evaluation & Testing Index|Model Evaluation & Testing]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Supplies criteria for [[02 Concepts/Lifecycle/MLOps & Operations/Release Gate|Release Gate]]. **Condition:** Holds when rubric items are converted into automated or reviewed checks.

- Scores accumulated [[02 Concepts/Lifecycle/MLOps & Operations/ML Technical Debt|ML Technical Debt]]. **Condition:** The rubric must be applied repeatedly to the same system to track change over time.

- Requires evidence from [[02 Concepts/Lifecycle/Model Evaluation & Testing/Integration Testing|Integration Testing]]. **Condition:** Holds for the infrastructure and pipeline sections of the rubric.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
