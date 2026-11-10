---
title: Prefill Decode Disaggregation
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/LLM_Generative_Inference
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Prefill-decode disaggregation
taxonomy_id: mlsys.pd-disaggregation
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Prefill Decode Disaggregation

Running prefill and decode on separate resource pools, transferring KV state between them, so each phase is provisioned and batched independently.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/LLM & Generative Inference Subject|LLM & Generative Inference]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Provisions separate resources for each phase of [[02 Concepts/Lifecycle/Deployment & Serving/Prefill and Decode|Prefill and Decode]]. **Condition:** Pays off when interference between phases costs more than transferring KV state between pools.

- Can increase [[02 Concepts/Lifecycle/Deployment & Serving/SLO Goodput|SLO Goodput]]. **Condition:** Holds when TTFT and TPOT targets would otherwise force over-provisioning of a colocated deployment.

- Requires [[02 Concepts/Lifecycle/Deployment & Serving/KV Cache Transfer|KV Cache Transfer]]. **Condition:** Disaggregation is profitable only when KV transfer between pools is faster than the decode-latency gain it buys.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: disaggregated serving.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
