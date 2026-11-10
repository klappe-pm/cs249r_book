---
title: V4-05 Physical Data
type: Chapter
volume: 4
chapter: 5
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol4/05_data/05_data.qmd
source_anchor: sec-data
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_4
rendered_source_url: https://mlsysbook.ai/vol4/05_data/05_data.html
---

# V4-05 Physical Data

[[Home|Home]] · [[01 Books/Volume IV - Physical AI/Volume 4 Overview|Volume Overview]]

^sec-data

[Lecture slides](https://mlsysbook.ai/slides/vol4.html#ch-05) for this chapter

![[90 Assets/Volume IV/05 Data/Cover Data Blueprint Labeled 903cd58b1f.webp]]

*Isometric blueprint showing the physical data and ingestion pipeline: bilateral teleoperation leader arm, 6-axis operator load cell, calibrated stereo vision sensor head, micro-lidar rangefinder, optical calibration checkerboard, and deterministic flash logger.*

## Chapter Sections

- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05.01 Purpose|V4-05.01 Purpose]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05.02 Endogenous Experience|V4-05.02 Endogenous Experience]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05.03 Mechanics of Endogenous Covariate Shift|V4-05.03 Mechanics of Endogenous Covariate Shift]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05.04 Recovery and Compounding Error|V4-05.04 Recovery and Compounding Error]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05.05 Physical Telemetry Sources and Collection Paths|V4-05.05 Physical Telemetry Sources and Collection Paths]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05.06 Action Label Selection Across the Control Boundary|V4-05.06 Action Label Selection Across the Control Boundary]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05.07 Teleoperation Demonstration Costs|V4-05.07 Teleoperation Demonstration Costs]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05.08 Collection Policy Coverage|V4-05.08 Collection Policy Coverage]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05.09 Intervention and Recovery Data|V4-05.09 Intervention and Recovery Data]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05.10 Cross-Embodiment Transfer|V4-05.10 Cross-Embodiment Transfer]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05.11 Dataset Degradation and Physical Distribution Shift|V4-05.11 Dataset Degradation and Physical Distribution Shift]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05.12 The Dataset Schema|V4-05.12 The Dataset Schema]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05.13 Fallacies and Pitfalls|V4-05.13 Fallacies and Pitfalls]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05.14 Summary|V4-05.14 Summary]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05.15 Historical Perspective and Further Reading|V4-05.15 Historical Perspective and Further Reading]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05.16 Source References|V4-05.16 Source References]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05.17 Footnotes|V4-05.17 Footnotes]]

Next: [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05.01 Purpose|V4-05.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/05_data/05_data.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol4/05_data/05_data.html#sec-data). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Lifecycle/Training & Adaptation/Compounding Error in Sequential Decisions|Compounding Error in Sequential Decisions]]
- [[02 Concepts/Lifecycle/MLOps & Operations/Distribution Shift|Distribution Shift]]
- [[02 Concepts/Lifecycle/Training & Adaptation/Interactive Imitation Learning|Interactive Imitation Learning]]
- [[02 Concepts/Qualities/Safety & Assurance/Operational Design Domain|Operational Design Domain]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume IV - Physical AI/00 Introduction/01 The Causal Boundary/V4-01 The Causal Boundary|V4-01 The Causal Boundary]] — Irreversibility and recovery; Proposal boundary; Elementary stopping budget.
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/02 The Physical Body/V4-02 The Physical Body|V4-02 The Physical Body]] — Limit record; Thermal duty limits; Reflected rotor inertia; Delivered torque ceiling.
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/03 The Cognitive Brain/V4-03 The Cognitive Brain|V4-03 The Cognitive Brain]] — Chunking is a supply lever.
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/04 The Nervous System/V4-04 The Nervous System|V4-04 The Nervous System]] — Handoff record and event timing.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/05_data/data_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06 Policy Training|V4-06 Policy Training]] — Reward as specification; Reality gap as a vector; Simulator contact exploit; Physical RL exploration cost; Policy manifest.
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07 Closed-Loop Evaluation|V4-07 Closed-Loop Evaluation]] — Predeclared trial protocol.
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/08 Sensor Perception/V4-08 Sensor Perception|V4-08 Sensor Perception]] — Capture epoch.
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/11 Trajectory Planning/V4-11 Trajectory Planning|V4-11 Trajectory Planning]] — Kinodynamic feasibility; Manipulator Jacobian.
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12 Safety Enforcement|V4-12 Safety Enforcement]] — Kinetic barrier.
- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/14 Supervisory Intervention/V4-14 Supervisory Intervention|V4-14 Supervisory Intervention]] — Takeover delay in the stopping budget; Authority record.
- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/16 Deployment Release/V4-16 Deployment Release|V4-16 Deployment Release]] — Release manifest.
- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/17 Responsible Physical AI/V4-17 Responsible Physical AI|V4-17 Responsible Physical AI]] — Recorded people; Worker burden.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/05_data/data_concepts.yml)

<!-- Semantic Navigation: End -->
