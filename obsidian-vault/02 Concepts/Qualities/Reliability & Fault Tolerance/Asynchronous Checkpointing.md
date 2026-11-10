---
title: Asynchronous Checkpointing
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Checkpointing_Elastic_Recovery
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Asynchronous checkpointing
taxonomy_id: mlsys.async-checkpointing
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Asynchronous Checkpointing

Snapshotting training state quickly to host memory and persisting it in the background so computation resumes before the durable write completes.

## Browsing Home

[[02 Concepts/Qualities/Reliability & Fault Tolerance/Checkpointing & Elastic Recovery Subject|Checkpointing & Elastic Recovery]] → [[02 Concepts/Qualities/Reliability & Fault Tolerance/Reliability & Fault Tolerance Index|Reliability & Fault Tolerance]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Shortens [[02 Concepts/Qualities/Reliability & Fault Tolerance/Optimal Checkpoint Interval|Optimal Checkpoint Interval]]. **Condition:** When the blocking snapshot to host memory costs much less than the durable write, lowering the effective checkpoint cost.

- Hides the training stall from [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Checkpoint IO|Checkpoint IO]]. **Condition:** A fast snapshot to host memory lets persistence proceed in the background.

- Requires [[02 Concepts/Qualities/Reliability & Fault Tolerance/Consistent Checkpoint Cut|Consistent Checkpoint Cut]]. **Condition:** When every rank snapshots its shard at the same step boundary before background persistence begins.

- Increases [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Training Goodput|Training Goodput]]. **Condition:** When the blocking snapshot is much cheaper than the durable write, so training stalls less per checkpoint.

## Themes

- [[03 Themes/Reliability and Recovery|Reliability and Recovery]]

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
