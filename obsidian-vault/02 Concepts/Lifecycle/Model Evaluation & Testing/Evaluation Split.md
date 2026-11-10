---
title: Evaluation Split
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Evaluation_Design_Experiments
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Evaluation split
taxonomy_id: mlsys.evaluation-split
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Evaluation Split

A partitioning protocol that separates learning, selection, and final assessment.

## Browsing Home

[[02 Concepts/Lifecycle/Model Evaluation & Testing/Evaluation Design & Experiments Subject|Evaluation Design & Experiments]] → [[02 Concepts/Lifecycle/Model Evaluation & Testing/Model Evaluation & Testing Index|Model Evaluation & Testing]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/15 Trajectory Curation/V3-15.05 Split Design#^sec-vol3-trajectory-curation-heldout-protection|V3-15.05 Split Design]] — Task-group split. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/15_trajectory_curation/15_trajectory_curation.qmd#L395).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Supports unbiased estimates of [[02 Concepts/Lifecycle/Model Evaluation & Testing/Generalization|Generalization]]. **Condition:** The partition and sampling unit must match the intended deployment question.

- Guards against [[02 Concepts/Lifecycle/Data Engineering/Data Leakage|Data Leakage]]. **Condition:** Holds when splits respect time, entity, and duplicate boundaries.

- Keeps a final test partition free of [[02 Concepts/Lifecycle/Model Evaluation & Testing/Model Selection Optimism|Model Selection Optimism]]. **Condition:** Holds only if the final test partition is not used for any selection decision.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
