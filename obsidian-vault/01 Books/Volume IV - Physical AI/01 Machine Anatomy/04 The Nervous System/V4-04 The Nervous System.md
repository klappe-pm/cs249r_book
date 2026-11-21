---
title: V4-04 The Nervous System
type: Chapter
volume: 4
chapter: 4
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol4/04_nervous/04_nervous.qmd
source_anchor: sec-nervous
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_4
rendered_source_url: https://mlsysbook.ai/vol4/04_nervous/04_nervous.html
---

# V4-04 The Nervous System

[[Home|Home]] · [[01 Books/Volume IV - Physical AI/Volume 4 Overview|Volume Overview]]

^sec-nervous

[Lecture slides](https://mlsysbook.ai/slides/vol4.html#ch-04) for this chapter

![[90 Assets/Volume IV/04 Nervous/Cover Nervous Blueprint Labeled c6747877c3.webp]]

*Isometric blueprint showing the Nervous System architecture: embedded real-time MCU, 1 kHz clock and jitter monitor, shielded real-time network ring, shared SRAM seqlock mailbox, and control barrier reflex filter.*

## Chapter Sections

- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/04 The Nervous System/V4-04.01 Purpose|V4-04.01 Purpose]]
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/04 The Nervous System/V4-04.02 The Multi-Rate Bridge|V4-04.02 The Multi-Rate Bridge]]
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/04 The Nervous System/V4-04.03 The Independence Requirement and the Two-Processor Hypothesis|V4-04.03 The Independence Requirement and the Two-Processor Hypothesis]]
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/04 The Nervous System/V4-04.04 Multi-Rate Cadences|V4-04.04 Multi-Rate Cadences]]
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/04 The Nervous System/V4-04.05 Chunk Lease Sizing from the Stopping Budget|V4-04.05 Chunk Lease Sizing from the Stopping Budget]]
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/04 The Nervous System/V4-04.06 Real-Time Command Transport and Bus Determinism|V4-04.06 Real-Time Command Transport and Bus Determinism]]
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/04 The Nervous System/V4-04.07 Actuation Authority|V4-04.07 Actuation Authority]]
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/04 The Nervous System/V4-04.08 Hardware Isolation and Fault Containment|V4-04.08 Hardware Isolation and Fault Containment]]
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/04 The Nervous System/V4-04.09 Invariant Checking|V4-04.09 Invariant Checking]]
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/04 The Nervous System/V4-04.10 The Handoffs Matrix|V4-04.10 The Handoffs Matrix]]
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/04 The Nervous System/V4-04.11 Fallacies and Pitfalls|V4-04.11 Fallacies and Pitfalls]]
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/04 The Nervous System/V4-04.12 Summary|V4-04.12 Summary]]
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/04 The Nervous System/V4-04.13 Historical Perspective and Further Reading|V4-04.13 Historical Perspective and Further Reading]]
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/04 The Nervous System/V4-04.14 Source References|V4-04.14 Source References]]
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/04 The Nervous System/V4-04.15 Footnotes|V4-04.15 Footnotes]]

Next: [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/04 The Nervous System/V4-04.01 Purpose|V4-04.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/04_nervous/04_nervous.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol4/04_nervous/04_nervous.html#sec-nervous). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/System Types/Embodied & Physical Systems/Feedback Control|Feedback Control]]
- [[02 Concepts/System Types/Embodied & Physical Systems/Feedback Delay|Feedback Delay]]
- [[02 Concepts/Stack/Parallelism & Distributed Execution/Lease|Lease]]
- [[02 Concepts/System Types/Embodied & Physical Systems/Real Time Scheduling|Real Time Scheduling]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume IV - Physical AI/00 Introduction/01 The Causal Boundary/V4-01 The Causal Boundary|V4-01 The Causal Boundary]] — Causal boundary; Irreversibility and recovery; Proposal boundary; Five-level machine; Elementary stopping budget.
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/02 The Physical Body/V4-02 The Physical Body|V4-02 The Physical Body]] — Reflected rotor inertia; Velocity ceiling; Measurement freshness deadline; Four boundary events; Virtual spring-damper; Shared-rail power integrity; Thermal duty limits; Limit record.
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/03 The Cognitive Brain/V4-03 The Cognitive Brain|V4-03 The Cognitive Brain]] — Two-speed brain; Memory-wall renewal ceiling; Proposal payload.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/04_nervous/nervous_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05 Physical Data|V4-05 Physical Data]] — Action-label semantics.
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/08 Sensor Perception/V4-08 Sensor Perception|V4-08 Sensor Perception]] — Observation age.
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/10 Grounded Intent/V4-10 Grounded Intent|V4-10 Grounded Intent]] — Expiring intent lease.
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/11 Trajectory Planning/V4-11 Trajectory Planning|V4-11 Trajectory Planning]] — Replacement latency and handoff tail.
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12 Safety Enforcement|V4-12 Safety Enforcement]] — Stopping envelope; Kinetic barrier; Certified floor beneath an unrated layer; Functional-safety integrity grading.
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/13 Workload Placement/V4-13 Workload Placement|V4-13 Workload Placement]] — Mixed-criticality scheduling; Priced remediation ladder; Dispatch-to-admission allocation.
- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/14 Supervisory Intervention/V4-14 Supervisory Intervention|V4-14 Supervisory Intervention]] — Authenticating interventions.
- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/15 Adversarial Verification/V4-15 Adversarial Verification|V4-15 Adversarial Verification]] — Fault-list derivation.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/04_nervous/nervous_concepts.yml)

<!-- Semantic Navigation: End -->
