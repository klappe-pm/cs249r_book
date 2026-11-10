---
title: Evaluation Metrics
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Metrics_Calibration_Uncertainty
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Evaluation metrics
taxonomy_id: mlsys.metrics
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Evaluation Metrics

Specified measurements of predictive or task behavior, with explicit populations and aggregation.

## Browsing Home

[[02 Concepts/Lifecycle/Model Evaluation & Testing/Metrics, Calibration & Uncertainty Subject|Metrics, Calibration & Uncertainty]] → [[02 Concepts/Lifecycle/Model Evaluation & Testing/Model Evaluation & Testing Index|Model Evaluation & Testing]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/03 Optimization/12 Benchmarking/V1-12.02 The Benchmark–Production Gap#^sec-benchmarking-machine-learning-benchmarking-framework-70b8|V1-12.02 The Benchmark–Production Gap]] — Model quality. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/12_benchmarking/12_benchmarking.qmd#L67).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Measure [[02 Concepts/Lifecycle/Model Evaluation & Testing/Generalization|Generalization]]. **Condition:** The metric, sampling protocol, and target distribution determine what the estimate means.

- Gate advancement during [[02 Concepts/Lifecycle/MLOps & Operations/Staged Rollout|Staged Rollout]]. **Condition:** Release criteria and populations must be specified before interpreting candidate results.

- Can assess support for [[02 Concepts/Lifecycle/Model Evaluation & Testing/Hallucination|Hallucination]]. **Condition:** For tasks requiring factual or source-grounded assertions, evaluate support in addition to fluency or schema validity; not every task has the same truth criterion.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
