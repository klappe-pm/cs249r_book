---
title: Model Selection
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Hyperparameter_Search_Experiment_Management
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Model selection
taxonomy_id: mlsys.model-selection
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Model Selection

Choosing among candidate model families, architectures, and hyperparameters by validated performance under the system's accuracy, cost, and latency constraints.

## Browsing Home

[[02 Concepts/Lifecycle/Training & Adaptation/Hyperparameter Search & Experiment Management Subject|Hyperparameter Search & Experiment Management]] → [[02 Concepts/Lifecycle/Training & Adaptation/Training & Adaptation Index|Training & Adaptation]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Estimates candidate performance with [[02 Concepts/Lifecycle/Model Evaluation & Testing/Cross Validation|Cross Validation]]. **Condition:** Data is too small for a dedicated validation split.

- Can inflate estimates through [[02 Concepts/Lifecycle/Model Evaluation & Testing/Model Selection Optimism|Model Selection Optimism]]. **Condition:** Selection and final assessment reuse the same validation data.

- Compares candidates against [[02 Concepts/Foundations/Workloads & Requirements/Baseline|Baseline]]. **Condition:** The baseline is evaluated under the same protocol.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: model development.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
