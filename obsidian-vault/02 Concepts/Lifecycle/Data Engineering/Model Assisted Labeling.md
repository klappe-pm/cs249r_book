---
title: Model Assisted Labeling
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Data_Collection_Labeling
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Model-assisted labeling
taxonomy_id: mlsys.model-assisted-labeling
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Model Assisted Labeling

Using a model's predictions as draft labels that annotators accept or correct, which raises labeling throughput but can anchor annotators to the model's errors.

## Browsing Home

[[02 Concepts/Lifecycle/Data Engineering/Data Collection & Labeling Subject|Data Collection & Labeling]] → [[02 Concepts/Lifecycle/Data Engineering/Data Engineering Index|Data Engineering]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Trades annotation throughput against the quality of [[02 Concepts/Lifecycle/Data Engineering/Label Quality|Label Quality]]. **Condition:** When annotators review model drafts rather than labeling from scratch, so anchoring can carry model errors into labels.

- Keeps a per-item human review step that is not part of [[02 Concepts/Lifecycle/Data Engineering/Weak Supervision|Weak Supervision]]. **Condition:** When the label budget allows human confirmation of each draft label.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: pre-labeling; model-in-the-loop annotation.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
