---
title: Compute Optimal Allocation
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Scaling_Laws_Compute_Optimal_Allocation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Compute-optimal allocation
taxonomy_id: mlsys.compute-optimal-allocation
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Compute Optimal Allocation

Choosing model size and training data quantity to minimize loss under a fixed training compute budget, using fitted scaling laws.

## Browsing Home

[[02 Concepts/Foundations/Quantitative System Models/Scaling Laws & Compute Optimal Allocation Subject|Scaling Laws & Compute Optimal Allocation]] → [[02 Concepts/Foundations/Quantitative System Models/Quantitative System Models Index|Quantitative System Models]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/03 Optimization/09 Data Selection/V1-09.03 Measuring Data Value#^sec-data-selection-computeoptimal-frontier-24ba|V1-09.03 Measuring Data Value]] — Model-data allocation. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/09_data_selection/09_data_selection.qmd#L661).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is derived from [[02 Concepts/Foundations/Quantitative System Models/Empirical Scaling Laws|Empirical Scaling Laws]]. **Condition:** The fitted law is used within the range of model and data sizes it was fit on.

- Uses [[02 Concepts/Foundations/Quantitative System Models/Training Compute Estimate|Training Compute Estimate]]. **Condition:** Dense models are trained where the six-operations-per-parameter-per-token approximation holds.

- Can trade off against lifecycle [[02 Concepts/Qualities/Sustainability & Cost/Cost per Useful Outcome|Cost per Useful Outcome]]. **Condition:** Large inference volume can favor smaller models trained beyond the compute-optimal point.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: Chinchilla scaling.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
