---
title: Federated Averaging
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Federated_Decentralized_Learning
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Federated averaging
taxonomy_id: mlsys.federated-averaging
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Federated Averaging

A federated algorithm in which sampled clients run several local optimization steps and a server averages their model updates, weighted by data size.

## Browsing Home

[[02 Concepts/Stack/Parallelism & Distributed Execution/Federated & Decentralized Learning Subject|Federated & Decentralized Learning]] → [[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism & Distributed Execution Index|Parallelism & Distributed Execution]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume II - Scaling/03 The Fleet in Production/11 Edge Intelligence/V2-11.07 Federated Learning Algorithms#^sec-edge-intelligence-learning-protocols-139a|V2-11.07 Federated Learning Algorithms]] — Federated averaging. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/11_edge_intelligence/11_edge_intelligence.qmd#L1856).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is a baseline algorithm for [[02 Concepts/Stack/Parallelism & Distributed Execution/Federated Learning|Federated Learning]]. **Condition:** Clients can run local optimization steps between communication rounds.

- Can combine updates through [[02 Concepts/Qualities/Security & Privacy/Secure Aggregation|Secure Aggregation]]. **Condition:** The server must not see individual client updates.

- Is a federated instance of [[02 Concepts/Stack/Parallelism & Distributed Execution/Local SGD|Local SGD]]. **Condition:** Clients run several local epochs before averaging.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: FedAvg.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
