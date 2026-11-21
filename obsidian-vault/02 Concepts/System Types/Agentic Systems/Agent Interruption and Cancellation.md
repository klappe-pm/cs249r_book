---
title: Agent Interruption and Cancellation
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Agent_Harness_Control_Loop
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Agent interruption and cancellation
taxonomy_id: mlsys.agent-interruption
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Agent Interruption and Cancellation

Operator controls that pause, redirect, cancel, or terminate a running agent at defined boundaries while settling in-flight tool calls into a known state.

## Browsing Home

[[02 Concepts/System Types/Agentic Systems/Agent Harness & Control Loop Subject|Agent Harness & Control Loop]] → [[02 Concepts/System Types/Agentic Systems/Agentic Systems Index|Agentic Systems]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is an intervention mechanism within [[02 Concepts/Qualities/Responsible AI/Human Oversight|Human Oversight]]. **Condition:** Operators can act during execution.

- Undoes partial work with [[02 Concepts/Qualities/Reliability & Fault Tolerance/Compensating Action|Compensating Action]]. **Condition:** Cancelled work already produced side effects.

- Takes effect only at turn boundaries enforced by the [[02 Concepts/System Types/Agentic Systems/Agent Harness|Agent Harness]]. **Condition:** When a runtime owns continuation and dispatch, enforces cancellation at defined execution boundaries, and separately settles already issued external actions.

- Leaves, when it cancels mid-dispatch, an [[02 Concepts/Qualities/Reliability & Fault Tolerance/In Doubt Action|In Doubt Action]]. **Condition:** When a tool call was sent before the cancel and its result never arrived.

- Lets an operator override the next step chosen by [[02 Concepts/System Types/Agentic Systems/Model Directed Control Flow|Model Directed Control Flow]]. **Condition:** Interruption boundaries must sit at tool-call granularity so a pending action is not half-applied.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: pause and cancel; operator interrupt; agent kill switch.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
