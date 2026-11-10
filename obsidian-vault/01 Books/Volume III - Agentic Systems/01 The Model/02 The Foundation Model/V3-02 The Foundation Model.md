---
title: V3-02 The Foundation Model
type: Chapter
volume: 3
chapter: 2
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol3/02_foundation_model/02_foundation_model.qmd
source_anchor: sec-vol3-foundation-model
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_3
rendered_source_url: https://mlsysbook.ai/vol3/02_foundation_model/02_foundation_model.html
---

# V3-02 The Foundation Model

[[Home|Home]] · [[01 Books/Volume III - Agentic Systems/Volume 3 Overview|Volume Overview]]

^sec-vol3-foundation-model

[Lecture slides](https://mlsysbook.ai/slides/vol3.html#ch-02) for this chapter

![[90 Assets/Volume III/02 Foundation Model/Cover Processor Blueprint Labeled ceec72a296.webp]]

*Isometric illustration of a small robot laying orange token tiles along a track while a larger robot checks each tile, turning accepted tiles green and diverting a rejected red tile into a bin, so that only checked tokens continue down the track.*

## Chapter Sections

- [[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02.01 Purpose|V3-02.01 Purpose]]
- [[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02.02 One Turn of the Repair Loop|V3-02.02 One Turn of the Repair Loop]]
- [[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02.03 The Model Call Boundary|V3-02.03 The Model Call Boundary]]
- [[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02.04 Tokenizing the Request|V3-02.04 Tokenizing the Request]]
- [[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02.05 Autoregressive Generation|V3-02.05 Autoregressive Generation]]
- [[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02.06 The Invocation Contract|V3-02.06 The Invocation Contract]]
- [[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02.07 Checking Candidate Outputs|V3-02.07 Checking Candidate Outputs]]
- [[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02.08 Grammar-Guided Decoding|V3-02.08 Grammar-Guided Decoding]]
- [[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02.09 The Cost of a Model Call|V3-02.09 The Cost of a Model Call]]
- [[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02.10 Comparing Output Interfaces|V3-02.10 Comparing Output Interfaces]]
- [[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02.11 Fallacies and Pitfalls|V3-02.11 Fallacies and Pitfalls]]
- [[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02.12 Summary|V3-02.12 Summary]]
- [[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02.13 Historical Perspective and Further Reading|V3-02.13 Historical Perspective and Further Reading]]
- [[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02.14 Exercises|V3-02.14 Exercises]]
- [[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02.15 Source References|V3-02.15 Source References]]
- [[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02.16 Footnotes|V3-02.16 Footnotes]]

Next: [[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02.01 Purpose|V3-02.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/02_foundation_model/02_foundation_model.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol3/02_foundation_model/02_foundation_model.html#sec-vol3-foundation-model). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Lifecycle/Deployment & Serving/Constrained Decoding|Constrained Decoding]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume III - Agentic Systems/00 Introduction/01 Introduction/V3-01 Introduction|V3-01 Introduction]] — Task contract; Fail-plausible fault; H·S·A exposures; Invariant closure; Closure evidence levels; Cost per accepted task; Lighthouse workloads.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/02_foundation_model/foundation_model_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume III - Agentic Systems/01 The Model/03 Test-Time Compute/V3-03 Test-Time Compute|V3-03 Test-Time Compute]] — Allocation axes; Verifier precision.
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04 Context Engineering|V3-04 Context Engineering]] — Working-set partition.
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05 KV Cache Management|V3-05 KV Cache Management]] — KV footprint and resident fit; Reusable is not applicable; Paused-state policy.
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07 Tool Calling|V3-07 Tool Calling]] — Complete mediation; Bounded observation.
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08 Agent Sandboxes|V3-08 Agent Sandboxes]] — Containment beneath the model.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10 The Agent Harness|V3-10 The Agent Harness]] — Harness owns continuation.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11 Durable Execution|V3-11 Durable Execution]] — Record and replay.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12 Failure Recovery|V3-12 Failure Recovery]] — Recovery decision order.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13 Agent Evaluation|V3-13 Agent Evaluation]] — Matched-budget evaluation; Grader calibration; Repeated-run consistency.
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/16 Trajectory Fine-Tuning/V3-16 Trajectory Fine-Tuning|V3-16 Trajectory Fine-Tuning]] — Loss masking.
- [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/19 Agent Economics/V3-19 Agent Economics|V3-19 Agent Economics]] — Speculative decoding profitability; Prefix-cache pricing and compaction payback.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/02_foundation_model/foundation_model_concepts.yml)

<!-- Semantic Navigation: End -->
