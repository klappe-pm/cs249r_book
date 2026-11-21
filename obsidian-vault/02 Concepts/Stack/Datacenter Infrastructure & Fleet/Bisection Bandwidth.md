---
title: Bisection Bandwidth
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Network_Fabrics
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Bisection bandwidth
taxonomy_id: mlsys.bisection-bandwidth
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Bisection Bandwidth

The minimum total bandwidth across any cut dividing a network into two equal halves, bounding throughput of all-to-all and global exchanges.

## Browsing Home

[[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Network Fabrics Subject|Network Fabrics]] → [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Infrastructure & Fleet Index|Datacenter Infrastructure & Fleet]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume II - Scaling/01 The Fleet/03 Network Fabrics/V2-03.06 Level 3 Switch and Topology#^sec-network-fabrics-topology|V2-03.06 Level 3 Switch and Topology]] — Bisection bandwidth. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/03_network_fabrics/03_network_fabrics.qmd#L1202).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Bounds throughput of [[02 Concepts/Stack/Parallelism & Distributed Execution/All to All Exchange|All to All Exchange]]. **Condition:** Traffic crosses the network bisection rather than staying within local groups.

- Summarizes the capacity of [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Network Topology|Network Topology]]. **Condition:** Traffic is uniform enough that the worst-case cut is relevant.

## Themes

- [[03 Themes/Scaling and Coordination|Scaling and Coordination]]

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
