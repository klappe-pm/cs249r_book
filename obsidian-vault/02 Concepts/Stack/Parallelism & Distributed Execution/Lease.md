---
title: Lease
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Coordination_Consensus
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Lease
taxonomy_id: mlsys.lease
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Lease

A time-bounded grant of authority or cached state that expires unless renewed, letting a system recover from failed holders without explicit release.

## Browsing Home

[[02 Concepts/Stack/Parallelism & Distributed Execution/Coordination & Consensus Subject|Coordination & Consensus]] → [[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism & Distributed Execution Index|Parallelism & Distributed Execution]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/04 The Nervous System/V4-04.05 Chunk Lease Sizing from the Stopping Budget#^sec-nervous-lease-sizing|V4-04.05 Chunk Lease Sizing from the Stopping Budget]] — Chunk lease. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/04_nervous/04_nervous.qmd#L985).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Needs epoch fencing to be safe, as in [[02 Concepts/Stack/Parallelism & Distributed Execution/Fencing|Fencing]]. **Condition:** Clocks are bounded in drift so expired holders can be rejected safely.

- Enables timed [[02 Concepts/Qualities/Reliability & Fault Tolerance/Replication and Failover|Replication and Failover]]. **Condition:** A standby can take over once the failed holder's lease has expired.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
