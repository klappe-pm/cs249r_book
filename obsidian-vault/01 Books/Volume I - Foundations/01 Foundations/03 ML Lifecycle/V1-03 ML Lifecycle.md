---
title: V1-03 ML Lifecycle
type: Chapter
volume: 1
chapter: 3
publication_status: Released
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol1/03_ml_lifecycle/03_ml_lifecycle.qmd
source_anchor: sec-ml-workflow
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_1
rendered_source_url: https://mlsysbook.ai/vol1/03_ml_lifecycle/03_ml_lifecycle.html
---

# V1-03 ML Lifecycle

[[Home|Home]] · [[01 Books/Volume I - Foundations/Volume 1 Overview|Volume Overview]]

^sec-ml-workflow

[Lecture slides](https://mlsysbook.ai/slides/vol1.html#ch-03) for this chapter

![[90 Assets/Volume I/03 ML Lifecycle/Cover ML Lifecycle Blueprint Labeled 1d33dc59fb.webp]]

*Isometric blueprint of an ML workflow loop connecting definition, data, training, deployment, monitoring, and feedback around a central model workbench.*

## Chapter Sections

- [[01 Books/Volume I - Foundations/01 Foundations/03 ML Lifecycle/V1-03.01 Purpose|V1-03.01 Purpose]]
- [[01 Books/Volume I - Foundations/01 Foundations/03 ML Lifecycle/V1-03.02 The Lifecycle as a Loop|V1-03.02 The Lifecycle as a Loop]]
- [[01 Books/Volume I - Foundations/01 Foundations/03 ML Lifecycle/V1-03.03 How Decisions Cascade the Constraint Propagation Principle|V1-03.03 How Decisions Cascade the Constraint Propagation Principle]]
- [[01 Books/Volume I - Foundations/01 Foundations/03 ML Lifecycle/V1-03.04 Where the Hours Go Quantifying the ML Lifecycle|V1-03.04 Where the Hours Go Quantifying the ML Lifecycle]]
- [[01 Books/Volume I - Foundations/01 Foundations/03 ML Lifecycle/V1-03.05 Stage Ownership and Hand-Offs|V1-03.05 Stage Ownership and Hand-Offs]]
- [[01 Books/Volume I - Foundations/01 Foundations/03 ML Lifecycle/V1-03.06 Stage 1 Problem Definition|V1-03.06 Stage 1 Problem Definition]]
- [[01 Books/Volume I - Foundations/01 Foundations/03 ML Lifecycle/V1-03.07 Stage 2 Data Collection and Preparation|V1-03.07 Stage 2 Data Collection and Preparation]]
- [[01 Books/Volume I - Foundations/01 Foundations/03 ML Lifecycle/V1-03.08 Stage 3 Model Development and Training|V1-03.08 Stage 3 Model Development and Training]]
- [[01 Books/Volume I - Foundations/01 Foundations/03 ML Lifecycle/V1-03.09 Stage 4 Evaluation and Validation|V1-03.09 Stage 4 Evaluation and Validation]]
- [[01 Books/Volume I - Foundations/01 Foundations/03 ML Lifecycle/V1-03.10 Stage 5 Deployment and Integration|V1-03.10 Stage 5 Deployment and Integration]]
- [[01 Books/Volume I - Foundations/01 Foundations/03 ML Lifecycle/V1-03.11 Stage 6 Monitoring and Maintenance|V1-03.11 Stage 6 Monitoring and Maintenance]]
- [[01 Books/Volume I - Foundations/01 Foundations/03 ML Lifecycle/V1-03.12 Systems Thinking Across the Lifecycle|V1-03.12 Systems Thinking Across the Lifecycle]]
- [[01 Books/Volume I - Foundations/01 Foundations/03 ML Lifecycle/V1-03.13 Fallacies and Pitfalls|V1-03.13 Fallacies and Pitfalls]]
- [[01 Books/Volume I - Foundations/01 Foundations/03 ML Lifecycle/V1-03.14 Summary|V1-03.14 Summary]]
- [[01 Books/Volume I - Foundations/01 Foundations/03 ML Lifecycle/V1-03.15 Self-Check Answers|V1-03.15 Self-Check Answers]]
- [[01 Books/Volume I - Foundations/01 Foundations/03 ML Lifecycle/V1-03.16 Source References|V1-03.16 Source References]]
- [[01 Books/Volume I - Foundations/01 Foundations/03 ML Lifecycle/V1-03.17 Footnotes|V1-03.17 Footnotes]]

Next: [[01 Books/Volume I - Foundations/01 Foundations/03 ML Lifecycle/V1-03.01 Purpose|V1-03.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/03_ml_lifecycle/03_ml_lifecycle.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol1/03_ml_lifecycle/03_ml_lifecycle.html#sec-ml-workflow). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Lifecycle/Data Engineering/Data Contract|Data Contract]]
- [[02 Concepts/Lifecycle/MLOps & Operations/Release Gate|Release Gate]]
- [[02 Concepts/Foundations/Workloads & Requirements/System Requirements|System Requirements]]

## Related Themes

- [[03 Themes/Constraints Drive Architecture|Constraints Drive Architecture]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume I - Foundations/00 Introduction/01 Introduction/V1-01 Introduction|V1-01 Introduction]] — Data defines behavior; Silent degradation; Iron law of ML systems.
- [[01 Books/Volume I - Foundations/01 Foundations/02 System Paradigms/V1-02 System Paradigms|V1-02 System Paradigms]] — Physical walls set deployment tiers; Data locality invariant; Total cost of ownership; Screen then cost; Workload archetypes and lighthouses.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/03_ml_lifecycle/ml_lifecycle_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume I - Foundations/01 Foundations/04 Data Engineering/V1-04 Data Engineering|V1-04 Data Engineering]] — Data cascades; The feeding problem; Data as code practice; Dataset releases and lineage; Drift statistics.
- [[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08 Model Training|V1-08 Model Training]] — Fine-tuning scope.
- [[01 Books/Volume I - Foundations/03 Optimization/12 Benchmarking/V1-12 Benchmarking|V1-12 Benchmarking]] — Quality beyond accuracy; Differences beyond noise.
- [[01 Books/Volume I - Foundations/04 Deployment/14 ML Operations/V1-14 ML Operations|V1-14 ML Operations]] — Safe release and tested rollback; Operations loop; Layered monitoring and detection delay; Reproducibility and the model registry; Hidden technical debt; Retraining economics.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/03_ml_lifecycle/ml_lifecycle_concepts.yml)

<!-- Semantic Navigation: End -->
