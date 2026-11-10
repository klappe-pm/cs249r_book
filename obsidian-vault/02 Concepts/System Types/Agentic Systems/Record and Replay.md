---
title: Record and Replay
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Durable_Execution_Agent_State
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Record and replay
taxonomy_id: mlsys.deterministic-replay
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Record and Replay

Re-executing a trajectory from its log by substituting recorded model outputs and tool results, to reproduce, debug, or test a divergence.

## Browsing Home

[[02 Concepts/System Types/Agentic Systems/Durable Execution & Agent State Subject|Durable Execution & Agent State]] → [[02 Concepts/System Types/Agentic Systems/Agentic Systems Index|Agentic Systems]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Reuses the log of [[02 Concepts/System Types/Agentic Systems/Durable Execution|Durable Execution]]. **Condition:** Replay is exact only if every nondeterministic input, including model samples and tool results, was recorded.

- Makes repeatable [[02 Concepts/Lifecycle/Model Evaluation & Testing/Trajectory Evaluation|Trajectory Evaluation]]. **Condition:** Holds when tool responses and model outputs are recorded so a run can be re-executed exactly.

- Can take recorded model outputs and tool results from [[02 Concepts/Lifecycle/MLOps & Operations/Model and Agent Call Tracing|Model and Agent Call Tracing]]. **Condition:** When traces retain full payloads rather than sampled or truncated spans; otherwise replay needs the trajectory log.

- Enables [[02 Concepts/Lifecycle/MLOps & Operations/ML Failure Attribution|ML Failure Attribution]]. **Condition:** When a failing trajectory can be re-run step by step with its original inputs.

- Substitutes recorded model outputs and tool results from the [[02 Concepts/System Types/Agentic Systems/Trajectory Log|Trajectory Log]]. **Condition:** When the log contains every input needed for the declared replay boundary.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: deterministic replay.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
