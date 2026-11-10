---
title: ML Aware Cluster Scheduling
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Cluster_Scheduling_Orchestration
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: ML-aware cluster scheduling
taxonomy_id: mlsys.ml-aware-scheduling
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# ML Aware Cluster Scheduling

Allocating cluster accelerators using ML job properties, such as scaling curves, iteration time, and parallelism choice, to optimize objectives like job completion time or goodput.

## Browsing Home

[[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Cluster Scheduling & Orchestration Subject|Cluster Scheduling & Orchestration]] → [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Infrastructure & Fleet Index|Datacenter Infrastructure & Fleet]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Resizes jobs through [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Elastic Training|Elastic Training]]. **Condition:** Jobs tolerate changes in worker count.

- Co-allocates workers with [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Gang Scheduling|Gang Scheduling]]. **Condition:** Distributed jobs need all workers simultaneously.

- Raises cluster-wide [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Training Goodput|Training Goodput]]. **Condition:** Jobs' scaling behavior is measured or predicted.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: deep-learning cluster scheduling; goodput-aware scheduling.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
