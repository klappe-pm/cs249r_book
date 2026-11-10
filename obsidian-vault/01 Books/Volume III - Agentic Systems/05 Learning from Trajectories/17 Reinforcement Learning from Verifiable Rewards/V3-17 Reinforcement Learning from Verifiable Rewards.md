---
title: V3-17 Reinforcement Learning from Verifiable Rewards
type: Chapter
volume: 3
chapter: 17
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol3/17_rlvr/17_rlvr.qmd
source_anchor: sec-vol3-rlvr
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_3
rendered_source_url: https://mlsysbook.ai/vol3/17_rlvr/17_rlvr.html
---

# V3-17 Reinforcement Learning from Verifiable Rewards

[[Home|Home]] · [[01 Books/Volume III - Agentic Systems/Volume 3 Overview|Volume Overview]]

^sec-vol3-rlvr

[Lecture slides](https://mlsysbook.ai/slides/vol3.html#ch-17) for this chapter

![[90 Assets/Volume III/17 Rlvr/Cover Rlvr Blueprint Labeled 407fb807b1.webp]]

*Blueprint for Reinforcement Learning from Verifiable Rewards.*

## Chapter Sections

- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/17 Reinforcement Learning from Verifiable Rewards/V3-17.01 Purpose|V3-17.01 Purpose]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/17 Reinforcement Learning from Verifiable Rewards/V3-17.02 Learning from a Check|V3-17.02 Learning from a Check]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/17 Reinforcement Learning from Verifiable Rewards/V3-17.03 Foundations of Verifiable Rewards|V3-17.03 Foundations of Verifiable Rewards]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/17 Reinforcement Learning from Verifiable Rewards/V3-17.04 Verifiable Rewards|V3-17.04 Verifiable Rewards]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/17 Reinforcement Learning from Verifiable Rewards/V3-17.05 Credit Across Turns|V3-17.05 Credit Across Turns]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/17 Reinforcement Learning from Verifiable Rewards/V3-17.06 Group Relative Policy Optimization|V3-17.06 Group Relative Policy Optimization]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/17 Reinforcement Learning from Verifiable Rewards/V3-17.07 Multi-Turn Agentic RL|V3-17.07 Multi-Turn Agentic RL]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/17 Reinforcement Learning from Verifiable Rewards/V3-17.08 Verifier Isolation|V3-17.08 Verifier Isolation]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/17 Reinforcement Learning from Verifiable Rewards/V3-17.09 Training Pathologies|V3-17.09 Training Pathologies]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/17 Reinforcement Learning from Verifiable Rewards/V3-17.10 Environments and Rollouts|V3-17.10 Environments and Rollouts]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/17 Reinforcement Learning from Verifiable Rewards/V3-17.11 Case Study Reinforcing the Repair Policy|V3-17.11 Case Study Reinforcing the Repair Policy]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/17 Reinforcement Learning from Verifiable Rewards/V3-17.12 Fallacies and Pitfalls|V3-17.12 Fallacies and Pitfalls]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/17 Reinforcement Learning from Verifiable Rewards/V3-17.13 Summary|V3-17.13 Summary]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/17 Reinforcement Learning from Verifiable Rewards/V3-17.14 Historical Perspective and Further Reading|V3-17.14 Historical Perspective and Further Reading]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/17 Reinforcement Learning from Verifiable Rewards/V3-17.15 Exercises|V3-17.15 Exercises]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/17 Reinforcement Learning from Verifiable Rewards/V3-17.16 Source References|V3-17.16 Source References]]
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/17 Reinforcement Learning from Verifiable Rewards/V3-17.17 Footnotes|V3-17.17 Footnotes]]

Next: [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/17 Reinforcement Learning from Verifiable Rewards/V3-17.01 Purpose|V3-17.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/17_rlvr/17_rlvr.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol3/17_rlvr/17_rlvr.html#sec-vol3-rlvr). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Lifecycle/Training & Adaptation/Credit Assignment|Credit Assignment]]
- [[02 Concepts/Lifecycle/Training & Adaptation/Reward Hacking|Reward Hacking]]
- [[02 Concepts/Lifecycle/Training & Adaptation/RL with Verifiable Rewards|RL with Verifiable Rewards]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume III - Agentic Systems/00 Introduction/01 Introduction/V3-01 Introduction|V3-01 Introduction]] — Closure evidence levels; Horizon compounding; Cost per accepted task; Invariant closure; H·S·A exposures.
- [[01 Books/Volume III - Agentic Systems/01 The Model/03 Test-Time Compute/V3-03 Test-Time Compute|V3-03 Test-Time Compute]] — Verifier precision; Selection pressure; Step-level evidence.
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05 KV Cache Management|V3-05 KV Cache Management]] — Little's law; Reusable is not applicable.
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07 Tool Calling|V3-07 Tool Calling]] — Complete mediation.
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08 Agent Sandboxes|V3-08 Agent Sandboxes]] — Isolation envelopes; Egress control.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12 Failure Recovery|V3-12 Failure Recovery]] — Semantic watchdog.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13 Agent Evaluation|V3-13 Agent Evaluation]] — Grader isolation; Grader calibration; Task acceptance contract; Repeated-run consistency; Matched-budget evaluation; Hermetic evaluation gym.
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/15 Trajectory Curation/V3-15 Trajectory Curation|V3-15 Trajectory Curation]] — Learning artifacts from one record; Task-group splits; Self-selection narrowing; Bounded collection flow.
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/16 Trajectory Fine-Tuning/V3-16 Trajectory Fine-Tuning|V3-16 Trajectory Fine-Tuning]] — Delivered-prefix serialization; Loss masking; Exposure bias; Closed-loop release criterion.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/17_rlvr/rlvr_concepts.yml)

<!-- Semantic Navigation: End -->
