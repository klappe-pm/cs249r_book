---
title: Collective Algorithm Selection
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Collective_Communication
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Collective algorithm selection
taxonomy_id: mlsys.collective-algorithm-selection
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Collective Algorithm Selection

Choosing, per call, among collective algorithms (ring, tree, switch-offloaded) and wire protocols by message size, participant count, and link hierarchy, to minimize latency for small messages and maximize bandwidth for large ones.

## Browsing Home

[[02 Concepts/Stack/Parallelism & Distributed Execution/Collective Communication Subject|Collective Communication]] → [[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism & Distributed Execution Index|Parallelism & Distributed Execution]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Chooses the crossover message size between latency- and bandwidth-optimal schedules using [[02 Concepts/Stack/Parallelism & Distributed Execution/Alpha Beta Communication Model|Alpha Beta Communication Model]]. **Condition:** When tuning collective execution across intra-node and inter-node links.

- Selects, for large messages, [[02 Concepts/Stack/Parallelism & Distributed Execution/Ring All Reduce|Ring All Reduce]]. **Condition:** When message size is large relative to participant count.

- Selects, for small messages or many participants, [[02 Concepts/Stack/Parallelism & Distributed Execution/Tree and Hierarchical All Reduce|Tree and Hierarchical All Reduce]]. **Condition:** When per-step latency dominates transfer time.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: collective protocol selection; ring versus tree crossover.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
