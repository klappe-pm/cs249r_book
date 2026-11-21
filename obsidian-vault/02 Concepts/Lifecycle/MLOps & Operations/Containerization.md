---
title: Containerization
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/ML_Pipelines_Reproducibility
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Containerization
taxonomy_id: mlsys.containerization
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Containerization

Packaging a model, its code, and its dependencies as an immutable image that runs unchanged across machines, leaving the scheduling of those containers across a cluster to the cluster manager.

## Browsing Home

[[02 Concepts/Lifecycle/MLOps & Operations/ML Pipelines & Reproducibility Subject|ML Pipelines & Reproducibility]] → [[02 Concepts/Lifecycle/MLOps & Operations/MLOps & Operations Index|MLOps & Operations]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Packages [[02 Concepts/Lifecycle/MLOps & Operations/Dependency Environment|Dependency Environment]]. **Condition:** The image pins packages, native libraries, and runtime configuration.

- Makes reruns practical for [[02 Concepts/Lifecycle/MLOps & Operations/Experiment Reproducibility|Experiment Reproducibility]]. **Condition:** Images are versioned and run unchanged across machines.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: containers; Docker.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
