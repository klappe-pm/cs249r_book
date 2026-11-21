---
title: Non Prefix KV Reuse
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/LLM_Generative_Inference
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Non-prefix KV reuse
taxonomy_id: mlsys.non-prefix-kv-reuse
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Non Prefix KV Reuse

Reusing precomputed KV entries for text chunks appearing at arbitrary positions across requests, selectively recomputing cross-chunk attention instead of the full prefill.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/LLM & Generative Inference Subject|LLM & Generative Inference]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Generalizes beyond the exact-prefix matching of [[02 Concepts/Lifecycle/Deployment & Serving/Prefix Caching|Prefix Caching]]. **Condition:** Shared chunks appear at different positions across requests.

- Shortens [[02 Concepts/Lifecycle/Deployment & Serving/Time to First Token|Time to First Token]]. **Condition:** Reused chunks such as retrieved documents dominate prompt length.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: position-independent KV caching; KV cache blending.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
