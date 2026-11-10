---
title: V1-08 Model Training
type: Chapter
volume: 1
chapter: 8
publication_status: Released
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol1/08_training/08_training.qmd
source_anchor: sec-model-training
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_1
rendered_source_url: https://mlsysbook.ai/vol1/08_training/08_training.html
---

# V1-08 Model Training

[[Home|Home]] · [[01 Books/Volume I - Foundations/Volume 1 Overview|Volume Overview]]

^sec-model-training

Lecture slides for this chapter: [Part 1](https://mlsysbook.ai/slides/vol1.html#lec-08) · [Part 2](https://mlsysbook.ai/slides/vol1.html#lec-08b)

![[90 Assets/Volume I/08 Training/Cover Training Blueprint Labeled 22bced9d4a.webp]]

*Isometric training cutaway showing a forward pass storing activations, a loss signal, returning gradients, and weight updates.*

## Chapter Sections

- [[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08.01 Purpose|V1-08.01 Purpose]]
- [[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08.02 From One Step to a Training Run|V1-08.02 From One Step to a Training Run]]
- [[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08.03 Training-Time Law|V1-08.03 Training-Time Law]]
- [[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08.04 Computation and Memory Costs of Training|V1-08.04 Computation and Memory Costs of Training]]
- [[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08.05 Pipeline Architecture|V1-08.05 Pipeline Architecture]]
- [[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08.06 Identifying Bottlenecks|V1-08.06 Identifying Bottlenecks]]
- [[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08.07 Pipeline Optimizations|V1-08.07 Pipeline Optimizations]]
- [[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08.08 Scaling Training Systems|V1-08.08 Scaling Training Systems]]
- [[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08.09 Fallacies and Pitfalls|V1-08.09 Fallacies and Pitfalls]]
- [[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08.10 Summary|V1-08.10 Summary]]
- [[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08.11 Self-Check Answers|V1-08.11 Self-Check Answers]]
- [[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08.12 Source References|V1-08.12 Source References]]
- [[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08.13 Footnotes|V1-08.13 Footnotes]]

Next: [[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08.01 Purpose|V1-08.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/08_training/08_training.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol1/08_training/08_training.html#sec-model-training). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Lifecycle/Training & Adaptation/Activation Recomputation|Activation Recomputation]]
- [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Model FLOPS Utilization|Model FLOPS Utilization]]
- [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Time to Train|Time to Train]]
- [[02 Concepts/Lifecycle/Training & Adaptation/Training Batch Size|Training Batch Size]]
- [[02 Concepts/Foundations/Quantitative System Models/Training Compute Estimate|Training Compute Estimate]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume I - Foundations/00 Introduction/01 Introduction/V1-01 Introduction|V1-01 Introduction]] — Iron law of ML systems; Bitter lesson and bottleneck migration; D·A·M diagnosis.
- [[01 Books/Volume I - Foundations/01 Foundations/02 System Paradigms/V1-02 System Paradigms|V1-02 System Paradigms]] — Workload archetypes and lighthouses; Silicon contract.
- [[01 Books/Volume I - Foundations/01 Foundations/03 ML Lifecycle/V1-03 ML Lifecycle|V1-03 ML Lifecycle]] — Stage interface contracts.
- [[01 Books/Volume I - Foundations/01 Foundations/04 Data Engineering/V1-04 Data Engineering|V1-04 Data Engineering]] — The feeding problem; Storage tiers and access patterns.
- [[01 Books/Volume I - Foundations/02 Development/05 Neural Computation/V1-05 Neural Computation|V1-05 Neural Computation]] — Loss and mini-batch descent; Backprop over saved activations; Training holds four kinds of state; Activation functions; Batching raises dense-layer intensity.
- [[01 Books/Volume I - Foundations/02 Development/06 Network Architectures/V1-06 Network Architectures|V1-06 Network Architectures]] — Skip connections and normalization.
- [[01 Books/Volume I - Foundations/02 Development/07 ML Frameworks/V1-07 ML Frameworks|V1-07 ML Frameworks]] — Mixed precision and checkpointing mechanics; Kernel fusion; Saved forward state.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/08_training/training_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume I - Foundations/03 Optimization/09 Data Selection/V1-09 Data Selection|V1-09 Data Selection]] — Selection inequality.
- [[01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10 Model Compression|V1-10 Model Compression]] — Combined techniques do not multiply; Quantization regimes and the cliff.
- [[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11 Hardware Acceleration|V1-11 Hardware Acceleration]] — Roofline and ridge point; Amdahl's law; Tiling; Matching primitives to execution units; Energy ladder.
- [[01 Books/Volume I - Foundations/03 Optimization/12 Benchmarking/V1-12 Benchmarking|V1-12 Benchmarking]] — Time to quality target.
- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13 Model Serving|V1-13 Model Serving]] — Serving inverts training.
- [[01 Books/Volume I - Foundations/04 Deployment/15 Responsible Engineering/V1-15 Responsible Engineering|V1-15 Responsible Engineering]] — Lifecycle TCO; Energy to carbon.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/08_training/training_concepts.yml)

<!-- Semantic Navigation: End -->
