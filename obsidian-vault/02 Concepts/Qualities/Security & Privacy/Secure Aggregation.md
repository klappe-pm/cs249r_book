---
title: Secure Aggregation
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Privacy_Leakage_Differential_Privacy
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Secure aggregation
taxonomy_id: mlsys.secure-aggregation
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Secure Aggregation

A cryptographic protocol that lets a server compute the sum of client updates without seeing any individual client's update.

## Browsing Home

[[02 Concepts/Qualities/Security & Privacy/Privacy Leakage & Differential Privacy Subject|Privacy Leakage & Differential Privacy]] → [[02 Concepts/Qualities/Security & Privacy/Security & Privacy Index|Security & Privacy]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume II - Scaling/03 The Fleet in Production/11 Edge Intelligence/V2-11.08 Federated Learning Systems at Scale#^sec-edge-intelligence-federated-privacy-a1ed|V2-11.08 Federated Learning Systems at Scale]] — Secure aggregation. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/11_edge_intelligence/11_edge_intelligence.qmd#L2272).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Hinders detection of, increasing exposure to [[02 Concepts/Qualities/Security & Privacy/Data Poisoning|Data Poisoning]]. **Condition:** Because the server sees only aggregated updates, it cannot inspect individual client updates for anomalies.

- Blocks gradient-based [[02 Concepts/Qualities/Security & Privacy/Model Inversion|Model Inversion]]. **Condition:** When the server could otherwise reconstruct a client's data from its individual update.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
