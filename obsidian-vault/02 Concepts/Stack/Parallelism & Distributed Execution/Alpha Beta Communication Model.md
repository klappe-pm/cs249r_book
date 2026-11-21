---
title: Alpha Beta Communication Model
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Collective_Communication
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Alpha-beta communication model
taxonomy_id: mlsys.alpha-beta-model
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Alpha Beta Communication Model

A cost model estimating message time as a fixed latency term plus message size times a per-byte cost, used to compare collective algorithms.

## Browsing Home

[[02 Concepts/Stack/Parallelism & Distributed Execution/Collective Communication Subject|Collective Communication]] → [[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism & Distributed Execution Index|Parallelism & Distributed Execution]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume II - Scaling/01 The Fleet/03 Network Fabrics/V2-03.05 Level 2 Transport and the Performance Model#^sec-network-fabrics-performance-model|V2-03.05 Level 2 Transport and the Performance Model]] — Message startup latency. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/03_network_fabrics/03_network_fabrics.qmd#L750).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Predicts the cost of [[02 Concepts/Stack/Parallelism & Distributed Execution/Ring All Reduce|Ring All Reduce]]. **Condition:** Link latency and bandwidth are roughly uniform and contention is ignored.

- Predicts the cost of [[02 Concepts/Stack/Parallelism & Distributed Execution/Tree and Hierarchical All Reduce|Tree and Hierarchical All Reduce]]. **Condition:** Link latency and bandwidth are roughly uniform and contention is ignored.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: latency-bandwidth model; network transfer time; transfer time.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
