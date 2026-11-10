---
title: V1-12 Benchmarking
type: Chapter
volume: 1
chapter: 12
publication_status: Released
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol1/12_benchmarking/12_benchmarking.qmd
source_anchor: sec-benchmarking
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_1
rendered_source_url: https://mlsysbook.ai/vol1/12_benchmarking/12_benchmarking.html
---

# V1-12 Benchmarking

[[Home|Home]] · [[01 Books/Volume I - Foundations/Volume 1 Overview|Volume Overview]]

^sec-benchmarking

Lecture slides for this chapter: [Part 1](https://mlsysbook.ai/slides/vol1.html#lec-12) · [Part 2](https://mlsysbook.ai/slides/vol1.html#lec-12b)

![[90 Assets/Volume I/12 Benchmarking/Cover Benchmarking Blueprint Labeled 1dabf468ca.webp]]

*Isometric benchmarking rig showing a workload passing through nested measurement scopes with a visible gap between peak capability and sustained behavior.*

## Chapter Sections

- [[01 Books/Volume I - Foundations/03 Optimization/12 Benchmarking/V1-12.01 Purpose|V1-12.01 Purpose]]
- [[01 Books/Volume I - Foundations/03 Optimization/12 Benchmarking/V1-12.02 The Benchmark–Production Gap|V1-12.02 The Benchmark–Production Gap]]
- [[01 Books/Volume I - Foundations/03 Optimization/12 Benchmarking/V1-12.03 Benchmark Carpentry|V1-12.03 Benchmark Carpentry]]
- [[01 Books/Volume I - Foundations/03 Optimization/12 Benchmarking/V1-12.04 Benchmarking Granularity|V1-12.04 Benchmarking Granularity]]
- [[01 Books/Volume I - Foundations/03 Optimization/12 Benchmarking/V1-12.05 Benchmark Suites|V1-12.05 Benchmark Suites]]
- [[01 Books/Volume I - Foundations/03 Optimization/12 Benchmarking/V1-12.06 Training Benchmarks|V1-12.06 Training Benchmarks]]
- [[01 Books/Volume I - Foundations/03 Optimization/12 Benchmarking/V1-12.07 Inference Benchmarks|V1-12.07 Inference Benchmarks]]
- [[01 Books/Volume I - Foundations/03 Optimization/12 Benchmarking/V1-12.08 Power and Energy Measurement|V1-12.08 Power and Energy Measurement]]
- [[01 Books/Volume I - Foundations/03 Optimization/12 Benchmarking/V1-12.09 Benchmarking Best Practices|V1-12.09 Benchmarking Best Practices]]
- [[01 Books/Volume I - Foundations/03 Optimization/12 Benchmarking/V1-12.10 Model and Data Evaluation|V1-12.10 Model and Data Evaluation]]
- [[01 Books/Volume I - Foundations/03 Optimization/12 Benchmarking/V1-12.11 Fallacies and Pitfalls|V1-12.11 Fallacies and Pitfalls]]
- [[01 Books/Volume I - Foundations/03 Optimization/12 Benchmarking/V1-12.12 Summary|V1-12.12 Summary]]
- [[01 Books/Volume I - Foundations/03 Optimization/12 Benchmarking/V1-12.13 Self-Check Answers|V1-12.13 Self-Check Answers]]
- [[01 Books/Volume I - Foundations/03 Optimization/12 Benchmarking/V1-12.14 Source References|V1-12.14 Source References]]
- [[01 Books/Volume I - Foundations/03 Optimization/12 Benchmarking/V1-12.15 Footnotes|V1-12.15 Footnotes]]

Next: [[01 Books/Volume I - Foundations/03 Optimization/12 Benchmarking/V1-12.01 Purpose|V1-12.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/12_benchmarking/12_benchmarking.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol1/12_benchmarking/12_benchmarking.html#sec-benchmarking). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Benchmark Protocol|Benchmark Protocol]]
- [[02 Concepts/Lifecycle/Model Evaluation & Testing/Evaluation Metrics|Evaluation Metrics]]
- [[02 Concepts/Lifecycle/Deployment & Serving/Latency Percentiles|Latency Percentiles]]
- [[02 Concepts/Foundations/Workloads & Requirements/Service Level Objective|Service Level Objective]]
- [[02 Concepts/Lifecycle/Model Evaluation & Testing/Sliced Evaluation|Sliced Evaluation]]

## Related Themes

- [[03 Themes/Constraints Drive Architecture|Constraints Drive Architecture]]
- [[03 Themes/Latency and Throughput|Latency and Throughput]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume I - Foundations/00 Introduction/01 Introduction/V1-01 Introduction|V1-01 Introduction]] — Iron law of ML systems; D·A·M diagnosis; Bitter lesson and bottleneck migration.
- [[01 Books/Volume I - Foundations/01 Foundations/02 System Paradigms/V1-02 System Paradigms|V1-02 System Paradigms]] — Workload archetypes and lighthouses.
- [[01 Books/Volume I - Foundations/01 Foundations/04 Data Engineering/V1-04 Data Engineering|V1-04 Data Engineering]] — Labels are the specification; Drift statistics; Data leakage; The feeding problem.
- [[01 Books/Volume I - Foundations/02 Development/06 Network Architectures/V1-06 Network Architectures|V1-06 Network Architectures]] — Autoregressive decode and the KV cache.
- [[01 Books/Volume I - Foundations/02 Development/07 ML Frameworks/V1-07 ML Frameworks|V1-07 ML Frameworks]] — Eager, graph, and JIT execution.
- [[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08 Model Training|V1-08 Model Training]] — Model FLOPs utilization; Training memory at scale; Single-node data parallelism; Profile to find the limiting term.
- [[01 Books/Volume I - Foundations/03 Optimization/09 Data Selection/V1-09 Data Selection|V1-09 Data Selection]] — Measuring data value.
- [[01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10 Model Compression|V1-10 Model Compression]] — Quantization regimes and the cliff; Structured vs unstructured pruning; Accuracy-efficiency frontier.
- [[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11 Hardware Acceleration|V1-11 Hardware Acceleration]] — Roofline and ridge point; Amdahl's law; Operand-supply hierarchy; Matching primitives to execution units; Heterogeneous SoCs and CMOS power; Energy ladder.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/12_benchmarking/benchmarking_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13 Model Serving|V1-13 Model Serving]] — Batching trades latency for throughput; Queueing sets headroom; LLM serving phases.
- [[01 Books/Volume I - Foundations/04 Deployment/14 ML Operations/V1-14 ML Operations|V1-14 ML Operations]] — Layered monitoring and detection delay; Safe release and tested rollback.
- [[01 Books/Volume I - Foundations/04 Deployment/15 Responsible Engineering/V1-15 Responsible Engineering|V1-15 Responsible Engineering]] — Fairness criteria for release.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/12_benchmarking/benchmarking_concepts.yml)

<!-- Semantic Navigation: End -->
