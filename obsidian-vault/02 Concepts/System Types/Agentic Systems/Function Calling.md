---
title: Function Calling
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Tool_Use_Action_Interfaces
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Function calling
taxonomy_id: mlsys.function-calling
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Function Calling

A model emitting a structured invocation of a declared tool, which the harness validates, executes, and returns as an observation.

## Browsing Home

[[02 Concepts/System Types/Agentic Systems/Tool Use & Action Interfaces Subject|Tool Use & Action Interfaces]] → [[02 Concepts/System Types/Agentic Systems/Agentic Systems Index|Agentic Systems]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is validated against [[02 Concepts/System Types/Agentic Systems/Tool Contract|Tool Contract]]. **Condition:** The harness must validate calls against the contract; schema conformance does not imply authority.

- Constrains arguments with [[02 Concepts/Lifecycle/Deployment & Serving/Structured Output Constraint|Structured Output Constraint]]. **Condition:** Applies when tool arguments must match a declared schema.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: tool calling; tool use.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
