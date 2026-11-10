---
title: Minimal Risk Condition
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Runtime_Assurance_Safety_Filters
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Minimal-risk condition
taxonomy_id: mlsys.minimal-risk-condition
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Minimal Risk Condition

A predefined reduced-capability state the system reaches when it can no longer operate safely, often via an ordered ladder of fallback behaviors.

## Browsing Home

[[02 Concepts/Qualities/Safety & Assurance/Runtime Assurance & Safety Filters Subject|Runtime Assurance & Safety Filters]] → [[02 Concepts/Qualities/Safety & Assurance/Safety & Assurance Index|Safety & Assurance]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Can be the final stage of [[02 Concepts/Qualities/Reliability & Fault Tolerance/Graceful Degradation|Graceful Degradation]]. **Condition:** When degradation in a physical system proceeds to a safe stop.

- Is an alternative to [[02 Concepts/Qualities/Responsible AI/Authority Handover|Authority Handover]]. **Condition:** When the system can no longer operate safely, it can either hand control to a human or reach a minimal-risk state itself.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: MRC; safe fallback; fallback ladder.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
