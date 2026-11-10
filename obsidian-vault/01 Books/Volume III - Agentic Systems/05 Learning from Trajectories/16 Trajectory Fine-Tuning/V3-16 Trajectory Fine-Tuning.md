---
title: V3-16 Trajectory Fine-Tuning
type: Chapter
volume: 3
chapter: 16
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol3/16_fine_tuning/16_fine_tuning.qmd
source_anchor: sec-vol3-fine-tuning
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_3
rendered_source_url: https://mlsysbook.ai/vol3/16_fine_tuning/16_fine_tuning.html
---

# V3-16 Trajectory Fine-Tuning

[[Home|Home]] · [[01 Books/Volume III - Agentic Systems/Volume 3 Overview|Volume Overview]]

^sec-vol3-fine-tuning

[Lecture slides](https://mlsysbook.ai/slides/vol3.html#ch-16) for this chapter

![[90 Assets/Volume III/16 Fine Tuning/Cover Sft Blueprint Labeled 15cd25aaba.webp]]

*Blueprint for trajectory fine-tuning.*

## Chapter Sections

- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/16 Trajectory Fine-Tuning/V3-16.01 Purpose|V3-16.01 Purpose]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/16 Trajectory Fine-Tuning/V3-16.02 Recovery Records as Training Data|V3-16.02 Recovery Records as Training Data]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/16 Trajectory Fine-Tuning/V3-16.03 Scope of Supervised Fine-Tuning|V3-16.03 Scope of Supervised Fine-Tuning]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/16 Trajectory Fine-Tuning/V3-16.04 Serializing Trajectories|V3-16.04 Serializing Trajectories]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/16 Trajectory Fine-Tuning/V3-16.05 Observation Loss Masking|V3-16.05 Observation Loss Masking]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/16 Trajectory Fine-Tuning/V3-16.06 Batching Variable-Length Trajectories|V3-16.06 Batching Variable-Length Trajectories]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/16 Trajectory Fine-Tuning/V3-16.07 Exposure Bias|V3-16.07 Exposure Bias]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/16 Trajectory Fine-Tuning/V3-16.08 Schema Robustness|V3-16.08 Schema Robustness]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/16 Trajectory Fine-Tuning/V3-16.09 Trajectory Preference Optimization|V3-16.09 Trajectory Preference Optimization]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/16 Trajectory Fine-Tuning/V3-16.10 Policy Distillation|V3-16.10 Policy Distillation]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/16 Trajectory Fine-Tuning/V3-16.11 Parameter-Efficient Fine-Tuning|V3-16.11 Parameter-Efficient Fine-Tuning]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/16 Trajectory Fine-Tuning/V3-16.12 Evaluating a Fine-Tuned Agent|V3-16.12 Evaluating a Fine-Tuned Agent]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/16 Trajectory Fine-Tuning/V3-16.13 Case Study Training the Repair Policy|V3-16.13 Case Study Training the Repair Policy]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/16 Trajectory Fine-Tuning/V3-16.14 Fallacies and Pitfalls|V3-16.14 Fallacies and Pitfalls]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/16 Trajectory Fine-Tuning/V3-16.15 Summary|V3-16.15 Summary]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/16 Trajectory Fine-Tuning/V3-16.16 Historical Perspective and Further Reading|V3-16.16 Historical Perspective and Further Reading]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/16 Trajectory Fine-Tuning/V3-16.17 Exercises|V3-16.17 Exercises]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/16 Trajectory Fine-Tuning/V3-16.18 Source References|V3-16.18 Source References]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/16 Trajectory Fine-Tuning/V3-16.19 Footnotes|V3-16.19 Footnotes]]

Next: [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/16 Trajectory Fine-Tuning/V3-16.01 Purpose|V3-16.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/16_fine_tuning/16_fine_tuning.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol3/16_fine_tuning/16_fine_tuning.html#sec-vol3-fine-tuning). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Lifecycle/Model Evaluation & Testing/Closed Loop Policy Evaluation|Closed Loop Policy Evaluation]]
- [[02 Concepts/Lifecycle/Training & Adaptation/Compounding Error in Sequential Decisions|Compounding Error in Sequential Decisions]]
- [[02 Concepts/Lifecycle/Training & Adaptation/Loss Masking and Token Normalization|Loss Masking and Token Normalization]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume III - Agentic Systems/00 Introduction/01 Introduction/V3-01 Introduction|V3-01 Introduction]] — Invariant closure; Horizon compounding; Cost per accepted task.
- [[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02 The Foundation Model|V3-02 The Foundation Model]] — Proposal boundary; Invocation contract; Quadratic resend and prefix reuse.
- [[01 Books/Volume III - Agentic Systems/01 The Model/03 Test-Time Compute/V3-03 Test-Time Compute|V3-03 Test-Time Compute]] — Coverage is not selection.
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04 Context Engineering|V3-04 Context Engineering]] — Hysteretic compaction scheduling.
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05 KV Cache Management|V3-05 KV Cache Management]] — Reusable is not applicable.
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07 Tool Calling|V3-07 Tool Calling]] — Settlement before retry.
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08 Agent Sandboxes|V3-08 Agent Sandboxes]] — Least privilege.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11 Durable Execution|V3-11 Durable Execution]] — Trajectory log.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12 Failure Recovery|V3-12 Failure Recovery]] — Compensation.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13 Agent Evaluation|V3-13 Agent Evaluation]] — Task acceptance contract; Repeated-run consistency; Matched-budget evaluation; Paired comparison; Contamination; Hermetic evaluation gym.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/14 Operating Agents/V3-14 Operating Agents|V3-14 Operating Agents]] — Release gate.
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/15 Trajectory Curation/V3-15 Trajectory Curation|V3-15 Trajectory Curation]] — Capability-gap triage; Recovery demonstrations; Learning artifacts from one record; Admission cascade; Record lineage; Task-group splits; Mixture specification; Self-selection narrowing.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/16_fine_tuning/fine_tuning_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/17 Reinforcement Learning from Verifiable Rewards/V3-17 Reinforcement Learning from Verifiable Rewards|V3-17 Reinforcement Learning from Verifiable Rewards]] — Sampled reward contrast.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/16_fine_tuning/fine_tuning_concepts.yml)

<!-- Semantic Navigation: End -->
