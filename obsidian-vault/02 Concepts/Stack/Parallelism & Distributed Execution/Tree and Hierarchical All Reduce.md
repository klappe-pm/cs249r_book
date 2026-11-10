---
title: Tree and Hierarchical All Reduce
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Collective_Communication
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Tree and hierarchical all-reduce
taxonomy_id: mlsys.tree-allreduce
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Tree and Hierarchical All Reduce

All-reduce schedules over trees or hierarchical groups, with latency logarithmic in participants, suited to small messages and multi-level networks.

## Browsing Home

[[02 Concepts/Stack/Parallelism & Distributed Execution/Collective Communication Subject|Collective Communication]] → [[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism & Distributed Execution Index|Parallelism & Distributed Execution]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is an alternative to [[02 Concepts/Stack/Parallelism & Distributed Execution/Ring All Reduce|Ring All Reduce]]. **Condition:** Messages are small or participants many, so latency terms dominate.

- Is an algorithm for [[02 Concepts/Stack/Parallelism & Distributed Execution/Collective Communication|Collective Communication]]. **Condition:** Participants are arranged in trees or hierarchical groups.

- Is an algorithm for [[02 Concepts/Stack/Parallelism & Distributed Execution/All Reduce|All Reduce]]. **Condition:** When participants are arranged in trees or hierarchical groups so latency grows logarithmically.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
