---
title: Network Topology
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Network_Fabrics
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Network topology
taxonomy_id: mlsys.network-topology
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Network Topology

The connectivity and capacity structure that constrains communication paths.

## Browsing Home

[[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Network Fabrics Subject|Network Fabrics]] → [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Infrastructure & Fleet Index|Datacenter Infrastructure & Fleet]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume II - Scaling/01 The Fleet/03 Network Fabrics/V2-03.06 Level 3 Switch and Topology#^sec-network-fabrics-topology|V2-03.06 Level 3 Switch and Topology]] — Bisection bandwidth. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/03_network_fabrics/03_network_fabrics.qmd#L1202).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Constrains achievable rates of [[02 Concepts/Stack/Parallelism & Distributed Execution/Collective Communication|Collective Communication]]. **Condition:** Available paths and contention determine achievable exchange rates.

- Shapes the group mapping of [[02 Concepts/Stack/Parallelism & Distributed Execution/Hybrid Parallelism|Hybrid Parallelism]]. **Condition:** Link bandwidth differs between levels of the hardware hierarchy.

- Determines the axis alignment of [[02 Concepts/Stack/Parallelism & Distributed Execution/Device Mesh|Device Mesh]]. **Condition:** The busiest parallel axis is mapped onto the fastest links.

- Helps determine network-related [[02 Concepts/Qualities/Reliability & Fault Tolerance/Failure Domain|Failure Domain]]. **Condition:** Components depend on shared network elements; power, software, and other dependencies may define additional or overlapping failure domains.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
