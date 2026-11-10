---
title: Inter Token Latency
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Latency_Throughput_Goodput
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Inter-token latency
taxonomy_id: mlsys.inter-token-latency
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Inter Token Latency

The time between consecutive output tokens or chunks delivered to a streaming client, whose distribution, not only its mean, exposes decode stalls that an average time per output token hides.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Latency, Throughput & Goodput Subject|Latency, Throughput & Goodput]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Measures gaps in incremental output delivery [[02 Concepts/Lifecycle/Deployment & Serving/Token Streaming|Token Streaming]]. **Condition:** When timestamps and the number of tokens carried by each streamed output are recorded.

- Decides whether streamed requests count toward [[02 Concepts/Lifecycle/Deployment & Serving/SLO Goodput|SLO Goodput]]. **Condition:** When the service objective bounds per-gap latency, with workload and other acceptance criteria fixed.

- Gives the per-gap distribution whose request average is [[02 Concepts/Lifecycle/Deployment & Serving/Time per Output Token|Time per Output Token]]. **Condition:** When streamed outputs are timestamped individually rather than only at request end.

## Themes

- [[03 Themes/Latency and Throughput|Latency and Throughput]]

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: ITL.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
