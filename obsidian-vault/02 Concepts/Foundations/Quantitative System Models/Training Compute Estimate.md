---
title: Training Compute Estimate
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Scaling_Laws_Compute_Optimal_Allocation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Training compute estimate
taxonomy_id: mlsys.training-compute-estimate
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Training Compute Estimate

Approximating dense transformer training compute as roughly six floating-point operations per parameter per training token.

## Browsing Home

[[02 Concepts/Foundations/Quantitative System Models/Scaling Laws & Compute Optimal Allocation Subject|Scaling Laws & Compute Optimal Allocation]] → [[02 Concepts/Foundations/Quantitative System Models/Quantitative System Models Index|Quantitative System Models]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08.04 Computation and Memory Costs of Training#^sec-model-training-time-to-quality|V1-08.04 Computation and Memory Costs of Training]] — Time to target quality. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/08_training/08_training.qmd#L1252).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is a special case of [[02 Concepts/Foundations/Workloads & Requirements/Operation and Byte Accounting|Operation and Byte Accounting]]. **Condition:** The model is a dense transformer and attention cost is small relative to parameter compute.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: 6ND.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
