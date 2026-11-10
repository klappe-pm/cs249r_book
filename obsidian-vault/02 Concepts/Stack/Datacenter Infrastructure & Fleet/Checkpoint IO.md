---
title: Checkpoint IO
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Storage_Data_Delivery
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Checkpoint I/O
taxonomy_id: mlsys.checkpoint-io
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Checkpoint IO

Writing and reading large training-state snapshots, where storage bandwidth, asynchronous persistence, and sharded layout determine checkpoint cost.

## Browsing Home

[[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Storage & Data Delivery Subject|Storage & Data Delivery]] → [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Infrastructure & Fleet Index|Datacenter Infrastructure & Fleet]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Sets the cost of taking [[02 Concepts/Qualities/Reliability & Fault Tolerance/Recovery Checkpoint|Recovery Checkpoint]]. **Condition:** Training state is large relative to available storage bandwidth.

- Commonly writes to a [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Parallel File System|Parallel File System]]. **Condition:** Sharded checkpoints are written concurrently by many ranks.

- Sets the write-cost input to [[02 Concepts/Qualities/Reliability & Fault Tolerance/Optimal Checkpoint Interval|Optimal Checkpoint Interval]]. **Condition:** The optimal interval scales with the square root of checkpoint cost times MTBF.

- Stages snapshots on a fast local tier before draining them through [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Storage Tiering and Caching|Storage Tiering and Caching]]. **Condition:** The local tier must hold several snapshots and drain faster than the checkpoint interval.

## Themes

- [[03 Themes/Reliability and Recovery|Reliability and Recovery]]

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
