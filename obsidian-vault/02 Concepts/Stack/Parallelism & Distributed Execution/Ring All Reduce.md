---
title: Ring All Reduce
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Collective_Communication
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Ring all-reduce
taxonomy_id: mlsys.ring-allreduce
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Ring All Reduce

An all-reduce performed as reduce-scatter then all-gather around a ring, bandwidth-optimal for large messages but with latency linear in participants.

## Browsing Home

[[02 Concepts/Stack/Parallelism & Distributed Execution/Collective Communication Subject|Collective Communication]] → [[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism & Distributed Execution Index|Parallelism & Distributed Execution]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is an algorithm for [[02 Concepts/Stack/Parallelism & Distributed Execution/Collective Communication|Collective Communication]]. **Condition:** Participants can be arranged in a ring with comparable link bandwidth.

- Is an algorithm for [[02 Concepts/Stack/Parallelism & Distributed Execution/All Reduce|All Reduce]]. **Condition:** When participants can be arranged in a ring with comparable link bandwidth.

- Is composed of [[02 Concepts/Stack/Parallelism & Distributed Execution/Reduce Scatter and All Gather|Reduce Scatter and All Gather]]. **Condition:** When all-reduce is decomposed into a reduce-scatter followed by an all-gather around the ring.

- Runs at full link bandwidth on the rings of [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Torus Topology|Torus Topology]]. **Condition:** When each ring of the collective maps onto one torus dimension so every step uses a direct link.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
