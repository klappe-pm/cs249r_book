---
title: V1-11 Hardware Acceleration
type: Chapter
volume: 1
chapter: 11
publication_status: Released
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol1/11_hw_acceleration/11_hw_acceleration.qmd
source_anchor: sec-hardware-acceleration
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_1
rendered_source_url: https://mlsysbook.ai/vol1/11_hw_acceleration/11_hw_acceleration.html
---

# V1-11 Hardware Acceleration

[[Home|Home]] · [[01 Books/Volume I - Foundations/Volume 1 Overview|Volume Overview]]

^sec-hardware-acceleration

Lecture slides for this chapter: [Part 1](https://mlsysbook.ai/slides/vol1.html#lec-11) · [Part 2](https://mlsysbook.ai/slides/vol1.html#lec-11b)

![[90 Assets/Volume I/11 Hw Acceleration/Cover Hw Acceleration Blueprint Labeled d8add34ce4.webp]]

*Layered isometric hardware blueprint where a tensor operation lowers into tiles, local SRAM, and an execution array while avoiding an off-chip memory wall.*

## Chapter Sections

- [[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.01 Purpose|V1-11.01 Purpose]]
- [[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.02 Anatomy of an Accelerator|V1-11.02 Anatomy of an Accelerator]]
- [[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.03 Hardware Specialization|V1-11.03 Hardware Specialization]]
- [[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.04 Compute Primitives|V1-11.04 Compute Primitives]]
- [[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.05 Compute Units|V1-11.05 Compute Units]]
- [[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.06 Memory Systems|V1-11.06 Memory Systems]]
- [[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.07 Performance Bounds|V1-11.07 Performance Bounds]]
- [[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.08 Hardware Mapping|V1-11.08 Hardware Mapping]]
- [[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.09 Compilers and Runtimes|V1-11.09 Compilers and Runtimes]]
- [[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.10 Beyond One Accelerator|V1-11.10 Beyond One Accelerator]]
- [[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.11 Heterogeneous SoC Design|V1-11.11 Heterogeneous SoC Design]]
- [[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.12 Choosing an Accelerator|V1-11.12 Choosing an Accelerator]]
- [[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.13 Fallacies and Pitfalls|V1-11.13 Fallacies and Pitfalls]]
- [[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.14 Summary|V1-11.14 Summary]]
- [[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.15 Self-Check Answers|V1-11.15 Self-Check Answers]]
- [[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.16 Source References|V1-11.16 Source References]]
- [[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.17 Footnotes|V1-11.17 Footnotes]]

Next: [[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.01 Purpose|V1-11.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/11_hw_acceleration/11_hw_acceleration.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol1/11_hw_acceleration/11_hw_acceleration.html#sec-hardware-acceleration). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Stack/Hardware & Accelerators/Accelerator Dataflow|Accelerator Dataflow]]
- [[02 Concepts/Foundations/Quantitative System Models/Amdahl's Law|Amdahl's Law]]
- [[02 Concepts/Foundations/Quantitative System Models/Arithmetic Intensity|Arithmetic Intensity]]
- [[02 Concepts/Stack/Hardware & Accelerators/Memory Bandwidth|Memory Bandwidth]]
- [[02 Concepts/Stack/Hardware & Accelerators/Memory Hierarchy|Memory Hierarchy]]
- [[02 Concepts/Foundations/Quantitative System Models/Roofline Bound|Roofline Bound]]
- [[02 Concepts/Foundations/Quantitative System Models/Serial Fraction|Serial Fraction]]
- [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Tiling|Tiling]]

## Related Themes

- [[03 Themes/Constraints Drive Architecture|Constraints Drive Architecture]]
- [[03 Themes/Memory and Bandwidth|Memory and Bandwidth]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume I - Foundations/00 Introduction/01 Introduction/V1-01 Introduction|V1-01 Introduction]] — Iron law of ML systems; Bitter lesson and bottleneck migration.
- [[01 Books/Volume I - Foundations/01 Foundations/02 System Paradigms/V1-02 System Paradigms|V1-02 System Paradigms]] — Memory wall; Workload archetypes and lighthouses; Silicon contract.
- [[01 Books/Volume I - Foundations/01 Foundations/04 Data Engineering/V1-04 Data Engineering|V1-04 Data Engineering]] — The feeding problem.
- [[01 Books/Volume I - Foundations/02 Development/06 Network Architectures/V1-06 Network Architectures|V1-06 Network Architectures]] — Architectures as cost signatures; Every family lowers onto GEMM; Autoregressive decode and the KV cache.
- [[01 Books/Volume I - Foundations/02 Development/07 ML Frameworks/V1-07 ML Frameworks|V1-07 ML Frameworks]] — Kernel fusion; Eager, graph, and JIT execution; Dispatch overhead law; Saved forward state.
- [[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08 Model Training|V1-08 Model Training]] — Mixed precision; IO-aware attention; Single-node data parallelism.
- [[01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10 Model Compression|V1-10 Model Compression]] — Structured vs unstructured pruning; Sparse storage break-even; Compression-specific fusion; Quantization regimes and the cliff.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/11_hw_acceleration/hw_acceleration_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume I - Foundations/03 Optimization/12 Benchmarking/V1-12 Benchmarking|V1-12 Benchmarking]] — Benchmark granularity; Standardized benchmark suites.
- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13 Model Serving|V1-13 Model Serving]] — Batching trades latency for throughput; KV cache budget bounds concurrency; Speculative decoding; Runtime and precision selection.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/11_hw_acceleration/hw_acceleration_concepts.yml)

<!-- Semantic Navigation: End -->
