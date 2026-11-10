---
title: Agent Credentials and Delegated Authority
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Access_Control_Isolation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Agent credentials and delegated authority
taxonomy_id: mlsys.agent-credentials
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Agent Credentials and Delegated Authority

Issuing tool-using agents scoped, short-lived credentials that act on a user's behalf, brokering secrets outside model context so authority stays bounded and revocable.

## Browsing Home

[[02 Concepts/Qualities/Security & Privacy/Access Control & Isolation Subject|Access Control & Isolation]] → [[02 Concepts/Qualities/Security & Privacy/Security & Privacy Index|Security & Privacy]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Realizes [[02 Concepts/Qualities/Security & Privacy/Least Privilege|Least Privilege]]. **Condition:** Credentials are scoped to the task and expire after it.

- Issues attenuated rights through [[02 Concepts/Qualities/Security & Privacy/Capability Based Authorization|Capability Based Authorization]]. **Condition:** Delegated tokens carry narrower scope than the user holds.

- Draws on [[02 Concepts/Qualities/Security & Privacy/Workload Identity and Secrets Management|Workload Identity and Secrets Management]]. **Condition:** Agents act with credentials issued by the platform.

- Scopes and brokers per-action tokens outside model context to limit [[02 Concepts/Qualities/Security & Privacy/Confused Deputy|Confused Deputy]]. **Condition:** When tool calls require explicit user- and resource-scoped delegation.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: agent identity; delegated tokens; secret brokering.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
