---
title: Elastic Training
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Cluster_Scheduling_Orchestration
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Elastic training
taxonomy_id: mlsys.elastic-training
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Elastic Training

Training that continues while the number of workers changes, resharding state and adjusting batch size or learning rate as resources join or leave.

## Browsing Home

[[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Cluster Scheduling & Orchestration Subject|Cluster Scheduling & Orchestration]] → [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Infrastructure & Fleet Index|Datacenter Infrastructure & Fleet]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Reduces lost work from [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Job Preemption|Job Preemption]]. **Condition:** The job can reshard state and continue with fewer workers.

- Resumes from [[02 Concepts/Qualities/Reliability & Fault Tolerance/Recovery Checkpoint|Recovery Checkpoint]]. **Condition:** When the job restarts on a changed worker set and state must be resharded from the latest consistent checkpoint.

- Can raise [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Training Goodput|Training Goodput]]. **Condition:** When replacing failed nodes takes longer than continuing at reduced width and the optimizer tolerates the batch-size change.

- Requires [[02 Concepts/Qualities/Reliability & Fault Tolerance/Checkpoint Resharding|Checkpoint Resharding]]. **Condition:** Holds whenever a restart changes world size or parallel layout relative to the saved checkpoint.

- Makes usable [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Spot and Preemptible Capacity|Spot and Preemptible Capacity]]. **Condition:** Training continues while preempted workers leave and replacements join.

- Re-runs [[02 Concepts/Stack/Parallelism & Distributed Execution/Distributed Job Launch and Process Groups|Distributed Job Launch and Process Groups]]. **Condition:** Workers join or leave and groups are rebuilt.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
