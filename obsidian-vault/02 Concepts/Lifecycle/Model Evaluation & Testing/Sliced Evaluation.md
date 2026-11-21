---
title: Sliced Evaluation
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Sliced_Robustness_Evaluation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Sliced evaluation
taxonomy_id: mlsys.sliced-evaluation
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Sliced Evaluation

Measuring behavior separately on relevant populations, conditions, or workload groups.

## Browsing Home

[[02 Concepts/Lifecycle/Model Evaluation & Testing/Sliced & Robustness Evaluation Subject|Sliced & Robustness Evaluation]] → [[02 Concepts/Lifecycle/Model Evaluation & Testing/Model Evaluation & Testing Index|Model Evaluation & Testing]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/03 Optimization/12 Benchmarking/V1-12.02 The Benchmark–Production Gap#^sec-benchmarking-machine-learning-benchmarking-framework-70b8|V1-12.02 The Benchmark–Production Gap]] — Model quality. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/12_benchmarking/12_benchmarking.qmd#L67).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Tests specified [[02 Concepts/Qualities/Responsible AI/Fairness Criteria|Fairness Criteria]]. **Condition:** An aggregate score cannot establish performance for every subgroup.

- Exposes subset regressions caused by [[02 Concepts/Lifecycle/MLOps & Operations/Entanglement|Entanglement]]. **Condition:** Applies when a change to one input or hyperparameter is evaluated on the same fixed slices before and after.

- Exposes, on a slice of borderline benign prompts, [[02 Concepts/Qualities/Safety & Assurance/Over Refusal|Over Refusal]]. **Condition:** When the evaluation set includes benign prompts that resemble harmful ones.

- Localizes, by a drop concentrated in one slice, the population affected by [[02 Concepts/Lifecycle/MLOps & Operations/Distribution Shift|Distribution Shift]]. **Condition:** Slices are defined on production inputs and labels or proxies exist for the window.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
