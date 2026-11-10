---
title: Causal Language Modeling
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Learning_Paradigms
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Causal language modeling
taxonomy_id: mlsys.causal-lm
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Causal Language Modeling

Training a model to predict each token from the tokens before it, maximizing the likelihood of text under a left-to-right factorization.

## Browsing Home

[[02 Concepts/Lifecycle/Training & Adaptation/Learning Paradigms Subject|Learning Paradigms]] → [[02 Concepts/Lifecycle/Training & Adaptation/Training & Adaptation Index|Training & Adaptation]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is a text case of [[02 Concepts/Lifecycle/Training & Adaptation/Self Supervised Learning|Self Supervised Learning]]. **Condition:** Targets are the next tokens of the input itself.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: next-token prediction; autoregressive language modeling.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
