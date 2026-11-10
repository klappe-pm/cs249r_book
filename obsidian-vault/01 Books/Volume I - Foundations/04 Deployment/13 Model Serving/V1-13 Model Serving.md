---
title: V1-13 Model Serving
type: Chapter
volume: 1
chapter: 13
publication_status: Released
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol1/13_model_serving/13_model_serving.qmd
source_anchor: sec-model-serving
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_1
rendered_source_url: https://mlsysbook.ai/vol1/13_model_serving/13_model_serving.html
---

# V1-13 Model Serving

[[Home|Home]] · [[01 Books/Volume I - Foundations/Volume 1 Overview|Volume Overview]]

^sec-model-serving

Lecture slides for this chapter: [Part 1](https://mlsysbook.ai/slides/vol1.html#lec-13) · [Part 2](https://mlsysbook.ai/slides/vol1.html#lec-13b)

![[90 Assets/Volume I/13 Model Serving/Cover Model Serving Blueprint Labeled 5c03e6473c.webp]]

*Isometric serving pipeline where variable requests become scheduled batches, occupy cache pages, run through inference workers, and return responses under latency pressure.*

## Chapter Sections

- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.01 Purpose|V1-13.01 Purpose]]
- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.02 The Serving Inversion|V1-13.02 The Serving Inversion]]
- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.03 Serving System Architecture|V1-13.03 Serving System Architecture]]
- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.04 Request Lifecycle|V1-13.04 Request Lifecycle]]
- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.05 Queuing Theory|V1-13.05 Queuing Theory]]
- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.06 Throughput Optimization|V1-13.06 Throughput Optimization]]
- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.07 Inference Runtime Selection|V1-13.07 Inference Runtime Selection]]
- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.08 Node-Level Optimization|V1-13.08 Node-Level Optimization]]
- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.09 Model Loading and Versioning|V1-13.09 Model Loading and Versioning]]
- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.10 LLM Serving|V1-13.10 LLM Serving]]
- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.11 Economics and Planning|V1-13.11 Economics and Planning]]
- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.12 Fallacies and Pitfalls|V1-13.12 Fallacies and Pitfalls]]
- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.13 Summary|V1-13.13 Summary]]
- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.14 Self-Check Answers|V1-13.14 Self-Check Answers]]
- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.15 Source References|V1-13.15 Source References]]
- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.16 Footnotes|V1-13.16 Footnotes]]

Next: [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.01 Purpose|V1-13.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/13_model_serving/13_model_serving.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol1/13_model_serving/13_model_serving.html#sec-model-serving). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Foundations/Quantitative System Models/Arrival Rate|Arrival Rate]]
- [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Capacity Planning|Capacity Planning]]
- [[02 Concepts/Lifecycle/Deployment & Serving/Continuous Batching|Continuous Batching]]
- [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Cross Stack Profiling|Cross Stack Profiling]]
- [[02 Concepts/Lifecycle/Deployment & Serving/KV Cache|KV Cache]]
- [[02 Concepts/Foundations/Workloads & Requirements/Latency Budget|Latency Budget]]
- [[02 Concepts/Foundations/Quantitative System Models/Little's Law|Little's Law]]
- [[02 Concepts/Lifecycle/Deployment & Serving/Paged KV Allocation|Paged KV Allocation]]
- [[02 Concepts/Lifecycle/Deployment & Serving/Prefill and Decode|Prefill and Decode]]
- [[02 Concepts/Lifecycle/Deployment & Serving/Prefix Caching|Prefix Caching]]
- [[02 Concepts/Foundations/Quantitative System Models/Queueing Delay|Queueing Delay]]
- [[02 Concepts/Lifecycle/Deployment & Serving/Request Batching|Request Batching]]
- [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Resource Utilization|Resource Utilization]]
- [[02 Concepts/Foundations/Quantitative System Models/Service Capacity|Service Capacity]]
- [[02 Concepts/Lifecycle/Deployment & Serving/Tail Latency|Tail Latency]]
- [[02 Concepts/Lifecycle/Deployment & Serving/Time per Output Token|Time per Output Token]]
- [[02 Concepts/Lifecycle/Deployment & Serving/Time to First Token|Time to First Token]]

## Related Themes

- [[03 Themes/Constraints Drive Architecture|Constraints Drive Architecture]]
- [[03 Themes/Latency and Throughput|Latency and Throughput]]
- [[03 Themes/Memory and Bandwidth|Memory and Bandwidth]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume I - Foundations/00 Introduction/01 Introduction/V1-01 Introduction|V1-01 Introduction]] — Iron law of ML systems; Bitter lesson and bottleneck migration.
- [[01 Books/Volume I - Foundations/01 Foundations/02 System Paradigms/V1-02 System Paradigms|V1-02 System Paradigms]] — Physical walls set deployment tiers; Device energy budgets.
- [[01 Books/Volume I - Foundations/01 Foundations/04 Data Engineering/V1-04 Data Engineering|V1-04 Data Engineering]] — Training-serving consistency.
- [[01 Books/Volume I - Foundations/02 Development/06 Network Architectures/V1-06 Network Architectures|V1-06 Network Architectures]] — Autoregressive decode and the KV cache.
- [[01 Books/Volume I - Foundations/02 Development/07 ML Frameworks/V1-07 ML Frameworks|V1-07 ML Frameworks]] — Dispatch overhead law; Kernel fusion.
- [[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08 Model Training|V1-08 Model Training]] — Profile to find the limiting term.
- [[01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10 Model Compression|V1-10 Model Compression]] — Quantization regimes and the cliff; Compression-specific fusion; Low-rank factorization.
- [[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11 Hardware Acceleration|V1-11 Hardware Acceleration]] — Roofline and ridge point; Amdahl's law; Energy ladder.
- [[01 Books/Volume I - Foundations/03 Optimization/12 Benchmarking/V1-12 Benchmarking|V1-12 Benchmarking]] — Latency distribution and the SLO; Standardized benchmark suites; Benchmark granularity; Verification gap.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/13_model_serving/model_serving_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume I - Foundations/04 Deployment/14 ML Operations/V1-14 ML Operations|V1-14 ML Operations]] — Safe release and tested rollback; Request-keyed parity testing; Layered monitoring and detection delay; Reproducibility and the model registry.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/13_model_serving/model_serving_concepts.yml)

<!-- Semantic Navigation: End -->
