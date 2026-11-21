---
title: Tokenization
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Architecture_Building_Blocks
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Tokenization
taxonomy_id: mlsys.tokenization
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Tokenization

Mapping text into vocabulary-dependent token identifiers, which sets sequence lengths and so influences context usage, embedding size, and processing cost.

## Browsing Home

[[02 Concepts/Foundations/Models & Architectures/Architecture Building Blocks Subject|Architecture Building Blocks]] → [[02 Concepts/Foundations/Models & Architectures/Models & Architectures Index|Models & Architectures]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Sets the sequence length processed by [[02 Concepts/Foundations/Models & Architectures/Attention|Attention]]. **Condition:** For a fixed text, changing vocabulary and segmentation can change sequence length.

- Defines the lookup identities of [[02 Concepts/Foundations/Models & Architectures/Embeddings|Embeddings]]. **Condition:** Embedding rows must correspond to the model's tokenizer and vocabulary.

- Sets how much text fits in [[02 Concepts/Foundations/Models & Architectures/Context Window|Context Window]]. **Condition:** For a fixed window, a tokenizer that produces more tokens per word admits less source text.

- Sets the unit of [[02 Concepts/Lifecycle/Model Evaluation & Testing/Perplexity|Perplexity]]. **Condition:** Per-token perplexities are comparable only under one tokenizer; bits per byte normalizes.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: subword tokenization; BPE.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
