---
title: Critical Batch Size
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Optimization_Training_Dynamics
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Critical batch size
taxonomy_id: mlsys.critical-batch-size
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Critical Batch Size

The batch size beyond which increasing it further yields diminishing reductions in optimization steps to reach a target loss.

## Browsing Home

[[02 Concepts/Lifecycle/Training & Adaptation/Optimization & Training Dynamics Subject|Optimization & Training Dynamics]] → [[02 Concepts/Lifecycle/Training & Adaptation/Training & Adaptation Index|Training & Adaptation]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06.05 Scaling Efficiency and Convergence#^sec-distributed-training-systems-systems-critical-batch-size-parallelism-hurt-4961|V2-06.05 Scaling Efficiency and Convergence]] — Critical batch size. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/06_distributed_training/06_distributed_training.qmd#L2938).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Limits useful scaling of [[02 Concepts/Stack/Parallelism & Distributed Execution/Data Parallelism|Data Parallelism]]. **Condition:** Holds when adding replicas increases the global batch beyond the critical batch size.

- Bounds useful data-parallel [[02 Concepts/Foundations/Quantitative System Models/Weak Scaling|Weak Scaling]]. **Condition:** Growing the global batch with worker count stops reducing optimization steps beyond the critical batch size.

- Bounds the useful [[02 Concepts/Lifecycle/Training & Adaptation/Training Batch Size|Training Batch Size]]. **Condition:** Holds for a given target loss and training phase; it grows as loss falls.

- Bounds the data-parallel speedup of [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Time to Train|Time to Train]]. **Condition:** Holds because beyond it more examples per step no longer cut the steps needed to reach the target loss.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
