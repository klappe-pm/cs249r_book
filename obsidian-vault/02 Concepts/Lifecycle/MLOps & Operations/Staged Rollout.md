---
title: Staged Rollout
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Versioning_Rollout_Rollback
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Staged rollout
taxonomy_id: mlsys.rollout
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Staged Rollout

Increasing exposure to a candidate system through bounded release stages.

## Browsing Home

[[02 Concepts/Lifecycle/MLOps & Operations/Versioning, Rollout & Rollback Subject|Versioning, Rollout & Rollback]] → [[02 Concepts/Lifecycle/MLOps & Operations/MLOps & Operations Index|MLOps & Operations]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume II - Scaling/03 The Fleet in Production/12 ML Operations at Scale/V2-12.06 CI CD for ML at Scale#^sec-ml-operations-scale-staged-rollout-strategies-2d1f|V2-12.06 CI CD for ML at Scale]] — Staged rollout. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/12_ops_scale/12_ops_scale.qmd#L2013).

- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/14 Operating Agents/V3-14.06 Staged Releases#^sec-vol3-evaluation-releases|V3-14.06 Staged Releases]] — Staged release. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/14_agent_operations/14_agent_operations.qmd#L562).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Requires pinned [[02 Concepts/Lifecycle/MLOps & Operations/Artifact Versioning|Artifact Versioning]]. **Condition:** Evidence and compatibility must refer to the exact candidate being deployed.

- Can use [[02 Concepts/Lifecycle/MLOps & Operations/Rollback|Rollback]]. **Condition:** A rollout can use rollback when acceptance criteria fail; state compatibility and external effects may limit recovery.

- Reduces [[02 Concepts/Qualities/Reliability & Fault Tolerance/Blast Radius|Blast Radius]]. **Condition:** When each stage exposes a small fraction of traffic and gates promotion on health signals.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: canary release; canary deployment; progressive delivery.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
