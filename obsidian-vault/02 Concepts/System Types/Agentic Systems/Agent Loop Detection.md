---
title: Agent Loop Detection
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Agent_Harness_Control_Loop
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Agent loop detection
taxonomy_id: mlsys.agent-loop-detection
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Agent Loop Detection

Monitoring an agent trajectory for repeated actions, cycling states, or absent progress, and halting or escalating when the agent appears stuck.

## Browsing Home

[[02 Concepts/System Types/Agentic Systems/Agent Harness & Control Loop Subject|Agent Harness & Control Loop]] → [[02 Concepts/System Types/Agentic Systems/Agentic Systems Index|Agentic Systems]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12.07 Semantic Watchdogs#^sec-vol3-sagas-watchdogs|V3-12.07 Semantic Watchdogs]] — Semantic watchdog. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/12_failure_recovery/12_failure_recovery.qmd#L628).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is a progress monitor within [[02 Concepts/System Types/Agentic Systems/Agent Harness|Agent Harness]]. **Condition:** The harness can inspect the trajectory between steps.

- Flags looping instances of [[02 Concepts/System Types/Agentic Systems/Multi Agent Coordination Failure|Multi Agent Coordination Failure]]. **Condition:** Agents repeat steps or hand work back and forth.

- Stops stuck runs earlier than [[02 Concepts/System Types/Agentic Systems/Agent Execution Budget|Agent Execution Budget]]. **Condition:** Progress can be judged before a budget is exhausted.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: semantic watchdog; livelock detection; repetition detection.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
