---
title: Request Batching
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Batching_Admission_Autoscaling
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Request batching
taxonomy_id: mlsys.batching
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Request Batching

Executing requests together to share work or improve resource use.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Batching, Admission & Autoscaling Subject|Batching, Admission & Autoscaling]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.06 Throughput Optimization#^sec-model-serving-batching-helps-f1dc|V1-13.06 Throughput Optimization]] — Batching. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/13_model_serving/13_model_serving.qmd#L2796).

- [[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10.07 Batching Strategies at Scale#^sec-inference-scale-physics-batching-efficiency-curve-021c|V2-10.07 Batching Strategies at Scale]] — Request batching. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/10_inference/10_inference.qmd#L1419).

- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.06 Throughput Optimization#^sec-model-serving-batching-tax|V1-13.06 Throughput Optimization]] — Batch formation delay. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/13_model_serving/13_model_serving.qmd#L3117).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Can increase [[02 Concepts/Foundations/Quantitative System Models/Service Capacity|Service Capacity]]. **Condition:** Workload, memory, and kernel efficiency bound the gain.

- Can increase [[02 Concepts/Lifecycle/Deployment & Serving/Tail Latency|Tail Latency]]. **Condition:** Waiting to form a batch can add delay; the net effect depends on queueing and service changes.

- Reduces [[02 Concepts/Qualities/Sustainability & Cost/Cost per Token|Cost per Token]]. **Condition:** When larger or continuous batches raise tokens per accelerator-second without violating latency objectives.

- Moves the operating point along [[02 Concepts/Foundations/Quantitative System Models/Latency Throughput Curve|Latency Throughput Curve]]. **Condition:** Larger batches raise throughput while adding batch-formation and execution delay.

## Themes

- [[03 Themes/Latency and Throughput|Latency and Throughput]]

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
