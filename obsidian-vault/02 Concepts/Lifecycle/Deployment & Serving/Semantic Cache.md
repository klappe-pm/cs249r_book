---
title: Semantic Cache
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Compound_AI_Systems_Model_Routing
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Semantic cache
taxonomy_id: mlsys.semantic-cache
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Semantic Cache

Returning a stored model response when a new request is close in embedding space to an earlier one, trading answer fidelity for latency and cost.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Compound AI Systems & Model Routing Subject|Compound AI Systems & Model Routing]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Finds similar past requests with [[02 Concepts/Lifecycle/Deployment & Serving/Approximate Nearest Neighbor Search|Approximate Nearest Neighbor Search]]. **Condition:** Requests are embedded and indexed.

- Avoids model calls that drive [[02 Concepts/Qualities/Sustainability & Cost/Cost per Useful Outcome|Cost per Useful Outcome]]. **Condition:** Workloads with many near-duplicate requests.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: semantic caching.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
