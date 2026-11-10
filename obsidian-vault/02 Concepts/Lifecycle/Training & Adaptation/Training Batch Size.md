---
title: Training Batch Size
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Optimization_Training_Dynamics
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Training batch size
taxonomy_id: mlsys.batch-size
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Training Batch Size

The number of examples contributing to an optimization update or microstep.

## Browsing Home

[[02 Concepts/Lifecycle/Training & Adaptation/Optimization & Training Dynamics Subject|Optimization & Training Dynamics]] → [[02 Concepts/Lifecycle/Training & Adaptation/Training & Adaptation Index|Training & Adaptation]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08.05 Pipeline Architecture#^sec-model-training-batch-size-parameter-updates-4d0b|V1-08.05 Pipeline Architecture]] — Training batch size. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/08_training/08_training.qmd#L3141).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Sets gradient noise and step count for [[02 Concepts/Lifecycle/Training & Adaptation/Optimization Algorithm|Optimization Algorithm]]. **Condition:** Changing the batch can alter gradient noise and statistical efficiency.

- Shifts the best peak rate of [[02 Concepts/Lifecycle/Training & Adaptation/Learning Rate Schedule|Learning Rate Schedule]]. **Condition:** Holds below the critical batch size, where learning rate is typically scaled with batch.

- Bounds the in-batch negatives available to [[02 Concepts/Lifecycle/Training & Adaptation/Contrastive Learning|Contrastive Learning]]. **Condition:** When negatives are drawn from the same batch rather than a memory bank.

- Sets the arithmetic intensity, and so the binding ceiling, of weight-streaming kernels in [[02 Concepts/Foundations/Quantitative System Models/Compute Bound vs. Memory Bound|Compute Bound vs. Memory Bound]]. **Condition:** Holds for kernels whose bytes are dominated by weights reused across the batch, such as GEMM and decode attention.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
