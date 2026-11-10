---
title: Context Selection
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Context_Engineering_Agent_Memory
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Context selection
taxonomy_id: mlsys.context-selection
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Context Selection

Choosing which instructions, tool descriptions, retrieved items, state, and observations enter a model's limited context at each step, within a token budget.

## Browsing Home

[[02 Concepts/System Types/Agentic Systems/Context Engineering & Agent Memory Subject|Context Engineering & Agent Memory]] → [[02 Concepts/System Types/Agentic Systems/Agentic Systems Index|Agentic Systems]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04.03 The Working-Set Decision#^sec-vol3-context-engineering-decision|V3-04.03 The Working-Set Decision]] — Working context. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/04_context_engineering/04_context_engineering.qmd#L85).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Gathers candidates with [[02 Concepts/Lifecycle/Deployment & Serving/Retrieval|Retrieval]]. **Condition:** Relevant items are fetched on demand rather than preloaded.

- Limits distractor content that drives [[02 Concepts/Foundations/Models & Architectures/Long Context Degradation|Long Context Degradation]]. **Condition:** Irrelevant tokens otherwise dilute attention.

- Draws recalled records into the working set from [[02 Concepts/System Types/Agentic Systems/Long Term Agent Memory|Long Term Agent Memory]]. **Condition:** When the agent has persistent memory; the recalled record competes for the same token budget as instructions, tool descriptions, and observations.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: context budget allocation; tool selection; working-set selection.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
