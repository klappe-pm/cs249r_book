---
title: V3-03 Test-Time Compute
type: Chapter
volume: 3
chapter: 3
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol3/03_test_time_compute/03_test_time_compute.qmd
source_anchor: sec-vol3-test-time-compute
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_3
rendered_source_url: https://mlsysbook.ai/vol3/03_test_time_compute/03_test_time_compute.html
---

# V3-03 Test-Time Compute

[[Home|Home]] · [[01 Books/Volume III - Agentic Systems/Volume 3 Overview|Volume Overview]]

^sec-vol3-test-time-compute

[Lecture slides](https://mlsysbook.ai/slides/vol3.html#ch-03) for this chapter

![[90 Assets/Volume III/03 Test Time Compute/Cover Deliberation Blueprint Labeled 6bd3be4ea5.webp]]

*Isometric blueprint of a branching search tree on a gridded slab, beside a small robot holding a stylus.*

## Chapter Sections

- [[01 Books/Volume III - Agentic Systems/01 The Model/03 Test-Time Compute/V3-03.01 Purpose|V3-03.01 Purpose]]
- [[01 Books/Volume III - Agentic Systems/01 The Model/03 Test-Time Compute/V3-03.02 Limits of a Single Response|V3-03.02 Limits of a Single Response]]
- [[01 Books/Volume III - Agentic Systems/01 The Model/03 Test-Time Compute/V3-03.03 Three Axes of Test-Time Compute|V3-03.03 Three Axes of Test-Time Compute]]
- [[01 Books/Volume III - Agentic Systems/01 The Model/03 Test-Time Compute/V3-03.04 Selecting from a Candidate Pool|V3-03.04 Selecting from a Candidate Pool]]
- [[01 Books/Volume III - Agentic Systems/01 The Model/03 Test-Time Compute/V3-03.05 Verifying Candidates|V3-03.05 Verifying Candidates]]
- [[01 Books/Volume III - Agentic Systems/01 The Model/03 Test-Time Compute/V3-03.06 Revising Candidate Plans|V3-03.06 Revising Candidate Plans]]
- [[01 Books/Volume III - Agentic Systems/01 The Model/03 Test-Time Compute/V3-03.07 Bounded Search|V3-03.07 Bounded Search]]
- [[01 Books/Volume III - Agentic Systems/01 The Model/03 Test-Time Compute/V3-03.08 Evaluating Deliberation Policies|V3-03.08 Evaluating Deliberation Policies]]
- [[01 Books/Volume III - Agentic Systems/01 The Model/03 Test-Time Compute/V3-03.09 Fallacies and Pitfalls|V3-03.09 Fallacies and Pitfalls]]
- [[01 Books/Volume III - Agentic Systems/01 The Model/03 Test-Time Compute/V3-03.10 Summary|V3-03.10 Summary]]
- [[01 Books/Volume III - Agentic Systems/01 The Model/03 Test-Time Compute/V3-03.11 Historical Perspective and Further Reading|V3-03.11 Historical Perspective and Further Reading]]
- [[01 Books/Volume III - Agentic Systems/01 The Model/03 Test-Time Compute/V3-03.12 Exercises|V3-03.12 Exercises]]
- [[01 Books/Volume III - Agentic Systems/01 The Model/03 Test-Time Compute/V3-03.13 Source References|V3-03.13 Source References]]
- [[01 Books/Volume III - Agentic Systems/01 The Model/03 Test-Time Compute/V3-03.14 Footnotes|V3-03.14 Footnotes]]

Next: [[01 Books/Volume III - Agentic Systems/01 The Model/03 Test-Time Compute/V3-03.01 Purpose|V3-03.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/03_test_time_compute/03_test_time_compute.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol3/03_test_time_compute/03_test_time_compute.html#sec-vol3-test-time-compute). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Lifecycle/Deployment & Serving/Inference Time Search|Inference Time Search]]
- [[02 Concepts/Lifecycle/Model Evaluation & Testing/Pass@k|Pass@k]]
- [[02 Concepts/Lifecycle/Deployment & Serving/Verifier|Verifier]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume III - Agentic Systems/00 Introduction/01 Introduction/V3-01 Introduction|V3-01 Introduction]] — Horizon compounding; Cost per accepted task; Invariant closure; Lighthouse workloads.
- [[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02 The Foundation Model|V3-02 The Foundation Model]] — Invocation contract; Output-bound call latency; Sampling shapes candidates, not correctness; Quadratic resend and prefix reuse; Checks certify named properties.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/03_test_time_compute/test_time_compute_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04 Context Engineering|V3-04 Context Engineering]] — Context compaction.
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05 KV Cache Management|V3-05 KV Cache Management]] — Copy-on-write block sharing; Radix prefix cache.
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08 Agent Sandboxes|V3-08 Agent Sandboxes]] — Copy-on-write workspace.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10 The Agent Harness|V3-10 The Agent Harness]] — Budget reservation.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11 Durable Execution|V3-11 Durable Execution]] — Durable intent before dispatch.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12 Failure Recovery|V3-12 Failure Recovery]] — Trajectory saga.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13 Agent Evaluation|V3-13 Agent Evaluation]] — Repeated-run consistency; Grader isolation; Matched-budget evaluation.
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/17 Reinforcement Learning from Verifiable Rewards/V3-17 Reinforcement Learning from Verifiable Rewards|V3-17 Reinforcement Learning from Verifiable Rewards]] — Sampled reward contrast.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/03_test_time_compute/test_time_compute_concepts.yml)

<!-- Semantic Navigation: End -->
