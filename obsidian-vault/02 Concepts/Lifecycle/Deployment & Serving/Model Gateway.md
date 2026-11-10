---
title: Model Gateway
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Compound_AI_Systems_Model_Routing
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Model gateway
taxonomy_id: mlsys.model-gateway
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Model Gateway

A proxy in front of one or more model providers that centralizes authentication, routing, rate limits, fallbacks, and usage logging for model calls.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Compound AI Systems & Model Routing Subject|Compound AI Systems & Model Routing]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Directs requests by [[02 Concepts/Lifecycle/Deployment & Serving/Model Routing|Model Routing]]. **Condition:** Several models or providers serve the same application.

- Records usage for [[02 Concepts/Qualities/Sustainability & Cost/Cost Attribution|Cost Attribution]]. **Condition:** All model calls pass through the gateway.

- Can serve repeated requests from [[02 Concepts/Lifecycle/Deployment & Serving/Semantic Cache|Semantic Cache]]. **Condition:** Responses are reusable across users and sessions.

- Enforces per-client rate limits as [[02 Concepts/Lifecycle/Deployment & Serving/Admission Control|Admission Control]]. **Condition:** When all model calls pass through the gateway and limits are expressed per key, tenant, or application.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: LLM gateway; AI gateway.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
