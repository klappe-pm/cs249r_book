---
title: Release Gate
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Versioning_Rollout_Rollback
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Release gate
taxonomy_id: mlsys.release-gate
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Release Gate

A predeclared set of checks a candidate model must pass before it advances to a wider deployment stage.

## Browsing Home

[[02 Concepts/Lifecycle/MLOps & Operations/Versioning, Rollout & Rollback Subject|Versioning, Rollout & Rollback]] → [[02 Concepts/Lifecycle/MLOps & Operations/MLOps & Operations Index|MLOps & Operations]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/01 Foundations/03 ML Lifecycle/V1-03.09 Stage 4 Evaluation and Validation#^sec-ml-workflow-validation-deployment-readiness-207c|V1-03.09 Stage 4 Evaluation and Validation]] — Release decision. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/03_ml_lifecycle/03_ml_lifecycle.qmd#L1483).

- [[01 Books/Volume II - Scaling/03 The Fleet in Production/12 ML Operations at Scale/V2-12.06 CI CD for ML at Scale#^sec-ops-scale-end-to-end-evaluation-contract|V2-12.06 CI CD for ML at Scale]] — Evaluation contract. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/12_ops_scale/12_ops_scale.qmd#L2336).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Controls advancement of [[02 Concepts/Lifecycle/MLOps & Operations/Staged Rollout|Staged Rollout]]. **Condition:** Holds when each rollout stage has predeclared pass criteria.

- Compares candidates against [[02 Concepts/Foundations/Workloads & Requirements/Baseline|Baseline]]. **Condition:** A candidate advances only if it beats or matches the incumbent baseline on the gated metrics under the same protocol.

- Can block on failures of [[02 Concepts/Lifecycle/Model Evaluation & Testing/Behavioral Testing|Behavioral Testing]]. **Condition:** Applies when capability tests are part of the predeclared checks.

- Can block on thresholds crossed in [[02 Concepts/Lifecycle/Model Evaluation & Testing/Dangerous Capability Evaluation|Dangerous Capability Evaluation]]. **Condition:** Applies to frontier-model releases governed by a scaling policy.

- Decides promotion with [[02 Concepts/Lifecycle/Model Evaluation & Testing/Paired Comparison and Noninferiority Testing|Paired Comparison and Noninferiority Testing]]. **Condition:** Candidate and incumbent are evaluated on the same set.

- Checks the candidate's tokenizer, schema, and operator set against the serving stack, revealing broken [[02 Concepts/Lifecycle/MLOps & Operations/Model and Feature Compatibility|Model and Feature Compatibility]]. **Condition:** The gate runs against the same runtime image that will serve the model.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: validation gate.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
