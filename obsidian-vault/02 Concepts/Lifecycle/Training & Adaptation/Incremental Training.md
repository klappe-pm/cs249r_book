---
title: Incremental Training
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Continual_Online_Learning
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Incremental training
taxonomy_id: mlsys.incremental-training
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Incremental Training

Continuing training of an existing model from its current weights on new data instead of training from scratch.

## Browsing Home

[[02 Concepts/Lifecycle/Training & Adaptation/Continual & Online Learning Subject|Continual & Online Learning]] → [[02 Concepts/Lifecycle/Training & Adaptation/Training & Adaptation Index|Training & Adaptation]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is one way to carry out [[02 Concepts/Lifecycle/MLOps & Operations/Retraining|Retraining]]. **Condition:** When warm-started training produces the replacement for a deployed model.

- Can cause [[02 Concepts/Lifecycle/Training & Adaptation/Catastrophic Forgetting|Catastrophic Forgetting]]. **Condition:** Holds when new data differs from the original distribution and old data is not replayed.

- Commonly mixes in [[02 Concepts/Lifecycle/Training & Adaptation/Experience Replay|Experience Replay]]. **Condition:** Applies when earlier data is retained and permitted for reuse.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: stateful training; warm-start training; continued pretraining; domain-adaptive pretraining; continual pretraining.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
