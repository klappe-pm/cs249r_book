---
title: V1-10 Model Compression
type: Chapter
volume: 1
chapter: 10
publication_status: Released
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol1/10_model_compression/10_model_compression.qmd
source_anchor: sec-model-compression
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_1
rendered_source_url: https://mlsysbook.ai/vol1/10_model_compression/10_model_compression.html
---

# V1-10 Model Compression

[[Home|Home]] · [[01 Books/Volume I - Foundations/Volume 1 Overview|Volume Overview]]

^sec-model-compression

Lecture slides for this chapter: [Part 1](https://mlsysbook.ai/slides/vol1.html#lec-10) · [Part 2](https://mlsysbook.ai/slides/vol1.html#lec-10b)

![[90 Assets/Volume I/10 Model Compression/Cover Model Compression Blueprint Labeled 6f25111323.webp]]

*Isometric compression workshop where a large model passes through pruning, distillation, and quantization stations before fitting into a constrained device envelope.*

## Chapter Sections

- [[01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10.01 Purpose|V1-10.01 Purpose]]
- [[01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10.02 Fitting the Deployment Budget|V1-10.02 Fitting the Deployment Budget]]
- [[01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10.03 Structural Optimization Changing What the Model Computes|V1-10.03 Structural Optimization Changing What the Model Computes]]
- [[01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10.04 Numerical Precision Changing How Values Are Stored|V1-10.04 Numerical Precision Changing How Values Are Stored]]
- [[01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10.05 Hardware Implementation Changing How the Model Executes|V1-10.05 Hardware Implementation Changing How the Model Executes]]
- [[01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10.06 Choosing and Combining Techniques|V1-10.06 Choosing and Combining Techniques]]
- [[01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10.07 Measuring Compression Gains|V1-10.07 Measuring Compression Gains]]
- [[01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10.08 Fallacies and Pitfalls|V1-10.08 Fallacies and Pitfalls]]
- [[01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10.09 Summary|V1-10.09 Summary]]
- [[01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10.10 Self-Check Answers|V1-10.10 Self-Check Answers]]
- [[01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10.11 Source References|V1-10.11 Source References]]
- [[01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10.12 Footnotes|V1-10.12 Footnotes]]

Next: [[01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10.01 Purpose|V1-10.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/10_model_compression/10_model_compression.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol1/10_model_compression/10_model_compression.html#sec-model-compression). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Numerical Precision|Numerical Precision]]
- [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Post Training Quantization|Post Training Quantization]]
- [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Quantization|Quantization]]
- [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Quantization Aware Training|Quantization Aware Training]]
- [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Sparsity|Sparsity]]
- [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Structured Pruning|Structured Pruning]]

## Related Themes

- [[03 Themes/Accuracy and Efficiency|Accuracy and Efficiency]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume I - Foundations/00 Introduction/01 Introduction/V1-01 Introduction|V1-01 Introduction]] — Iron law of ML systems; Bitter lesson and bottleneck migration; D·A·M diagnosis.
- [[01 Books/Volume I - Foundations/01 Foundations/02 System Paradigms/V1-02 System Paradigms|V1-02 System Paradigms]] — Silicon contract; Physical walls set deployment tiers; Workload archetypes and lighthouses.
- [[01 Books/Volume I - Foundations/02 Development/06 Network Architectures/V1-06 Network Architectures|V1-06 Network Architectures]] — Efficient architecture families; Autoregressive decode and the KV cache.
- [[01 Books/Volume I - Foundations/02 Development/07 ML Frameworks/V1-07 ML Frameworks|V1-07 ML Frameworks]] — Kernel fusion; Eager, graph, and JIT execution.
- [[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08 Model Training|V1-08 Model Training]] — Mixed precision; Profile to find the limiting term; IO-aware attention.
- [[01 Books/Volume I - Foundations/03 Optimization/09 Data Selection/V1-09 Data Selection|V1-09 Data Selection]] — Synthetic data as a lever.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/10_model_compression/model_compression_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11 Hardware Acceleration|V1-11 Hardware Acceleration]] — Roofline and ridge point; Operand-supply hierarchy; Stationary dataflows; Amdahl's law; Energy ladder; Reduced-precision and sparse datapaths; Fusion limits on accelerators.
- [[01 Books/Volume I - Foundations/03 Optimization/12 Benchmarking/V1-12 Benchmarking|V1-12 Benchmarking]] — Latency distribution and the SLO; Quality beyond accuracy; Benchmark granularity.
- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13 Model Serving|V1-13 Model Serving]] — Batching trades latency for throughput; Runtime and precision selection.
- [[01 Books/Volume I - Foundations/04 Deployment/14 ML Operations/V1-14 ML Operations|V1-14 ML Operations]] — Layered monitoring and detection delay; Reproducibility and the model registry.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/10_model_compression/model_compression_concepts.yml)

<!-- Semantic Navigation: End -->
