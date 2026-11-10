---
title: Federated Learning
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Federated_Decentralized_Learning
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Federated learning
taxonomy_id: mlsys.federated-learning
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Federated Learning

Coordinating model learning across separately controlled data holders.

## Browsing Home

[[02 Concepts/Stack/Parallelism & Distributed Execution/Federated & Decentralized Learning Subject|Federated & Decentralized Learning]] → [[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism & Distributed Execution Index|Parallelism & Distributed Execution]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume II - Scaling/03 The Fleet in Production/11 Edge Intelligence/V2-11.07 Federated Learning Algorithms#^sec-edge-intelligence-learning-protocols-139a|V2-11.07 Federated Learning Algorithms]] — Federated averaging. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/11_edge_intelligence/11_edge_intelligence.qmd#L1856).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Must address [[02 Concepts/Qualities/Security & Privacy/Privacy Requirements|Privacy Requirements]]. **Condition:** Keeping raw records local alone does not establish privacy of updates or outputs.

- Can use, to hide individual client updates, [[02 Concepts/Qualities/Security & Privacy/Secure Aggregation|Secure Aggregation]]. **Condition:** When enough clients participate per round that the aggregate does not reveal any single client's update.

- Requires [[02 Concepts/Lifecycle/Training & Adaptation/On Device Training|On Device Training]]. **Condition:** Holds for cross-device federation; cross-silo clients train on servers.

- Combines client updates with [[02 Concepts/Qualities/Security & Privacy/Byzantine Robust Aggregation|Byzantine Robust Aggregation]]. **Condition:** Clients are untrusted.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
