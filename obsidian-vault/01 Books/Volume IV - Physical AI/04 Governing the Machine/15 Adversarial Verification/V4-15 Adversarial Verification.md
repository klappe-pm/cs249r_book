---
title: V4-15 Adversarial Verification
type: Chapter
volume: 4
chapter: 15
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol4/15_verification/15_verification.qmd
source_anchor: sec-verification
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_4
rendered_source_url: https://mlsysbook.ai/vol4/15_verification/15_verification.html
---

# V4-15 Adversarial Verification

[[Home|Home]] · [[01 Books/Volume IV - Physical AI/Volume 4 Overview|Volume Overview]]

^sec-verification

[Lecture slides](https://mlsysbook.ai/slides/vol4.html#ch-15) for this chapter

![[90 Assets/Volume IV/15 Verification/Cover Verification Blueprint Labeled 5c5cb1a30a.webp]]

*Isometric blueprint showing adversarial cyber-physical verification: four-rung qualification ladder with virtual simulation crucible, processor-in-the-loop board, hardware-in-the-loop dynamometer, crimson adversarial fault injection needles, and surveillance telemetry towers.*

## Chapter Sections

- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/15 Adversarial Verification/V4-15.01 Purpose|V4-15.01 Purpose]]
- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/15 Adversarial Verification/V4-15.02 The Claim a Fault Trial Must Test|V4-15.02 The Claim a Fault Trial Must Test]]
- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/15 Adversarial Verification/V4-15.03 The Operating Envelope|V4-15.03 The Operating Envelope]]
- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/15 Adversarial Verification/V4-15.04 One F1 Trial from Injection to Record|V4-15.04 One F1 Trial from Injection to Record]]
- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/15 Adversarial Verification/V4-15.05 Fault Oracles and Acceptance|V4-15.05 Fault Oracles and Acceptance]]
- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/15 Adversarial Verification/V4-15.06 Extending the Trial to the Envelope|V4-15.06 Extending the Trial to the Envelope]]
- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/15 Adversarial Verification/V4-15.07 Deriving the Fault List|V4-15.07 Deriving the Fault List]]
- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/15 Adversarial Verification/V4-15.08 The Qualification Ladder|V4-15.08 The Qualification Ladder]]
- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/15 Adversarial Verification/V4-15.09 Fault Injection on Hardware|V4-15.09 Fault Injection on Hardware]]
- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/15 Adversarial Verification/V4-15.10 Searching Beyond the First Trial|V4-15.10 Searching Beyond the First Trial]]
- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/15 Adversarial Verification/V4-15.11 Interpreting Campaign Statistics|V4-15.11 Interpreting Campaign Statistics]]
- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/15 Adversarial Verification/V4-15.12 Fault Records for Release|V4-15.12 Fault Records for Release]]
- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/15 Adversarial Verification/V4-15.13 Fallacies and Pitfalls|V4-15.13 Fallacies and Pitfalls]]
- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/15 Adversarial Verification/V4-15.14 Summary|V4-15.14 Summary]]
- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/15 Adversarial Verification/V4-15.15 Historical Perspective and Further Reading|V4-15.15 Historical Perspective and Further Reading]]
- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/15 Adversarial Verification/V4-15.16 Source References|V4-15.16 Source References]]
- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/15 Adversarial Verification/V4-15.17 Footnotes|V4-15.17 Footnotes]]

Next: [[01 Books/Volume IV - Physical AI/04 Governing the Machine/15 Adversarial Verification/V4-15.01 Purpose|V4-15.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/15_verification/15_verification.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol4/15_verification/15_verification.html#sec-verification). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Qualities/Reliability & Fault Tolerance/Failure Injection|Failure Injection]]
- [[02 Concepts/Lifecycle/Model Evaluation & Testing/Test Oracle|Test Oracle]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume IV - Physical AI/00 Introduction/01 The Causal Boundary/V4-01 The Causal Boundary|V4-01 The Causal Boundary]] — Causal boundary; Five-level machine; Proposal boundary; Safety convergence at the permission path.
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/02 The Physical Body/V4-02 The Physical Body|V4-02 The Physical Body]] — Velocity ceiling.
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/03 The Cognitive Brain/V4-03 The Cognitive Brain|V4-03 The Cognitive Brain]] — Two-speed brain.
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/04 The Nervous System/V4-04 The Nervous System|V4-04 The Nervous System]] — Chunk lease; Authority-expiry timers; Independence requirement.
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05 Physical Data|V4-05 Physical Data]] — Effective sample size of telemetry.
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06 Policy Training|V4-06 Policy Training]] — Paired probing; Policy manifest.
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07 Closed-Loop Evaluation|V4-07 Closed-Loop Evaluation]] — Zero-failure bound; Exposure wall; Evaluation record.
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/08 Sensor Perception/V4-08 Sensor Perception|V4-08 Sensor Perception]] — Observation contract; Observation age.
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/09 Spatial Memory/V4-09 Spatial Memory|V4-09 Spatial Memory]] — Occlusion and free-space erosion.
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/10 Grounded Intent/V4-10 Grounded Intent|V4-10 Grounded Intent]] — Calibrated referent refusal; Admission checks physics not meaning.
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/11 Trajectory Planning/V4-11 Trajectory Planning|V4-11 Trajectory Planning]] — Jerk-limited stopping suffix.
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12 Safety Enforcement|V4-12 Safety Enforcement]] — Stopping envelope; State-matched fallback ladder; Enforcement record.
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/13 Workload Placement/V4-13 Workload Placement|V4-13 Workload Placement]] — Dispatch-to-admission allocation; Memory contention and miss handling; Placement record.
- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/14 Supervisory Intervention/V4-14 Supervisory Intervention|V4-14 Supervisory Intervention]] — Single-writer handover handshake; Clearance-derived fallback deadline; Authority record.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/15_verification/verification_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/16 Deployment Release/V4-16 Deployment Release|V4-16 Deployment Release]] — Safety case; Certification authorizes a configuration; Three signed verdicts; Standing conditions.
- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/17 Responsible Physical AI/V4-17 Responsible Physical AI|V4-17 Responsible Physical AI]] — Detection gaps become stopping gaps.
- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/18 Engineering Physical AI/V4-18 Engineering Physical AI|V4-18 Engineering Physical AI]] — Residual-claims register.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/15_verification/verification_concepts.yml)

<!-- Semantic Navigation: End -->
