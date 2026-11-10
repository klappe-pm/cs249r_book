---
title: Homomorphic Encryption Inference
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Privacy_Leakage_Differential_Privacy
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Homomorphic-encryption inference
taxonomy_id: mlsys.he-inference
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Homomorphic Encryption Inference

Evaluating a model on encrypted inputs with homomorphic encryption so the server never sees plaintext, at large compute overhead and with polynomial approximations of nonlinearities.

## Browsing Home

[[02 Concepts/Qualities/Security & Privacy/Privacy Leakage & Differential Privacy Subject|Privacy Leakage & Differential Privacy]] → [[02 Concepts/Qualities/Security & Privacy/Security & Privacy Index|Security & Privacy]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Trades compute overhead for hardware trust versus [[02 Concepts/Qualities/Security & Privacy/Confidential Computing|Confidential Computing]]. **Condition:** Homomorphic encryption avoids trusting server hardware but costs orders of magnitude more compute than enclave execution.

- Multiplies [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Execution Time|Execution Time]]. **Condition:** Homomorphic evaluation costs orders of magnitude more compute than plaintext inference, especially for nonlinear layers.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: HE inference; encrypted inference.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
