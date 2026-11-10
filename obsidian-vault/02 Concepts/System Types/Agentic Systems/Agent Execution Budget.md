---
title: Agent Execution Budget
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Agent_Harness_Control_Loop
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Agent execution budget
taxonomy_id: mlsys.agent-budget
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Agent Execution Budget

Limits on turns, tokens, wall-clock time, or spend for a trajectory, with stopping rules applied when a limit or completion criterion is reached.

## Browsing Home

[[02 Concepts/System Types/Agentic Systems/Agent Harness & Control Loop Subject|Agent Harness & Control Loop]] → [[02 Concepts/System Types/Agentic Systems/Agentic Systems Index|Agentic Systems]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10.10 Budgets and Ceilings#^sec-vol3-harness-multidim-budgets|V3-10.10 Budgets and Ceilings]] — Trajectory budget. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/10_agent_harness/10_agent_harness.qmd#L798).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Caps per-trajectory [[02 Concepts/Qualities/Sustainability & Cost/Cost per Useful Outcome|Cost per Useful Outcome]]. **Condition:** Budgets cap spend per trajectory; cost per accepted task also depends on success rate.

- Bounds the search depth of [[02 Concepts/System Types/Agentic Systems/Agent Planning|Agent Planning]]. **Condition:** When turn, token, or time limits cap how many alternatives a plan can explore.

- Bounds the length of [[02 Concepts/System Types/Agentic Systems/Agent Trajectory|Agent Trajectory]]. **Condition:** When limits on turns, tokens, or wall-clock time stop the run before completion.

- Bounds the runs of [[02 Concepts/System Types/Agentic Systems/Model Directed Control Flow|Model Directed Control Flow]]. **Condition:** When the harness enforces step, token, or cost limits on model-chosen actions.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
