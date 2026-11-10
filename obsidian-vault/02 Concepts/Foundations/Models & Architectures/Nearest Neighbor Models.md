---
title: Nearest Neighbor Models
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Model_Families
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Nearest-neighbor models
taxonomy_id: mlsys.nearest-neighbor
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Nearest Neighbor Models

Predictions or retrieval based on similarity to stored examples or vectors.

## Browsing Home

[[02 Concepts/Foundations/Models & Architectures/Model Families Subject|Model Families]] → [[02 Concepts/Foundations/Models & Architectures/Models & Architectures Index|Models & Architectures]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Can use [[02 Concepts/Lifecycle/Deployment & Serving/Approximate Nearest Neighbor Search|Approximate Nearest Neighbor Search]]. **Condition:** Approximation trades exact recovery for search cost in compatible applications.

- Determines the contents of [[02 Concepts/Foundations/Models & Architectures/Model Artifact|Model Artifact]]. **Condition:** Stored vectors, metadata, and optional indexes contribute capacity and search cost.

- Searches over [[02 Concepts/Foundations/Models & Architectures/Embeddings|Embeddings]]. **Condition:** Neighbors are found by distance in a learned or engineered vector space whose quality determines result quality.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: k-nearest neighbors; kNN.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
