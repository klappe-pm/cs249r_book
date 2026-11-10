---
title: Analytical Performance Model
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Roofline_Performance_Models_Simulation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Analytical performance model
taxonomy_id: mlsys.analytical-performance-model
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Analytical Performance Model

A closed-form model composing compute, memory, communication, and queueing terms to predict a workload's time, memory, and cost on a configuration without running it.

## Browsing Home

[[02 Concepts/Foundations/Quantitative System Models/Roofline, Performance Models & Simulation Subject|Roofline, Performance Models & Simulation]] → [[02 Concepts/Foundations/Quantitative System Models/Quantitative System Models Index|Quantitative System Models]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Composes [[02 Concepts/Foundations/Quantitative System Models/Roofline Bound|Roofline Bound]]. **Condition:** Per-operator roofline bounds are summed or overlapped with communication and queueing terms under stated overlap assumptions.

- Composes [[02 Concepts/Stack/Parallelism & Distributed Execution/Alpha Beta Communication Model|Alpha Beta Communication Model]]. **Condition:** Communication terms use per-collective latency and bandwidth parameters measured or specified for the target fabric.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
