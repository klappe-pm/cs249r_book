---
title: Remote Attestation
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Access_Control_Isolation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Remote attestation
taxonomy_id: mlsys.remote-attestation
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Remote Attestation

A procedure by which a platform proves to a remote verifier the identity and measured state of its hardware and software before receiving secrets.

## Browsing Home

[[02 Concepts/Qualities/Security & Privacy/Access Control & Isolation Subject|Access Control & Isolation]] → [[02 Concepts/Qualities/Security & Privacy/Security & Privacy Index|Security & Privacy]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Establishes trust in [[02 Concepts/Qualities/Security & Privacy/Confidential Computing|Confidential Computing]]. **Condition:** When the verifier checks attestation evidence against reference values before releasing keys, data, or model weights.

- Detects [[02 Concepts/Qualities/Security & Privacy/ML Supply Chain Compromise|ML Supply Chain Compromise]]. **Condition:** For platform firmware or software whose measured state differs from trusted reference values.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
