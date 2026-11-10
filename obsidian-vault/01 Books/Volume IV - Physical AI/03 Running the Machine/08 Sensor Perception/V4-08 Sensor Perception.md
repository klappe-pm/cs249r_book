---
title: V4-08 Sensor Perception
type: Chapter
volume: 4
chapter: 8
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol4/08_perception/08_perception.qmd
source_anchor: sec-perception
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_4
rendered_source_url: https://mlsysbook.ai/vol4/08_perception/08_perception.html
---

# V4-08 Sensor Perception

[[Home|Home]] · [[01 Books/Volume IV - Physical AI/Volume 4 Overview|Volume Overview]]

^sec-perception

[Lecture slides](https://mlsysbook.ai/slides/vol4.html#ch-08) for this chapter

![[90 Assets/Volume IV/08 Perception/Cover Perception Blueprint Labeled db52a44d1a.webp]]

*Isometric blueprint showing multimodal sensor perception: stereo optical camera rail with sightline frustums, solid-state micro-lidar point cloud fan, precision calibration target with coordinate axes, dynamic uncertainty covariance ellipsoid, and latency drift vector.*

## Chapter Sections

- [[01 Books/Volume IV - Physical AI/03 Running the Machine/08 Sensor Perception/V4-08.01 Purpose|V4-08.01 Purpose]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/08 Sensor Perception/V4-08.02 Choosing Evidence for a Spatial Decision|V4-08.02 Choosing Evidence for a Spatial Decision]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/08 Sensor Perception/V4-08.03 Capture Physics and Calibration|V4-08.03 Capture Physics and Calibration]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/08 Sensor Perception/V4-08.04 Dating and Placing the Measurement|V4-08.04 Dating and Placing the Measurement]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/08 Sensor Perception/V4-08.05 Bounding Observation Age|V4-08.05 Bounding Observation Age]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/08 Sensor Perception/V4-08.06 Ingestion Overhead and Memory Bus Contention|V4-08.06 Ingestion Overhead and Memory Bus Contention]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/08 Sensor Perception/V4-08.07 Spatial Error and Clearance Bounds|V4-08.07 Spatial Error and Clearance Bounds]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/08 Sensor Perception/V4-08.08 Perception Failure Modes and Sensor Degradation|V4-08.08 Perception Failure Modes and Sensor Degradation]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/08 Sensor Perception/V4-08.09 The Observation Contract|V4-08.09 The Observation Contract]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/08 Sensor Perception/V4-08.10 Fallacies and Pitfalls|V4-08.10 Fallacies and Pitfalls]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/08 Sensor Perception/V4-08.11 Summary|V4-08.11 Summary]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/08 Sensor Perception/V4-08.12 Historical Perspective and Further Reading|V4-08.12 Historical Perspective and Further Reading]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/08 Sensor Perception/V4-08.13 Source References|V4-08.13 Source References]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/08 Sensor Perception/V4-08.14 Footnotes|V4-08.14 Footnotes]]

Next: [[01 Books/Volume IV - Physical AI/03 Running the Machine/08 Sensor Perception/V4-08.01 Purpose|V4-08.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/08_perception/08_perception.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol4/08_perception/08_perception.html#sec-perception). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/System Types/Embodied & Physical Systems/Observation Age|Observation Age]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume IV - Physical AI/00 Introduction/01 The Causal Boundary/V4-01 The Causal Boundary|V4-01 The Causal Boundary]] — Causal boundary; Proposal boundary; Record chain; Elementary stopping budget.
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/02 The Physical Body/V4-02 The Physical Body|V4-02 The Physical Body]] — Measurement freshness deadline.
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/03 The Cognitive Brain/V4-03 The Cognitive Brain|V4-03 The Cognitive Brain]] — Softmax illusion.
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/04 The Nervous System/V4-04 The Nervous System|V4-04 The Nervous System]] — Chunk lease; Handoff record and event timing; Delay spends phase margin.
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05 Physical Data|V4-05 Physical Data]] — Action-label semantics; Compounding error and recoverability; Operational design domain.
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07 Closed-Loop Evaluation|V4-07 Closed-Loop Evaluation]] — Evaluation record; Runtime monitor channels.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/08_perception/perception_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume IV - Physical AI/03 Running the Machine/09 Spatial Memory/V4-09 Spatial Memory|V4-09 Spatial Memory]] — Recursive estimation on dated measurements; Frames age; Occlusion and free-space erosion.
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/11 Trajectory Planning/V4-11 Trajectory Planning|V4-11 Trajectory Planning]] — Jerk-limited stopping suffix.
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12 Safety Enforcement|V4-12 Safety Enforcement]] — Certified floor beneath an unrated layer; Stopping envelope.
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/13 Workload Placement/V4-13 Workload Placement|V4-13 Workload Placement]] — Dispatch-to-admission allocation; Memory contention and miss handling.
- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/15 Adversarial Verification/V4-15 Adversarial Verification|V4-15 Adversarial Verification]] — Qualification ladder.
- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/17 Responsible Physical AI/V4-17 Responsible Physical AI|V4-17 Responsible Physical AI]] — Detection gaps become stopping gaps.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/08_perception/perception_concepts.yml)

<!-- Semantic Navigation: End -->
