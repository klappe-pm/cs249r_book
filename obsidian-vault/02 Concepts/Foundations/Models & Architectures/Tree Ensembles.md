---
title: Tree Ensembles
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Model_Families
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Tree ensembles
taxonomy_id: mlsys.tree-ensemble
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Tree Ensembles

Collections of decision trees whose branch traversal and aggregation determine predictions.

## Browsing Home

[[02 Concepts/Foundations/Models & Architectures/Model Families Subject|Model Families]] → [[02 Concepts/Foundations/Models & Architectures/Models & Architectures Index|Models & Architectures]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Determines the contents of [[02 Concepts/Foundations/Models & Architectures/Model Artifact|Model Artifact]]. **Condition:** Tree structures, thresholds, leaf values, and aggregation rules require storage and compatible execution.

- Splits on [[02 Concepts/Lifecycle/Data Engineering/Feature Engineering|Feature Engineering]]. **Condition:** Trees operate on tabular features without requiring scaling; feature engineering still determines what interactions are available.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: gradient-boosted decision trees; GBDT; random forest; XGBoost.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
