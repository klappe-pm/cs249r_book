---
title: Topology Aware Placement
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Cluster_Scheduling_Orchestration
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Topology-aware placement
taxonomy_id: mlsys.topology-aware-placement
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Topology Aware Placement

Assigning a job's workers to devices and nodes so that heavily communicating groups share fast links or switches.

## Browsing Home

[[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Cluster Scheduling & Orchestration Subject|Cluster Scheduling & Orchestration]] → [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Infrastructure & Fleet Index|Datacenter Infrastructure & Fleet]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08.07 Topology-Aware Scheduling#^sec-fleet-orchestration-topology-aware|V2-08.07 Topology-Aware Scheduling]] — Topology-aware placement. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/08_fleet_orchestration/08_fleet_orchestration.qmd#L1026).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Reduces the cost of [[02 Concepts/Stack/Parallelism & Distributed Execution/Collective Communication|Collective Communication]]. **Condition:** Communicating workers are placed on shared fast links or switches.

- Refines [[02 Concepts/Foundations/Workloads & Requirements/Execution Placement|Execution Placement]]. **Condition:** Placement decisions are made at node and device granularity.

- Places communicating workers according to [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Network Topology|Network Topology]]. **Condition:** When the scheduler holds a map of links, switches, and scale-up domains and the job declares which workers communicate most.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
