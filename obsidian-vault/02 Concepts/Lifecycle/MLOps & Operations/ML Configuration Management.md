---
title: ML Configuration Management
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/ML_Pipelines_Reproducibility
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: ML configuration management
taxonomy_id: mlsys.configuration-management
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# ML Configuration Management

Treating model, feature, and pipeline configuration as versioned, reviewed, and tested code.

## Browsing Home

[[02 Concepts/Lifecycle/MLOps & Operations/ML Pipelines & Reproducibility Subject|ML Pipelines & Reproducibility]] → [[02 Concepts/Lifecycle/MLOps & Operations/MLOps & Operations Index|MLOps & Operations]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Reduces configuration [[02 Concepts/Lifecycle/MLOps & Operations/ML Technical Debt|ML Technical Debt]]. **Condition:** Holds when configuration is reviewed, tested, and versioned like code.

- Pins the settings required for [[02 Concepts/Lifecycle/MLOps & Operations/Experiment Reproducibility|Experiment Reproducibility]]. **Condition:** Holds when every run records the exact reviewed configuration version it executed.

- Makes configuration changes revertible through [[02 Concepts/Lifecycle/MLOps & Operations/Rollback|Rollback]]. **Condition:** Applies when configuration is versioned and deployed through the same pipeline as code.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
