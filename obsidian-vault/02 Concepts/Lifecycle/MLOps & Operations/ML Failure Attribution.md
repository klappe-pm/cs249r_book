---
title: ML Failure Attribution
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Incident_Response
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: ML failure attribution
taxonomy_id: mlsys.failure-attribution
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# ML Failure Attribution

Determining whether a production failure stems from data, model, code, configuration, or infrastructure, or from an adversary.

## Browsing Home

[[02 Concepts/Lifecycle/MLOps & Operations/Incident Response Subject|Incident Response]] → [[02 Concepts/Lifecycle/MLOps & Operations/MLOps & Operations Index|MLOps & Operations]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/14 Operating Agents/V3-14.05 Incident Postmortems#^sec-vol3-postmortem-ablation|V3-14.05 Incident Postmortems]] — Causal diagnosis. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/14_agent_operations/14_agent_operations.qmd#L467).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Depends on [[02 Concepts/Lifecycle/MLOps & Operations/System Observability|System Observability]]. **Condition:** Distinguishing data, model, and infrastructure causes requires versioned, correlated signals from each layer.

- Traces data and artifact versions through [[02 Concepts/Lifecycle/Data Engineering/Data Lineage|Data Lineage]]. **Condition:** Holds when the failing prediction can be tied to the data and artifact versions that produced it.

- Reconstructs the failing request from [[02 Concepts/Lifecycle/MLOps & Operations/Prediction Logging|Prediction Logging]]. **Condition:** When logs retain inputs, model version, and outputs for the incident window.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
