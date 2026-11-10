---
title: Capability Based Authorization
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Access_Control_Isolation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Capability-based authorization
taxonomy_id: mlsys.capability-based-security
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Capability Based Authorization

Authorization in which holding an unforgeable, scoped reference grants a specific right that can be delegated with attenuated scope and later revoked.

## Browsing Home

[[02 Concepts/Qualities/Security & Privacy/Access Control & Isolation Subject|Access Control & Isolation]] → [[02 Concepts/Qualities/Security & Privacy/Security & Privacy Index|Security & Privacy]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08.05 Capabilities and Credentials#^sec-vol3-sandboxes-scoped-grants|V3-08.05 Capabilities and Credentials]] — Capability grant. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/08_sandboxes/08_sandboxes.qmd#L373).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is a reference-based form of [[02 Concepts/Qualities/Security & Privacy/Authorization|Authorization]]. **Condition:** Rights travel with unforgeable tokens.

- Realizes [[02 Concepts/Qualities/Security & Privacy/Least Privilege|Least Privilege]]. **Condition:** Delegated capabilities are attenuated to the task's needs.

- Binds each action to narrow, task-scoped authority to prevent [[02 Concepts/Qualities/Security & Privacy/Confused Deputy|Confused Deputy]]. **Condition:** When ambient user or service credentials are replaced with attenuated capabilities.

## Themes

- [[03 Themes/Security and Trust|Security and Trust]]

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: capability tokens; object capabilities; attenuated credentials.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
