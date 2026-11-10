---
title: V3-18 Multi-Agent Coordination
type: Chapter
volume: 3
chapter: 18
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol3/18_multi_agent/18_multi_agent.qmd
source_anchor: sec-vol3-multi-agent
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_3
rendered_source_url: https://mlsysbook.ai/vol3/18_multi_agent/18_multi_agent.html
---

# V3-18 Multi-Agent Coordination

[[Home|Home]] · [[01 Books/Volume III - Agentic Systems/Volume 3 Overview|Volume Overview]]

^sec-vol3-multi-agent

[Lecture slides](https://mlsysbook.ai/slides/vol3.html#ch-18) for this chapter

![[90 Assets/Volume III/18 Multi Agent/Cover Multi Agent Blueprint Labeled 9a23ef0702.webp]]

*Blueprint for Multi-Agent Coordination.*

## Chapter Sections

- [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/18 Multi-Agent Coordination/V3-18.01 Purpose|V3-18.01 Purpose]]
- [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/18 Multi-Agent Coordination/V3-18.02 Splitting the Repair Agent’s Work|V3-18.02 Splitting the Repair Agent’s Work]]
- [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/18 Multi-Agent Coordination/V3-18.03 The Delegation Trade-Off|V3-18.03 The Delegation Trade-Off]]
- [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/18 Multi-Agent Coordination/V3-18.04 Coordination Topologies|V3-18.04 Coordination Topologies]]
- [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/18 Multi-Agent Coordination/V3-18.05 Typed Task Envelopes|V3-18.05 Typed Task Envelopes]]
- [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/18 Multi-Agent Coordination/V3-18.06 Optimistic Concurrency Control|V3-18.06 Optimistic Concurrency Control]]
- [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/18 Multi-Agent Coordination/V3-18.07 Correlated Ensemble Failures|V3-18.07 Correlated Ensemble Failures]]
- [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/18 Multi-Agent Coordination/V3-18.08 Bounding In-Flight Work|V3-18.08 Bounding In-Flight Work]]
- [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/18 Multi-Agent Coordination/V3-18.09 Capability Delegation|V3-18.09 Capability Delegation]]
- [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/18 Multi-Agent Coordination/V3-18.10 Benchmarking Against a Single Agent|V3-18.10 Benchmarking Against a Single Agent]]
- [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/18 Multi-Agent Coordination/V3-18.11 Fallacies and Pitfalls|V3-18.11 Fallacies and Pitfalls]]
- [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/18 Multi-Agent Coordination/V3-18.12 Summary|V3-18.12 Summary]]
- [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/18 Multi-Agent Coordination/V3-18.13 Historical Perspective and Further Reading|V3-18.13 Historical Perspective and Further Reading]]
- [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/18 Multi-Agent Coordination/V3-18.14 Exercises|V3-18.14 Exercises]]
- [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/18 Multi-Agent Coordination/V3-18.15 Source References|V3-18.15 Source References]]
- [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/18 Multi-Agent Coordination/V3-18.16 Footnotes|V3-18.16 Footnotes]]

Next: [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/18 Multi-Agent Coordination/V3-18.01 Purpose|V3-18.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/18_multi_agent/18_multi_agent.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol3/18_multi_agent/18_multi_agent.html#sec-vol3-multi-agent). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/System Types/Agentic Systems/Multi Agent Orchestration|Multi Agent Orchestration]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume III - Agentic Systems/00 Introduction/01 Introduction/V3-01 Introduction|V3-01 Introduction]] — Cost per accepted task; Horizon compounding; Fail-plausible fault.
- [[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02 The Foundation Model|V3-02 The Foundation Model]] — Quadratic resend and prefix reuse.
- [[01 Books/Volume III - Agentic Systems/01 The Model/03 Test-Time Compute/V3-03 Test-Time Compute|V3-03 Test-Time Compute]] — Coverage is not selection.
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04 Context Engineering|V3-04 Context Engineering]] — Change-rate ordering; Context invalidation; Scope rule.
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05 KV Cache Management|V3-05 KV Cache Management]] — Little's law.
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07 Tool Calling|V3-07 Tool Calling]] — Action-time preconditions; Settlement before retry; Operation identity; Confused deputy.
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08 Agent Sandboxes|V3-08 Agent Sandboxes]] — Copy-on-write workspace; Capability grants; Attenuation and revocation.
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/09 Agent Security/V3-09 Agent Security|V3-09 Agent Security]] — Action-bound approval.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10 The Agent Harness|V3-10 The Agent Harness]] — Bounded-liability admission; Turn-boundary control; Settlement rule.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11 Durable Execution|V3-11 Durable Execution]] — Fencing tokens; Durable intent before dispatch.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12 Failure Recovery|V3-12 Failure Recovery]] — Cleanup graph.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13 Agent Evaluation|V3-13 Agent Evaluation]] — Grader isolation; Matched-budget evaluation.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/14 Operating Agents/V3-14 Operating Agents|V3-14 Operating Agents]] — Critical path.
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/15 Trajectory Curation/V3-15 Trajectory Curation|V3-15 Trajectory Curation]] — Bounded collection flow.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/18_multi_agent/multi_agent_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/19 Agent Economics/V3-19 Agent Economics|V3-19 Agent Economics]] — Architecture pricing with human fallback; Budget conservation; Cohort cost per accepted task.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/18_multi_agent/multi_agent_concepts.yml)

<!-- Semantic Navigation: End -->
