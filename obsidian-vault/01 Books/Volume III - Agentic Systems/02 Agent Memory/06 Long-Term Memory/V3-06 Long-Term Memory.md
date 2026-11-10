---
title: V3-06 Long-Term Memory
type: Chapter
volume: 3
chapter: 6
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol3/06_long_term_memory/06_long_term_memory.qmd
source_anchor: sec-vol3-long-term-memory
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_3
rendered_source_url: https://mlsysbook.ai/vol3/06_long_term_memory/06_long_term_memory.html
---

# V3-06 Long-Term Memory

[[Home|Home]] · [[01 Books/Volume III - Agentic Systems/Volume 3 Overview|Volume Overview]]

^sec-vol3-long-term-memory

[Lecture slides](https://mlsysbook.ai/slides/vol3.html#ch-06) for this chapter

![[90 Assets/Volume III/06 Long Term Memory/Cover Episodic Memory Blueprint Labeled 951222b27d.webp]]

*Blueprint for Persistent Storage.*

## Chapter Sections

- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/06 Long-Term Memory/V3-06.01 Purpose|V3-06.01 Purpose]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/06 Long-Term Memory/V3-06.02 Memory Beyond One Session|V3-06.02 Memory Beyond One Session]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/06 Long-Term Memory/V3-06.03 Persistent Records|V3-06.03 Persistent Records]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/06 Long-Term Memory/V3-06.04 The Retrieval Contract|V3-06.04 The Retrieval Contract]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/06 Long-Term Memory/V3-06.05 Agentic Retrieval|V3-06.05 Agentic Retrieval]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/06 Long-Term Memory/V3-06.06 Lexical and Structural Retrieval|V3-06.06 Lexical and Structural Retrieval]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/06 Long-Term Memory/V3-06.07 Dense and Hybrid Retrieval|V3-06.07 Dense and Hybrid Retrieval]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/06 Long-Term Memory/V3-06.08 Multi-Hop Retrieval|V3-06.08 Multi-Hop Retrieval]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/06 Long-Term Memory/V3-06.09 The Memory Write Path|V3-06.09 The Memory Write Path]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/06 Long-Term Memory/V3-06.10 Storage Invalidation|V3-06.10 Storage Invalidation]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/06 Long-Term Memory/V3-06.11 Evaluating Memory Policies|V3-06.11 Evaluating Memory Policies]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/06 Long-Term Memory/V3-06.12 Fallacies and Pitfalls|V3-06.12 Fallacies and Pitfalls]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/06 Long-Term Memory/V3-06.13 Summary|V3-06.13 Summary]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/06 Long-Term Memory/V3-06.14 Historical Perspective and Further Reading|V3-06.14 Historical Perspective and Further Reading]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/06 Long-Term Memory/V3-06.15 Exercises|V3-06.15 Exercises]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/06 Long-Term Memory/V3-06.16 Source References|V3-06.16 Source References]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/06 Long-Term Memory/V3-06.17 Footnotes|V3-06.17 Footnotes]]

Next: [[01 Books/Volume III - Agentic Systems/02 Agent Memory/06 Long-Term Memory/V3-06.01 Purpose|V3-06.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/06_long_term_memory/06_long_term_memory.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol3/06_long_term_memory/06_long_term_memory.html#sec-vol3-long-term-memory). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Lifecycle/Data Engineering/Data Lineage|Data Lineage]]
- [[02 Concepts/System Types/Agentic Systems/Long Term Agent Memory|Long Term Agent Memory]]
- [[02 Concepts/Lifecycle/Deployment & Serving/Retrieval|Retrieval]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume III - Agentic Systems/00 Introduction/01 Introduction/V3-01 Introduction|V3-01 Introduction]] — Cost per accepted task; Horizon compounding; H·S·A exposures; Invariant closure; Lighthouse workloads.
- [[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02 The Foundation Model|V3-02 The Foundation Model]] — Output-bound call latency.
- [[01 Books/Volume III - Agentic Systems/01 The Model/03 Test-Time Compute/V3-03 Test-Time Compute|V3-03 Test-Time Compute]] — Verifier precision.
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04 Context Engineering|V3-04 Context Engineering]] — Context invalidation; Scope rule; Usable working context.
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05 KV Cache Management|V3-05 KV Cache Management]] — Reusable is not applicable; KV footprint and resident fit.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/06_long_term_memory/long_term_memory_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07 Tool Calling|V3-07 Tool Calling]] — Action-time preconditions.
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/09 Agent Security/V3-09 Agent Security|V3-09 Agent Security]] — Structural prompt injection; Information-flow labels.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11 Durable Execution|V3-11 Durable Execution]] — Trajectory log.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13 Agent Evaluation|V3-13 Agent Evaluation]] — Hermetic evaluation gym; Contamination.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/06_long_term_memory/long_term_memory_concepts.yml)

<!-- Semantic Navigation: End -->
