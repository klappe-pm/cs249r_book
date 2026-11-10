---
title: Ephemeral Sandbox
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Access_Control_Isolation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Ephemeral sandbox
taxonomy_id: mlsys.ephemeral-sandbox
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Ephemeral Sandbox

An isolated execution environment created per task from a snapshot, often copy-on-write, and destroyed or reset afterward so no state carries across tasks or tenants.

## Browsing Home

[[02 Concepts/Qualities/Security & Privacy/Access Control & Isolation Subject|Access Control & Isolation]] → [[02 Concepts/Qualities/Security & Privacy/Security & Privacy Index|Security & Privacy]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Provides per-task [[02 Concepts/Qualities/Security & Privacy/Execution Isolation|Execution Isolation]]. **Condition:** Each task or tenant receives a fresh environment.

- Confines local damage that would otherwise become [[02 Concepts/Qualities/Reliability & Fault Tolerance/Irreversible Effects|Irreversible Effects]]. **Condition:** Effects stay inside the sandbox rather than reaching external systems.

- Restricts outbound network access with [[02 Concepts/Qualities/Security & Privacy/Network Egress Control|Network Egress Control]]. **Condition:** The sandbox has network access.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: copy-on-write workspace; disposable execution environment; microVM sandbox.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
