---
title: Encoder Only, Decoder Only, and Encoder Decoder Transformers
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Model_Families
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Encoder-only, decoder-only, and encoder-decoder Transformers
taxonomy_id: mlsys.transformer-variants
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Encoder Only, Decoder Only, and Encoder Decoder Transformers

The three arrangements of Transformer stacks, which differ in whether inputs are processed bidirectionally, outputs are generated autoregressively, or both, and therefore in how they are trained, cached, and served.

## Browsing Home

[[02 Concepts/Foundations/Models & Architectures/Model Families Subject|Model Families]] → [[02 Concepts/Foundations/Models & Architectures/Models & Architectures Index|Models & Architectures]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Are arrangements of [[02 Concepts/Foundations/Models & Architectures/Transformer|Transformer]]. **Condition:** Models are built from Transformer blocks.

- Decides whether serving has separate [[02 Concepts/Lifecycle/Deployment & Serving/Prefill and Decode|Prefill and Decode]]. **Condition:** The model generates output autoregressively.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: encoder-only model; decoder-only model; encoder-decoder model; seq2seq Transformer.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
