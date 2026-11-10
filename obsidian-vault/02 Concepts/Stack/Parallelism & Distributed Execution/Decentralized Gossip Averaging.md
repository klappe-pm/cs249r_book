---
title: Decentralized Gossip Averaging
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Federated_Decentralized_Learning
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Decentralized gossip averaging
taxonomy_id: mlsys.gossip-averaging
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Decentralized Gossip Averaging

Training in which each worker averages its model with a few neighbors instead of a central server or global all-reduce, so updates diffuse through the communication graph.

## Browsing Home

[[02 Concepts/Stack/Parallelism & Distributed Execution/Federated & Decentralized Learning Subject|Federated & Decentralized Learning]] → [[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism & Distributed Execution Index|Parallelism & Distributed Execution]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Coordinates, without a central server, [[02 Concepts/Stack/Parallelism & Distributed Execution/Federated Learning|Federated Learning]]. **Condition:** When participants are separately controlled data holders that exchange model updates with peers rather than with a server.

- Replaces global collectives with neighbor exchange [[02 Concepts/Stack/Parallelism & Distributed Execution/Collective Communication|Collective Communication]]. **Condition:** Global synchronization is too slow or unreliable.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: gossip SGD; decentralized SGD.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
