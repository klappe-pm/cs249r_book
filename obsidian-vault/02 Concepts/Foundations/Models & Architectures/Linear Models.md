---
title: Linear Models
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Model_Families
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Linear models
taxonomy_id: mlsys.linear-model
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Linear Models

Models whose score is linear in their supplied features, with a possible output link function.

## Browsing Home

[[02 Concepts/Foundations/Models & Architectures/Model Families Subject|Model Families]] → [[02 Concepts/Foundations/Models & Architectures/Models & Architectures Index|Models & Architectures]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Operates on [[02 Concepts/Lifecycle/Data Engineering/Feature Engineering|Feature Engineering]]. **Condition:** A linear score can use engineered or learned input features.

- Determines the contents of [[02 Concepts/Foundations/Models & Architectures/Model Artifact|Model Artifact]]. **Condition:** Feature transforms and output rules are part of the execution contract.

- Is an alternative to [[02 Concepts/Foundations/Models & Architectures/Tree Ensembles|Tree Ensembles]]. **Condition:** Both are standard choices for tabular supervised prediction; trees capture interactions linear scores need engineered features for.

- Represents interactions through [[02 Concepts/Lifecycle/Data Engineering/Feature Cross|Feature Cross]]. **Condition:** Interactions not otherwise expressible by an additive model.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: logistic regression; linear regression.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
