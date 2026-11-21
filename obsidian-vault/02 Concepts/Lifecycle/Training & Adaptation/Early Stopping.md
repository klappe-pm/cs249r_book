---
title: Early Stopping
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Optimization_Training_Dynamics
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Early stopping
taxonomy_id: mlsys.early-stopping
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Early Stopping

Ending training according to a held-out validation criterion and selecting a checkpoint under that criterion, limiting additional compute and potentially reducing overfitting.

## Browsing Home

[[02 Concepts/Lifecycle/Training & Adaptation/Optimization & Training Dynamics Subject|Optimization & Training Dynamics]] → [[02 Concepts/Lifecycle/Training & Adaptation/Training & Adaptation Index|Training & Adaptation]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Acts, by truncating training, as a form of [[02 Concepts/Lifecycle/Training & Adaptation/Regularization|Regularization]]. **Condition:** When validation performance peaks before the training loss plateaus.

- Monitors a validation partition from [[02 Concepts/Lifecycle/Model Evaluation & Testing/Evaluation Split|Evaluation Split]]. **Condition:** The stopping decision must not use the final test partition, or the reported score is optimistically biased.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: validation-based stopping.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
