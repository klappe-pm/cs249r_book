---
title: Stop Conditions and Output Length Limits
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Decoding_Sampling_Structured_Output
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Stop conditions and output-length limits
taxonomy_id: mlsys.generation-stopping
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Stop Conditions and Output Length Limits

Rules that terminate autoregressive generation when a stopping criterion is met, including an end token, a stop sequence, or an output-token limit.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Decoding, Sampling & Structured Output Subject|Decoding, Sampling & Structured Output]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Caps per-request growth of [[02 Concepts/Lifecycle/Deployment & Serving/KV Cache|KV Cache]]. **Condition:** A server-enforced output-token cap limits additional retained token positions in engines whose autoregressive cache grows with generation; it does not bound all allocated cache memory.

- Limits the output-length contribution to [[02 Concepts/Lifecycle/Deployment & Serving/Tail Latency|Tail Latency]]. **Condition:** Decode-step time is bounded, while queueing, stalls, and retries are accounted for separately.

- Caps the output tokens one request can consume, blunting [[02 Concepts/Qualities/Security & Privacy/Resource Exhaustion Attack|Resource Exhaustion Attack]]. **Condition:** A server-enforced output cap limits generated-token work per request; separate controls are needed for prompt processing, request rate, and aggregate client consumption.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: stop sequences; max new tokens; end-of-sequence handling.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
