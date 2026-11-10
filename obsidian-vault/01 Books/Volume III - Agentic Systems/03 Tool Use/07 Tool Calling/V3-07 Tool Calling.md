---
title: V3-07 Tool Calling
type: Chapter
volume: 3
chapter: 7
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol3/07_tool_calling/07_tool_calling.qmd
source_anchor: sec-vol3-tool-calling
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_3
rendered_source_url: https://mlsysbook.ai/vol3/07_tool_calling/07_tool_calling.html
---

# V3-07 Tool Calling

[[Home|Home]] · [[01 Books/Volume III - Agentic Systems/Volume 3 Overview|Volume Overview]]

^sec-vol3-tool-calling

[Lecture slides](https://mlsysbook.ai/slides/vol3.html#ch-07) for this chapter

![[90 Assets/Volume III/07 Tool Calling/Cover Actuation Blueprint Labeled fefea21269.webp]]

*Blueprint for Tool Execution.*

## Chapter Sections

- [[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07.01 Purpose|V3-07.01 Purpose]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07.02 The Tool Boundary|V3-07.02 The Tool Boundary]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07.03 Tool Subsystem Architecture|V3-07.03 Tool Subsystem Architecture]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07.04 Tool Interface Schemas|V3-07.04 Tool Interface Schemas]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07.05 Interoperable Tool Discovery|V3-07.05 Interoperable Tool Discovery]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07.06 Retrying Uncertain Actions|V3-07.06 Retrying Uncertain Actions]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07.07 Observation Stream Truncation|V3-07.07 Observation Stream Truncation]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07.08 Terminal Output Normalization|V3-07.08 Terminal Output Normalization]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07.09 Asynchronous Tool Dispatch|V3-07.09 Asynchronous Tool Dispatch]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07.10 Designing the Active Toolkit|V3-07.10 Designing the Active Toolkit]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07.11 Visual Actuation and Computer Use|V3-07.11 Visual Actuation and Computer Use]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07.12 Fallacies and Pitfalls|V3-07.12 Fallacies and Pitfalls]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07.13 Summary|V3-07.13 Summary]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07.14 Historical Perspective and Further Reading|V3-07.14 Historical Perspective and Further Reading]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07.15 Exercises|V3-07.15 Exercises]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07.16 Source References|V3-07.16 Source References]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07.17 Footnotes|V3-07.17 Footnotes]]

Next: [[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07.01 Purpose|V3-07.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/07_tool_calling/07_tool_calling.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol3/07_tool_calling/07_tool_calling.html#sec-vol3-tool-calling). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Qualities/Reliability & Fault Tolerance/Idempotency|Idempotency]]

## Related Themes

- [[03 Themes/Reliability and Recovery|Reliability and Recovery]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume III - Agentic Systems/00 Introduction/01 Introduction/V3-01 Introduction|V3-01 Introduction]] — Six-phase turn lifecycle; Side-effect classes; Zero ambient authority; Invariant closure; Cost per accepted task.
- [[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02 The Foundation Model|V3-02 The Foundation Model]] — Proposal boundary; Grammar-constrained decoding; Invocation contract; Interface choice under matched budgets.
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04 Context Engineering|V3-04 Context Engineering]] — Working-set partition; Change-rate ordering.
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05 KV Cache Management|V3-05 KV Cache Management]] — Paused-state policy; Radix prefix cache.
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/06 Long-Term Memory/V3-06 Long-Term Memory|V3-06 Long-Term Memory]] — Retrieval contract.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/07_tool_calling/tool_calling_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08 Agent Sandboxes|V3-08 Agent Sandboxes]] — Reset contract; Isolation envelopes; Least privilege.
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/09 Agent Security/V3-09 Agent Security|V3-09 Agent Security]] — Structural prompt injection.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11 Durable Execution|V3-11 Durable Execution]] — Durable intent before dispatch; Resume protocol; Fencing tokens.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12 Failure Recovery|V3-12 Failure Recovery]] — Trajectory saga.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/07_tool_calling/tool_calling_concepts.yml)

<!-- Semantic Navigation: End -->
