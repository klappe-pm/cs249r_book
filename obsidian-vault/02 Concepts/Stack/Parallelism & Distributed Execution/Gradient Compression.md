---
title: Gradient Compression
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Collective_Communication
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Gradient compression
taxonomy_id: mlsys.gradient-compression
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Gradient Compression

Reducing gradient communication through quantization, sparsification, or low-rank approximation, often with error feedback to preserve convergence.

## Browsing Home

[[02 Concepts/Stack/Parallelism & Distributed Execution/Collective Communication Subject|Collective Communication]] → [[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism & Distributed Execution Index|Parallelism & Distributed Execution]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05.10 Gradient Compression Under Bandwidth Scarcity#^sec-communication-collective-operations-collective-operations-gradient-compression-7a5c|V2-05.10 Gradient Compression Under Bandwidth Scarcity]] — Gradient compression. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/05_collective_communication/05_collective_communication.qmd#L3195).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Can reduce [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Time to Train|Time to Train]]. **Condition:** Training is communication-bound and compression preserves convergence at the chosen ratio.

- Can transmit only top-magnitude gradients, using [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Sparsity|Sparsity]]. **Condition:** Residuals are accumulated locally so dropped values are sent later.

- Lowers the bytes per step counted by [[02 Concepts/Foundations/Quantitative System Models/Communication to Computation Ratio|Communication to Computation Ratio]]. **Condition:** When compressed gradients replace full-precision exchange.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
