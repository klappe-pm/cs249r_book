---
title: Network Propagation Delay
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Network_Fabrics
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Network propagation delay
taxonomy_id: mlsys.network-propagation-delay
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Network Propagation Delay

The minimum latency set by the distance a signal travels through the medium, which sets a floor under round-trip time between regions regardless of bandwidth.

## Browsing Home

[[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Network Fabrics Subject|Network Fabrics]] → [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Infrastructure & Fleet Index|Datacenter Infrastructure & Fleet]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Sets a floor under [[02 Concepts/Lifecycle/Deployment & Serving/Tail Latency|Tail Latency]]. **Condition:** Requests cross regions or continents.

- Contributes to the latency term of [[02 Concepts/Stack/Parallelism & Distributed Execution/Alpha Beta Communication Model|Alpha Beta Communication Model]]. **Condition:** Messages travel long physical distances.

- Sets the round-trip floor of [[02 Concepts/Foundations/Quantitative System Models/Bandwidth Delay Product|Bandwidth Delay Product]]. **Condition:** For a single path; queueing and processing delay add to the round-trip time.

- Sets a lower bound on each synchronous exchange of [[02 Concepts/Stack/Parallelism & Distributed Execution/Geo Distributed Training|Geo Distributed Training]]. **Condition:** When sites are hundreds of kilometers apart, so the round trip bounds every cross-site exchange regardless of bandwidth.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: speed-of-light latency.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
