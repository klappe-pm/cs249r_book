---
title: V4-06 Policy Training
type: Chapter
volume: 4
chapter: 6
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol4/06_training/06_training.qmd
source_anchor: sec-training
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_4
rendered_source_url: https://mlsysbook.ai/vol4/06_training/06_training.html
---

# V4-06 Policy Training

[[Home|Home]] · [[01 Books/Volume IV - Physical AI/Volume 4 Overview|Volume Overview]]

^sec-training

[Lecture slides](https://mlsysbook.ai/slides/vol4.html#ch-06) for this chapter

![[90 Assets/Volume IV/06 Training/Cover Training Blueprint Labeled 95151a8b9f.webp]]

*Isometric blueprint showing sim-to-real policy training for an agile quadruped robot: a virtual physics digital twin in a simulation grid with randomized friction cones, a central domain randomization prism, and a physical quadruped on an instrumented dynamometer treadmill with real-time telemetry.*

## Chapter Sections

- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06.01 Purpose|V4-06.01 Purpose]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06.02 Dual Failure Modes of Policy Training|V4-06.02 Dual Failure Modes of Policy Training]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06.03 Policy Training Regimes|V4-06.03 Policy Training Regimes]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06.04 Reinforcement Learning and Environment Interaction|V4-06.04 Reinforcement Learning and Environment Interaction]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06.05 The Simulator as a System Component|V4-06.05 The Simulator as a System Component]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06.06 Physical Channels of the Sim-To-Real Gap|V4-06.06 Physical Channels of the Sim-To-Real Gap]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06.07 Real-Robot Fine-Tuning and Residual Control|V4-06.07 Real-Robot Fine-Tuning and Residual Control]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06.08 Training Failure Modes and Permission-Path Interceptors|V4-06.08 Training Failure Modes and Permission-Path Interceptors]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06.09 The Policy Manifest|V4-06.09 The Policy Manifest]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06.10 Fallacies and Pitfalls|V4-06.10 Fallacies and Pitfalls]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06.11 Summary|V4-06.11 Summary]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06.12 Historical Perspective and Further Reading|V4-06.12 Historical Perspective and Further Reading]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06.13 Source References|V4-06.13 Source References]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06.14 Footnotes|V4-06.14 Footnotes]]

Next: [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06.01 Purpose|V4-06.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/06_training/06_training.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol4/06_training/06_training.html#sec-training). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/System Types/Embodied & Physical Systems/Domain Randomization|Domain Randomization]]
- [[02 Concepts/System Types/Embodied & Physical Systems/Simulation to Real Transfer|Simulation to Real Transfer]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume IV - Physical AI/00 Introduction/01 The Causal Boundary/V4-01 The Causal Boundary|V4-01 The Causal Boundary]] — Proposal boundary; Irreversibility and recovery; Elementary stopping budget.
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/02 The Physical Body/V4-02 The Physical Body|V4-02 The Physical Body]] — Thermal duty limits; Transmission compliance and backlash.
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/03 The Cognitive Brain/V4-03 The Cognitive Brain|V4-03 The Cognitive Brain]] — Chunking is a supply lever; Memory-wall renewal ceiling; Two-speed brain; Temporal ensembling and real-time chunking.
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/04 The Nervous System/V4-04 The Nervous System|V4-04 The Nervous System]] — Chunk lease; Delay spends phase margin.
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05 Physical Data|V4-05 Physical Data]] — Behavioral cloning; Action-label semantics; Compounding error and recoverability; Intervention curation; Operational design domain; Provenance record; Embodiment contract; Demonstration yield and wear.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/06_training/training_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07 Closed-Loop Evaluation|V4-07 Closed-Loop Evaluation]] — Evaluation record.
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/11 Trajectory Planning/V4-11 Trajectory Planning|V4-11 Trajectory Planning]] — Kinodynamic feasibility.
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12 Safety Enforcement|V4-12 Safety Enforcement]] — State-matched fallback ladder; Minimal-intervention filter.
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/13 Workload Placement/V4-13 Workload Placement|V4-13 Workload Placement]] — Per-resource independence inventory.
- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/14 Supervisory Intervention/V4-14 Supervisory Intervention|V4-14 Supervisory Intervention]] — Bumpless transfer; Causal intervention masking; Authority record.
- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/15 Adversarial Verification/V4-15 Adversarial Verification|V4-15 Adversarial Verification]] — Fault-list derivation.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/06_training/training_concepts.yml)

<!-- Semantic Navigation: End -->
