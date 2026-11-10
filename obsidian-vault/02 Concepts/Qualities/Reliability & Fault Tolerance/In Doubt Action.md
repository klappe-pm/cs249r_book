---
title: In Doubt Action
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Failure_Models_Retries_Degradation
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: In-doubt action
taxonomy_id: mlsys.in-doubt-action
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# In Doubt Action

An external action whose outcome is unknown after dispatch, requiring reconciliation or retry-safe endpoint semantics before recovery chooses whether to repeat or skip it.

## Browsing Home

[[02 Concepts/Qualities/Reliability & Fault Tolerance/Failure Models, Retries & Degradation Subject|Failure Models, Retries & Degradation]] → [[02 Concepts/Qualities/Reliability & Fault Tolerance/Reliability & Fault Tolerance Index|Reliability & Fault Tolerance]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Cannot be compensated until it is known to have happened, so it bounds [[02 Concepts/Qualities/Reliability & Fault Tolerance/Compensating Action|Compensating Action]]. **Condition:** A compensating action for an effect that never occurred is itself a new effect.

- Blocks, until settled, the resumption of [[02 Concepts/System Types/Agentic Systems/Durable Execution|Durable Execution]]. **Condition:** When a resumed workflow reaches a step whose effect may or may not have happened.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: unknown outcome; in-doubt operation.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
