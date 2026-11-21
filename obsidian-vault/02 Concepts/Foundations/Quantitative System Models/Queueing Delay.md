---
title: Queueing Delay
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Queueing_Capacity_Models
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Queueing delay
taxonomy_id: mlsys.queueing
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Queueing Delay

Time a request waits for a resource before receiving service.

## Browsing Home

[[02 Concepts/Foundations/Quantitative System Models/Queueing & Capacity Models Subject|Queueing & Capacity Models]] → [[02 Concepts/Foundations/Quantitative System Models/Quantitative System Models Index|Quantitative System Models]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.05 Queuing Theory#^sec-model-serving-utilizationlatency-relationship-a2f0|V1-13.05 Queuing Theory]] — Queueing delay. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/13_model_serving/13_model_serving.qmd#L2293).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Contributes to [[02 Concepts/Lifecycle/Deployment & Serving/Tail Latency|Tail Latency]]. **Condition:** Service, batching, network, and other delays also contribute.

- Bends upward the [[02 Concepts/Foundations/Quantitative System Models/Latency Throughput Curve|Latency Throughput Curve]]. **Condition:** Utilization approaches service capacity, so waiting time grows sharply.

- Increases [[02 Concepts/Lifecycle/Deployment & Serving/Time to First Token|Time to First Token]]. **Condition:** Holds under load when requests wait for a prefill slot.

## Themes

- [[03 Themes/Latency and Throughput|Latency and Throughput]]

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
