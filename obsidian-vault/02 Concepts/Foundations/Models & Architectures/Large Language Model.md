---
title: Large Language Model
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Model_Families
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Large language model
taxonomy_id: mlsys.large-language-model
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Large Language Model

A language model large enough that parameter memory, attention state that grows with context, and, when serving, token-by-token decoding dominate its resource demands.

## Browsing Home

[[02 Concepts/Foundations/Models & Architectures/Model Families Subject|Model Families]] → [[02 Concepts/Foundations/Models & Architectures/Models & Architectures Index|Models & Architectures]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is usually built on [[02 Concepts/Foundations/Models & Architectures/Transformer|Transformer]]. **Condition:** Most current language models use decoder-only Transformer stacks.

- Is a large-scale instance of [[02 Concepts/Foundations/Models & Architectures/Neural Networks|Neural Networks]]. **Condition:** The model is a parameterized composition of differentiable operations.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: LLM; LLM workload.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
