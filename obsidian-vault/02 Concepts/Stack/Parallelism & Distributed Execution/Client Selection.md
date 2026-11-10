---
title: Client Selection
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Federated_Decentralized_Learning
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Client selection
taxonomy_id: mlsys.client-sampling
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Client Selection

Choosing which available devices participate in each federated round, subject to availability, connectivity, and power constraints.

## Browsing Home

[[02 Concepts/Stack/Parallelism & Distributed Execution/Federated & Decentralized Learning Subject|Federated & Decentralized Learning]] → [[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism & Distributed Execution Index|Parallelism & Distributed Execution]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume II - Scaling/03 The Fleet in Production/11 Edge Intelligence/V2-11.08 Federated Learning Systems at Scale#^sec-edge-intelligence-client-scheduling-f675|V2-11.08 Federated Learning Systems at Scale]] — Client participation. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/11_edge_intelligence/11_edge_intelligence.qmd#L2095).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Sets which clients' distributions enter each round, shaping the effective [[02 Concepts/Stack/Parallelism & Distributed Execution/Statistical Heterogeneity|Statistical Heterogeneity]]. **Condition:** When participation correlates with client characteristics such as connectivity, device class, or time zone.

- Is the per-round selection step of [[02 Concepts/Stack/Parallelism & Distributed Execution/Federated Averaging|Federated Averaging]]. **Condition:** Each round samples a subset of available clients.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
