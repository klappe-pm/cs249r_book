---
title: Service Capacity
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Queueing_Capacity_Models
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Service capacity
taxonomy_id: mlsys.service-capacity
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Service Capacity

The completion rate supported by a service under a stated workload and operating point.

## Browsing Home

[[02 Concepts/Foundations/Quantitative System Models/Queueing & Capacity Models Subject|Queueing & Capacity Models]] → [[02 Concepts/Foundations/Quantitative System Models/Quantitative System Models Index|Quantitative System Models]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.11 Economics and Planning#^sec-model-serving-capacity-planning-96a3|V1-13.11 Economics and Planning]] — Serving capacity. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/13_model_serving/13_model_serving.qmd#L5702).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Bounds the sustainable [[02 Concepts/Foundations/Quantitative System Models/Arrival Rate|Arrival Rate]]. **Condition:** The request mix and service-time distribution determine demand.

- Bounds sustainable [[02 Concepts/Lifecycle/Deployment & Serving/SLO Goodput|SLO Goodput]]. **Condition:** Only for matching work units, counting boundary, workload, operating state, and horizon. A measured throughput is not a universal capacity ceiling.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: service rate.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
