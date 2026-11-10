---
title: Context Length Extension
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Long_Context_Efficient_Sequence_Models
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Context-length extension
taxonomy_id: mlsys.context-extension
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Context Length Extension

Techniques that extend a trained model's usable sequence length, such as position-encoding interpolation followed by long-sequence fine-tuning.

## Browsing Home

[[02 Concepts/Foundations/Models & Architectures/Long Context & Efficient Sequence Models Subject|Long Context & Efficient Sequence Models]] → [[02 Concepts/Foundations/Models & Architectures/Models & Architectures Index|Models & Architectures]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Rescales or interpolates [[02 Concepts/Foundations/Models & Architectures/Position Encoding|Position Encoding]]. **Condition:** The model uses a position encoding, such as rotary embeddings, that can be rescaled or interpolated.

- Extends the usable length of [[02 Concepts/Foundations/Models & Architectures/Context Window|Context Window]]. **Condition:** The model is fine-tuned briefly on longer sequences after rescaling positions; quality at the new length must be checked.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: RoPE scaling.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
