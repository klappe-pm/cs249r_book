---
title: Consistency Availability Trade Off
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Coordination_Consensus
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Consistency-availability trade-off
taxonomy_id: mlsys.cap-tradeoff
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Consistency Availability Trade Off

Under a network partition, a replicated system must choose between answering with possibly stale state and refusing requests until replicas agree.

## Browsing Home

[[02 Concepts/Stack/Parallelism & Distributed Execution/Coordination & Consensus Subject|Coordination & Consensus]] → [[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism & Distributed Execution Index|Parallelism & Distributed Execution]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Forces a minority partition to stop answering in [[02 Concepts/Stack/Parallelism & Distributed Execution/Replicated Log Consensus|Replicated Log Consensus]]. **Condition:** A partition separates replicas.

- Decides whether stale values are served for [[02 Concepts/Lifecycle/Data Engineering/Feature Freshness|Feature Freshness]]. **Condition:** Feature or model replicas span regions that can partition.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: CAP theorem; partition tolerance.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
