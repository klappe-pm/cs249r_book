---
title: In Network Reduction
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Network_Fabrics
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: In-network reduction
taxonomy_id: mlsys.in-network-reduction
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# In Network Reduction

Performing collective reductions inside network switches so data crosses each link fewer times, lowering all-reduce traffic and latency.

## Browsing Home

[[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Network Fabrics Subject|Network Fabrics]] → [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Infrastructure & Fleet Index|Datacenter Infrastructure & Fleet]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Offloads reduction steps of [[02 Concepts/Stack/Parallelism & Distributed Execution/Tree and Hierarchical All Reduce|Tree and Hierarchical All Reduce]]. **Condition:** Switches support aggregation for the data types and operations used.

- Reduces link traffic and latency of [[02 Concepts/Stack/Parallelism & Distributed Execution/Collective Communication|Collective Communication]]. **Condition:** Switches support aggregation for the data types and reduction operations used.

- Is an alternative to [[02 Concepts/Stack/Parallelism & Distributed Execution/Ring All Reduce|Ring All Reduce]]. **Condition:** Both perform all-reduce; switch aggregation shortens paths while rings need only end-host support.

- Performs inside switches the reduction steps of [[02 Concepts/Stack/Parallelism & Distributed Execution/All Reduce|All Reduce]]. **Condition:** When switches support aggregation for the data type and reduction operation used and also distribute the reduced result to every participant.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: SHARP.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
