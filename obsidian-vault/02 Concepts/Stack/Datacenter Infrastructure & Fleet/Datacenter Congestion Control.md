---
title: Datacenter Congestion Control
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Network_Fabrics
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Datacenter congestion control
taxonomy_id: mlsys.congestion-control
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Datacenter Congestion Control

End-host and switch mechanisms, such as ECN-driven rate control, that limit queue buildup from incast and synchronized collective traffic.

## Browsing Home

[[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Network Fabrics Subject|Network Fabrics]] → [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Infrastructure & Fleet Index|Datacenter Infrastructure & Fleet]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume II - Scaling/01 The Fleet/03 Network Fabrics/V2-03.07 Level 4 Fabric Behavior, Congestion, and Routing#^sec-network-fabrics-behavior|V2-03.07 Level 4 Fabric Behavior, Congestion, and Routing]] — Network congestion. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/03_network_fabrics/03_network_fabrics.qmd#L2001).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Can reduce network-induced [[02 Concepts/Stack/Parallelism & Distributed Execution/Stragglers|Stragglers]]. **Condition:** Synchronized collective traffic or incast creates switch queue buildup.

- Mitigates network [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Performance Interference|Performance Interference]]. **Condition:** Jobs share switch queues on a common fabric.

- Throttles senders during [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Incast Congestion|Incast Congestion]]. **Condition:** Senders react to congestion signals before buffers overflow.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: DCQCN.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
