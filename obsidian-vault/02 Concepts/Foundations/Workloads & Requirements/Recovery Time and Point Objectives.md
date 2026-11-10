---
title: Recovery Time and Point Objectives
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Requirements_SLOs_Baselines
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Recovery time and point objectives
taxonomy_id: mlsys.recovery-objectives
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Recovery Time and Point Objectives

Stated limits on how long restoring service may take (RTO) and how far recovered state may lag the state before the failure (RPO), which constrain checkpointing, replication, and failover design.

## Browsing Home

[[02 Concepts/Foundations/Workloads & Requirements/Requirements, SLOs & Baselines Subject|Requirements, SLOs & Baselines]] → [[02 Concepts/Foundations/Workloads & Requirements/Workloads & Requirements Index|Workloads & Requirements]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Caps the longest acceptable [[02 Concepts/Qualities/Reliability & Fault Tolerance/Optimal Checkpoint Interval|Optimal Checkpoint Interval]]. **Condition:** When recovery restarts from the last checkpoint and the RPO is shorter than the interval that failure rate and write cost would otherwise favor.

- Sets the recovery speed required of [[02 Concepts/Qualities/Reliability & Fault Tolerance/Replication and Failover|Replication and Failover]]. **Condition:** When the RTO is shorter than the time to restore from a checkpoint, so a standby must take over.

## Themes

- [[03 Themes/Reliability and Recovery|Reliability and Recovery]]

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: RTO; RPO; recovery time objective; recovery point objective; recovery time accounting.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
