---
title: Backfill Scheduling
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Cluster_Scheduling_Orchestration
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Backfill scheduling
taxonomy_id: mlsys.backfill-scheduling
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Backfill Scheduling

Running lower-priority jobs in idle resource-time gaps without delaying the reserved start of a higher-priority job, which raises cluster utilization.

## Browsing Home

[[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Cluster Scheduling & Orchestration Subject|Cluster Scheduling & Orchestration]] → [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Infrastructure & Fleet Index|Datacenter Infrastructure & Fleet]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Fills idle resources to raise [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Resource Utilization|Resource Utilization]]. **Condition:** When job runtime estimates are accurate enough that backfilled jobs finish before the reserved start.

- Shortens the wait of small jobs in [[02 Concepts/Foundations/Quantitative System Models/Queueing Delay|Queueing Delay]]. **Condition:** When small jobs fit into gaps ahead of a large gang job's reserved start and their runtime estimates are accurate.

- Uses whole-job allocation reservations established by [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Gang Scheduling|Gang Scheduling]]. **Condition:** When the backfill planner consults reserved start times and resource sets for gang-allocated jobs and admits other jobs only when their bounded resource use preserves those starts.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: backfilling; EASY backfilling.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
