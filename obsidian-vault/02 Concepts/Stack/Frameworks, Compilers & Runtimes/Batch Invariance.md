---
title: Batch Invariance
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Numerical_Formats_Precision
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Batch invariance
taxonomy_id: mlsys.batch-invariance
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Batch Invariance

A kernel property that each request's output is bitwise independent of batch size and co-batched requests, one way to remove a source of run-to-run numerical variation in serving.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Numerical Formats & Precision Subject|Numerical Formats & Precision]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Removes the batch-composition source of [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Numerical Nondeterminism|Numerical Nondeterminism]]. **Condition:** Achieved by fixing reduction strategies independent of batch size, typically at some kernel throughput cost.

- Aligns inference numerics with training for [[02 Concepts/Lifecycle/Training & Adaptation/RL Rollout Generation|RL Rollout Generation]]. **Condition:** Matters when rollout log-probabilities from the serving engine are reused in on-policy training objectives.

- Enables bitwise-reproducible serving within [[02 Concepts/Lifecycle/MLOps & Operations/Experiment Reproducibility|Experiment Reproducibility]]. **Condition:** Kernels use fixed reduction strategies independent of batch size and co-batched requests.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: batch-invariant kernels.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
