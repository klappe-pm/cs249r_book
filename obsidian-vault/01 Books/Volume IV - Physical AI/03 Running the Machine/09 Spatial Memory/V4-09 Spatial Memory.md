---
title: V4-09 Spatial Memory
type: Chapter
volume: 4
chapter: 9
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol4/09_memory/09_memory.qmd
source_anchor: sec-memory
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_4
rendered_source_url: https://mlsysbook.ai/vol4/09_memory/09_memory.html
---

# V4-09 Spatial Memory

[[Home|Home]] · [[01 Books/Volume IV - Physical AI/Volume 4 Overview|Volume Overview]]

^sec-memory

[Lecture slides](https://mlsysbook.ai/slides/vol4.html#ch-09) for this chapter

![[90 Assets/Volume IV/09 Memory/Cover Memory Blueprint Labeled aab42ddc53.webp]]

*Isometric blueprint showing persistent spatial memory: tiered octree 3D voxel grid with fresh observation updates, frosted glass occlusion divider, floating spatial belief decay uncertainty halos, cylindrical lease store, and crimson stale token eviction basin.*

## Chapter Sections

- [[01 Books/Volume IV - Physical AI/03 Running the Machine/09 Spatial Memory/V4-09.01 Purpose|V4-09.01 Purpose]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/09 Spatial Memory/V4-09.02 Spatial Belief Persistence and Expiry|V4-09.02 Spatial Belief Persistence and Expiry]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/09 Spatial Memory/V4-09.03 Estimating State from Dated Measurements|V4-09.03 Estimating State from Dated Measurements]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/09 Spatial Memory/V4-09.04 The Spatial Memory Handoff and State Invariants|V4-09.04 The Spatial Memory Handoff and State Invariants]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/09 Spatial Memory/V4-09.05 State Epochs and Temporal Anchoring|V4-09.05 State Epochs and Temporal Anchoring]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/09 Spatial Memory/V4-09.06 Coordinate Transform Expiry and Localization Drift|V4-09.06 Coordinate Transform Expiry and Localization Drift]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/09 Spatial Memory/V4-09.07 Certified Spatial Assertions in Scene Memory|V4-09.07 Certified Spatial Assertions in Scene Memory]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/09 Spatial Memory/V4-09.08 Forward State Propagation and Occlusion Decay|V4-09.08 Forward State Propagation and Occlusion Decay]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/09 Spatial Memory/V4-09.09 Observability Ceilings and Estimation Limits|V4-09.09 Observability Ceilings and Estimation Limits]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/09 Spatial Memory/V4-09.10 Spatial Belief Failure Modes and Map Corruption|V4-09.10 Spatial Belief Failure Modes and Map Corruption]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/09 Spatial Memory/V4-09.11 The Belief Record Schema|V4-09.11 The Belief Record Schema]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/09 Spatial Memory/V4-09.12 Fallacies and Pitfalls|V4-09.12 Fallacies and Pitfalls]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/09 Spatial Memory/V4-09.13 Summary|V4-09.13 Summary]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/09 Spatial Memory/V4-09.14 Historical Perspective and Further Reading|V4-09.14 Historical Perspective and Further Reading]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/09 Spatial Memory/V4-09.15 Source References|V4-09.15 Source References]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/09 Spatial Memory/V4-09.16 Footnotes|V4-09.16 Footnotes]]

Next: [[01 Books/Volume IV - Physical AI/03 Running the Machine/09 Spatial Memory/V4-09.01 Purpose|V4-09.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/09_memory/09_memory.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol4/09_memory/09_memory.html#sec-memory). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/System Types/Embodied & Physical Systems/Recursive State Filtering|Recursive State Filtering]]
- [[02 Concepts/System Types/Embodied & Physical Systems/State Estimation|State Estimation]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume IV - Physical AI/00 Introduction/01 The Causal Boundary/V4-01 The Causal Boundary|V4-01 The Causal Boundary]] — Proposal boundary.
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/02 The Physical Body/V4-02 The Physical Body|V4-02 The Physical Body]] — Measurement freshness deadline; Credible deceleration.
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/03 The Cognitive Brain/V4-03 The Cognitive Brain|V4-03 The Cognitive Brain]] — Softmax illusion; Two-speed brain.
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/04 The Nervous System/V4-04 The Nervous System|V4-04 The Nervous System]] — Freshest-proposal mailbox; Chunk lease; Worst-case execution time.
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06 Policy Training|V4-06 Policy Training]] — Privileged information limits.
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/08 Sensor Perception/V4-08 Sensor Perception|V4-08 Sensor Perception]] — Capture epoch; Observation contract; Observation age; Latency waterfall; Clearance inset from measured residuals; Calibration chain.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/09_memory/memory_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume IV - Physical AI/03 Running the Machine/10 Grounded Intent/V4-10 Grounded Intent|V4-10 Grounded Intent]] — Forward occupancy screening; Expiring intent lease.
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12 Safety Enforcement|V4-12 Safety Enforcement]] — Kinetic barrier; Human separation distance; Recoverable set.
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/13 Workload Placement/V4-13 Workload Placement|V4-13 Workload Placement]] — Memory contention and miss handling.
- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/18 Engineering Physical AI/V4-18 Engineering Physical AI|V4-18 Engineering Physical AI]] — Residual-claims register; Observational indistinguishability.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/09_memory/memory_concepts.yml)

<!-- Semantic Navigation: End -->
