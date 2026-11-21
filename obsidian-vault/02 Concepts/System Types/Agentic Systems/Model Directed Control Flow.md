---
title: Model Directed Control Flow
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Agent_Harness_Control_Loop
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Model-directed control flow
taxonomy_id: mlsys.model-directed-control-flow
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Model Directed Control Flow

A control structure in which model outputs select the next step, tool call, or stopping decision within runtime-enforced limits, increasing flexibility while making cost and behavior harder to predict and test.

## Browsing Home

[[02 Concepts/System Types/Agentic Systems/Agent Harness & Control Loop Subject|Agent Harness & Control Loop]] → [[02 Concepts/System Types/Agentic Systems/Agentic Systems Index|Agentic Systems]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Replaces code-defined step selection in [[02 Concepts/Lifecycle/MLOps & Operations/Workflow Orchestration|Workflow Orchestration]]. **Condition:** When the steps cannot be enumerated in advance.

- Is the decision loop inside [[02 Concepts/System Types/Agentic Systems/Agent Harness|Agent Harness]]. **Condition:** When the harness lets model outputs choose the next action.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: agent autonomy level; ReAct loop; reason-act loop.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
