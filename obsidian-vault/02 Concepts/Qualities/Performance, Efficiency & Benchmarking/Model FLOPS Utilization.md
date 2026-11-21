---
title: Model FLOPS Utilization
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Profiling_Utilization
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Model FLOPs utilization
taxonomy_id: mlsys.model-flops-utilization
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Model FLOPS Utilization

Model-required floating-point operations per second achieved, divided by the aggregate peak FLOP rate of the hardware used, excluding recomputation.

## Browsing Home

[[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Profiling & Utilization Subject|Profiling & Utilization]] → [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Performance, Efficiency & Benchmarking Index|Performance, Efficiency & Benchmarking]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08.06 Identifying Bottlenecks#^sec-model-training-identifying-bottlenecks-f57f|V1-08.06 Identifying Bottlenecks]] — Model FLOPs utilization. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/08_training/08_training.qmd#L3482).

- [[01 Books/Volume II - Scaling/03 The Fleet in Production/09 Fleet Efficiency/V2-09.08 Recovering Program Goodput#^sec-performance-engineering-program-goodput|V2-09.08 Recovering Program Goodput]] — Program goodput. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/09_performance_engineering/09_performance_engineering.qmd#L2337).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Specializes [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Resource Utilization|Resource Utilization]]. **Condition:** Holds when utilization is defined as model-required FLOPs per second over aggregate peak FLOP rate, excluding recomputed work.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: MFU.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
