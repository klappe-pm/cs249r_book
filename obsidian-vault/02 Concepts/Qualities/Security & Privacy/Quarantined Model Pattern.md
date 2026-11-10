---
title: Quarantined Model Pattern
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Access_Control_Isolation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Quarantined-model pattern
taxonomy_id: mlsys.quarantined-model-pattern
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Quarantined Model Pattern

Separating privileged planning from an unprivileged model that parses untrusted content, so that parsed values reach the planner only as references and a trusted runtime, often with provenance tracking, checks derived values before tool execution.

## Browsing Home

[[02 Concepts/Qualities/Security & Privacy/Access Control & Isolation Subject|Access Control & Isolation]] → [[02 Concepts/Qualities/Security & Privacy/Security & Privacy Index|Security & Privacy]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Removes the channel from untrusted text to privileged actions used by [[02 Concepts/Qualities/Security & Privacy/Prompt Injection|Prompt Injection]]. **Condition:** When the planner and runtime are trusted, untrusted content stays isolated in the quarantined model, and runtime policies validate derived arguments and data flows before any privileged effect.

- Tags quarantined outputs and checks tool arguments with [[02 Concepts/Qualities/Security & Privacy/Information Flow Control|Information Flow Control]]. **Condition:** When a value derived from untrusted data must be policy-checked before it reaches a side-effecting tool.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: dual-LLM pattern; privileged and quarantined LLM; CaMeL; quarantined reader.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
