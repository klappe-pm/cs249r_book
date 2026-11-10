---
title: V1-05 Neural Computation
type: Chapter
volume: 1
chapter: 5
publication_status: Released
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol1/05_nn_computation/05_nn_computation.qmd
source_anchor: sec-neural-computation
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_1
rendered_source_url: https://mlsysbook.ai/vol1/05_nn_computation/05_nn_computation.html
---

# V1-05 Neural Computation

[[Home|Home]] · [[01 Books/Volume I - Foundations/Volume 1 Overview|Volume Overview]]

^sec-neural-computation

[Lecture slides](https://mlsysbook.ai/slides/vol1.html#ch-05) for this chapter

![[90 Assets/Volume I/05 Nn Computation/Cover Nn Computation Blueprint Labeled 7e8c0de844.webp]]

*Layered isometric blueprint of neural computation where inputs move through weighted layers, activations form, and a loss signal returns through the model.*

## Chapter Sections

- [[01 Books/Volume I - Foundations/02 Development/05 Neural Computation/V1-05.01 Purpose|V1-05.01 Purpose]]
- [[01 Books/Volume I - Foundations/02 Development/05 Neural Computation/V1-05.02 From Logic to Arithmetic|V1-05.02 From Logic to Arithmetic]]
- [[01 Books/Volume I - Foundations/02 Development/05 Neural Computation/V1-05.03 Computing with Patterns|V1-05.03 Computing with Patterns]]
- [[01 Books/Volume I - Foundations/02 Development/05 Neural Computation/V1-05.04 Neural Network Fundamentals|V1-05.04 Neural Network Fundamentals]]
- [[01 Books/Volume I - Foundations/02 Development/05 Neural Computation/V1-05.05 Learning Process|V1-05.05 Learning Process]]
- [[01 Books/Volume I - Foundations/02 Development/05 Neural Computation/V1-05.06 Inference Pipeline|V1-05.06 Inference Pipeline]]
- [[01 Books/Volume I - Foundations/02 Development/05 Neural Computation/V1-05.07 Handwritten Digit Recognition|V1-05.07 Handwritten Digit Recognition]]
- [[01 Books/Volume I - Foundations/02 Development/05 Neural Computation/V1-05.08 D·A·M Reading of Neural Computation|V1-05.08 D·A·M Reading of Neural Computation]]
- [[01 Books/Volume I - Foundations/02 Development/05 Neural Computation/V1-05.09 Fallacies and Pitfalls|V1-05.09 Fallacies and Pitfalls]]
- [[01 Books/Volume I - Foundations/02 Development/05 Neural Computation/V1-05.10 Summary|V1-05.10 Summary]]
- [[01 Books/Volume I - Foundations/02 Development/05 Neural Computation/V1-05.11 Self-Check Answers|V1-05.11 Self-Check Answers]]
- [[01 Books/Volume I - Foundations/02 Development/05 Neural Computation/V1-05.12 Source References|V1-05.12 Source References]]
- [[01 Books/Volume I - Foundations/02 Development/05 Neural Computation/V1-05.13 Footnotes|V1-05.13 Footnotes]]

Next: [[01 Books/Volume I - Foundations/02 Development/05 Neural Computation/V1-05.01 Purpose|V1-05.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/05_nn_computation/05_nn_computation.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol1/05_nn_computation/05_nn_computation.html#sec-neural-computation). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Matrix Multiplication|Matrix Multiplication]]
- [[02 Concepts/Lifecycle/Training & Adaptation/Optimization Algorithm|Optimization Algorithm]]
- [[02 Concepts/Lifecycle/Training & Adaptation/Training Loss|Training Loss]]
- [[02 Concepts/Lifecycle/Training & Adaptation/Training State|Training State]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume I - Foundations/00 Introduction/01 Introduction/V1-01 Introduction|V1-01 Introduction]] — Iron law of ML systems; D·A·M diagnosis; Bitter lesson and bottleneck migration.
- [[01 Books/Volume I - Foundations/01 Foundations/02 System Paradigms/V1-02 System Paradigms|V1-02 System Paradigms]] — Silicon contract; Memory wall; Physical walls set deployment tiers.
- [[01 Books/Volume I - Foundations/01 Foundations/03 ML Lifecycle/V1-03 ML Lifecycle|V1-03 ML Lifecycle]] — Problem framing; Lab-to-field gap.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/05_nn_computation/nn_computation_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume I - Foundations/02 Development/06 Network Architectures/V1-06 Network Architectures|V1-06 Network Architectures]] — Inductive bias buys data and cost; Skip connections and normalization; Autoregressive decode and the KV cache; Every family lowers onto GEMM.
- [[01 Books/Volume I - Foundations/02 Development/07 ML Frameworks/V1-07 ML Frameworks|V1-07 ML Frameworks]] — Reverse-mode autodiff; Dispatch overhead law; Kernel fusion.
- [[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08 Model Training|V1-08 Model Training]] — Training memory at scale; Checkpointing and accumulation; Mixed precision; Training checkpoints; Training-time law.
- [[01 Books/Volume I - Foundations/03 Optimization/09 Data Selection/V1-09 Data Selection|V1-09 Data Selection]] — Compute-optimal frontier.
- [[01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10 Model Compression|V1-10 Model Compression]] — Quantization regimes and the cliff.
- [[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11 Hardware Acceleration|V1-11 Hardware Acceleration]] — Roofline and ridge point; Amdahl's law; Energy ladder; Reduced-precision and sparse datapaths; Tiling.
- [[01 Books/Volume I - Foundations/03 Optimization/12 Benchmarking/V1-12 Benchmarking|V1-12 Benchmarking]] — Quality beyond accuracy; Time to quality target.
- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13 Model Serving|V1-13 Model Serving]] — Batching trades latency for throughput.
- [[01 Books/Volume I - Foundations/04 Deployment/14 ML Operations/V1-14 ML Operations|V1-14 ML Operations]] — Retraining economics.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/05_nn_computation/nn_computation_concepts.yml)

<!-- Semantic Navigation: End -->
