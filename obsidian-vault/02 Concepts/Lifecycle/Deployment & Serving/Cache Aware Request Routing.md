---
title: Cache Aware Request Routing
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Batching_Admission_Autoscaling
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Cache-aware request routing
taxonomy_id: mlsys.cache-aware-routing
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Cache Aware Request Routing

Sending each request to the replica that already holds a reusable prefix or KV cache for it, trading load balance against cache reuse.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Batching, Admission & Autoscaling Subject|Batching, Admission & Autoscaling]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Routes requests to replicas holding compatible cached prefixes of [[02 Concepts/Lifecycle/Deployment & Serving/Prefix Caching|Prefix Caching]]. **Condition:** When requests share prompt prefixes or belong to multi-turn sessions and the cached prefix is replica-local.

- Trades cache reuse against [[02 Concepts/Lifecycle/Deployment & Serving/Request Load Balancing|Request Load Balancing]]. **Condition:** Popular prefixes concentrate traffic on a few replicas.

- Skips recomputing a cached prefix and so lowers [[02 Concepts/Lifecycle/Deployment & Serving/Time to First Token|Time to First Token]]. **Condition:** Requests share prefixes and the routed replica still holds the cached state.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: prefix-affinity routing; KV-aware routing; session affinity.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
