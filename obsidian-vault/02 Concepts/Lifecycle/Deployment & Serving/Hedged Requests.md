---
title: Hedged Requests
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Latency_Throughput_Goodput
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Hedged requests
taxonomy_id: mlsys.hedged-requests
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Hedged Requests

Issuing a duplicate request to another replica when the first has not responded within a delay, and using whichever returns first.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Latency, Throughput & Goodput Subject|Latency, Throughput & Goodput]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Reduces [[02 Concepts/Lifecycle/Deployment & Serving/Tail Latency|Tail Latency]]. **Condition:** Holds when slow responses come from replica-specific variability and the extra load from duplicates is small.

- Adds duplicate load to [[02 Concepts/Foundations/Quantitative System Models/Arrival Rate|Arrival Rate]]. **Condition:** Extra load stays small when hedges fire only after a high-percentile delay.

- Mitigates [[02 Concepts/Stack/Parallelism & Distributed Execution/Stragglers|Stragglers]]. **Condition:** Holds when slowness is replica-specific rather than shared.

- Cuts the slow-subrequest tail behind [[02 Concepts/Lifecycle/Deployment & Serving/Fan Out Tail Amplification|Fan Out Tail Amplification]]. **Condition:** When alternate replicas have independent delays, spare capacity exists, and redundant work is cancelled.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
