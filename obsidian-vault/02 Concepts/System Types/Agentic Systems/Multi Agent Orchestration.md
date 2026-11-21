---
title: Multi Agent Orchestration
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Multi_Agent_Orchestration
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Multi-agent orchestration
taxonomy_id: mlsys.multi-agent-orchestration
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Multi Agent Orchestration

Structuring a task as delegated subtasks among agents under a topology, such as orchestrator-worker or peer, with typed handoffs and result merging.

## Browsing Home

[[02 Concepts/System Types/Agentic Systems/Multi Agent Orchestration Subject|Multi Agent Orchestration]] → [[02 Concepts/System Types/Agentic Systems/Agentic Systems Index|Agentic Systems]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/18 Multi-Agent Coordination/V3-18.05 Typed Task Envelopes#^sec-vol3-multiagent-contracts|V3-18.05 Typed Task Envelopes]] — Task delegation. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/18_multi_agent/18_multi_agent.qmd#L452).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Can introduce [[02 Concepts/System Types/Agentic Systems/Multi Agent Coordination Failure|Multi Agent Coordination Failure]]. **Condition:** Each delegation and handoff adds a point where specification or context can be lost.

- Is justified by comparison against a single-agent [[02 Concepts/Foundations/Workloads & Requirements/Baseline|Baseline]]. **Condition:** When the orchestration's added cost is evaluated against a single agent at matched total compute or token budget.

- Attenuates delegated rights to each worker through [[02 Concepts/Qualities/Security & Privacy/Capability Based Authorization|Capability Based Authorization]]. **Condition:** When a worker agent must receive narrower authority than its orchestrator.

- Multiplies, by duplicating context across workers, [[02 Concepts/System Types/Agentic Systems/Agentic Workload|Agentic Workload]]. **Condition:** When each delegated agent carries its own context and makes its own dependent model calls, so total tokens exceed a single-agent run on the same task.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: orchestrator-worker; delegation.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
