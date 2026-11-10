---
title: Chat Template
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Model_Artifacts_Formats
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Chat template
taxonomy_id: mlsys.chat-template
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Chat Template

The fixed scheme of role markers and special tokens that serializes system instructions, user and assistant turns, and tool calls into one token sequence, which must match between fine-tuning and serving or the model misreads turn boundaries.

## Browsing Home

[[02 Concepts/Foundations/Models & Architectures/Model Artifacts & Formats Subject|Model Artifacts & Formats]] → [[02 Concepts/Foundations/Models & Architectures/Models & Architectures Index|Models & Architectures]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Causes, when rendered differently in training and serving, [[02 Concepts/Lifecycle/Data Engineering/Training Serving Skew|Training Serving Skew]]. **Condition:** When the serving stack renders turns with different markers or whitespace from the training renderer.

- Reserves special tokens in [[02 Concepts/Foundations/Models & Architectures/Tokenization|Tokenization]]. **Condition:** When role markers are single reserved tokens rather than plain text.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: conversation formatting; role markers; prompt format; turn delimiters.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
