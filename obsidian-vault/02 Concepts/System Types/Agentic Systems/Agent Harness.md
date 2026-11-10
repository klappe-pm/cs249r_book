---
title: Agent Harness
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Agent_Harness_Control_Loop
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Agent harness
taxonomy_id: mlsys.agent-harness
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Agent Harness

The runtime that repeatedly calls a model, dispatches its tool actions, appends observations, and decides whether the trajectory continues, pauses, or ends.

## Browsing Home

[[02 Concepts/System Types/Agentic Systems/Agent Harness & Control Loop Subject|Agent Harness & Control Loop]] → [[02 Concepts/System Types/Agentic Systems/Agentic Systems Index|Agentic Systems]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10.05 Trajectory States#^sec-vol3-agent-harness-transition-guards|V3-10.05 Trajectory States]] — Transition guard. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/10_agent_harness/10_agent_harness.qmd#L241).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Produces and records [[02 Concepts/System Types/Agentic Systems/Agent Trajectory|Agent Trajectory]]. **Condition:** The harness, not the model, owns continuation and the authoritative trajectory record.

- Dispatches tool actions through [[02 Concepts/System Types/Agentic Systems/Function Calling|Function Calling]]. **Condition:** When the model emits structured calls that the harness validates and executes.

- Enforces stopping rules from [[02 Concepts/System Types/Agentic Systems/Agent Execution Budget|Agent Execution Budget]]. **Condition:** The harness, not the model, applies turn, token, time, and spend limits.

- Writes, as the sole author, the [[02 Concepts/System Types/Agentic Systems/Trajectory Log|Trajectory Log]]. **Condition:** When the harness, not the model, owns continuation and records each step before dispatching it.

- Retries tool steps safely through [[02 Concepts/Qualities/Reliability & Fault Tolerance/Idempotency|Idempotency]]. **Condition:** When a step is re-issued after a timeout or crash and the tool contract declares an idempotency key or deduplication.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: agent loop; agent runtime.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
