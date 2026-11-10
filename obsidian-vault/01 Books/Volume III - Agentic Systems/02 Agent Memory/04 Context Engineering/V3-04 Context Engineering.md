---
title: V3-04 Context Engineering
type: Chapter
volume: 3
chapter: 4
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol3/04_context_engineering/04_context_engineering.qmd
source_anchor: sec-vol3-context-engineering
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_3
rendered_source_url: https://mlsysbook.ai/vol3/04_context_engineering/04_context_engineering.html
---

# V3-04 Context Engineering

[[Home|Home]] · [[01 Books/Volume III - Agentic Systems/Volume 3 Overview|Volume Overview]]

^sec-vol3-context-engineering

[Lecture slides](https://mlsysbook.ai/slides/vol3.html#ch-04) for this chapter

![[90 Assets/Volume III/04 Context Engineering/Cover Working Sets Blueprint Labeled c658c95ae1.webp]]

*Blueprint illustration of a bounded working context.*

## Chapter Sections

- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04.01 Purpose|V3-04.01 Purpose]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04.02 Carrying a Repair Across Turns|V3-04.02 Carrying a Repair Across Turns]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04.03 The Working-Set Decision|V3-04.03 The Working-Set Decision]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04.04 Usable Working Context|V3-04.04 Usable Working Context]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04.05 Staging the Next Invocation|V3-04.05 Staging the Next Invocation]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04.06 Context Compaction|V3-04.06 Context Compaction]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04.07 Structured Progress Records|V3-04.07 Structured Progress Records]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04.08 Context Invalidation|V3-04.08 Context Invalidation]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04.09 Evaluating Context Policies|V3-04.09 Evaluating Context Policies]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04.10 Fallacies and Pitfalls|V3-04.10 Fallacies and Pitfalls]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04.11 Summary|V3-04.11 Summary]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04.12 Historical Perspective and Further Reading|V3-04.12 Historical Perspective and Further Reading]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04.13 Exercises|V3-04.13 Exercises]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04.14 Source References|V3-04.14 Source References]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04.15 Footnotes|V3-04.15 Footnotes]]

Next: [[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04.01 Purpose|V3-04.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/04_context_engineering/04_context_engineering.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol3/04_context_engineering/04_context_engineering.html#sec-vol3-context-engineering). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/System Types/Agentic Systems/Context Compaction|Context Compaction]]
- [[02 Concepts/System Types/Agentic Systems/Context Selection|Context Selection]]
- [[02 Concepts/System Types/Agentic Systems/Context Staleness|Context Staleness]]
- [[02 Concepts/Foundations/Models & Architectures/Context Window|Context Window]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume III - Agentic Systems/00 Introduction/01 Introduction/V3-01 Introduction|V3-01 Introduction]] — Lighthouse workloads; Task contract; Horizon compounding; Cost per accepted task; H·S·A exposures.
- [[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02 The Foundation Model|V3-02 The Foundation Model]] — Token-measured admission; Quadratic resend and prefix reuse; Grammar-constrained decoding; Recorded calls replay, served calls do not.
- [[01 Books/Volume III - Agentic Systems/01 The Model/03 Test-Time Compute/V3-03 Test-Time Compute|V3-03 Test-Time Compute]] — Revisable candidate plans.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/04_context_engineering/context_engineering_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05 KV Cache Management|V3-05 KV Cache Management]] — Radix prefix cache; Reusable is not applicable.
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/06 Long-Term Memory/V3-06 Long-Term Memory|V3-06 Long-Term Memory]] — Record roles.
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07 Tool Calling|V3-07 Tool Calling]] — Action-time preconditions.
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/09 Agent Security/V3-09 Agent Security|V3-09 Agent Security]] — Structural prompt injection; Information-flow labels.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11 Durable Execution|V3-11 Durable Execution]] — Checkpoint binding.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13 Agent Evaluation|V3-13 Agent Evaluation]] — Task sampling and score intervals; Task acceptance contract.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/04_context_engineering/context_engineering_concepts.yml)

<!-- Semantic Navigation: End -->
