---
title: V3-10 The Agent Harness
type: Chapter
volume: 3
chapter: 10
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol3/10_agent_harness/10_agent_harness.qmd
source_anchor: sec-vol3-agent-harness
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_3
rendered_source_url: https://mlsysbook.ai/vol3/10_agent_harness/10_agent_harness.html
---

# V3-10 The Agent Harness

[[Home|Home]] · [[01 Books/Volume III - Agentic Systems/Volume 3 Overview|Volume Overview]]

^sec-vol3-agent-harness

[Lecture slides](https://mlsysbook.ai/slides/vol3.html#ch-10) for this chapter

![[90 Assets/Volume III/10 Agent Harness/Cover Interrupts Blueprint Labeled da2a258bf7.webp]]

*Blueprint illustration for the agent harness chapter.*

## Chapter Sections

- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10.01 Purpose|V3-10.01 Purpose]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10.02 Supervising Continuation|V3-10.02 Supervising Continuation]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10.03 The Loop and the Harness|V3-10.03 The Loop and the Harness]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10.04 The Trajectory Record|V3-10.04 The Trajectory Record]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10.05 Trajectory States|V3-10.05 Trajectory States]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10.06 Control Actions|V3-10.06 Control Actions]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10.07 Supervised Waiting|V3-10.07 Supervised Waiting]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10.08 Approval Gates|V3-10.08 Approval Gates]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10.09 Scheduling Concurrent Trajectories|V3-10.09 Scheduling Concurrent Trajectories]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10.10 Budgets and Ceilings|V3-10.10 Budgets and Ceilings]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10.11 Fallacies and Pitfalls|V3-10.11 Fallacies and Pitfalls]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10.12 Summary|V3-10.12 Summary]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10.13 Historical Perspective and Further Reading|V3-10.13 Historical Perspective and Further Reading]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10.14 Exercises|V3-10.14 Exercises]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10.15 Source References|V3-10.15 Source References]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10.16 Footnotes|V3-10.16 Footnotes]]

Next: [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10.01 Purpose|V3-10.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/10_agent_harness/10_agent_harness.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol3/10_agent_harness/10_agent_harness.html#sec-vol3-agent-harness). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/System Types/Agentic Systems/Agent Execution Budget|Agent Execution Budget]]
- [[02 Concepts/System Types/Agentic Systems/Agent Harness|Agent Harness]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume III - Agentic Systems/00 Introduction/01 Introduction/V3-01 Introduction|V3-01 Introduction]] — Six-phase turn lifecycle; Horizon compounding; Invariant closure; Cost per accepted task; Lighthouse workloads.
- [[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02 The Foundation Model|V3-02 The Foundation Model]] — Invocation contract; Output-bound call latency; Quadratic resend and prefix reuse.
- [[01 Books/Volume III - Agentic Systems/01 The Model/03 Test-Time Compute/V3-03 Test-Time Compute|V3-03 Test-Time Compute]] — Search accounting; Stopping precedence; Revisable candidate plans.
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04 Context Engineering|V3-04 Context Engineering]] — Context compaction; Usable working context.
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05 KV Cache Management|V3-05 KV Cache Management]] — Residency tax; Little's law; Paused-state policy.
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07 Tool Calling|V3-07 Tool Calling]] — Operation identity; Settlement before retry; Acknowledgment is not completion; Action-time preconditions.
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08 Agent Sandboxes|V3-08 Agent Sandboxes]] — Copy-on-write workspace; Reset contract.
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/09 Agent Security/V3-09 Agent Security|V3-09 Agent Security]] — Action-bound approval.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/10_agent_harness/agent_harness_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11 Durable Execution|V3-11 Durable Execution]] — Durable intent before dispatch; Trajectory log.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12 Failure Recovery|V3-12 Failure Recovery]] — Compensation; Semantic watchdog.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13 Agent Evaluation|V3-13 Agent Evaluation]] — Matched-budget evaluation; Task acceptance contract.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/10_agent_harness/agent_harness_concepts.yml)

<!-- Semantic Navigation: End -->
