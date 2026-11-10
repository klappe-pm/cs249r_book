---
title: Hyperparameter Transfer
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Hyperparameter_Search_Experiment_Management
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Hyperparameter transfer
taxonomy_id: mlsys.hyperparameter-transfer
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Hyperparameter Transfer

Tuning hyperparameters on smaller proxy models and reusing them at larger scale under a parameterization designed to keep them stable.

## Browsing Home

[[02 Concepts/Lifecycle/Training & Adaptation/Hyperparameter Search & Experiment Management Subject|Hyperparameter Search & Experiment Management]] → [[02 Concepts/Lifecycle/Training & Adaptation/Training & Adaptation Index|Training & Adaptation]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Reduces large-scale spend of [[02 Concepts/Lifecycle/Training & Adaptation/Experiment Budget Allocation|Experiment Budget Allocation]]. **Condition:** Holds only under a parameterization in which optimal hyperparameters remain stable as width or depth grows.

- Carries tuned settings into [[02 Concepts/Lifecycle/Training & Adaptation/Learning Rate Schedule|Learning Rate Schedule]]. **Condition:** Holds under a parameterization such as muP that keeps optima stable across width.

- Runs on small proxies [[02 Concepts/Lifecycle/Training & Adaptation/Hyperparameter Search|Hyperparameter Search]]. **Condition:** Holds when proxy models share the target's parameterization.

- Prescribes width-dependent scales for [[02 Concepts/Lifecycle/Training & Adaptation/Weight Initialization|Weight Initialization]]. **Condition:** Hyperparameters tuned on a small model are reused at a larger width.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: muP.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
