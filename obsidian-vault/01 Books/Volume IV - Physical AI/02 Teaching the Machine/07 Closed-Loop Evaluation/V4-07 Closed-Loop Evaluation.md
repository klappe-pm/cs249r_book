---
title: V4-07 Closed-Loop Evaluation
type: Chapter
volume: 4
chapter: 7
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol4/07_evaluation/07_evaluation.qmd
source_anchor: sec-evaluation
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_4
rendered_source_url: https://mlsysbook.ai/vol4/07_evaluation/07_evaluation.html
---

# V4-07 Closed-Loop Evaluation

[[Home|Home]] · [[01 Books/Volume IV - Physical AI/Volume 4 Overview|Volume Overview]]

^sec-evaluation

[Lecture slides](https://mlsysbook.ai/slides/vol4.html#ch-07) for this chapter

![[90 Assets/Volume IV/07 Evaluation/Cover Evaluation Blueprint Labeled 9190afece8.webp]]

*Isometric blueprint showing closed-loop evaluation and metrology: instrumented testing cage with motion capture cameras, tracking marker constellation, flush ground force-torque dynamometer, articulated reliability scorecard with confidence intervals, and crimson intervention tripwire.*

## Chapter Sections

- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07.01 Purpose|V4-07.01 Purpose]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07.02 From Clean Runs to Bounded Claims|V4-07.02 From Clean Runs to Bounded Claims]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07.03 What a Physical Success Rate Measures|V4-07.03 What a Physical Success Rate Measures]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07.04 Closed-Loop Dynamics|V4-07.04 Closed-Loop Dynamics]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07.05 Evidence Regimes|V4-07.05 Evidence Regimes]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07.06 Fixing the Trial Protocol|V4-07.06 Fixing the Trial Protocol]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07.07 Confidence from a Finite Campaign|V4-07.07 Confidence from a Finite Campaign]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07.08 Trial Budgets, Stopping Rules, and Comparisons|V4-07.08 Trial Budgets, Stopping Rules, and Comparisons]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07.09 The Evaluation Record|V4-07.09 The Evaluation Record]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07.10 Verification Ceilings and the Exposure Wall|V4-07.10 Verification Ceilings and the Exposure Wall]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07.11 Evaluation Pitfalls and Metric Masking|V4-07.11 Evaluation Pitfalls and Metric Masking]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07.12 Fallacies and Pitfalls|V4-07.12 Fallacies and Pitfalls]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07.13 Summary|V4-07.13 Summary]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07.14 Historical Perspective and Further Reading|V4-07.14 Historical Perspective and Further Reading]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07.15 Source References|V4-07.15 Source References]]
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07.16 Footnotes|V4-07.16 Footnotes]]

Next: [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07.01 Purpose|V4-07.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/07_evaluation/07_evaluation.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol4/07_evaluation/07_evaluation.html#sec-evaluation). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Lifecycle/Model Evaluation & Testing/Closed Loop Policy Evaluation|Closed Loop Policy Evaluation]]
- [[02 Concepts/Qualities/Safety & Assurance/Rare Event Safety Validation|Rare Event Safety Validation]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume IV - Physical AI/00 Introduction/01 The Causal Boundary/V4-01 The Causal Boundary|V4-01 The Causal Boundary]] — Irreversibility and recovery; Proposal boundary; Causal boundary.
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/02 The Physical Body/V4-02 The Physical Body|V4-02 The Physical Body]] — Thermal duty limits.
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/04 The Nervous System/V4-04 The Nervous System|V4-04 The Nervous System]] — Independence requirement; Chunk lease.
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05 Physical Data|V4-05 Physical Data]] — Endogenous covariate shift; Compounding error and recoverability; Operational design domain; Rig-to-rig divergence; Demonstration yield and wear; Intervention curation.
- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06 Policy Training|V4-06 Policy Training]] — Policy manifest; Paired probing; Simulator contact exploit; Reality gap as a vector; Mode averaging.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/07_evaluation/evaluation_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume IV - Physical AI/03 Running the Machine/08 Sensor Perception/V4-08 Sensor Perception|V4-08 Sensor Perception]] — Capture epoch.
- [[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12 Safety Enforcement|V4-12 Safety Enforcement]] — State-matched fallback ladder.
- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/15 Adversarial Verification/V4-15 Adversarial Verification|V4-15 Adversarial Verification]] — Qualification ladder; Rare-event rates and tails; Fault-list derivation; Fault-record set; Extreme value theory.
- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/16 Deployment Release/V4-16 Deployment Release|V4-16 Deployment Release]] — Safety case.
- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/18 Engineering Physical AI/V4-18 Engineering Physical AI|V4-18 Engineering Physical AI]] — Observational indistinguishability.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/07_evaluation/evaluation_concepts.yml)

<!-- Semantic Navigation: End -->
