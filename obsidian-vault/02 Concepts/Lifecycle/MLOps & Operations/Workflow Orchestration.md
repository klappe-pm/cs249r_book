---
title: Workflow Orchestration
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/ML_Pipelines_Reproducibility
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Workflow orchestration
taxonomy_id: mlsys.workflow-orchestration
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Workflow Orchestration

Coordinating dependent computation steps, their data or control flow, execution conditions, and failure handling.

## Browsing Home

[[02 Concepts/Lifecycle/MLOps & Operations/ML Pipelines & Reproducibility Subject|ML Pipelines & Reproducibility]] → [[02 Concepts/Lifecycle/MLOps & Operations/MLOps & Operations Index|MLOps & Operations]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Can record execution evidence as [[02 Concepts/Lifecycle/Data Engineering/Data Lineage|Data Lineage]]. **Condition:** Only when actual input/output artifacts, parameters, steps, and execution identities are captured; orchestration alone does not establish complete provenance.

- Requires retry-safe steps through [[02 Concepts/Qualities/Reliability & Fault Tolerance/Idempotency|Idempotency]]. **Condition:** When steps can be retried after ambiguous completion, repeated external effects need explicit handling; idempotency is one option rather than a universal orchestration guarantee.

- Runs the pipelines of [[02 Concepts/Lifecycle/MLOps & Operations/Continuous Training|Continuous Training]]. **Condition:** Holds when retraining, validation, and registration steps run as an orchestrated pipeline.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
