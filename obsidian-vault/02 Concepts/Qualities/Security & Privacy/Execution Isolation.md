---
title: Execution Isolation
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Access_Control_Isolation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Execution isolation
taxonomy_id: mlsys.isolation
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Execution Isolation

Restricting which resources and effects a computation can access.

## Browsing Home

[[02 Concepts/Qualities/Security & Privacy/Access Control & Isolation Subject|Access Control & Isolation]] → [[02 Concepts/Qualities/Security & Privacy/Security & Privacy Index|Security & Privacy]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08.06 Choosing an Isolation Envelope#^sec-vol3-sandboxes-microvms|V3-08.06 Choosing an Isolation Envelope]] — Isolation envelope. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/08_sandboxes/08_sandboxes.qmd#L481).

- [[01 Books/Volume IV - Physical AI/03 Running the Machine/13 Workload Placement/V4-13.07 Silicon Isolation Decisions#^sec-placement-isolation-decisions|V4-13.07 Silicon Isolation Decisions]] — Resource isolation. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/13_placement/13_placement.qmd#L1365).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Enforces the access boundaries of [[02 Concepts/Qualities/Security & Privacy/Authorization|Authorization]]. **Condition:** Isolation can restrict resource access, but it does not choose the authorization policy or prove external-effect correctness.

- Contains the effects of [[02 Concepts/Qualities/Security & Privacy/Unsafe Model Deserialization|Unsafe Model Deserialization]]. **Condition:** When untrusted model files are loaded inside a sandbox with no credentials or network access.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
