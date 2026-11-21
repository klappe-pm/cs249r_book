---
title: Service Level Objective
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Requirements_SLOs_Baselines
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Service-level objective
taxonomy_id: mlsys.slo
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Service Level Objective

A target for a defined service measure over a specified population and window.

## Browsing Home

[[02 Concepts/Foundations/Workloads & Requirements/Requirements, SLOs & Baselines Subject|Requirements, SLOs & Baselines]] → [[02 Concepts/Foundations/Workloads & Requirements/Workloads & Requirements Index|Workloads & Requirements]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/03 Optimization/12 Benchmarking/V1-12.07 Inference Benchmarks#^sec-benchmarking-latency-tail-latency-5cde|V1-12.07 Inference Benchmarks]] — Latency SLO. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/12_benchmarking/12_benchmarking.qmd#L2224).

- [[01 Books/Volume II - Scaling/03 The Fleet in Production/12 ML Operations at Scale/V2-12.06 CI CD for ML at Scale#^sec-ops-scale-end-to-end-evaluation-contract|V2-12.06 CI CD for ML at Scale]] — Evaluation contract. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/12_ops_scale/12_ops_scale.qmd#L2336).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Defines the counting rule for [[02 Concepts/Lifecycle/Deployment & Serving/SLO Goodput|SLO Goodput]]. **Condition:** The counting rule must specify latency, quality, failures, and the workload population.

- Sets the size of [[02 Concepts/Foundations/Workloads & Requirements/Error Budget|Error Budget]]. **Condition:** The objective is stated as a fraction over a defined window.

- Sets the total allocated by [[02 Concepts/Foundations/Workloads & Requirements/Latency Budget|Latency Budget]]. **Condition:** Holds when the end-to-end SLO is decomposed into per-stage targets that sum within it.

## Themes

- [[03 Themes/Constraints Drive Architecture|Constraints Drive Architecture]]
- [[03 Themes/Latency and Throughput|Latency and Throughput]]

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: SLO.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
