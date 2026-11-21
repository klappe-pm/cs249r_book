---
title: Experiment Budget Allocation
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Hyperparameter_Search_Experiment_Management
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Experiment-budget allocation
taxonomy_id: mlsys.experiment-budget
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Experiment Budget Allocation

Dividing a finite evaluation budget across configurations, repetitions, and fidelities.

## Browsing Home

[[02 Concepts/Lifecycle/Training & Adaptation/Hyperparameter Search & Experiment Management Subject|Hyperparameter Search & Experiment Management]] → [[02 Concepts/Lifecycle/Training & Adaptation/Training & Adaptation Index|Training & Adaptation]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Allocates small proxy runs to fit, and a large run to exploit, [[02 Concepts/Foundations/Quantitative System Models/Empirical Scaling Laws|Empirical Scaling Laws]]. **Condition:** When the budget is split between runs that fit a law at small scale and the final run whose size the law predicts; extrapolation beyond the fitted range is not guaranteed.

- Stops unpromising trials early under [[02 Concepts/Lifecycle/Training & Adaptation/Early Stopping|Early Stopping]]. **Condition:** When a trial is abandoned once its validation metric plateaus, freeing its remaining budget for other configurations.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
