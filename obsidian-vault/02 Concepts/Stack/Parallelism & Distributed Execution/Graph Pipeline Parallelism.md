---
title: Graph Pipeline Parallelism
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Parallelism_Strategies
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Graph pipeline parallelism
taxonomy_id: mlsys.graph-pipeline-parallelism
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Graph Pipeline Parallelism

Pipeline parallelism that partitions a model whose layers form a branching graph into stages that follow the graph, so independent branches, such as separate modality encoders, run concurrently in parallel stages instead of being serialized into one chain.

## Browsing Home

[[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism Strategies Subject|Parallelism Strategies]] → [[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism & Distributed Execution Index|Parallelism & Distributed Execution]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is the branching-graph form of [[02 Concepts/Stack/Parallelism & Distributed Execution/Pipeline Parallelism|Pipeline Parallelism]]. **Condition:** When the model's layer graph has branches with no data dependence between them.

- Shortens the pipeline's critical path, shrinking the fill and drain time of [[02 Concepts/Stack/Parallelism & Distributed Execution/Pipeline Bubble|Pipeline Bubble]]. **Condition:** Relative to a linearized schedule on the same devices and microbatch count, when the branches are balanced closely enough that parallel stages finish at similar times.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: branch-parallel pipelining; multi-branch pipeline scheduling.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
