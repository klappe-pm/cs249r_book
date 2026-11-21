---
title: Drift Detection
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Monitoring_Observability
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Drift detection
taxonomy_id: mlsys.drift-detection
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Drift Detection

Statistical tests or distances comparing production and reference distributions of inputs, predictions, or outcomes to flag change.

## Browsing Home

[[02 Concepts/Lifecycle/MLOps & Operations/Monitoring & Observability Subject|Monitoring & Observability]] → [[02 Concepts/Lifecycle/MLOps & Operations/MLOps & Operations Index|MLOps & Operations]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/04 Deployment/14 ML Operations/V1-14.06 Production Monitoring#^sec-ml-operations-model-infrastructure-monitoring-3988|V1-14.06 Production Monitoring]] — Distribution shift. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/14_ml_ops/14_ml_ops.qmd#L1793).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Detects [[02 Concepts/Lifecycle/MLOps & Operations/Distribution Shift|Distribution Shift]]. **Condition:** Holds for shifts visible in monitored statistics; detected drift need not degrade quality, and some harmful shifts are not detected.

- Is part of [[02 Concepts/Lifecycle/MLOps & Operations/Production Monitoring|Production Monitoring]]. **Condition:** Applies when distribution checks run alongside service and quality signals in production.

- Compares distributions from [[02 Concepts/Lifecycle/MLOps & Operations/Prediction Logging|Prediction Logging]]. **Condition:** Holds because production distributions are reconstructed from logged inputs and predictions.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
