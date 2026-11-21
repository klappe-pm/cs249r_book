---
title: Trajectory Evaluation
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Evaluating_Generative_Agentic_Systems
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Trajectory evaluation
taxonomy_id: mlsys.agent-evaluation
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Trajectory Evaluation

Assessing task outcomes, intermediate effects, and constraint compliance across a complete agent run.

## Browsing Home

[[02 Concepts/Lifecycle/Model Evaluation & Testing/Evaluating Generative & Agentic Systems Subject|Evaluating Generative & Agentic Systems]] → [[02 Concepts/Lifecycle/Model Evaluation & Testing/Model Evaluation & Testing Index|Model Evaluation & Testing]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13.03 The Task Acceptance Contract#^sec-vol3-evaluation-contract|V3-13.03 The Task Acceptance Contract]] — Task acceptance. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/13_evaluation/13_evaluation.qmd#L218).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Measures accepted outcomes of [[02 Concepts/System Types/Agentic Systems/Agent Trajectory|Agent Trajectory]]. **Condition:** Evaluate external effects and constraint compliance, not only final text.

- Can grade trajectories with [[02 Concepts/Lifecycle/Model Evaluation & Testing/Model Based Grading|Model Based Grading]]. **Condition:** Applies where task success lacks a programmatic check.

- Measures plan quality through [[02 Concepts/System Types/Agentic Systems/Agent Planning|Agent Planning]]. **Condition:** When intermediate steps, not only final outcomes, are scored across the trajectory.

- Measures [[02 Concepts/System Types/Agentic Systems/Computer Use|Computer Use]]. **Condition:** When tasks run in real applications and success is checked from the resulting system state.

- Scores intermediate effects and constraint compliance from the [[02 Concepts/System Types/Agentic Systems/Trajectory Log|Trajectory Log]]. **Condition:** When evaluation reads the record of what was dispatched rather than only the final answer.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
