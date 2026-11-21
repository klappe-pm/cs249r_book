---
title: Experiment Reproducibility
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/ML_Pipelines_Reproducibility
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Experiment reproducibility
taxonomy_id: mlsys.experiment-reproducibility
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Experiment Reproducibility

The ability to repeat an experimental procedure and obtain results consistent with declared criteria when its inputs, environment, randomness, and execution conditions are specified.

## Browsing Home

[[02 Concepts/Lifecycle/MLOps & Operations/ML Pipelines & Reproducibility Subject|ML Pipelines & Reproducibility]] → [[02 Concepts/Lifecycle/MLOps & Operations/MLOps & Operations Index|MLOps & Operations]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Requires a pinned [[02 Concepts/Lifecycle/MLOps & Operations/Dependency Environment|Dependency Environment]]. **Condition:** Package identity alone is insufficient: hardware, data, seeds, nondeterministic operations, external services, and acceptance criteria may also matter.

- Requires [[02 Concepts/Lifecycle/Data Engineering/Dataset Versioning|Dataset Versioning]]. **Condition:** Holds whenever training or evaluation data can change after a run.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
