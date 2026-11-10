---
title: Online Learning
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Continual_Online_Learning
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Online learning
taxonomy_id: mlsys.online-learning
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Online Learning

Updating a model incrementally as each example or small batch arrives, rather than retraining on a fixed dataset.

## Browsing Home

[[02 Concepts/Lifecycle/Training & Adaptation/Continual & Online Learning Subject|Continual & Online Learning]] → [[02 Concepts/Lifecycle/Training & Adaptation/Training & Adaptation Index|Training & Adaptation]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Shortens the cycle of [[02 Concepts/Lifecycle/MLOps & Operations/Deployment Feedback Loop|Deployment Feedback Loop]]. **Condition:** Holds when the model's own predictions influence the data it next learns from.

- Consumes examples from [[02 Concepts/Lifecycle/Data Engineering/Stream Processing|Stream Processing]]. **Condition:** Applies when updates happen as events arrive.

- Adapts to [[02 Concepts/Lifecycle/MLOps & Operations/Concept Drift|Concept Drift]]. **Condition:** Holds when labels arrive quickly enough to track the change.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
