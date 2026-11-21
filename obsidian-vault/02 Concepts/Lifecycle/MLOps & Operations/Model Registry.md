---
title: Model Registry
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Versioning_Rollout_Rollback
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Model registry
taxonomy_id: mlsys.model-registry
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Model Registry

A versioned store of model artifacts with metadata, lineage, and lifecycle stage used to govern promotion and deployment.

## Browsing Home

[[02 Concepts/Lifecycle/MLOps & Operations/Versioning, Rollout & Rollback Subject|Versioning, Rollout & Rollback]] → [[02 Concepts/Lifecycle/MLOps & Operations/MLOps & Operations Index|MLOps & Operations]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume II - Scaling/03 The Fleet in Production/12 ML Operations at Scale/V2-12.04 Governance of State and Change#^sec-ml-operations-scale-model-registries-scale-ccba|V2-12.04 Governance of State and Change]] — Dependency registry. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/12_ops_scale/12_ops_scale.qmd#L928).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Stores and governs [[02 Concepts/Lifecycle/MLOps & Operations/Artifact Versioning|Artifact Versioning]]. **Condition:** Holds when every deployable model is registered with its lineage and stage.

- Is a shared component of [[02 Concepts/Lifecycle/MLOps & Operations/ML Platform|ML Platform]]. **Condition:** Typical when promotion and deployment are standardized across teams.

- Keeps prior versions available for [[02 Concepts/Lifecycle/MLOps & Operations/Rollback|Rollback]]. **Condition:** Holds when prior versions and their serving configuration remain registered and deployable.

- Uses [[02 Concepts/Qualities/Security & Privacy/Model Artifact Signing|Model Artifact Signing]]. **Condition:** When the registry signs artifacts on promotion and verifies them before deployment.

- Stores and versions [[02 Concepts/Qualities/Responsible AI/Model Card|Model Card]]. **Condition:** When documentation is required for promotion alongside the model artifact.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
