---
title: Hyperparameter Search
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Hyperparameter_Search_Experiment_Management
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Hyperparameter search
taxonomy_id: mlsys.hyperparameter-search
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Hyperparameter Search

Choosing model or training settings through a sequence of evaluations.

## Browsing Home

[[02 Concepts/Lifecycle/Training & Adaptation/Hyperparameter Search & Experiment Management Subject|Hyperparameter Search & Experiment Management]] → [[02 Concepts/Lifecycle/Training & Adaptation/Training & Adaptation Index|Training & Adaptation]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Can induce [[02 Concepts/Lifecycle/Model Evaluation & Testing/Model Selection Optimism|Model Selection Optimism]]. **Condition:** Selecting among noisy validation scores can produce an optimistic winner.

- Compares trials through [[02 Concepts/Lifecycle/Training & Adaptation/Experiment Tracking|Experiment Tracking]]. **Condition:** Applies whenever more than a handful of configurations are evaluated.

- Is a stage within [[02 Concepts/Lifecycle/Training & Adaptation/Model Selection|Model Selection]]. **Condition:** Hyperparameters are chosen on validation data.

- Allocates trials under [[02 Concepts/Lifecycle/Training & Adaptation/Experiment Budget Allocation|Experiment Budget Allocation]]. **Condition:** Whenever the number of configurations exceeds what can be trained to completion, so trials, repetitions, and fidelities compete for one budget.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: Hyperparameter optimization; HPO.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
