---
title: Long Term Agent Memory
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Context_Engineering_Agent_Memory
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Long-term agent memory
taxonomy_id: mlsys.agent-memory
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Long Term Agent Memory

A persistent store an agent writes to and retrieves from across calls and sessions, with policies for consolidation, expiry, and invalidation.

## Browsing Home

[[02 Concepts/System Types/Agentic Systems/Context Engineering & Agent Memory Subject|Context Engineering & Agent Memory]] → [[02 Concepts/System Types/Agentic Systems/Agentic Systems Index|Agentic Systems]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/06 Long-Term Memory/V3-06.03 Persistent Records#^sec-vol3-long-term-memory-record-roles|V3-06.03 Persistent Records]] — Persistent memory record. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/06_long_term_memory/06_long_term_memory.qmd#L85).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is read through [[02 Concepts/Lifecycle/Deployment & Serving/Retrieval|Retrieval]]. **Condition:** Memory recall quality is bounded by the retrieval contract and index freshness.

- Can retain facts that produce [[02 Concepts/System Types/Agentic Systems/Context Staleness|Context Staleness]]. **Condition:** Stored observations are not revalidated after the environment changes.

- Enables persistent [[02 Concepts/Qualities/Security & Privacy/Prompt Injection|Prompt Injection]]. **Condition:** When attacker-controlled instructions can be stored in agent memory and later retrieved into a context where the model may treat them as authoritative.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
