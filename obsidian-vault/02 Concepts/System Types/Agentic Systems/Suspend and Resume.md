---
title: Suspend and Resume
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Durable_Execution_Agent_State
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Suspend and resume
taxonomy_id: mlsys.suspend-resume
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Suspend and Resume

Persisting a trajectory while it waits on a human, timer, or external event, then resuming with a validated state and authority.

## Browsing Home

[[02 Concepts/System Types/Agentic Systems/Durable Execution & Agent State Subject|Durable Execution & Agent State]] → [[02 Concepts/System Types/Agentic Systems/Agentic Systems Index|Agentic Systems]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Enables long waits for [[02 Concepts/System Types/Agentic Systems/Action Approval Gate|Action Approval Gate]]. **Condition:** Resumption must revalidate state and authority that may have changed during the wait.

- Requires [[02 Concepts/Stack/Parallelism & Distributed Execution/Fencing|Fencing]]. **Condition:** Holds when a resumed worker could race a stale one that still believes it owns the trajectory.

- Persists waiting state through [[02 Concepts/System Types/Agentic Systems/Durable Execution|Durable Execution]]. **Condition:** When a trajectory must survive process restarts while waiting on a human or external event.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
