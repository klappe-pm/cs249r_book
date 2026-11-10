---
title: Reduce Scatter and All Gather
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Collective_Communication
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Reduce-scatter and all-gather
taxonomy_id: mlsys.reduce-scatter-all-gather
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Reduce Scatter and All Gather

The complementary collectives in which each participant receives one reduced shard of the group's tensors (reduce-scatter) or the concatenation of every participant's shard (all-gather), the pair that moves sharded parameters and gradients in fully sharded training and composes into a bandwidth-optimal all-reduce.

## Browsing Home

[[02 Concepts/Stack/Parallelism & Distributed Execution/Collective Communication Subject|Collective Communication]] → [[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism & Distributed Execution Index|Parallelism & Distributed Execution]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Are kinds of [[02 Concepts/Stack/Parallelism & Distributed Execution/Collective Communication|Collective Communication]]. **Condition:** When each participant holds or receives a distinct shard rather than the whole tensor.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: ReduceScatter; AllGather; reduce-scatter; all-gather.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
