---
title: Closed Loop Policy Evaluation
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Evaluation_Design_Experiments
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Closed-loop policy evaluation
taxonomy_id: mlsys.closed-loop-evaluation
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Closed Loop Policy Evaluation

Evaluating a policy by letting its own actions determine subsequent observations, in simulation or deployment, rather than scoring its predictions against logged data.

## Browsing Home

[[02 Concepts/Lifecycle/Model Evaluation & Testing/Evaluation Design & Experiments Subject|Evaluation Design & Experiments]] → [[02 Concepts/Lifecycle/Model Evaluation & Testing/Model Evaluation & Testing Index|Model Evaluation & Testing]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/16 Trajectory Fine-Tuning/V3-16.12 Evaluating a Fine-Tuned Agent#^sec-vol3-fine-tuning-eval-decoupling|V3-16.12 Evaluating a Fine-Tuned Agent]] — Closed-loop evaluation. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/16_fine_tuning/16_fine_tuning.qmd#L1253).

- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07.03 What a Physical Success Rate Measures#^sec-evaluation-what-measured|V4-07.03 What a Physical Success Rate Measures]] — Closed-loop trial. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/07_evaluation/07_evaluation.qmd#L162).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Reveals [[02 Concepts/Lifecycle/Training & Adaptation/Compounding Error in Sequential Decisions|Compounding Error in Sequential Decisions]]. **Condition:** Errors alter later observations, unlike open-loop replay.

- Scores, by physical trial success rate, [[02 Concepts/System Types/Embodied & Physical Systems/Simulation to Real Transfer|Simulation to Real Transfer]]. **Condition:** When comparable closed-loop simulation and physical trials give an explicit transfer comparison under matched task and measurement conditions.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: closed-loop testing; interactive policy evaluation.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
