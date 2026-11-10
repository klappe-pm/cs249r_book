---
title: Speculative Decoding
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/LLM_Generative_Inference
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Speculative decoding
taxonomy_id: mlsys.speculative-decoding
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Speculative Decoding

Using proposed tokens and a validating procedure to accelerate generation while preserving a specified output distribution.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/LLM & Generative Inference Subject|LLM & Generative Inference]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Can raise effective decode throughput of [[02 Concepts/Foundations/Quantitative System Models/Service Capacity|Service Capacity]]. **Condition:** Acceptance rate, proposer cost, verification, and workload determine the net gain.

- Reduces [[02 Concepts/Lifecycle/Deployment & Serving/Time per Output Token|Time per Output Token]]. **Condition:** Holds when the draft acceptance rate is high and decode is memory-bound.

- Verifies several tokens per weight read, raising [[02 Concepts/Foundations/Quantitative System Models/Arithmetic Intensity|Arithmetic Intensity]]. **Condition:** Holds at small batch sizes where decode is memory-bound.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: draft-and-verify; EAGLE; self-speculative decoding; multi-token draft heads.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
