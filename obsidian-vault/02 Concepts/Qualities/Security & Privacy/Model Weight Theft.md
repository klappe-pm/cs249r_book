---
title: Model Weight Theft
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Model_Supply_Chain_Security
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Model weight theft
taxonomy_id: mlsys.weight-exfiltration
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Model Weight Theft

Theft of a model's parameter files from training, storage, or serving infrastructure by insiders or intruders, as distinct from reconstructing the model through its query interface, which the owner counters with access control, encryption at rest, attested execution, and egress limits.

## Browsing Home

[[02 Concepts/Qualities/Security & Privacy/Model & Supply Chain Security Subject|Model & Supply Chain Security]] → [[02 Concepts/Qualities/Security & Privacy/Security & Privacy Index|Security & Privacy]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Obtains the model directly instead of reconstructing it by queries as in [[02 Concepts/Qualities/Security & Privacy/Model Extraction|Model Extraction]]. **Condition:** Both yield a usable copy; theft needs infrastructure access, extraction needs only the prediction interface.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: weight exfiltration.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
