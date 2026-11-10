---
title: Idempotency
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Failure_Models_Retries_Degradation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Idempotency
taxonomy_id: mlsys.idempotency
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Idempotency

A specified operation's repeated execution having the same intended effect as one execution.

## Browsing Home

[[02 Concepts/Qualities/Reliability & Fault Tolerance/Failure Models, Retries & Degradation Subject|Failure Models, Retries & Degradation]] → [[02 Concepts/Qualities/Reliability & Fault Tolerance/Reliability & Fault Tolerance Index|Reliability & Fault Tolerance]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07.06 Retrying Uncertain Actions#^sec-vol3-tool-calling-operation-ids|V3-07.06 Retrying Uncertain Actions]] — Operation identity. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/07_tool_calling/07_tool_calling.qmd#L474).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Makes safe the retry of an [[02 Concepts/Qualities/Reliability & Fault Tolerance/In Doubt Action|In Doubt Action]]. **Condition:** When the operation carries an identity the endpoint deduplicates.

## Themes

- [[03 Themes/Reliability and Recovery|Reliability and Recovery]]

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
