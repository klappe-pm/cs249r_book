---
title: V1-07 ML Frameworks
type: Chapter
volume: 1
chapter: 7
publication_status: Released
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol1/07_frameworks/07_frameworks.qmd
source_anchor: sec-ml-frameworks
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_1
rendered_source_url: https://mlsysbook.ai/vol1/07_frameworks/07_frameworks.html
---

# V1-07 ML Frameworks

[[Home|Home]] · [[01 Books/Volume I - Foundations/Volume 1 Overview|Volume Overview]]

^sec-ml-frameworks

[Lecture slides](https://mlsysbook.ai/slides/vol1.html#ch-07) for this chapter

![[90 Assets/Volume I/07 Frameworks/Cover Frameworks Blueprint Labeled a4f9817b1a.webp]]

*Layered blueprint showing high-level model intent lowering through graph capture, autograd, fusion, and kernel dispatch into executable work.*

## Chapter Sections

- [[01 Books/Volume I - Foundations/02 Development/07 ML Frameworks/V1-07.01 Purpose|V1-07.01 Purpose]]
- [[01 Books/Volume I - Foundations/02 Development/07 ML Frameworks/V1-07.02 Three Framework Problems|V1-07.02 Three Framework Problems]]
- [[01 Books/Volume I - Foundations/02 Development/07 ML Frameworks/V1-07.03 Evolution of Framework Abstractions|V1-07.03 Evolution of Framework Abstractions]]
- [[01 Books/Volume I - Foundations/02 Development/07 ML Frameworks/V1-07.04 Execution from Graphs to Kernels|V1-07.04 Execution from Graphs to Kernels]]
- [[01 Books/Volume I - Foundations/02 Development/07 ML Frameworks/V1-07.05 Differentiation Automatic Gradient Computation|V1-07.05 Differentiation Automatic Gradient Computation]]
- [[01 Books/Volume I - Foundations/02 Development/07 ML Frameworks/V1-07.06 Abstraction Tensors, Devices, and Operations|V1-07.06 Abstraction Tensors, Devices, and Operations]]
- [[01 Books/Volume I - Foundations/02 Development/07 ML Frameworks/V1-07.07 Modules from Operations to Models|V1-07.07 Modules from Operations to Models]]
- [[01 Books/Volume I - Foundations/02 Development/07 ML Frameworks/V1-07.08 Anatomy of a Training Step|V1-07.08 Anatomy of a Training Step]]
- [[01 Books/Volume I - Foundations/02 Development/07 ML Frameworks/V1-07.09 Major Frameworks TensorFlow, PyTorch, and JAX|V1-07.09 Major Frameworks TensorFlow, PyTorch, and JAX]]
- [[01 Books/Volume I - Foundations/02 Development/07 ML Frameworks/V1-07.10 Choosing a Framework|V1-07.10 Choosing a Framework]]
- [[01 Books/Volume I - Foundations/02 Development/07 ML Frameworks/V1-07.11 Fallacies and Pitfalls|V1-07.11 Fallacies and Pitfalls]]
- [[01 Books/Volume I - Foundations/02 Development/07 ML Frameworks/V1-07.12 Summary|V1-07.12 Summary]]
- [[01 Books/Volume I - Foundations/02 Development/07 ML Frameworks/V1-07.13 Self-Check Answers|V1-07.13 Self-Check Answers]]
- [[01 Books/Volume I - Foundations/02 Development/07 ML Frameworks/V1-07.14 Source References|V1-07.14 Source References]]
- [[01 Books/Volume I - Foundations/02 Development/07 ML Frameworks/V1-07.15 Footnotes|V1-07.15 Footnotes]]

Next: [[01 Books/Volume I - Foundations/02 Development/07 ML Frameworks/V1-07.01 Purpose|V1-07.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/07_frameworks/07_frameworks.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol1/07_frameworks/07_frameworks.html#sec-ml-frameworks). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Automatic Differentiation|Automatic Differentiation]]
- [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Host Dispatch Overhead|Host Dispatch Overhead]]
- [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Kernel Fusion|Kernel Fusion]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume I - Foundations/00 Introduction/01 Introduction/V1-01 Introduction|V1-01 Introduction]] — Iron law of ML systems; Bitter lesson and bottleneck migration.
- [[01 Books/Volume I - Foundations/01 Foundations/02 System Paradigms/V1-02 System Paradigms|V1-02 System Paradigms]] — Memory wall; Workload archetypes and lighthouses.
- [[01 Books/Volume I - Foundations/01 Foundations/03 ML Lifecycle/V1-03 ML Lifecycle|V1-03 ML Lifecycle]] — Iteration tax.
- [[01 Books/Volume I - Foundations/01 Foundations/04 Data Engineering/V1-04 Data Engineering|V1-04 Data Engineering]] — The feeding problem.
- [[01 Books/Volume I - Foundations/02 Development/05 Neural Computation/V1-05 Neural Computation|V1-05 Neural Computation]] — Backprop over saved activations; Training holds four kinds of state.
- [[01 Books/Volume I - Foundations/02 Development/06 Network Architectures/V1-06 Network Architectures|V1-06 Network Architectures]] — Autoregressive decode and the KV cache.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/07_frameworks/frameworks_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08 Model Training|V1-08 Model Training]] — Mixed precision; Checkpointing and accumulation; Training checkpoints; Profile to find the limiting term; Single-node data parallelism; Sharding within one node; Training input pipeline; Training memory at scale.
- [[01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10 Model Compression|V1-10 Model Compression]] — Quantization regimes and the cliff; Compression-specific fusion.
- [[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11 Hardware Acceleration|V1-11 Hardware Acceleration]] — Roofline and ridge point; Compilers and runtimes; Tiling; Fusion limits on accelerators.
- [[01 Books/Volume I - Foundations/03 Optimization/12 Benchmarking/V1-12 Benchmarking|V1-12 Benchmarking]] — Latency distribution and the SLO.
- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13 Model Serving|V1-13 Model Serving]] — Runtime and precision selection.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/07_frameworks/frameworks_concepts.yml)

<!-- Semantic Navigation: End -->
