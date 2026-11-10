---
title: V2-05 Collective Communication
type: Chapter
volume: 2
chapter: 5
publication_status: Preview
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol2/05_collective_communication/05_collective_communication.qmd
source_anchor: sec-collective-communication
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_2
rendered_source_url: https://mlsysbook.ai/vol2/05_collective_communication/05_collective_communication.html
---

# V2-05 Collective Communication

[[Home|Home]] · [[01 Books/Volume II - Scaling/Volume 2 Overview|Volume Overview]]

^sec-collective-communication

[Lecture slides](https://mlsysbook.ai/slides/vol2.html#ch-05) for this chapter

![[90 Assets/Volume II/05 Collective Communication/Cover Collective Communication Blueprint Labeled 4f7a1433ab.webp]]

*Collective communication topology map where gradient fragments circulate through ring and tree reduction paths before broadcasting synchronized state.*

## Chapter Sections

- [[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05.01 Purpose|V2-05.01 Purpose]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05.02 From Parallelism to Communication Patterns|V2-05.02 From Parallelism to Communication Patterns]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05.03 The Physics of Data Movement|V2-05.03 The Physics of Data Movement]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05.04 Parallelism Strategies and Their Traffic|V2-05.04 Parallelism Strategies and Their Traffic]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05.05 Collective Operation Primitives|V2-05.05 Collective Operation Primitives]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05.06 Pricing Collectives by Rounds and Chunks|V2-05.06 Pricing Collectives by Rounds and Chunks]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05.07 AllReduce Algorithms and Topologies|V2-05.07 AllReduce Algorithms and Topologies]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05.08 Hierarchical Communication|V2-05.08 Hierarchical Communication]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05.09 AllToAll Exchanges at Scale|V2-05.09 AllToAll Exchanges at Scale]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05.10 Gradient Compression Under Bandwidth Scarcity|V2-05.10 Gradient Compression Under Bandwidth Scarcity]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05.11 Communication-Computation Overlap|V2-05.11 Communication-Computation Overlap]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05.12 Communication Libraries and Runtimes|V2-05.12 Communication Libraries and Runtimes]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05.13 Fallacies and Pitfalls|V2-05.13 Fallacies and Pitfalls]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05.14 Summary|V2-05.14 Summary]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05.15 Self-Check Answers|V2-05.15 Self-Check Answers]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05.16 Source References|V2-05.16 Source References]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05.17 Footnotes|V2-05.17 Footnotes]]

Next: [[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05.01 Purpose|V2-05.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/05_collective_communication/05_collective_communication.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol2/05_collective_communication/05_collective_communication.html#sec-collective-communication). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Stack/Parallelism & Distributed Execution/Collective Communication|Collective Communication]]
- [[02 Concepts/Stack/Parallelism & Distributed Execution/Communication Overlap|Communication Overlap]]
- [[02 Concepts/Stack/Parallelism & Distributed Execution/Gradient Compression|Gradient Compression]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume II - Scaling/00 Introduction/01 Introduction/V2-01 Introduction|V2-01 Introduction]] — Fleet Law; Scaling laws as the demand curve; Synchronous tight coupling.
- [[01 Books/Volume II - Scaling/01 The Fleet/02 Compute Infrastructure/V2-02 Compute Infrastructure|V2-02 Compute Infrastructure]] — Bandwidth hierarchy dictates placement.
- [[01 Books/Volume II - Scaling/01 The Fleet/03 Network Fabrics/V2-03 Network Fabrics|V2-03 Network Fabrics]] — Alpha-beta model; RDMA reliable-delivery contract; Bisection bandwidth and topology economics; Traffic-matched topology.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/05_collective_communication/collective_communication_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06 Distributed Training|V2-06 Distributed Training]] — Parallelism plan as joint placement; Sharded data parallelism; Expert parallelism; Pipeline parallelism bubble; Data-parallel update equivalence.
- [[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08 Fleet Orchestration|V2-08 Fleet Orchestration]] — Topology-aware placement.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/09 Fleet Efficiency/V2-09 Fleet Efficiency|V2-09 Fleet Efficiency]] — ML goodput; Fleet profiling by hierarchy and sampling.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/11 Edge Intelligence/V2-11 Edge Intelligence|V2-11 Edge Intelligence]] — Federated uplink budget.
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/15 Sustainable AI/V2-15 Sustainable AI|V2-15 Sustainable AI]] — Energy crossover versus performance ridge.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/05_collective_communication/collective_communication_concepts.yml)

<!-- Semantic Navigation: End -->
