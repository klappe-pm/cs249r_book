---
title: Neighbor Sampling
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Data_Loading_Input_Pipelines
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Neighbor sampling
taxonomy_id: mlsys.neighbor-sampling
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Neighbor Sampling

Building GNN mini-batches from sampled subsets of each node's multi-hop neighborhood, bounding the exponential neighbor growth that makes full-neighborhood computation exceed memory.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Data Loading & Input Pipelines Subject|Data Loading & Input Pipelines]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Bounds the per-batch [[02 Concepts/Foundations/Workloads & Requirements/Memory Footprint|Memory Footprint]]. **Condition:** Fanout per hop is capped.

- Adds sampling variance to gradient estimates and thus [[02 Concepts/Lifecycle/Model Evaluation & Testing/Statistical Uncertainty|Statistical Uncertainty]]. **Condition:** Sampled neighborhoods approximate full aggregation.

- Draws mini-batches across [[02 Concepts/Stack/Parallelism & Distributed Execution/Graph Partitioning for GNN Training|Graph Partitioning for GNN Training]]. **Condition:** Distributed training samples neighborhoods that span partitions.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: graph sampling; mini-batch graph sampling.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
