---
title: Graph Neural Network
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Model_Families
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Graph neural network
taxonomy_id: mlsys.graph-neural-network
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Graph Neural Network

Neural network that computes node, edge, or graph representations by repeatedly aggregating features from each node's neighbors along graph edges.

## Browsing Home

[[02 Concepts/Foundations/Models & Architectures/Model Families Subject|Model Families]] → [[02 Concepts/Foundations/Models & Architectures/Models & Architectures Index|Models & Architectures]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is a graph-structured form of [[02 Concepts/Foundations/Models & Architectures/Neural Networks|Neural Networks]]. **Condition:** Computation follows the input graph's edges.

- Aggregates neighbor features with [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Sparse Tensor Kernels|Sparse Tensor Kernels]]. **Condition:** Graph adjacency is stored sparsely.

- Trains on large graphs with [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Neighbor Sampling|Neighbor Sampling]]. **Condition:** Full multi-hop neighborhoods exceed device memory.

- Scales training across workers with [[02 Concepts/Stack/Parallelism & Distributed Execution/Graph Partitioning for GNN Training|Graph Partitioning for GNN Training]]. **Condition:** The graph and its features exceed one device or machine.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: GNN; message-passing neural network.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
