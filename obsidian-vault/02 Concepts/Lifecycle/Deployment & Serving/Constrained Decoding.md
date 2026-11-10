---
title: Constrained Decoding
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Decoding_Sampling_Structured_Output
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Constrained decoding
taxonomy_id: mlsys.constrained-decoding
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Constrained Decoding

A generation mechanism that restricts token choices to continuations permitted by an output constraint, so a successfully completed output satisfies the supported syntax or schema constraints.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Decoding, Sampling & Structured Output Subject|Decoding, Sampling & Structured Output]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02.08 Grammar-Guided Decoding#^sec-vol3-foundation-model-structural-guarantee-scope|V3-02.08 Grammar-Guided Decoding]] — Grammar constraint. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/02_foundation_model/02_foundation_model.qmd#L754).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Enforces [[02 Concepts/Lifecycle/Deployment & Serving/Structured Output Constraint|Structured Output Constraint]]. **Condition:** The constraint representation is supported, enforcement is compatible with the tokenizer, and generation completes successfully.

- Guarantees well-formed arguments for [[02 Concepts/System Types/Agentic Systems/Function Calling|Function Calling]]. **Condition:** The supported argument constraints are enforced during decoding and the output completes successfully; this does not establish argument truth or tool authorization.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: grammar-guided decoding.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
