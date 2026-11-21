---
title: V2-14 Robust AI
type: Chapter
volume: 2
chapter: 14
publication_status: Preview
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol2/14_robust_ai/14_robust_ai.qmd
source_anchor: sec-robust-ai
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_2
rendered_source_url: https://mlsysbook.ai/vol2/14_robust_ai/14_robust_ai.html
---

# V2-14 Robust AI

[[Home|Home]] · [[01 Books/Volume II - Scaling/Volume 2 Overview|Volume Overview]]

^sec-robust-ai

[Lecture slides](https://mlsysbook.ai/slides/vol2.html#ch-14) for this chapter

![[90 Assets/Volume II/14 Robust AI/Cover Robust AI Blueprint Labeled 3f241e2a64.webp]]

*Robust AI test chamber where a model service is exposed to drift, adversarial perturbation, and faults while monitors route adaptation and recovery.*

## Chapter Sections

- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/14 Robust AI/V2-14.01 Purpose|V2-14.01 Purpose]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/14 Robust AI/V2-14.02 The Silent Failure Problem|V2-14.02 The Silent Failure Problem]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/14 Robust AI/V2-14.03 Real-World Robustness Failures|V2-14.03 Real-World Robustness Failures]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/14 Robust AI/V2-14.04 A Unified Framework for Robust AI|V2-14.04 A Unified Framework for Robust AI]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/14 Robust AI/V2-14.05 Environmental Shifts|V2-14.05 Environmental Shifts]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/14 Robust AI/V2-14.06 Adversarial Attacks|V2-14.06 Adversarial Attacks]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/14 Robust AI/V2-14.07 Adversarial Defenses|V2-14.07 Adversarial Defenses]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/14 Robust AI/V2-14.08 Data Poisoning Defenses|V2-14.08 Data Poisoning Defenses]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/14 Robust AI/V2-14.09 Robustness of Generative Models|V2-14.09 Robustness of Generative Models]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/14 Robust AI/V2-14.10 System-Level Faults|V2-14.10 System-Level Faults]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/14 Robust AI/V2-14.11 Fallacies and Pitfalls|V2-14.11 Fallacies and Pitfalls]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/14 Robust AI/V2-14.12 Summary|V2-14.12 Summary]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/14 Robust AI/V2-14.13 Self-Check Answers|V2-14.13 Self-Check Answers]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/14 Robust AI/V2-14.14 Source References|V2-14.14 Source References]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/14 Robust AI/V2-14.15 Footnotes|V2-14.15 Footnotes]]

Next: [[01 Books/Volume II - Scaling/04 The Responsible Fleet/14 Robust AI/V2-14.01 Purpose|V2-14.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/14_robust_ai/14_robust_ai.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol2/14_robust_ai/14_robust_ai.html#sec-robust-ai). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Lifecycle/MLOps & Operations/Concept Drift|Concept Drift]]
- [[02 Concepts/Lifecycle/Model Evaluation & Testing/Conformal Prediction|Conformal Prediction]]
- [[02 Concepts/Lifecycle/MLOps & Operations/Distribution Shift|Distribution Shift]]
- [[02 Concepts/Lifecycle/Model Evaluation & Testing/Selective Prediction|Selective Prediction]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume II - Scaling/00 Introduction/01 Introduction/V2-01 Introduction|V2-01 Introduction]] — Fleet Law.
- [[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06 Distributed Training|V2-06 Distributed Training]] — Data-parallel update equivalence.
- [[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07 Fault Tolerance|V2-07 Fault Tolerance]] — Fault classification by persistence, manifestation, and scope; Silent data corruption verification; Graceful degradation ladder.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/11 Edge Intelligence/V2-11 Edge Intelligence|V2-11 Edge Intelligence]] — On-device drift and forgetting.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/12 ML Operations at Scale/V2-12 ML Operations at Scale|V2-12 ML Operations at Scale]] — Evaluation contract; Hierarchical fleet alerting.
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/13 Security & Privacy/V2-13 Security & Privacy|V2-13 Security & Privacy]] — ML threat model; Poisoning as a bilevel attack; Breakdown point of the gradient mean.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/14_robust_ai/robust_ai_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/15 Sustainable AI/V2-15 Sustainable AI|V2-15 Sustainable AI]] — Power ceiling versus energy account.
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/16 Responsible AI/V2-16 Responsible AI|V2-16 Responsible AI]] — Sociotechnical feedback and designed oversight; Assurance case.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/14_robust_ai/robust_ai_concepts.yml)

<!-- Semantic Navigation: End -->
