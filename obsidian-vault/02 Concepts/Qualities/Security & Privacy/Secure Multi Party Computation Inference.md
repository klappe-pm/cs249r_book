---
title: Secure Multi Party Computation Inference
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Privacy_Leakage_Differential_Privacy
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Secure multi-party computation inference
taxonomy_id: mlsys.secure-computation-inference
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Secure Multi Party Computation Inference

Jointly evaluating a model over secret-shared inputs or weights so no party learns another's data, with cost dominated by communication rounds for nonlinear layers.

## Browsing Home

[[02 Concepts/Qualities/Security & Privacy/Privacy Leakage & Differential Privacy Subject|Privacy Leakage & Differential Privacy]] → [[02 Concepts/Qualities/Security & Privacy/Security & Privacy Index|Security & Privacy]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Trades communication for computation versus [[02 Concepts/Qualities/Security & Privacy/Homomorphic Encryption Inference|Homomorphic Encryption Inference]]. **Condition:** Hybrid protocols use homomorphic encryption for linear layers and secret sharing or garbled circuits for nonlinear ones.

- Prevents input disclosure in [[02 Concepts/Qualities/Security & Privacy/Privacy Leakage|Privacy Leakage]]. **Condition:** Protects inputs during computation but not leakage from the revealed outputs themselves.

- Increases [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Execution Time|Execution Time]]. **Condition:** Latency is dominated by communication rounds and garbled-circuit evaluation of nonlinear layers.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: secure two-party inference; SMPC inference; 2PC inference.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
