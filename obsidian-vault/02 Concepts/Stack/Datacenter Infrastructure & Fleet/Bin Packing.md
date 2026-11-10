---
title: Bin Packing
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Cluster_Scheduling_Orchestration
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Bin packing
taxonomy_id: mlsys.bin-packing
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Bin Packing

Placing jobs onto nodes to minimize fragmentation of resources such as accelerators, trading packing density against interference and locality.

## Browsing Home

[[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Cluster Scheduling & Orchestration Subject|Cluster Scheduling & Orchestration]] → [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Infrastructure & Fleet Index|Datacenter Infrastructure & Fleet]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Trades off against [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Topology Aware Placement|Topology Aware Placement]]. **Condition:** Dense packing fragments the contiguous allocations that locality requires.

- Raises [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Resource Utilization|Resource Utilization]]. **Condition:** Jobs can share nodes without violating resource or isolation constraints.

- Can increase [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Performance Interference|Performance Interference]]. **Condition:** Dense co-location puts jobs on shared caches, memory bandwidth, and links.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
