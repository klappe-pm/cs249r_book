---
title: Production Monitoring
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Monitoring_Observability
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Production monitoring
taxonomy_id: mlsys.monitoring
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Production Monitoring

Collecting and interpreting signals about deployed system behavior and health.

## Browsing Home

[[02 Concepts/Lifecycle/MLOps & Operations/Monitoring & Observability Subject|Monitoring & Observability]] → [[02 Concepts/Lifecycle/MLOps & Operations/MLOps & Operations Index|MLOps & Operations]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/04 Deployment/14 ML Operations/V1-14.06 Production Monitoring#^sec-ml-operations-production-monitoring-5e1b|V1-14.06 Production Monitoring]] — Production monitoring. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/14_ml_ops/14_ml_ops.qmd#L1738).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Observes signs of [[02 Concepts/Lifecycle/MLOps & Operations/Distribution Shift|Distribution Shift]]. **Condition:** Signals require diagnosis and do not establish harmfulness by themselves.

- Tracks deployed [[02 Concepts/Lifecycle/Model Evaluation & Testing/Evaluation Metrics|Evaluation Metrics]]. **Condition:** Observed task metrics can be delayed, biased, or unavailable; system health alone does not establish task quality.

- Computes [[02 Concepts/Foundations/Workloads & Requirements/Service Level Indicator|Service Level Indicator]]. **Condition:** Monitoring records the events and counts over the population and window the indicator definition specifies.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
