---
title: V3-13 Agent Evaluation
type: Chapter
volume: 3
chapter: 13
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol3/13_evaluation/13_evaluation.qmd
source_anchor: sec-vol3-evaluation
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_3
rendered_source_url: https://mlsysbook.ai/vol3/13_evaluation/13_evaluation.html
---

# V3-13 Agent Evaluation

[[Home|Home]] · [[01 Books/Volume III - Agentic Systems/Volume 3 Overview|Volume Overview]]

^sec-vol3-evaluation

[Lecture slides](https://mlsysbook.ai/slides/vol3.html#ch-13) for this chapter

![[90 Assets/Volume III/13 Evaluation/Cover Evaluation Blueprint Labeled d4d72e0361.webp]]

*Isometric blueprint of an agent evaluation gym: a task contract card feeds a sealed glass test chamber with a reset ring, where a small robot runs repeated trial trajectories; outside, behind an isolation wall, a grader station sorts the runs into verdict tokens beside a caliper that stands for the confidence interval.*

## Chapter Sections

- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13.01 Purpose|V3-13.01 Purpose]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13.02 The Evaluation Problem|V3-13.02 The Evaluation Problem]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13.03 The Task Acceptance Contract|V3-13.03 The Task Acceptance Contract]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13.04 Hermetic Evaluation Gyms|V3-13.04 Hermetic Evaluation Gyms]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13.05 Grading Trajectories|V3-13.05 Grading Trajectories]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13.06 Statistical Evaluation Rigor|V3-13.06 Statistical Evaluation Rigor]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13.07 Fallacies and Pitfalls|V3-13.07 Fallacies and Pitfalls]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13.08 Summary|V3-13.08 Summary]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13.09 Historical Perspective and Further Reading|V3-13.09 Historical Perspective and Further Reading]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13.10 Exercises|V3-13.10 Exercises]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13.11 Source References|V3-13.11 Source References]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13.12 Footnotes|V3-13.12 Footnotes]]

Next: [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13.01 Purpose|V3-13.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/13_evaluation/13_evaluation.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol3/13_evaluation/13_evaluation.html#sec-vol3-evaluation). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Lifecycle/Model Evaluation & Testing/Pass@k|Pass@k]]
- [[02 Concepts/Lifecycle/Model Evaluation & Testing/Trajectory Evaluation|Trajectory Evaluation]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume III - Agentic Systems/00 Introduction/01 Introduction/V3-01 Introduction|V3-01 Introduction]] — Task contract; Closure evidence levels; Invariant closure; Cost per accepted task; Horizon compounding; H·S·A exposures; Lighthouse workloads.
- [[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02 The Foundation Model|V3-02 The Foundation Model]] — Checks certify named properties; Recorded calls replay, served calls do not.
- [[01 Books/Volume III - Agentic Systems/01 The Model/03 Test-Time Compute/V3-03 Test-Time Compute|V3-03 Test-Time Compute]] — Coverage is not selection; Verifier precision; Step-level evidence; Selection pressure; Allocation axes; Deliberation operating point.
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/06 Long-Term Memory/V3-06 Long-Term Memory|V3-06 Long-Term Memory]] — Memory policy evaluation.
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08 Agent Sandboxes|V3-08 Agent Sandboxes]] — Reset contract; In-process restriction fails.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10 The Agent Harness|V3-10 The Agent Harness]] — Bounded-liability admission.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11 Durable Execution|V3-11 Durable Execution]] — Record and replay.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12 Failure Recovery|V3-12 Failure Recovery]] — Compensation.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/13_evaluation/evaluation_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/15 Trajectory Curation/V3-15 Trajectory Curation|V3-15 Trajectory Curation]] — Task-group splits.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/13_evaluation/evaluation_concepts.yml)

<!-- Semantic Navigation: End -->
