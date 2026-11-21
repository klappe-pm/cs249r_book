---
title: Incast Congestion
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Network_Fabrics
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Incast congestion
taxonomy_id: mlsys.incast
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Incast Congestion

Congestion that occurs when many senders transmit to one receiver at once, overflowing its switch port buffer and causing queueing, drops, or pause propagation.

## Browsing Home

[[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Network Fabrics Subject|Network Fabrics]] → [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Infrastructure & Fleet Index|Datacenter Infrastructure & Fleet]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Raises [[02 Concepts/Lifecycle/Deployment & Serving/Tail Latency|Tail Latency]]. **Condition:** Buffers fill and packets queue or drop.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: incast; many-to-one congestion.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
