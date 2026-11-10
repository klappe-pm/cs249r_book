---
title: Benchmark Protocol
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/System_Benchmarking
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Benchmark protocol
taxonomy_id: mlsys.benchmark
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Benchmark Protocol

A reproducible specification of workload, measurement boundary, run rules, and comparison procedure that lets results from different systems be compared and lets a system be judged against a baseline.

## Browsing Home

[[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/System Benchmarking Subject|System Benchmarking]] → [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Performance, Efficiency & Benchmarking Index|Performance, Efficiency & Benchmarking]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/03 Optimization/12 Benchmarking/V1-12.03 Benchmark Carpentry#^sec-benchmarking-benchmark-components-97cc|V1-12.03 Benchmark Carpentry]] — Benchmark protocol. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/12_benchmarking/12_benchmarking.qmd#L330).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Specifies how to measure [[02 Concepts/Lifecycle/Deployment & Serving/Tail Latency|Tail Latency]]. **Condition:** Measurement needs a declared load model, warm-up, boundary, and quantile method.

- Requires [[02 Concepts/Lifecycle/MLOps & Operations/Experiment Reproducibility|Experiment Reproducibility]]. **Condition:** The benchmark protocol must state tolerances, repetitions, environment, and workload; reproducibility does not establish external validity.

- Is only meaningful for a stated [[02 Concepts/Foundations/Workloads & Requirements/Workload Characterization|Workload Characterization]]. **Condition:** Benchmark results transfer only to deployments whose input, request, and model distributions match the benchmark workload.

- Uses [[02 Concepts/Qualities/Sustainability & Cost/Energy Measurement Methodology|Energy Measurement Methodology]]. **Condition:** For energy or power benchmarks, which must declare sensor class, sampling, and system boundary to be comparable.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
