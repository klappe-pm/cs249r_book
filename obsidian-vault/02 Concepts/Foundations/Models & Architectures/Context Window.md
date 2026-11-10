---
title: Context Window
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Long_Context_Efficient_Sequence_Models
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Context window
taxonomy_id: mlsys.context
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Context Window

The maximum token span a model supports in a stated execution mode, bounding the history it can use and the longest sequences the system must process.

## Browsing Home

[[02 Concepts/Foundations/Models & Architectures/Long Context & Efficient Sequence Models Subject|Long Context & Efficient Sequence Models]] → [[02 Concepts/Foundations/Models & Architectures/Models & Architectures Index|Models & Architectures]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04.03 The Working-Set Decision#^sec-vol3-context-engineering-decision|V3-04.03 The Working-Set Decision]] — Working context. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/04_context_engineering/04_context_engineering.qmd#L85).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Bounds the history carried across an [[02 Concepts/System Types/Agentic Systems/Agent Trajectory|Agent Trajectory]]. **Condition:** Only selected observations and records fit in a model invocation.

- Bounds the passage volume injected by [[02 Concepts/Lifecycle/Deployment & Serving/Retrieval|Retrieval]]. **Condition:** Relevance, authorization, provenance, and token budget constrain what may be supplied.

- Scales the size of [[02 Concepts/Lifecycle/Deployment & Serving/KV Cache|KV Cache]]. **Condition:** Autoregressive decoding retains keys and values for every prior position.

- Caps the demonstrations available to [[02 Concepts/Lifecycle/Training & Adaptation/In Context Learning|In Context Learning]]. **Condition:** Demonstrations and instructions share one input budget.

- Sets the token budget for [[02 Concepts/System Types/Agentic Systems/Context Selection|Context Selection]]. **Condition:** Candidate content exceeds the input budget.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: context length.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
