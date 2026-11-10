---
title: Collective Communication
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Collective_Communication
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Collective communication
taxonomy_id: mlsys.collectives
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Collective Communication

Coordinated data exchange and reduction across a process group.

## Browsing Home

[[02 Concepts/Stack/Parallelism & Distributed Execution/Collective Communication Subject|Collective Communication]] → [[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism & Distributed Execution Index|Parallelism & Distributed Execution]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05.05 Collective Operation Primitives#^sec-collective-communication-six-core-primitives-8a66|V2-05.05 Collective Operation Primitives]] — AllReduce. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/05_collective_communication/05_collective_communication.qmd#L826).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Can reduce [[02 Concepts/Foundations/Quantitative System Models/Parallel Scaling Efficiency|Parallel Scaling Efficiency]]. **Condition:** Communication time is exposed rather than overlapped with computation.

- Idles every accelerator in lockstep during exposed, producing [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Synchronous Training Power Swings|Synchronous Training Power Swings]]. **Condition:** When collectives are synchronous and not overlapped, so the whole cluster alternates between full-power compute and low-power waiting at the same moments.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
