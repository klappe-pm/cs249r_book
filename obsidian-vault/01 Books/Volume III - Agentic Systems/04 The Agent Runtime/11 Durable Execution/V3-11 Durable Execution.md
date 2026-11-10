---
title: V3-11 Durable Execution
type: Chapter
volume: 3
chapter: 11
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol3/11_durable_execution/11_durable_execution.qmd
source_anchor: sec-vol3-durable-execution
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_3
rendered_source_url: https://mlsysbook.ai/vol3/11_durable_execution/11_durable_execution.html
---

# V3-11 Durable Execution

[[Home|Home]] · [[01 Books/Volume III - Agentic Systems/Volume 3 Overview|Volume Overview]]

^sec-vol3-durable-execution

[Lecture slides](https://mlsysbook.ai/slides/vol3.html#ch-11) for this chapter

![[90 Assets/Volume III/11 Durable Execution/Cover Checkpointing Blueprint Labeled 0f249b1b06.webp]]

*Blueprint for Durable Execution.*

## Chapter Sections

- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11.01 Purpose|V3-11.01 Purpose]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11.02 Worker Failure Mid-Trajectory|V3-11.02 Worker Failure Mid-Trajectory]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11.03 The Trajectory Log|V3-11.03 The Trajectory Log]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11.04 Durable Intent Before Dispatch|V3-11.04 Durable Intent Before Dispatch]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11.05 Checkpoints|V3-11.05 Checkpoints]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11.06 Resuming a Trajectory|V3-11.06 Resuming a Trajectory]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11.07 Recorded Trajectory Replay|V3-11.07 Recorded Trajectory Replay]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11.08 Locating a Divergence|V3-11.08 Locating a Divergence]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11.09 Log Retention and State Compaction|V3-11.09 Log Retention and State Compaction]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11.10 Fallacies and Pitfalls|V3-11.10 Fallacies and Pitfalls]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11.11 Summary|V3-11.11 Summary]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11.12 Historical Perspective and Further Reading|V3-11.12 Historical Perspective and Further Reading]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11.13 Exercises|V3-11.13 Exercises]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11.14 Source References|V3-11.14 Source References]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11.15 Footnotes|V3-11.15 Footnotes]]

Next: [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11.01 Purpose|V3-11.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/11_durable_execution/11_durable_execution.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol3/11_durable_execution/11_durable_execution.html#sec-vol3-durable-execution). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/System Types/Agentic Systems/Durable Execution|Durable Execution]]
- [[02 Concepts/Qualities/Reliability & Fault Tolerance/Recovery Checkpoint|Recovery Checkpoint]]

## Related Themes

- [[03 Themes/Reliability and Recovery|Reliability and Recovery]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume III - Agentic Systems/00 Introduction/01 Introduction/V3-01 Introduction|V3-01 Introduction]] — H·S·A exposures; Lighthouse workloads; Horizon compounding; Cost per accepted task; Invariant closure.
- [[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02 The Foundation Model|V3-02 The Foundation Model]] — Recorded calls replay, served calls do not.
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04 Context Engineering|V3-04 Context Engineering]] — Context compaction; Change-rate ordering.
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05 KV Cache Management|V3-05 KV Cache Management]] — Radix prefix cache.
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07 Tool Calling|V3-07 Tool Calling]] — Settlement before retry; Operation identity; Reconciliation probe; Bounded observation.
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08 Agent Sandboxes|V3-08 Agent Sandboxes]] — Credential brokering; Copy-on-write workspace.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10 The Agent Harness|V3-10 The Agent Harness]] — Trajectory record; Settlement rule; Guarded transitions; Bounded-liability admission; Approval escrow.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/11_durable_execution/durable_execution_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12 Failure Recovery|V3-12 Failure Recovery]] — Compensation; Recovery decision order; Semantic watchdog.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13 Agent Evaluation|V3-13 Agent Evaluation]] — Task sampling and score intervals.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/14 Operating Agents/V3-14 Operating Agents|V3-14 Operating Agents]] — Trace retention.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/11_durable_execution/durable_execution_concepts.yml)

<!-- Semantic Navigation: End -->
