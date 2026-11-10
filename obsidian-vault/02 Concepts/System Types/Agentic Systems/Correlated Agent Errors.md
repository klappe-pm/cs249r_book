---
title: Correlated Agent Errors
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Multi_Agent_Orchestration
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Correlated agent errors
taxonomy_id: mlsys.correlated-agent-errors
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Correlated Agent Errors

Errors shared across agents built on the same model or prompts, which make voting, debate, or cross-checking less independent than assumed.

## Browsing Home

[[02 Concepts/System Types/Agentic Systems/Multi Agent Orchestration Subject|Multi Agent Orchestration]] → [[02 Concepts/System Types/Agentic Systems/Agentic Systems Index|Agentic Systems]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Limits the benefit of [[02 Concepts/System Types/Agentic Systems/Multi Agent Orchestration|Multi Agent Orchestration]]. **Condition:** Holds when agents share a base model, prompts, or retrieved evidence.

- Limits the benefit of [[02 Concepts/Lifecycle/Deployment & Serving/Self Consistency Voting|Self Consistency Voting]]. **Condition:** When the sampled answers or voting agents share a base model and prompt, so their errors are not independent.

- Weakens the independence of [[02 Concepts/Lifecycle/Model Evaluation & Testing/Model Based Grading|Model Based Grading]]. **Condition:** When the judge shares a base model with the system it grades.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
