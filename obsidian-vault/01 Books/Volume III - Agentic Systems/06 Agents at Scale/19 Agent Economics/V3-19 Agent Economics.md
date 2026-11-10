---
title: V3-19 Agent Economics
type: Chapter
volume: 3
chapter: 19
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol3/19_agent_economics/19_agent_economics.qmd
source_anchor: sec-vol3-agent-economics
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_3
rendered_source_url: https://mlsysbook.ai/vol3/19_agent_economics/19_agent_economics.html
---

# V3-19 Agent Economics

[[Home|Home]] · [[01 Books/Volume III - Agentic Systems/Volume 3 Overview|Volume Overview]]

^sec-vol3-agent-economics

[Lecture slides](https://mlsysbook.ai/slides/vol3.html#ch-19) for this chapter

![[90 Assets/Volume III/19 Agent Economics/Cover Tokenomics Blueprint Labeled 3c2209ae7c.webp]]

*Blueprint for Agent Economics.*

## Chapter Sections

- [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/19 Agent Economics/V3-19.01 Purpose|V3-19.01 Purpose]]
- [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/19 Agent Economics/V3-19.02 The Bill Behind an Accepted Repair|V3-19.02 The Bill Behind an Accepted Repair]]
- [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/19 Agent Economics/V3-19.03 Cost per Accepted Task|V3-19.03 Cost per Accepted Task]]
- [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/19 Agent Economics/V3-19.04 Context Reuse and Retry Budgets|V3-19.04 Context Reuse and Retry Budgets]]
- [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/19 Agent Economics/V3-19.05 Critical-Path Latency|V3-19.05 Critical-Path Latency]]
- [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/19 Agent Economics/V3-19.06 Model Cascades and Routing|V3-19.06 Model Cascades and Routing]]
- [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/19 Agent Economics/V3-19.07 Capacity for Trajectories|V3-19.07 Capacity for Trajectories]]
- [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/19 Agent Economics/V3-19.08 Spending Governance|V3-19.08 Spending Governance]]
- [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/19 Agent Economics/V3-19.09 Pricing the Choice of Architecture|V3-19.09 Pricing the Choice of Architecture]]
- [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/19 Agent Economics/V3-19.10 Cost per Accepted Task by Archetype|V3-19.10 Cost per Accepted Task by Archetype]]
- [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/19 Agent Economics/V3-19.11 Fallacies and Pitfalls|V3-19.11 Fallacies and Pitfalls]]
- [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/19 Agent Economics/V3-19.12 Summary|V3-19.12 Summary]]
- [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/19 Agent Economics/V3-19.13 Historical Perspective and Further Reading|V3-19.13 Historical Perspective and Further Reading]]
- [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/19 Agent Economics/V3-19.14 Exercises|V3-19.14 Exercises]]
- [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/19 Agent Economics/V3-19.15 Source References|V3-19.15 Source References]]
- [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/19 Agent Economics/V3-19.16 Footnotes|V3-19.16 Footnotes]]

Next: [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/19 Agent Economics/V3-19.01 Purpose|V3-19.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/19_agent_economics/19_agent_economics.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol3/19_agent_economics/19_agent_economics.html#sec-vol3-agent-economics). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Qualities/Sustainability & Cost/Cost per Useful Outcome|Cost per Useful Outcome]]

## Related Themes

- [[03 Themes/Accuracy and Efficiency|Accuracy and Efficiency]]
- [[03 Themes/Energy and Cost|Energy and Cost]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume III - Agentic Systems/00 Introduction/01 Introduction/V3-01 Introduction|V3-01 Introduction]] — Cost per accepted task; Horizon compounding; H·S·A exposures; Closure evidence levels; Fixed workflow vs model-directed loop; Lighthouse workloads.
- [[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02 The Foundation Model|V3-02 The Foundation Model]] — Quadratic resend and prefix reuse; Output-bound call latency.
- [[01 Books/Volume III - Agentic Systems/01 The Model/03 Test-Time Compute/V3-03 Test-Time Compute|V3-03 Test-Time Compute]] — Budgeted deliberation; Verifier precision.
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04 Context Engineering|V3-04 Context Engineering]] — Context policy evaluation; Hysteretic compaction scheduling.
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05 KV Cache Management|V3-05 KV Cache Management]] — Reusable is not applicable; Little's law; Residency tax.
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07 Tool Calling|V3-07 Tool Calling]] — Complete mediation; Operation identity; Acknowledgment is not completion.
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08 Agent Sandboxes|V3-08 Agent Sandboxes]] — Sandbox pool sizing.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10 The Agent Harness|V3-10 The Agent Harness]] — Bounded-liability admission; Budget reservation; Fair model-call scheduling; Approval escrow.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11 Durable Execution|V3-11 Durable Execution]] — Durable intent before dispatch.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12 Failure Recovery|V3-12 Failure Recovery]] — Semantic watchdog.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13 Agent Evaluation|V3-13 Agent Evaluation]] — Matched-budget evaluation; Task sampling and score intervals.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/14 Operating Agents/V3-14 Operating Agents|V3-14 Operating Agents]] — Trajectory traces; Critical path.
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/15 Trajectory Curation/V3-15 Trajectory Curation|V3-15 Trajectory Curation]] — Admission cascade.
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/16 Trajectory Fine-Tuning/V3-16 Trajectory Fine-Tuning|V3-16 Trajectory Fine-Tuning]] — Trajectory distillation.
- [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/18 Multi-Agent Coordination/V3-18 Multi-Agent Coordination|V3-18 Multi-Agent Coordination]] — Coordination overhead; Amdahl's law; Matched single-controller baseline; Attenuated delegation; Subtree cancellation; Fan-out completion contracts.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/19_agent_economics/agent_economics_concepts.yml)

<!-- Semantic Navigation: End -->
