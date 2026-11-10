---
title: Shared Agent State
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Multi_Agent_Orchestration
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Shared agent state
taxonomy_id: mlsys.shared-agent-state
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Shared Agent State

Task state read and written by several agents, requiring concurrency control such as leases or optimistic versioning to avoid lost or conflicting updates.

## Browsing Home

[[02 Concepts/System Types/Agentic Systems/Multi Agent Orchestration Subject|Multi Agent Orchestration]] → [[02 Concepts/System Types/Agentic Systems/Agentic Systems Index|Agentic Systems]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Uses [[02 Concepts/Stack/Parallelism & Distributed Execution/Fencing|Fencing]]. **Condition:** Holds when leases can expire while a slow agent still attempts writes.

- Is part of [[02 Concepts/System Types/Agentic Systems/Multi Agent Orchestration|Multi Agent Orchestration]]. **Condition:** When several agents read and write task state under one orchestration topology.

- Can cause [[02 Concepts/System Types/Agentic Systems/Multi Agent Coordination Failure|Multi Agent Coordination Failure]]. **Condition:** When concurrent writes or stale reads go uncontrolled, so agents act on conflicting views of the task.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
