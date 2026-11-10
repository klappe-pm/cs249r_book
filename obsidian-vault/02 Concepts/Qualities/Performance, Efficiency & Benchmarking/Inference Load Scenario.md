---
title: Inference Load Scenario
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/System_Benchmarking
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Inference load scenario
taxonomy_id: mlsys.inference-load-scenario
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Inference Load Scenario

A specified query-arrival pattern and latency constraint, such as single-stream, server, or offline, under which inference performance is measured.

## Browsing Home

[[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/System Benchmarking Subject|System Benchmarking]] → [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Performance, Efficiency & Benchmarking Index|Performance, Efficiency & Benchmarking]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Sets the latency-percentile constraint on [[02 Concepts/Lifecycle/Deployment & Serving/Tail Latency|Tail Latency]]. **Condition:** Holds for server-style scenarios that report throughput only at a stated latency percentile.

- Determines the admissible [[02 Concepts/Lifecycle/Deployment & Serving/Request Batching|Request Batching]]. **Condition:** Offline scenarios permit large batches; server and single-stream scenarios limit batching by their latency constraint.

- Specifies the query [[02 Concepts/Foundations/Quantitative System Models/Arrival Rate|Arrival Rate]]. **Condition:** In server scenarios, where queries arrive by a stated random process at a target rate.

- Sets how closely measured results match deployment for [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Benchmark Representativeness|Benchmark Representativeness]]. **Condition:** Arrival pattern and latency constraint are chosen to mirror the target service.

- Fixes as open or closed loop the [[02 Concepts/Foundations/Quantitative System Models/Open Loop vs. Closed Loop Load|Open Loop vs. Closed Loop Load]]. **Condition:** Server scenarios issue queries by a timed random process; single-stream and multi-stream scenarios wait for each response.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
