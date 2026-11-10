---
title: V1-14 ML Operations
type: Chapter
volume: 1
chapter: 14
publication_status: Released
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol1/14_ml_ops/14_ml_ops.qmd
source_anchor: sec-ml-operations
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_1
rendered_source_url: https://mlsysbook.ai/vol1/14_ml_ops/14_ml_ops.html
---

# V1-14 ML Operations

[[Home|Home]] · [[01 Books/Volume I - Foundations/Volume 1 Overview|Volume Overview]]

^sec-ml-operations

Lecture slides for this chapter: [Part 1](https://mlsysbook.ai/slides/vol1.html#lec-14) · [Part 2](https://mlsysbook.ai/slides/vol1.html#lec-14b)

![[90 Assets/Volume I/14 ML Ops/Cover ML Ops Blueprint Labeled 9aafbc1043.webp]]

*Isometric operations loop around a deployed model service with telemetry, monitoring, drift response, retraining, and deployment updates.*

## Chapter Sections

- [[01 Books/Volume I - Foundations/04 Deployment/14 ML Operations/V1-14.01 Purpose|V1-14.01 Purpose]]
- [[01 Books/Volume I - Foundations/04 Deployment/14 ML Operations/V1-14.02 Silent Failure in Production|V1-14.02 Silent Failure in Production]]
- [[01 Books/Volume I - Foundations/04 Deployment/14 ML Operations/V1-14.03 Technical Debt|V1-14.03 Technical Debt]]
- [[01 Books/Volume I - Foundations/04 Deployment/14 ML Operations/V1-14.04 Development Infrastructure|V1-14.04 Development Infrastructure]]
- [[01 Books/Volume I - Foundations/04 Deployment/14 ML Operations/V1-14.05 Releasing Models|V1-14.05 Releasing Models]]
- [[01 Books/Volume I - Foundations/04 Deployment/14 ML Operations/V1-14.06 Production Monitoring|V1-14.06 Production Monitoring]]
- [[01 Books/Volume I - Foundations/04 Deployment/14 ML Operations/V1-14.07 Retraining Decisions|V1-14.07 Retraining Decisions]]
- [[01 Books/Volume I - Foundations/04 Deployment/14 ML Operations/V1-14.08 Incident Response and Governance|V1-14.08 Incident Response and Governance]]
- [[01 Books/Volume I - Foundations/04 Deployment/14 ML Operations/V1-14.09 Operational Maturity|V1-14.09 Operational Maturity]]
- [[01 Books/Volume I - Foundations/04 Deployment/14 ML Operations/V1-14.10 Case Studies|V1-14.10 Case Studies]]
- [[01 Books/Volume I - Foundations/04 Deployment/14 ML Operations/V1-14.11 Fallacies and Pitfalls|V1-14.11 Fallacies and Pitfalls]]
- [[01 Books/Volume I - Foundations/04 Deployment/14 ML Operations/V1-14.12 Summary|V1-14.12 Summary]]
- [[01 Books/Volume I - Foundations/04 Deployment/14 ML Operations/V1-14.13 Self-Check Answers|V1-14.13 Self-Check Answers]]
- [[01 Books/Volume I - Foundations/04 Deployment/14 ML Operations/V1-14.14 Source References|V1-14.14 Source References]]
- [[01 Books/Volume I - Foundations/04 Deployment/14 ML Operations/V1-14.15 Footnotes|V1-14.15 Footnotes]]

Next: [[01 Books/Volume I - Foundations/04 Deployment/14 ML Operations/V1-14.01 Purpose|V1-14.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/14_ml_ops/14_ml_ops.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol1/14_ml_ops/14_ml_ops.html#sec-ml-operations). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Lifecycle/MLOps & Operations/Distribution Shift|Distribution Shift]]
- [[02 Concepts/Lifecycle/MLOps & Operations/Drift Detection|Drift Detection]]
- [[02 Concepts/Lifecycle/MLOps & Operations/Production Monitoring|Production Monitoring]]
- [[02 Concepts/Lifecycle/MLOps & Operations/Rollback|Rollback]]

## Related Themes

- [[03 Themes/Reliability and Recovery|Reliability and Recovery]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume I - Foundations/00 Introduction/01 Introduction/V1-01 Introduction|V1-01 Introduction]] — Silent degradation; Iron law of ML systems; D·A·M diagnosis.
- [[01 Books/Volume I - Foundations/01 Foundations/02 System Paradigms/V1-02 System Paradigms|V1-02 System Paradigms]] — Physical walls set deployment tiers.
- [[01 Books/Volume I - Foundations/01 Foundations/03 ML Lifecycle/V1-03 ML Lifecycle|V1-03 ML Lifecycle]] — The lifecycle is a loop; Validation as the release decision.
- [[01 Books/Volume I - Foundations/01 Foundations/04 Data Engineering/V1-04 Data Engineering|V1-04 Data Engineering]] — Training-serving consistency; Drift statistics; Dataset releases and lineage; Data cascades; Data debt.
- [[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08 Model Training|V1-08 Model Training]] — Single-node data parallelism; Training checkpoints; Model FLOPs utilization.
- [[01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10 Model Compression|V1-10 Model Compression]] — Quantization regimes and the cliff; Accuracy-efficiency frontier.
- [[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11 Hardware Acceleration|V1-11 Hardware Acceleration]] — Roofline and ridge point; Amdahl's law.
- [[01 Books/Volume I - Foundations/03 Optimization/12 Benchmarking/V1-12 Benchmarking|V1-12 Benchmarking]] — Verification gap; Differences beyond noise.
- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13 Model Serving|V1-13 Model Serving]] — Latency budget; Queueing sets headroom; Static vs dynamic inference; KV cache budget bounds concurrency; Serving economics; Runtime and precision selection.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/14_ml_ops/ml_ops_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume I - Foundations/04 Deployment/15 Responsible Engineering/V1-15 Responsible Engineering|V1-15 Responsible Engineering]] — Bias feedback loops; Fairness criteria for release; Privacy and governance as architecture; Explanation cost on the serving path.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/14_ml_ops/ml_ops_concepts.yml)

<!-- Semantic Navigation: End -->
