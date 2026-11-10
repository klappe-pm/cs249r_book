---
title: V1-02 System Paradigms
type: Chapter
volume: 1
chapter: 2
publication_status: Released
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol1/02_system_paradigms/02_system_paradigms.qmd
source_anchor: sec-ml-systems
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_1
rendered_source_url: https://mlsysbook.ai/vol1/02_system_paradigms/02_system_paradigms.html
---

# V1-02 System Paradigms

[[Home|Home]] · [[01 Books/Volume I - Foundations/Volume 1 Overview|Volume Overview]]

^sec-ml-systems

[Lecture slides](https://mlsysbook.ai/slides/vol1.html#ch-02) for this chapter

![[90 Assets/Volume I/02 System Paradigms/Cover System Paradigms Blueprint Labeled 46a92a5459.webp]]

*Isometric blueprint showing one model artifact moving across cloud, edge, mobile, and tiny-device deployment environments with shrinking resource envelopes.*

## Chapter Sections

- [[01 Books/Volume I - Foundations/01 Foundations/02 System Paradigms/V1-02.01 Purpose|V1-02.01 Purpose]]
- [[01 Books/Volume I - Foundations/01 Foundations/02 System Paradigms/V1-02.02 Four Deployment Regimes Across Nine Orders of Magnitude|V1-02.02 Four Deployment Regimes Across Nine Orders of Magnitude]]
- [[01 Books/Volume I - Foundations/01 Foundations/02 System Paradigms/V1-02.03 Physical Constraints on Deployment|V1-02.03 Physical Constraints on Deployment]]
- [[01 Books/Volume I - Foundations/01 Foundations/02 System Paradigms/V1-02.04 Analyzing Workloads|V1-02.04 Analyzing Workloads]]
- [[01 Books/Volume I - Foundations/01 Foundations/02 System Paradigms/V1-02.05 System Balance and Hardware|V1-02.05 System Balance and Hardware]]
- [[01 Books/Volume I - Foundations/01 Foundations/02 System Paradigms/V1-02.06 Cloud ML Computational Power|V1-02.06 Cloud ML Computational Power]]
- [[01 Books/Volume I - Foundations/01 Foundations/02 System Paradigms/V1-02.07 Edge ML Latency and Privacy|V1-02.07 Edge ML Latency and Privacy]]
- [[01 Books/Volume I - Foundations/01 Foundations/02 System Paradigms/V1-02.08 Mobile ML Offline Intelligence|V1-02.08 Mobile ML Offline Intelligence]]
- [[01 Books/Volume I - Foundations/01 Foundations/02 System Paradigms/V1-02.09 TinyML Ubiquitous Sensing|V1-02.09 TinyML Ubiquitous Sensing]]
- [[01 Books/Volume I - Foundations/01 Foundations/02 System Paradigms/V1-02.10 Choosing a Deployment Paradigm|V1-02.10 Choosing a Deployment Paradigm]]
- [[01 Books/Volume I - Foundations/01 Foundations/02 System Paradigms/V1-02.11 Hybrid Architectures|V1-02.11 Hybrid Architectures]]
- [[01 Books/Volume I - Foundations/01 Foundations/02 System Paradigms/V1-02.12 What Every Tier Shares|V1-02.12 What Every Tier Shares]]
- [[01 Books/Volume I - Foundations/01 Foundations/02 System Paradigms/V1-02.13 Fallacies and Pitfalls|V1-02.13 Fallacies and Pitfalls]]
- [[01 Books/Volume I - Foundations/01 Foundations/02 System Paradigms/V1-02.14 Summary|V1-02.14 Summary]]
- [[01 Books/Volume I - Foundations/01 Foundations/02 System Paradigms/V1-02.15 Self-Check Answers|V1-02.15 Self-Check Answers]]
- [[01 Books/Volume I - Foundations/01 Foundations/02 System Paradigms/V1-02.16 Source References|V1-02.16 Source References]]
- [[01 Books/Volume I - Foundations/01 Foundations/02 System Paradigms/V1-02.17 Footnotes|V1-02.17 Footnotes]]

Next: [[01 Books/Volume I - Foundations/01 Foundations/02 System Paradigms/V1-02.01 Purpose|V1-02.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/02_system_paradigms/02_system_paradigms.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol1/02_system_paradigms/02_system_paradigms.html#sec-ml-systems). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Foundations/Quantitative System Models/Data Locality|Data Locality]]
- [[02 Concepts/Qualities/Sustainability & Cost/Energy per Inference|Energy per Inference]]
- [[02 Concepts/Stack/Hardware & Accelerators/Memory Capacity|Memory Capacity]]

## Related Themes

- [[03 Themes/Constraints Drive Architecture|Constraints Drive Architecture]]
- [[03 Themes/Energy and Cost|Energy and Cost]]
- [[03 Themes/Memory and Bandwidth|Memory and Bandwidth]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume I - Foundations/00 Introduction/01 Introduction/V1-01 Introduction|V1-01 Introduction]] — Iron law of ML systems; D·A·M diagnosis; Bitter lesson and bottleneck migration; Silent degradation.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/02_system_paradigms/system_paradigms_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume I - Foundations/01 Foundations/03 ML Lifecycle/V1-03 ML Lifecycle|V1-03 ML Lifecycle]] — Problem framing.
- [[01 Books/Volume I - Foundations/01 Foundations/04 Data Engineering/V1-04 Data Engineering|V1-04 Data Engineering]] — Drift statistics.
- [[01 Books/Volume I - Foundations/02 Development/06 Network Architectures/V1-06 Network Architectures|V1-06 Network Architectures]] — Efficient architecture families.
- [[01 Books/Volume I - Foundations/02 Development/07 ML Frameworks/V1-07 ML Frameworks|V1-07 ML Frameworks]] — Kernel fusion.
- [[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08 Model Training|V1-08 Model Training]] — Training memory at scale.
- [[01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10 Model Compression|V1-10 Model Compression]] — Quantization regimes and the cliff.
- [[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11 Hardware Acceleration|V1-11 Hardware Acceleration]] — Energy ladder; Roofline and ridge point; Amdahl's law.
- [[01 Books/Volume I - Foundations/03 Optimization/12 Benchmarking/V1-12 Benchmarking|V1-12 Benchmarking]] — Energy measurement boundary; Benchmark granularity.
- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13 Model Serving|V1-13 Model Serving]] — KV cache budget bounds concurrency.
- [[01 Books/Volume I - Foundations/04 Deployment/14 ML Operations/V1-14 ML Operations|V1-14 ML Operations]] — Layered monitoring and detection delay.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/02_system_paradigms/system_paradigms_concepts.yml)

<!-- Semantic Navigation: End -->
