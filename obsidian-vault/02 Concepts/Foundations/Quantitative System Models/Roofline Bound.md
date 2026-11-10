---
title: Roofline Bound
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Roofline_Performance_Models_Simulation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Roofline bound
taxonomy_id: mlsys.roofline
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Roofline Bound

A performance bound combining a compute ceiling with an intensity-dependent bandwidth ceiling.

## Browsing Home

[[02 Concepts/Foundations/Quantitative System Models/Roofline, Performance Models & Simulation Subject|Roofline, Performance Models & Simulation]] → [[02 Concepts/Foundations/Quantitative System Models/Quantitative System Models Index|Quantitative System Models]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.07 Performance Bounds#^sec-hardware-acceleration-roofline-model-3e1a|V1-11.07 Performance Bounds]] — Operand transfer time. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/11_hw_acceleration/11_hw_acceleration.qmd#L3159).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Implies a lower bound on [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Execution Time|Execution Time]]. **Condition:** For fixed arithmetic work, a throughput ceiling implies a lower execution-time bound. Additional overheads can lengthen actual runtime.

- Bounds attainable [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Model FLOPS Utilization|Model FLOPS Utilization]]. **Condition:** For a given kernel mix, attainable MFU cannot exceed the roofline bound implied by each kernel's arithmetic intensity.

## Themes

- [[03 Themes/Constraints Drive Architecture|Constraints Drive Architecture]]
- [[03 Themes/Memory and Bandwidth|Memory and Bandwidth]]

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: roofline model; roofline analysis.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
