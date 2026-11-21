---
title: Leader Election
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Coordination_Consensus
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Leader election
taxonomy_id: mlsys.leader-election
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Leader Election

Selecting a single coordinator among replicas, typically through consensus and leases, so control decisions have one authoritative source.

## Browsing Home

[[02 Concepts/Stack/Parallelism & Distributed Execution/Coordination & Consensus Subject|Coordination & Consensus]] → [[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism & Distributed Execution Index|Parallelism & Distributed Execution]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Commonly relies on [[02 Concepts/Stack/Parallelism & Distributed Execution/Replicated Log Consensus|Replicated Log Consensus]]. **Condition:** Replicas must agree on a single leader under partial failure.

- Holds leadership through a [[02 Concepts/Stack/Parallelism & Distributed Execution/Lease|Lease]]. **Condition:** The leader renews a time-bounded grant so a failed leader's authority lapses.

- Requires [[02 Concepts/Stack/Parallelism & Distributed Execution/Fencing|Fencing]]. **Condition:** A deposed leader may still act; resources must reject its stale epoch.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
