---
title: Latency Percentiles
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Latency_Throughput_Goodput
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Latency percentiles
taxonomy_id: mlsys.latency-percentiles
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Latency Percentiles

Summarizing a latency distribution by percentiles such as p50, p95, and p99, so that a service is judged by the experience of most requests and of the slow tail rather than by the mean.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Latency, Throughput & Goodput Subject|Latency, Throughput & Goodput]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/03 Optimization/12 Benchmarking/V1-12.07 Inference Benchmarks#^sec-benchmarking-latency-tail-latency-5cde|V1-12.07 Inference Benchmarks]] — Latency SLO. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/12_benchmarking/12_benchmarking.qmd#L2224).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Quantifies [[02 Concepts/Lifecycle/Deployment & Serving/Tail Latency|Tail Latency]]. **Condition:** High percentiles such as p99 are reported.

- Is a common form of [[02 Concepts/Foundations/Workloads & Requirements/Service Level Indicator|Service Level Indicator]]. **Condition:** The SLO is stated as a percentile under a threshold.

- Summarizes the distribution of [[02 Concepts/Lifecycle/Deployment & Serving/Time to First Token|Time to First Token]]. **Condition:** When time to first token is recorded per request rather than averaged.

## Themes

- [[03 Themes/Latency and Throughput|Latency and Throughput]]

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: p50; p99; percentile latency.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
