---
title: V2-06 Distributed Training
type: Chapter
volume: 2
chapter: 6
publication_status: Preview
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol2/06_distributed_training/06_distributed_training.qmd
source_anchor: sec-distributed-training-systems
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_2
rendered_source_url: https://mlsysbook.ai/vol2/06_distributed_training/06_distributed_training.html
---

# V2-06 Distributed Training

[[Home|Home]] · [[01 Books/Volume II - Scaling/Volume 2 Overview|Volume Overview]]

^sec-distributed-training-systems

[Lecture slides](https://mlsysbook.ai/slides/vol2.html#ch-06) for this chapter

![[90 Assets/Volume II/06 Distributed Training/Cover Distributed Training Blueprint Labeled ba11260fe9.webp]]

*Isometric distributed training map showing a large workload partitioned across accelerators along data, tensor, and pipeline axes with synchronization paths.*

## Chapter Sections

- [[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06.01 Purpose|V2-06.01 Purpose]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06.02 Why Distribution Is Necessary|V2-06.02 Why Distribution Is Necessary]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06.03 The Parallelism Design Space|V2-06.03 The Parallelism Design Space]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06.04 Data Parallelism|V2-06.04 Data Parallelism]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06.05 Scaling Efficiency and Convergence|V2-06.05 Scaling Efficiency and Convergence]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06.06 Model Parallelism|V2-06.06 Model Parallelism]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06.07 Hybrid Parallelism|V2-06.07 Hybrid Parallelism]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06.08 Multi-Model Training for Alignment and RLHF|V2-06.08 Multi-Model Training for Alignment and RLHF]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06.09 Parallelism Strategy Comparison|V2-06.09 Parallelism Strategy Comparison]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06.10 Frameworks and Runtime Contracts|V2-06.10 Frameworks and Runtime Contracts]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06.11 Fallacies and Pitfalls|V2-06.11 Fallacies and Pitfalls]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06.12 Summary|V2-06.12 Summary]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06.13 Self-Check Answers|V2-06.13 Self-Check Answers]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06.14 Source References|V2-06.14 Source References]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06.15 Footnotes|V2-06.15 Footnotes]]

Next: [[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06.01 Purpose|V2-06.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/06_distributed_training/06_distributed_training.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol2/06_distributed_training/06_distributed_training.html#sec-distributed-training-systems). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Lifecycle/Training & Adaptation/Critical Batch Size|Critical Batch Size]]
- [[02 Concepts/Stack/Parallelism & Distributed Execution/Data Parallelism|Data Parallelism]]
- [[02 Concepts/Stack/Parallelism & Distributed Execution/Pipeline Bubble|Pipeline Bubble]]
- [[02 Concepts/Stack/Parallelism & Distributed Execution/Pipeline Parallelism|Pipeline Parallelism]]
- [[02 Concepts/Stack/Parallelism & Distributed Execution/Pipeline Schedule|Pipeline Schedule]]
- [[02 Concepts/Stack/Parallelism & Distributed Execution/Tensor Parallelism|Tensor Parallelism]]
- [[02 Concepts/Stack/Parallelism & Distributed Execution/Training State Sharding|Training State Sharding]]

## Related Themes

- [[03 Themes/Scaling and Coordination|Scaling and Coordination]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume II - Scaling/00 Introduction/01 Introduction/V2-01 Introduction|V2-01 Introduction]] — Fleet Law; Communication intensity; Synchronous tight coupling; Scaling laws as the demand curve.
- [[01 Books/Volume II - Scaling/01 The Fleet/02 Compute Infrastructure/V2-02 Compute Infrastructure|V2-02 Compute Infrastructure]] — Bandwidth hierarchy dictates placement; Node aggregates private memories.
- [[01 Books/Volume II - Scaling/01 The Fleet/03 Network Fabrics/V2-03 Network Fabrics|V2-03 Network Fabrics]] — Alpha-beta model; ML traffic inversion; Traffic-matched topology.
- [[01 Books/Volume II - Scaling/01 The Fleet/04 Data Storage/V2-04 Data Storage|V2-04 Data Storage]] — Input delivery budget.
- [[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05 Collective Communication|V2-05 Collective Communication]] — Collective contracts; Ring AllReduce and the bandwidth bound; Hierarchical collectives; Ring-tree crossover; Exposed communication under overlap; AllToAll active bound; Gradient compression with error feedback.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/06_distributed_training/distributed_training_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07 Fault Tolerance|V2-07 Fault Tolerance]] — Fleet failure rate; Recovery-time budget and fencing.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/09 Fleet Efficiency/V2-09 Fleet Efficiency|V2-09 Fleet Efficiency]] — Program goodput.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10 Serving at Scale|V2-10 Serving at Scale]] — KV cache as admission budget.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/11 Edge Intelligence/V2-11 Edge Intelligence|V2-11 Edge Intelligence]] — FedAvg under sampling and non-IID data.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/06_distributed_training/distributed_training_concepts.yml)

<!-- Semantic Navigation: End -->
