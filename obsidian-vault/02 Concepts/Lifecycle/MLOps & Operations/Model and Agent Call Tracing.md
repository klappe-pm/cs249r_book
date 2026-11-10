---
title: Model and Agent Call Tracing
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Monitoring_Observability
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Model and agent call tracing
taxonomy_id: mlsys.llm-call-tracing
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Model and Agent Call Tracing

Tracing model calls, retrievals, and tool invocations as spans annotated with prompts, token counts, latency, and cost, so quality and spend are attributable per step.

## Browsing Home

[[02 Concepts/Lifecycle/MLOps & Operations/Monitoring & Observability Subject|Monitoring & Observability]] → [[02 Concepts/Lifecycle/MLOps & Operations/MLOps & Operations Index|MLOps & Operations]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/14 Operating Agents/V3-14.03 Distributed Trajectory Tracing#^sec-vol3-evaluation-tracing-fields|V3-14.03 Distributed Trajectory Tracing]] — Trajectory trace. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/14_agent_operations/14_agent_operations.qmd#L106).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Specializes [[02 Concepts/Lifecycle/MLOps & Operations/Distributed Tracing|Distributed Tracing]]. **Condition:** Adds model-specific span attributes such as token counts, model version, and cost under a shared semantic convention.

- Instruments [[02 Concepts/System Types/Agentic Systems/Agent Harness|Agent Harness]]. **Condition:** Each loop iteration, model call, and tool call is emitted as a child span of the task's root span.

- Attributes token spend per step for [[02 Concepts/Qualities/Sustainability & Cost/Cost Attribution|Cost Attribution]]. **Condition:** Holds when spans record token counts and model identity per call.

- Detects [[02 Concepts/System Types/Agentic Systems/Multi Agent Coordination Failure|Multi Agent Coordination Failure]]. **Condition:** When handoffs, delegated instructions, and per-agent outputs are recorded as linked spans.

- Attributes a refusal to the input filter, the model, or the output filter, localizing [[02 Concepts/Qualities/Safety & Assurance/Over Refusal|Over Refusal]]. **Condition:** Filter decisions are recorded as spans alongside the model call, and the refused requests are labeled benign by an independent rubric.

- Records the passages and index timestamps needed to judge [[02 Concepts/System Types/Agentic Systems/Context Staleness|Context Staleness]]. **Condition:** When recorded index timestamps are compared with source versions or validity intervals; recency alone does not establish freshness.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: LLM observability; GenAI tracing.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
