---
title: Information Flow Control
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Access_Control_Isolation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Information-flow control
taxonomy_id: mlsys.information-flow-control
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Information Flow Control

Labeling data with confidentiality and integrity tags and propagating them through computation so policy can block untrusted inputs from steering privileged actions or secrets from leaking.

## Browsing Home

[[02 Concepts/Qualities/Security & Privacy/Access Control & Isolation Subject|Access Control & Isolation]] → [[02 Concepts/Qualities/Security & Privacy/Security & Privacy Index|Security & Privacy]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume III - Agentic Systems/03 Tool Use/09 Agent Security/V3-09.07 Information-Flow Policy#^sec-vol3-security-integrity-confidentiality|V3-09.07 Information-Flow Policy]] — Information-flow policy. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/09_security/09_security.qmd#L481).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Prevents untrusted data from steering actions in [[02 Concepts/Qualities/Security & Privacy/Prompt Injection|Prompt Injection]]. **Condition:** Data from tools and documents carries low-integrity labels.

- Blocks labeled secrets from [[02 Concepts/Qualities/Security & Privacy/Privacy Leakage|Privacy Leakage]]. **Condition:** Confidential data is tagged at its source.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: taint tracking; data-flow labels.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
