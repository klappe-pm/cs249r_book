---
title: V3-14 Operating Agents
type: Chapter
volume: 3
chapter: 14
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol3/14_agent_operations/14_agent_operations.qmd
source_anchor: sec-vol3-operations
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_3
rendered_source_url: https://mlsysbook.ai/vol3/14_agent_operations/14_agent_operations.html
---

# V3-14 Operating Agents

[[Home|Home]] · [[01 Books/Volume III - Agentic Systems/Volume 3 Overview|Volume Overview]]

^sec-vol3-operations

[Lecture slides](https://mlsysbook.ai/slides/vol3.html#ch-14) for this chapter

![[90 Assets/Volume III/14 Agent Operations/Cover Observability Blueprint Labeled f052f4b6e3.webp]]

*Blueprint for System Observability.*

## Chapter Sections

- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/14 Operating Agents/V3-14.01 Purpose|V3-14.01 Purpose]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/14 Operating Agents/V3-14.02 From Offline Verdict to Live Operation|V3-14.02 From Offline Verdict to Live Operation]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/14 Operating Agents/V3-14.03 Distributed Trajectory Tracing|V3-14.03 Distributed Trajectory Tracing]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/14 Operating Agents/V3-14.04 Trace Retention and Privacy|V3-14.04 Trace Retention and Privacy]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/14 Operating Agents/V3-14.05 Incident Postmortems|V3-14.05 Incident Postmortems]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/14 Operating Agents/V3-14.06 Staged Releases|V3-14.06 Staged Releases]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/14 Operating Agents/V3-14.07 The Release Decision|V3-14.07 The Release Decision]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/14 Operating Agents/V3-14.08 Fallacies and Pitfalls|V3-14.08 Fallacies and Pitfalls]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/14 Operating Agents/V3-14.09 Summary|V3-14.09 Summary]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/14 Operating Agents/V3-14.10 Historical Perspective and Further Reading|V3-14.10 Historical Perspective and Further Reading]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/14 Operating Agents/V3-14.11 Exercises|V3-14.11 Exercises]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/14 Operating Agents/V3-14.12 Source References|V3-14.12 Source References]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/14 Operating Agents/V3-14.13 Footnotes|V3-14.13 Footnotes]]

Next: [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/14 Operating Agents/V3-14.01 Purpose|V3-14.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/14_agent_operations/14_agent_operations.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol3/14_agent_operations/14_agent_operations.html#sec-vol3-operations). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Lifecycle/MLOps & Operations/ML Failure Attribution|ML Failure Attribution]]
- [[02 Concepts/Lifecycle/MLOps & Operations/Model and Agent Call Tracing|Model and Agent Call Tracing]]
- [[02 Concepts/Lifecycle/MLOps & Operations/Staged Rollout|Staged Rollout]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume III - Agentic Systems/00 Introduction/01 Introduction/V3-01 Introduction|V3-01 Introduction]] — Invariant closure; Cost per accepted task; H·S·A exposures; Lighthouse workloads.
- [[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02 The Foundation Model|V3-02 The Foundation Model]] — Quadratic resend and prefix reuse.
- [[01 Books/Volume III - Agentic Systems/01 The Model/03 Test-Time Compute/V3-03 Test-Time Compute|V3-03 Test-Time Compute]] — Stopping precedence.
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07 Tool Calling|V3-07 Tool Calling]] — Bounded observation; Settlement before retry.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10 The Agent Harness|V3-10 The Agent Harness]] — Trajectory budget vector.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11 Durable Execution|V3-11 Durable Execution]] — Trajectory log; Record and replay; Resume protocol.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12 Failure Recovery|V3-12 Failure Recovery]] — Incident containment; Compensation.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13 Agent Evaluation|V3-13 Agent Evaluation]] — Task acceptance contract; Hermetic evaluation gym; Task sampling and score intervals; Paired comparison.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/14_agent_operations/agent_operations_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/15 Trajectory Curation/V3-15 Trajectory Curation|V3-15 Trajectory Curation]] — Capability-gap triage.
- [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/19 Agent Economics/V3-19 Agent Economics|V3-19 Agent Economics]] — Critical-path acceleration ceiling; Trajectory goodput.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/14_agent_operations/agent_operations_concepts.yml)

<!-- Semantic Navigation: End -->
