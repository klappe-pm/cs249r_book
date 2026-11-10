---
title: Authorization
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Access_Control_Isolation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Authorization
taxonomy_id: mlsys.authorization
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Authorization

Determining whether an actor may perform a specified action on a resource.

## Browsing Home

[[02 Concepts/Qualities/Security & Privacy/Access Control & Isolation Subject|Access Control & Isolation]] → [[02 Concepts/Qualities/Security & Privacy/Security & Privacy Index|Security & Privacy]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08.05 Capabilities and Credentials#^sec-vol3-sandboxes-scoped-grants|V3-08.05 Capabilities and Credentials]] — Capability grant. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/08_sandboxes/08_sandboxes.qmd#L373).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Blocks unauthorized actions triggered by [[02 Concepts/Qualities/Security & Privacy/Prompt Injection|Prompt Injection]]. **Condition:** Untrusted content must not silently acquire authority through model interpretation.

- Prevents unregistered [[02 Concepts/Lifecycle/MLOps & Operations/Undeclared Consumers|Undeclared Consumers]]. **Condition:** Applies when prediction endpoints and output tables require granted access per consumer.

- Checks a proposed tool call against the authority and effects declared in the [[02 Concepts/System Types/Agentic Systems/Tool Contract|Tool Contract]]. **Condition:** When tool calls are authorized per action from the contract rather than by ambient session rights; schema conformance alone grants nothing.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
