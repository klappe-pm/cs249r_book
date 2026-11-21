---
title: Tool Contract
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Tool_Use_Action_Interfaces
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Tool contract
taxonomy_id: mlsys.tool-contract
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Tool Contract

A specification of tool inputs, outputs, authority, effects, and failure behavior.

## Browsing Home

[[02 Concepts/System Types/Agentic Systems/Tool Use & Action Interfaces Subject|Tool Use & Action Interfaces]] → [[02 Concepts/System Types/Agentic Systems/Agentic Systems Index|Agentic Systems]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Declares retry safety in terms of [[02 Concepts/Qualities/Reliability & Fault Tolerance/Idempotency|Idempotency]]. **Condition:** When the contract states an idempotency key or at-most-once semantics so the harness can decide whether a re-issued call is safe.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
