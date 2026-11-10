---
title: Deep Recommendation Model
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Model_Families
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Deep recommendation model
taxonomy_id: mlsys.recommendation-model
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Deep Recommendation Model

Models combining large sparse embedding tables for categorical features with dense layers, whose cost is often dominated by embedding lookups and memory capacity.

## Browsing Home

[[02 Concepts/Foundations/Models & Architectures/Model Families Subject|Model Families]] → [[02 Concepts/Foundations/Models & Architectures/Models & Architectures Index|Models & Architectures]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is dominated by lookups in [[02 Concepts/Foundations/Models & Architectures/Embeddings|Embeddings]]. **Condition:** Categorical features are encoded through large embedding tables.

- Serves hot rows from an [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Embedding Cache and Tiering|Embedding Cache and Tiering]]. **Condition:** Lookups are skewed so a small set of rows receives most accesses.

- Commonly trains sparse tables through a [[02 Concepts/Stack/Parallelism & Distributed Execution/Parameter Server|Parameter Server]]. **Condition:** Updates touch only the rows looked up in each batch.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: DLRM.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
