---
title: Request Throughput
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Latency_Throughput_Goodput
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Request throughput
taxonomy_id: mlsys.request-throughput
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Request Throughput

The number of requests, or tokens, a serving system completes per unit time at a stated load and latency target.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Latency, Throughput & Goodput Subject|Latency, Throughput & Goodput]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is the horizontal axis of [[02 Concepts/Foundations/Quantitative System Models/Latency Throughput Curve|Latency Throughput Curve]]. **Condition:** Latency is measured across offered loads.

- Is an upper bound on [[02 Concepts/Lifecycle/Deployment & Serving/SLO Goodput|SLO Goodput]]. **Condition:** Goodput counts only completed requests that meet their latency targets.

## Themes

- [[03 Themes/Latency and Throughput|Latency and Throughput]]

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: queries per second; QPS; tokens per second.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
