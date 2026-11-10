---
title: Simulator Fidelity
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Roofline_Performance_Models_Simulation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Simulator fidelity
taxonomy_id: mlsys.model-fidelity
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Simulator Fidelity

Agreement between a performance model's or simulator's predictions and measured behavior on reference workloads, reported as validation error over stated configurations.

## Browsing Home

[[02 Concepts/Foundations/Quantitative System Models/Roofline, Performance Models & Simulation Subject|Roofline, Performance Models & Simulation]] → [[02 Concepts/Foundations/Quantitative System Models/Quantitative System Models Index|Quantitative System Models]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Bounds trust in [[02 Concepts/Foundations/Quantitative System Models/Analytical Performance Model|Analytical Performance Model]]. **Condition:** Predictions are credible only within the configurations where validation error against measurement has been reported.

- Bounds trust in [[02 Concepts/Foundations/Quantitative System Models/Performance Simulation|Performance Simulation]]. **Condition:** Simulator predictions are validated against measurement on reference workloads.

- Requires measurements from [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Profiling|Profiling]]. **Condition:** Validation compares predictions with profiled or benchmarked execution.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: validation error.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
