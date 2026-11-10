---
title: V3-15 Trajectory Curation
type: Chapter
volume: 3
chapter: 15
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol3/15_trajectory_curation/15_trajectory_curation.qmd
source_anchor: sec-vol3-trajectory-curation
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_3
rendered_source_url: https://mlsysbook.ai/vol3/15_trajectory_curation/15_trajectory_curation.html
---

# V3-15 Trajectory Curation

[[Home|Home]] · [[01 Books/Volume III - Agentic Systems/Volume 3 Overview|Volume Overview]]

^sec-vol3-trajectory-curation

[Lecture slides](https://mlsysbook.ai/slides/vol3.html#ch-15) for this chapter

![[90 Assets/Volume III/15 Trajectory Curation/Cover Data Flywheel Blueprint Labeled 22f242a209.webp]]

*Blueprint for Trajectory Harvesting.*

## Chapter Sections

- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/15 Trajectory Curation/V3-15.01 Purpose|V3-15.01 Purpose]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/15 Trajectory Curation/V3-15.02 From Trajectory Records to a Training Corpus|V3-15.02 From Trajectory Records to a Training Corpus]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/15 Trajectory Curation/V3-15.03 Capability Gap Diagnosis|V3-15.03 Capability Gap Diagnosis]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/15 Trajectory Curation/V3-15.04 Task Fixture Design|V3-15.04 Task Fixture Design]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/15 Trajectory Curation/V3-15.05 Split Design|V3-15.05 Split Design]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/15 Trajectory Curation/V3-15.06 Staged Verifier Cascades|V3-15.06 Staged Verifier Cascades]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/15 Trajectory Curation/V3-15.07 Recovery Demonstration Curation|V3-15.07 Recovery Demonstration Curation]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/15 Trajectory Curation/V3-15.08 The Self-Improvement Loop|V3-15.08 The Self-Improvement Loop]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/15 Trajectory Curation/V3-15.09 Collection Pipeline Architecture|V3-15.09 Collection Pipeline Architecture]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/15 Trajectory Curation/V3-15.10 Trajectory Provenance Tracking|V3-15.10 Trajectory Provenance Tracking]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/15 Trajectory Curation/V3-15.11 Case Study Curating the Repair Record|V3-15.11 Case Study Curating the Repair Record]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/15 Trajectory Curation/V3-15.12 Fallacies and Pitfalls|V3-15.12 Fallacies and Pitfalls]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/15 Trajectory Curation/V3-15.13 Summary|V3-15.13 Summary]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/15 Trajectory Curation/V3-15.14 Historical Perspective and Further Reading|V3-15.14 Historical Perspective and Further Reading]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/15 Trajectory Curation/V3-15.15 Exercises|V3-15.15 Exercises]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/15 Trajectory Curation/V3-15.16 Source References|V3-15.16 Source References]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/15 Trajectory Curation/V3-15.17 Footnotes|V3-15.17 Footnotes]]

Next: [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/15 Trajectory Curation/V3-15.01 Purpose|V3-15.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/15_trajectory_curation/15_trajectory_curation.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol3/15_trajectory_curation/15_trajectory_curation.html#sec-vol3-trajectory-curation). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Lifecycle/Model Evaluation & Testing/Evaluation Split|Evaluation Split]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume III - Agentic Systems/00 Introduction/01 Introduction/V3-01 Introduction|V3-01 Introduction]] — Cost per accepted task; H·S·A exposures; Horizon compounding; Invariant closure.
- [[01 Books/Volume III - Agentic Systems/01 The Model/03 Test-Time Compute/V3-03 Test-Time Compute|V3-03 Test-Time Compute]] — Coverage is not selection; Selection pressure.
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05 KV Cache Management|V3-05 KV Cache Management]] — Little's law.
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08 Agent Sandboxes|V3-08 Agent Sandboxes]] — Containment beneath the model; Reset contract.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11 Durable Execution|V3-11 Durable Execution]] — Record and replay.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12 Failure Recovery|V3-12 Failure Recovery]] — Trajectory saga; Dependency containment; Incident containment.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13 Agent Evaluation|V3-13 Agent Evaluation]] — Task acceptance contract; Hermetic evaluation gym; Grader isolation; Grader calibration; Contamination; Paired comparison.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/14 Operating Agents/V3-14 Operating Agents|V3-14 Operating Agents]] — Postmortem by intervention; Trace retention.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/15_trajectory_curation/trajectory_curation_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/16 Trajectory Fine-Tuning/V3-16 Trajectory Fine-Tuning|V3-16 Trajectory Fine-Tuning]] — Preference training; Loss masking; Exposure bias.
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/17 Reinforcement Learning from Verifiable Rewards/V3-17 Reinforcement Learning from Verifiable Rewards|V3-17 Reinforcement Learning from Verifiable Rewards]] — Sampled reward contrast; Zero-contrast groups.
- [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/18 Multi-Agent Coordination/V3-18 Multi-Agent Coordination|V3-18 Multi-Agent Coordination]] — Credit-window flow control.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/15_trajectory_curation/trajectory_curation_concepts.yml)

<!-- Semantic Navigation: End -->
