---
title: V4-12 Safety Enforcement
type: Chapter
volume: 4
chapter: 12
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol4/12_enforcement/12_enforcement.qmd
source_anchor: sec-enforcement
source_mode: Published HTML With Restored Source Headings
tags:
- Type/Chapter
- Book/Volume_4
rendered_source_url: https://mlsysbook.ai/vol4/12_enforcement/12_enforcement.html
---

# V4-12 Safety Enforcement

[[Home|Home]] · [[01 Books/Volume IV - Physical AI/Volume 4 Overview|Volume Overview]]

^sec-enforcement

[Lecture slides](https://mlsysbook.ai/slides/vol4.html#ch-12) for this chapter

![[90 Assets/Volume IV/12 Enforcement/Cover Enforcement Blueprint Labeled 846398642b.webp]]

*Isometric blueprint showing runtime safety enforcement for an autonomous mobile robot: omnidirectional mecanum base, translucent mint-green forward-invariant safe set boundary, candidate cyan neural proposal vector pointing toward a prohibited crimson hazard wall, amber CBF-QP projected admissible vector, and crimson emergency brake interlock.*

## Chapter Sections

- [[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12.01 Purpose|V4-12.01 Purpose]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12.02 The Per-Tick Gatekeeper|V4-12.02 The Per-Tick Gatekeeper]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12.03 The Tracker Handoff and Dynamic Reference Envelopes|V4-12.03 The Tracker Handoff and Dynamic Reference Envelopes]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12.04 Stopping Envelopes|V4-12.04 Stopping Envelopes]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12.05 Authority Exhaustion and Emergency Fallback|V4-12.05 Authority Exhaustion and Emergency Fallback]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12.06 Safe Sets as Conditional Permission|V4-12.06 Safe Sets as Conditional Permission]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12.07 Refusing Proposals and Enforcing State Invariants|V4-12.07 Refusing Proposals and Enforcing State Invariants]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12.08 The Minimal Intervention Principle and Optimization Filters|V4-12.08 The Minimal Intervention Principle and Optimization Filters]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12.09 Admission, Cyclic Checking, and Monitor Independence|V4-12.09 Admission, Cyclic Checking, and Monitor Independence]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12.10 The Fallback Ladder|V4-12.10 The Fallback Ladder]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12.11 Runtime Enforcement Failure Modes|V4-12.11 Runtime Enforcement Failure Modes]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12.12 The Enforcement Record|V4-12.12 The Enforcement Record]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12.13 Fallacies and Pitfalls|V4-12.13 Fallacies and Pitfalls]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12.14 Summary|V4-12.14 Summary]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12.15 Historical Perspective and Further Reading|V4-12.15 Historical Perspective and Further Reading]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12.16 Source References|V4-12.16 Source References]]
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12.17 Footnotes|V4-12.17 Footnotes]]

Next: [[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12.01 Purpose|V4-12.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/12_enforcement/12_enforcement.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol4/12_enforcement/12_enforcement.html#sec-enforcement). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/System Types/Embodied & Physical Systems/Contact and Compliance|Contact and Compliance]]
- [[02 Concepts/Qualities/Safety & Assurance/Functional Safety|Functional Safety]]
- [[02 Concepts/Qualities/Safety & Assurance/Runtime Assurance|Runtime Assurance]]
- [[02 Concepts/Qualities/Safety & Assurance/Safety Filter|Safety Filter]]
- [[02 Concepts/Qualities/Safety & Assurance/Safety Integrity Level|Safety Integrity Level]]
- [[02 Concepts/Qualities/Safety & Assurance/Stopping Envelope|Stopping Envelope]]

## Related Themes

- [[03 Themes/Security and Trust|Security and Trust]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume IV - Physical AI/00 Introduction/01 The Causal Boundary/V4-01 The Causal Boundary|V4-01 The Causal Boundary]] — Proposal boundary; Irreversibility and recovery; Elementary stopping budget.
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/02 The Physical Body/V4-02 The Physical Body|V4-02 The Physical Body]] — Velocity ceiling; Credible deceleration; Reflected rotor inertia; Thermal duty limits; Shared-rail power integrity; Limit record.
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/03 The Cognitive Brain/V4-03 The Cognitive Brain|V4-03 The Cognitive Brain]] — Two-speed brain.
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/04 The Nervous System/V4-04 The Nervous System|V4-04 The Nervous System]] — Chunk lease; Authority-expiry timers; Freshest-proposal mailbox; Independence requirement; Safety microcontroller; Handoff record and event timing.
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06 Policy Training|V4-06 Policy Training]] — Policy manifest.
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07 Closed-Loop Evaluation|V4-07 Closed-Loop Evaluation]] — Evaluation record.
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/08 Sensor Perception/V4-08 Sensor Perception|V4-08 Sensor Perception]] — Observation age; Observation contract; Clearance inset from measured residuals; Perception-side independence.
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/09 Spatial Memory/V4-09 Spatial Memory|V4-09 Spatial Memory]] — Occlusion and free-space erosion; Belief expiry.
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/11 Trajectory Planning/V4-11 Trajectory Planning|V4-11 Trajectory Planning]] — Trajectory record; Jerk-limited stopping suffix; Inevitable collision states.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/12_enforcement/enforcement_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume IV - Physical AI/03 Running the Machine/13 Workload Placement/V4-13 Workload Placement|V4-13 Workload Placement]] — Per-resource independence inventory; Dispatch-to-admission allocation; Declared WCET as falsification threshold.
- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/14 Supervisory Intervention/V4-14 Supervisory Intervention|V4-14 Supervisory Intervention]] — Single-writer handover handshake; Authority record.
- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/16 Deployment Release/V4-16 Deployment Release|V4-16 Deployment Release]] — Safety case; Certification authorizes a configuration.
- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/18 Engineering Physical AI/V4-18 Engineering Physical AI|V4-18 Engineering Physical AI]] — Residual-claims register.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/12_enforcement/enforcement_concepts.yml)

<!-- Semantic Navigation: End -->
