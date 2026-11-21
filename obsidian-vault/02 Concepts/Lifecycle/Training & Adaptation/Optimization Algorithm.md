---
title: Optimization Algorithm
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Optimization_Training_Dynamics
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Optimization algorithm
taxonomy_id: mlsys.optimizer
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Optimization Algorithm

A rule that uses training information to update model parameters and optimizer state.

## Browsing Home

[[02 Concepts/Lifecycle/Training & Adaptation/Optimization & Training Dynamics Subject|Optimization & Training Dynamics]] → [[02 Concepts/Lifecycle/Training & Adaptation/Training & Adaptation Index|Training & Adaptation]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/02 Development/05 Neural Computation/V1-05.05 Learning Process#^sec-neural-computation-minibatch-gradient-updates-4a04|V1-05.05 Learning Process]] — Parameter gradients. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/05_nn_computation/05_nn_computation.qmd#L3192).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Requires an objective from [[02 Concepts/Lifecycle/Training & Adaptation/Training Loss|Training Loss]]. **Condition:** Optimizing the training objective alone does not certify task success.

- Adds optimizer variables to [[02 Concepts/Lifecycle/Training & Adaptation/Training State|Training State]]. **Condition:** Different update rules retain different auxiliary state.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
