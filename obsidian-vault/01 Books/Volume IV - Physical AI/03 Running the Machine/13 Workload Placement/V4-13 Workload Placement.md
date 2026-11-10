---
title: V4-13 Workload Placement
type: Chapter
volume: 4
chapter: 13
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol4/13_placement/13_placement.qmd
source_anchor: sec-placement
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_4
rendered_source_url: https://mlsysbook.ai/vol4/13_placement/13_placement.html
---

# V4-13 Workload Placement

[[Home|Home]] · [[01 Books/Volume IV - Physical AI/Volume 4 Overview|Volume Overview]]

^sec-placement

[Lecture slides](https://mlsysbook.ai/slides/vol4.html#ch-13) for this chapter

![[90 Assets/Volume IV/13 Placement/Cover Placement Blueprint Labeled 7454b3eb0e.webp]]

*Isometric blueprint showing silicon placement: heterogeneous physical AI SoC with a neural accelerator cluster for the learned models, 3D memory stacks, perimeter thermal dissipation fins, shared interconnect crossbar bus, isolated deterministic real-time MCU enclave, and crimson QoS isolation trench.*

## Chapter Sections

- [[01 Books/Volume IV - Physical AI/03 Running the Machine/13 Workload Placement/V4-13.01 Purpose|V4-13.01 Purpose]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/13 Workload Placement/V4-13.02 The Silicon Substrate|V4-13.02 The Silicon Substrate]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/13 Workload Placement/V4-13.03 Two Paths and the Resources They Share|V4-13.03 Two Paths and the Resources They Share]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/13 Workload Placement/V4-13.04 Contention for Shared Resources|V4-13.04 Contention for Shared Resources]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/13 Workload Placement/V4-13.05 Thermal and Timing Coupling|V4-13.05 Thermal and Timing Coupling]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/13 Workload Placement/V4-13.06 The Boundary Contract|V4-13.06 The Boundary Contract]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/13 Workload Placement/V4-13.07 Silicon Isolation Decisions|V4-13.07 Silicon Isolation Decisions]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/13 Workload Placement/V4-13.08 Empirical Verification of Silicon Isolation|V4-13.08 Empirical Verification of Silicon Isolation]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/13 Workload Placement/V4-13.09 The Placement Record|V4-13.09 The Placement Record]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/13 Workload Placement/V4-13.10 Fallacies and Pitfalls|V4-13.10 Fallacies and Pitfalls]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/13 Workload Placement/V4-13.11 Summary|V4-13.11 Summary]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/13 Workload Placement/V4-13.12 Historical Perspective and Further Reading|V4-13.12 Historical Perspective and Further Reading]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/13 Workload Placement/V4-13.13 Source References|V4-13.13 Source References]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/13 Workload Placement/V4-13.14 Footnotes|V4-13.14 Footnotes]]

Next: [[01 Books/Volume IV - Physical AI/03 Running the Machine/13 Workload Placement/V4-13.01 Purpose|V4-13.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/13_placement/13_placement.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol4/13_placement/13_placement.html#sec-placement). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Qualities/Security & Privacy/Execution Isolation|Execution Isolation]]
- [[02 Concepts/Stack/Hardware & Accelerators/Thermal Behavior and Throttling|Thermal Behavior and Throttling]]
- [[02 Concepts/System Types/Embodied & Physical Systems/Worst Case Execution Time|Worst Case Execution Time]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume IV - Physical AI/00 Introduction/01 The Causal Boundary/V4-01 The Causal Boundary|V4-01 The Causal Boundary]] — Proposal boundary; Irreversibility and recovery; Causal boundary.
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/02 The Physical Body/V4-02 The Physical Body|V4-02 The Physical Body]] — Shared-rail power integrity; Thermal duty limits.
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/03 The Cognitive Brain/V4-03 The Cognitive Brain|V4-03 The Cognitive Brain]] — Memory-wall renewal ceiling; Quantized model is a new model; Two-speed brain.
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/04 The Nervous System/V4-04 The Nervous System|V4-04 The Nervous System]] — Independence requirement; Worst-case execution time; Response bound not percentile; Freshest-proposal mailbox; Authority-expiry timers; Chunk lease; Handoff record and event timing; Safety microcontroller.
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/08 Sensor Perception/V4-08 Sensor Perception|V4-08 Sensor Perception]] — Observation age; Latency waterfall.
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/09 Spatial Memory/V4-09 Spatial Memory|V4-09 Spatial Memory]] — Representation follows the query.
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/11 Trajectory Planning/V4-11 Trajectory Planning|V4-11 Trajectory Planning]] — Trajectory record.
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12 Safety Enforcement|V4-12 Safety Enforcement]] — Stopping envelope; State-matched fallback ladder; Certified floor beneath an unrated layer; Enforcement record.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/13_placement/placement_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/14 Supervisory Intervention/V4-14 Supervisory Intervention|V4-14 Supervisory Intervention]] — Takeover delay in the stopping budget.
- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/15 Adversarial Verification/V4-15 Adversarial Verification|V4-15 Adversarial Verification]] — Fault-list derivation.
- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/16 Deployment Release/V4-16 Deployment Release|V4-16 Deployment Release]] — Certification authorizes a configuration; Safety case.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/13_placement/placement_concepts.yml)

<!-- Semantic Navigation: End -->
