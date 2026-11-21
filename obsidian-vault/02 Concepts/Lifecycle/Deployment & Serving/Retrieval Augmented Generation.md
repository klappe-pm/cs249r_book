---
title: Retrieval Augmented Generation
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Retrieval_Vector_Search
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Retrieval-augmented generation
taxonomy_id: mlsys.rag
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Retrieval Augmented Generation

Conditioning generation on documents retrieved for the request so outputs can draw on information outside the model's parameters.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Retrieval & Vector Search Subject|Retrieval & Vector Search]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Can reduce [[02 Concepts/Lifecycle/Model Evaluation & Testing/Hallucination|Hallucination]]. **Condition:** Holds when retrieved passages are relevant and the model grounds its claims in them; irrelevant retrievals can mislead.

- Depends on [[02 Concepts/Lifecycle/Deployment & Serving/Retrieval|Retrieval]]. **Condition:** Generation quality is bounded by retrieval recall for the facts the answer needs.

- Is a common stage of [[02 Concepts/Lifecycle/Deployment & Serving/Compound AI System|Compound AI System]]. **Condition:** When retrieval and generation run as separately served and tuned components.

- Lengthens prompts and so [[02 Concepts/Lifecycle/Deployment & Serving/Time to First Token|Time to First Token]]. **Condition:** Holds because retrieved passages add prefill tokens and retrieval adds a serial step.

- Answers multi-step questions with [[02 Concepts/Lifecycle/Deployment & Serving/Iterative Multi Hop Retrieval|Iterative Multi Hop Retrieval]]. **Condition:** No single query retrieves all needed evidence.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: RAG.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
