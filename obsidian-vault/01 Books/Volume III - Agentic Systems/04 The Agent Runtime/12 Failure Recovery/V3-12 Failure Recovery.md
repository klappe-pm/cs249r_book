---
title: V3-12 Failure Recovery
type: Chapter
volume: 3
chapter: 12
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol3/12_failure_recovery/12_failure_recovery.qmd
source_anchor: sec-vol3-failure-recovery
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_3
rendered_source_url: https://mlsysbook.ai/vol3/12_failure_recovery/12_failure_recovery.html
---

# V3-12 Failure Recovery

[[Home|Home]] · [[01 Books/Volume III - Agentic Systems/Volume 3 Overview|Volume Overview]]

^sec-vol3-failure-recovery

[Lecture slides](https://mlsysbook.ai/slides/vol3.html#ch-12) for this chapter

![[90 Assets/Volume III/12 Failure Recovery/Cover Scheduling Blueprint Labeled e7ab11c526.webp]]

*Blueprint for Fault Recovery.*

## Chapter Sections

- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12.01 Purpose|V3-12.01 Purpose]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12.02 Recovering After Partial Effects|V3-12.02 Recovering After Partial Effects]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12.03 Effects Outside a Shared Transaction|V3-12.03 Effects Outside a Shared Transaction]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12.04 The Trajectory Saga Pattern|V3-12.04 The Trajectory Saga Pattern]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12.05 Forward Recovery|V3-12.05 Forward Recovery]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12.06 Irreversible Commitments|V3-12.06 Irreversible Commitments]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12.07 Semantic Watchdogs|V3-12.07 Semantic Watchdogs]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12.08 Tool Circuit Breakers|V3-12.08 Tool Circuit Breakers]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12.09 Incident Containment|V3-12.09 Incident Containment]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12.10 Fault-Tolerant System Synthesis|V3-12.10 Fault-Tolerant System Synthesis]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12.11 Fallacies and Pitfalls|V3-12.11 Fallacies and Pitfalls]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12.12 Summary|V3-12.12 Summary]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12.13 Historical Perspective and Further Reading|V3-12.13 Historical Perspective and Further Reading]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12.14 Exercises|V3-12.14 Exercises]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12.15 Source References|V3-12.15 Source References]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12.16 Footnotes|V3-12.16 Footnotes]]

Next: [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12.01 Purpose|V3-12.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/12_failure_recovery/12_failure_recovery.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol3/12_failure_recovery/12_failure_recovery.html#sec-vol3-failure-recovery). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/System Types/Agentic Systems/Agent Loop Detection|Agent Loop Detection]]
- [[02 Concepts/Qualities/Reliability & Fault Tolerance/Compensating Action|Compensating Action]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume III - Agentic Systems/00 Introduction/01 Introduction/V3-01 Introduction|V3-01 Introduction]] — Cost per accepted task; Side-effect classes.
- [[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02 The Foundation Model|V3-02 The Foundation Model]] — Quadratic resend and prefix reuse.
- [[01 Books/Volume III - Agentic Systems/01 The Model/03 Test-Time Compute/V3-03 Test-Time Compute|V3-03 Test-Time Compute]] — Allocation axes.
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05 KV Cache Management|V3-05 KV Cache Management]] — Radix prefix cache; Little's law.
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/06 Long-Term Memory/V3-06 Long-Term Memory|V3-06 Long-Term Memory]] — Memory poisoning.
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07 Tool Calling|V3-07 Tool Calling]] — Settlement before retry; Operation identity; Reconciliation probe.
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/09 Agent Security/V3-09 Agent Security|V3-09 Agent Security]] — Information-flow labels.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10 The Agent Harness|V3-10 The Agent Harness]] — Settlement rule; Bounded-liability admission; Guarded transitions; Trajectory budget vector; Approval escrow; Harness owns continuation.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11 Durable Execution|V3-11 Durable Execution]] — Durable intent before dispatch; Checkpoint binding; Resume protocol; Record and replay.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/12_failure_recovery/failure_recovery_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13 Agent Evaluation|V3-13 Agent Evaluation]] — Paired comparison; Grader isolation.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/14 Operating Agents/V3-14 Operating Agents|V3-14 Operating Agents]] — Release gate.
- [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/18 Multi-Agent Coordination/V3-18 Multi-Agent Coordination|V3-18 Multi-Agent Coordination]] — Subtree cancellation.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/12_failure_recovery/failure_recovery_concepts.yml)

<!-- Semantic Navigation: End -->
