---
title: Confidential Computing
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Access_Control_Isolation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Confidential computing
taxonomy_id: mlsys.confidential-computing
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Confidential Computing

Protecting data and models while in use by running computation inside hardware-isolated, attestable trusted execution environments.

## Browsing Home

[[02 Concepts/Qualities/Security & Privacy/Access Control & Isolation Subject|Access Control & Isolation]] → [[02 Concepts/Qualities/Security & Privacy/Security & Privacy Index|Security & Privacy]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is a hardware-attested form of [[02 Concepts/Qualities/Security & Privacy/Execution Isolation|Execution Isolation]]. **Condition:** When the trusted execution environment's hardware and firmware are trusted and the host operator is not.

- Keeps weights unreadable to the host operator, limiting [[02 Concepts/Qualities/Security & Privacy/Model Weight Theft|Model Weight Theft]]. **Condition:** When the weights are decrypted only inside the attested environment.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: trusted execution environment; TEE.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
