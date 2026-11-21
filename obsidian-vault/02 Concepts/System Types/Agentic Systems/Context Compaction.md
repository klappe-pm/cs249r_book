---
title: Context Compaction
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Context_Engineering_Agent_Memory
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Context compaction
taxonomy_id: mlsys.context-compaction
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Context Compaction

Replacing older parts of an agent's context with summaries or structured records so a long task fits the model's input budget.

## Browsing Home

[[02 Concepts/System Types/Agentic Systems/Context Engineering & Agent Memory Subject|Context Engineering & Agent Memory]] → [[02 Concepts/System Types/Agentic Systems/Agentic Systems Index|Agentic Systems]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04.06 Context Compaction#^sec-vol3-context-engineering-compaction|V3-04.06 Context Compaction]] — Context compaction. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/04_context_engineering/04_context_engineering.qmd#L661).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Trades saved tokens against the prefix reuse lost in [[02 Concepts/Lifecycle/Deployment & Serving/Prefix Caching|Prefix Caching]]. **Condition:** When rewriting earlier context invalidates the cached prefix, so compaction pays off only when the saved execution work over the remaining session exceeds the summarization and prefix-recompute cost.

- Mitigates [[02 Concepts/Foundations/Models & Architectures/Long Context Degradation|Long Context Degradation]]. **Condition:** Older material is summarized so relevant information stays short and near the end of the window.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
