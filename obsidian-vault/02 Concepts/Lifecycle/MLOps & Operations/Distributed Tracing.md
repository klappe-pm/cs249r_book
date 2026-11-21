---
title: Distributed Tracing
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Monitoring_Observability
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Distributed tracing
taxonomy_id: mlsys.distributed-tracing
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Distributed Tracing

Recording request-scoped, causally linked spans across services so that one request's latency and failures can be attributed to the components it traversed.

## Browsing Home

[[02 Concepts/Lifecycle/MLOps & Operations/Monitoring & Observability Subject|Monitoring & Observability]] → [[02 Concepts/Lifecycle/MLOps & Operations/MLOps & Operations Index|MLOps & Operations]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Provides request-level evidence within [[02 Concepts/Lifecycle/MLOps & Operations/System Observability|System Observability]]. **Condition:** Requires trace context to be propagated across every service and asynchronous hop the request traverses.

- Localizes the component behind [[02 Concepts/Lifecycle/MLOps & Operations/ML Failure Attribution|ML Failure Attribution]]. **Condition:** Holds when every component a request traverses propagates the trace context.

- Detects [[02 Concepts/Qualities/Reliability & Fault Tolerance/Gray Failure|Gray Failure]]. **Condition:** When traces record the latency and errors that callers actually experience rather than health-check results.

- Keeps a fraction of request traces through [[02 Concepts/Lifecycle/MLOps & Operations/Telemetry Sampling and Cardinality Control|Telemetry Sampling and Cardinality Control]]. **Condition:** When recording every span for every request would exceed storage or processing budgets.

- Attributes a slow request's time to the spans behind [[02 Concepts/Lifecycle/Deployment & Serving/Tail Latency|Tail Latency]]. **Condition:** Request-scoped tracing enabled across every hop on the path, with sampling that keeps slow requests.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: request tracing; spans.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
