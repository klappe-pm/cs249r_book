---
title: V4-11 Trajectory Planning
type: Chapter
volume: 4
chapter: 11
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol4/11_planning/11_planning.qmd
source_anchor: sec-planning
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_4
rendered_source_url: https://mlsysbook.ai/vol4/11_planning/11_planning.html
---

# V4-11 Trajectory Planning

[[Home|Home]] · [[01 Books/Volume IV - Physical AI/Volume 4 Overview|Volume Overview]]

^sec-planning

[Lecture slides](https://mlsysbook.ai/slides/vol4.html#ch-11) for this chapter

![[90 Assets/Volume IV/11 Planning/Cover Planning Blueprint Labeled 8ed0f452ab.webp]]

*Isometric blueprint showing 3D flight trajectory planning for an autonomous aerial quadrotor drone: brushless DC outrunner cutaway, aerodynamic thrust cones, executed cyan 3D polynomial spline threading an obstacle ring, prospective amber waypoint chunk, and crimson hover-recovery stopping suffix landing on a terminal perch.*

## Chapter Sections

- [[01 Books/Volume IV - Physical AI/03 Running the Machine/11 Trajectory Planning/V4-11.01 Purpose|V4-11.01 Purpose]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/11 Trajectory Planning/V4-11.02 Continuous Trajectory Generation|V4-11.02 Continuous Trajectory Generation]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/11 Trajectory Planning/V4-11.03 The Planning Handoff and the Trajectory Record|V4-11.03 The Planning Handoff and the Trajectory Record]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/11 Trajectory Planning/V4-11.04 Replacement Timing and the Planning Horizon|V4-11.04 Replacement Timing and the Planning Horizon]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/11 Trajectory Planning/V4-11.05 Kinodynamic Feasibility|V4-11.05 Kinodynamic Feasibility]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/11 Trajectory Planning/V4-11.06 Behavior at the Seam|V4-11.06 Behavior at the Seam]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/11 Trajectory Planning/V4-11.07 Choosing a Trajectory Generator|V4-11.07 Choosing a Trajectory Generator]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/11 Trajectory Planning/V4-11.08 Trajectory Planning Failure Modes and Infeasible Seams|V4-11.08 Trajectory Planning Failure Modes and Infeasible Seams]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/11 Trajectory Planning/V4-11.09 The Trajectory Record|V4-11.09 The Trajectory Record]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/11 Trajectory Planning/V4-11.10 Fallacies and Pitfalls|V4-11.10 Fallacies and Pitfalls]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/11 Trajectory Planning/V4-11.11 Summary|V4-11.11 Summary]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/11 Trajectory Planning/V4-11.12 Historical Perspective and Further Reading|V4-11.12 Historical Perspective and Further Reading]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/11 Trajectory Planning/V4-11.13 Source References|V4-11.13 Source References]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/11 Trajectory Planning/V4-11.14 Footnotes|V4-11.14 Footnotes]]

Next: [[01 Books/Volume IV - Physical AI/03 Running the Machine/11 Trajectory Planning/V4-11.01 Purpose|V4-11.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/11_planning/11_planning.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol4/11_planning/11_planning.html#sec-planning). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/System Types/Embodied & Physical Systems/Trajectory Feasibility|Trajectory Feasibility]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume IV - Physical AI/00 Introduction/01 The Causal Boundary/V4-01 The Causal Boundary|V4-01 The Causal Boundary]] — Proposal boundary; Irreversibility and recovery; Elementary stopping budget.
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/02 The Physical Body/V4-02 The Physical Body|V4-02 The Physical Body]] — Reflected rotor inertia; Delivered torque ceiling.
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/03 The Cognitive Brain/V4-03 The Cognitive Brain|V4-03 The Cognitive Brain]] — Chunking is a supply lever; Temporal ensembling and real-time chunking; Evidence horizon.
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/04 The Nervous System/V4-04 The Nervous System|V4-04 The Nervous System]] — Chunk lease; Handoff record and event timing; Authority-expiry timers.
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05 Physical Data|V4-05 Physical Data]] — Kinematic topology mismatch; Operational design domain.
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/08 Sensor Perception/V4-08 Sensor Perception|V4-08 Sensor Perception]] — Observation age; Latency waterfall.
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/09 Spatial Memory/V4-09 Spatial Memory|V4-09 Spatial Memory]] — Belief record.
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/10 Grounded Intent/V4-10 Grounded Intent|V4-10 Grounded Intent]] — Expiring intent lease.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/11_planning/planning_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12 Safety Enforcement|V4-12 Safety Enforcement]] — Stopping envelope; Kinetic barrier; State-matched fallback ladder; Tracking bound.
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/13 Workload Placement/V4-13 Workload Placement|V4-13 Workload Placement]] — Dispatch-to-admission allocation.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/11_planning/planning_concepts.yml)

<!-- Semantic Navigation: End -->
