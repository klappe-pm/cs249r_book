---
title: Gang Scheduling
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Cluster_Scheduling_Orchestration
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Gang scheduling
taxonomy_id: mlsys.gang-scheduling
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Gang Scheduling

Allocating all resources a parallel job needs at once, or none, so tightly coupled workers start together and partial allocations cannot deadlock.

## Browsing Home

[[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Cluster Scheduling & Orchestration Subject|Cluster Scheduling & Orchestration]] → [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Infrastructure & Fleet Index|Datacenter Infrastructure & Fleet]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08.05 Core Allocation Constraints#^sec-fleet-orchestration-gang-scheduling|V2-08.05 Core Allocation Constraints]] — Gang scheduling. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/08_fleet_orchestration/08_fleet_orchestration.qmd#L712).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Can reduce cluster [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Resource Utilization|Resource Utilization]]. **Condition:** Resources sit idle while waiting for a full allocation, unless backfilled.

- Can increase job [[02 Concepts/Foundations/Quantitative System Models/Queueing Delay|Queueing Delay]]. **Condition:** Large jobs wait until enough resources are free at once.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
