---
title: Durable Execution
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Durable_Execution_Agent_State
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Durable execution
taxonomy_id: mlsys.durable-execution
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Durable Execution

Execution that persists workflow progress and reuses recorded results on recovery, with external-effect guarantees determined by endpoint idempotency, transactional boundaries, and reconciliation.

## Browsing Home

[[02 Concepts/System Types/Agentic Systems/Durable Execution & Agent State Subject|Durable Execution & Agent State]] → [[02 Concepts/System Types/Agentic Systems/Agentic Systems Index|Agentic Systems]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11.03 The Trajectory Log#^sec-vol3-persistence-event-sourcing|V3-11.03 The Trajectory Log]] — Trajectory log. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/11_durable_execution/11_durable_execution.qmd#L85).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Relies on [[02 Concepts/Qualities/Reliability & Fault Tolerance/Idempotency|Idempotency]]. **Condition:** Resuming after a crash between dispatch and record can re-issue a step, which is safe only for idempotent or deduplicated effects.

- Is a kind of [[02 Concepts/Lifecycle/MLOps & Operations/Workflow Orchestration|Workflow Orchestration]]. **Condition:** When each step's intent and result are logged so recovery reuses recorded results; an effect completed before its result was recorded may need retry, deduplication, or reconciliation.

- Recovers progress and reuses recorded results from the [[02 Concepts/System Types/Agentic Systems/Trajectory Log|Trajectory Log]]. **Condition:** When each step's intent is appended before the effect is issued, so a crash between the two can be reconciled.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
