---
title: Performance Simulation
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Roofline_Performance_Models_Simulation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Performance simulation
taxonomy_id: mlsys.performance-simulation
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Performance Simulation

Predicting system behavior by executing a model of compute, memory, network, or scheduling events at a chosen granularity, trading simulation speed against detail.

## Browsing Home

[[02 Concepts/Foundations/Quantitative System Models/Roofline, Performance Models & Simulation Subject|Roofline, Performance Models & Simulation]] → [[02 Concepts/Foundations/Quantitative System Models/Quantitative System Models Index|Quantitative System Models]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Trades speed for detail against [[02 Concepts/Foundations/Quantitative System Models/Analytical Performance Model|Analytical Performance Model]]. **Condition:** Simulation captures contention and scheduling effects closed forms omit, at much higher evaluation cost per configuration.

- Replays [[02 Concepts/Foundations/Workloads & Requirements/Workload Trace|Workload Trace]]. **Condition:** Trace-driven simulation is used to compare scheduling, capacity, or serving policies on realistic demand.

- Replays workloads from [[02 Concepts/Foundations/Quantitative System Models/Operator Execution Trace|Operator Execution Trace]]. **Condition:** Traces are in a standardized format.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: system simulation.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
