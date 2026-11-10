---
title: V1-06 Network Architectures
type: Chapter
volume: 1
chapter: 6
publication_status: Released
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol1/06_nn_architectures/06_nn_architectures.qmd
source_anchor: sec-network-architectures
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_1
rendered_source_url: https://mlsysbook.ai/vol1/06_nn_architectures/06_nn_architectures.html
---

# V1-06 Network Architectures

[[Home|Home]] · [[01 Books/Volume I - Foundations/Volume 1 Overview|Volume Overview]]

^sec-network-architectures

Lecture slides for this chapter: [Part 1](https://mlsysbook.ai/slides/vol1.html#lec-06) · [Part 2](https://mlsysbook.ai/slides/vol1.html#lec-06b)

![[90 Assets/Volume I/06 Nn Architectures/Cover Nn Architectures Blueprint Labeled f5a4652980.webp]]

*Isometric architecture interchange where one representation stream branches into dense, spatial, sequence, and attention-like paths before rejoining.*

## Chapter Sections

- [[01 Books/Volume I - Foundations/02 Development/06 Network Architectures/V1-06.01 Purpose|V1-06.01 Purpose]]
- [[01 Books/Volume I - Foundations/02 Development/06 Network Architectures/V1-06.02 Architectural Principles|V1-06.02 Architectural Principles]]
- [[01 Books/Volume I - Foundations/02 Development/06 Network Architectures/V1-06.03 MLPs Dense Pattern Processing|V1-06.03 MLPs Dense Pattern Processing]]
- [[01 Books/Volume I - Foundations/02 Development/06 Network Architectures/V1-06.04 CNNs Spatial Pattern Processing|V1-06.04 CNNs Spatial Pattern Processing]]
- [[01 Books/Volume I - Foundations/02 Development/06 Network Architectures/V1-06.05 Skip Connections and Normalization|V1-06.05 Skip Connections and Normalization]]
- [[01 Books/Volume I - Foundations/02 Development/06 Network Architectures/V1-06.06 RNNs Sequential Pattern Processing|V1-06.06 RNNs Sequential Pattern Processing]]
- [[01 Books/Volume I - Foundations/02 Development/06 Network Architectures/V1-06.07 Attention Dynamic Processing|V1-06.07 Attention Dynamic Processing]]
- [[01 Books/Volume I - Foundations/02 Development/06 Network Architectures/V1-06.08 Transformers Parallel Sequence Processing|V1-06.08 Transformers Parallel Sequence Processing]]
- [[01 Books/Volume I - Foundations/02 Development/06 Network Architectures/V1-06.09 Sparse Architectures Recommendation Systems|V1-06.09 Sparse Architectures Recommendation Systems]]
- [[01 Books/Volume I - Foundations/02 Development/06 Network Architectures/V1-06.10 Comparing and Choosing Architectures|V1-06.10 Comparing and Choosing Architectures]]
- [[01 Books/Volume I - Foundations/02 Development/06 Network Architectures/V1-06.11 Fallacies and Pitfalls|V1-06.11 Fallacies and Pitfalls]]
- [[01 Books/Volume I - Foundations/02 Development/06 Network Architectures/V1-06.12 Summary|V1-06.12 Summary]]
- [[01 Books/Volume I - Foundations/02 Development/06 Network Architectures/V1-06.13 Self-Check Answers|V1-06.13 Self-Check Answers]]
- [[01 Books/Volume I - Foundations/02 Development/06 Network Architectures/V1-06.14 Source References|V1-06.14 Source References]]
- [[01 Books/Volume I - Foundations/02 Development/06 Network Architectures/V1-06.15 Footnotes|V1-06.15 Footnotes]]

Next: [[01 Books/Volume I - Foundations/02 Development/06 Network Architectures/V1-06.01 Purpose|V1-06.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/06_nn_architectures/06_nn_architectures.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol1/06_nn_architectures/06_nn_architectures.html#sec-network-architectures). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Foundations/Models & Architectures/Attention|Attention]]
- [[02 Concepts/Foundations/Models & Architectures/Inductive Bias|Inductive Bias]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume I - Foundations/00 Introduction/01 Introduction/V1-01 Introduction|V1-01 Introduction]] — Iron law of ML systems; Bitter lesson and bottleneck migration; D·A·M diagnosis.
- [[01 Books/Volume I - Foundations/01 Foundations/02 System Paradigms/V1-02 System Paradigms|V1-02 System Paradigms]] — Workload archetypes and lighthouses; Silicon contract.
- [[01 Books/Volume I - Foundations/02 Development/05 Neural Computation/V1-05 Neural Computation|V1-05 Neural Computation]] — Batching raises dense-layer intensity; Network as linear maps and nonlinearities; Cost from layer shapes; Backprop over saved activations; Numerical range.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/06_nn_architectures/nn_architectures_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume I - Foundations/02 Development/07 ML Frameworks/V1-07 ML Frameworks|V1-07 ML Frameworks]] — Kernel fusion.
- [[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08 Model Training|V1-08 Model Training]] — IO-aware attention; Checkpointing and accumulation; Single-node data parallelism; Sharding within one node; Training memory at scale.
- [[01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10 Model Compression|V1-10 Model Compression]] — Quantization regimes and the cliff; Accuracy-efficiency frontier; Input-dependent computation and NAS.
- [[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11 Hardware Acceleration|V1-11 Hardware Acceleration]] — Roofline and ridge point; Energy ladder; Operand-supply hierarchy; Matching primitives to execution units; Tiling; Fusion limits on accelerators.
- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13 Model Serving|V1-13 Model Serving]] — KV cache budget bounds concurrency; LLM serving phases.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/06_nn_architectures/nn_architectures_concepts.yml)

<!-- Semantic Navigation: End -->
