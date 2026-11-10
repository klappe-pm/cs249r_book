---
title: Over Refusal
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Runtime_Assurance_Safety_Filters
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Over-refusal
taxonomy_id: mlsys.over-refusal
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Over Refusal

Refusing benign requests that resemble harmful ones, the false-positive side of a safety filter or refusal policy, which is traded against missed harmful requests when setting the operating point.

## Browsing Home

[[02 Concepts/Qualities/Safety & Assurance/Runtime Assurance & Safety Filters Subject|Runtime Assurance & Safety Filters]] → [[02 Concepts/Qualities/Safety & Assurance/Safety & Assurance Index|Safety & Assurance]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Rejects valid requests, reducing [[02 Concepts/Lifecycle/Deployment & Serving/SLO Goodput|SLO Goodput]]. **Condition:** When benign task completion is required for work to count as useful.

- Is the false-positive side of the operating point whose false-negative side is [[02 Concepts/Qualities/Security & Privacy/Jailbreak|Jailbreak]]. **Condition:** When a single threshold or refusal policy decides both, so loosening it to admit benign requests also admits more successful bypasses.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: false refusal; exaggerated safety.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
