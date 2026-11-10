---
title: Artifact Versioning
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Versioning_Rollout_Rollback
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Artifact versioning
taxonomy_id: mlsys.artifact-version
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Artifact Versioning

Identifying the exact model, code, data, configuration, and dependencies in an execution or release.

## Browsing Home

[[02 Concepts/Lifecycle/MLOps & Operations/Versioning, Rollout & Rollback Subject|Versioning, Rollout & Rollback]] → [[02 Concepts/Lifecycle/MLOps & Operations/MLOps & Operations Index|MLOps & Operations]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume II - Scaling/01 The Fleet/04 Data Storage/V2-04.08 Versioned Data and Commit Boundaries#^sec-storage-data-versioning-orchestration|V2-04.08 Versioned Data and Commit Boundaries]] — Versioned artifact. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/04_data_storage/04_data_storage.qmd#L3866).

- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/16 Deployment Release/V4-16.09 The Release Manifest#^sec-release-manifest|V4-16.09 The Release Manifest]] — Release manifest. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/16_release/16_release.qmd#L1529).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Records the dependencies behind [[02 Concepts/Lifecycle/Data Engineering/Data Lineage|Data Lineage]]. **Condition:** Provenance must identify versions and transformations sufficient for reconstruction.

- Identifies the exact inputs for [[02 Concepts/Lifecycle/MLOps & Operations/Experiment Reproducibility|Experiment Reproducibility]]. **Condition:** Reproduction requires resolvable versions and the execution procedure/environment; version labels alone do not reproduce results.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: prompt versioning; prompt as artifact; system-prompt version.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
