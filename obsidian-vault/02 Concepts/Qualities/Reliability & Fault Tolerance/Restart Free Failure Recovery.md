---
title: Restart Free Failure Recovery
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Checkpointing_Elastic_Recovery
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Restart-free failure recovery
taxonomy_id: mlsys.restart-free-recovery
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Restart Free Failure Recovery

Reconfiguring distributed training around surviving replicas of model and optimizer state so that the job resumes after supported worker failures without a full-job restart or durable-checkpoint reload, reducing recovery delay at the cost of redundancy and reconfiguration.

## Browsing Home

[[02 Concepts/Qualities/Reliability & Fault Tolerance/Checkpointing & Elastic Recovery Subject|Checkpointing & Elastic Recovery]] → [[02 Concepts/Qualities/Reliability & Fault Tolerance/Reliability & Fault Tolerance Index|Reliability & Fault Tolerance]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Raises, by avoiding full-job restart and reducing recovery losses, the [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Training Goodput|Training Goodput]]. **Condition:** When, under the same accelerator-time accounting, saved restart and rollback losses exceed replication, redundant-computation, reconfiguration, and reserved-capacity costs for failures within the supported failure model.

- Replicates or re-partitions the stages of [[02 Concepts/Stack/Parallelism & Distributed Execution/Pipeline Parallelism|Pipeline Parallelism]]. **Condition:** For pipeline-parallel jobs, where a failed stage's work can be absorbed by redundant stages or by re-partitioning survivors.

## Themes

- [[03 Themes/Reliability and Recovery|Reliability and Recovery]]

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: recovery without restart.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
