---
title: Latency Budget
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Requirements_SLOs_Baselines
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Latency budget
taxonomy_id: mlsys.latency-budget
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Latency Budget

An allocation of an end-to-end latency target across the stages of a request path, such as network, preprocessing, inference, and postprocessing.

## Browsing Home

[[02 Concepts/Foundations/Workloads & Requirements/Requirements, SLOs & Baselines Subject|Requirements, SLOs & Baselines]] → [[02 Concepts/Foundations/Workloads & Requirements/Workloads & Requirements Index|Workloads & Requirements]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.04 Request Lifecycle#^sec-model-serving-request-lifecycle-d9c6|V1-13.04 Request Lifecycle]] — Request latency. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/13_model_serving/13_model_serving.qmd#L1285).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Allocates permitted [[02 Concepts/Lifecycle/Deployment & Serving/Tail Latency|Tail Latency]]. **Condition:** Stage latencies compose along a request path whose end-to-end target is fixed.

- Bounds the per-stage cost of [[02 Concepts/Lifecycle/Deployment & Serving/Multi Stage Retrieval and Ranking|Multi Stage Retrieval and Ranking]]. **Condition:** Each stage receives a share of the end-to-end budget and a candidate count it can afford to score.

- Caps the intermediate tokens allowed by [[02 Concepts/Lifecycle/Deployment & Serving/Reasoning Budget|Reasoning Budget]]. **Condition:** Interactive requests must answer within a fixed end-to-end latency target, so extra reasoning tokens consume the same budget.

- Bounds the stages of [[02 Concepts/Lifecycle/Deployment & Serving/Voice Interaction Pipeline|Voice Interaction Pipeline]]. **Condition:** Turn latency must stay within conversational expectations.

## Themes

- [[03 Themes/Constraints Drive Architecture|Constraints Drive Architecture]]
- [[03 Themes/Latency and Throughput|Latency and Throughput]]

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
