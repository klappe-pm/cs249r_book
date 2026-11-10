---
title: Safety Performance Indicator
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Safety_Cases_Standards_Certification
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Safety performance indicator
taxonomy_id: mlsys.safety-performance-indicator
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Safety Performance Indicator

A field-measured metric tied to a safety-case claim whose threshold violation signals that the argument may no longer hold.

## Browsing Home

[[02 Concepts/Qualities/Safety & Assurance/Safety Cases, Standards & Certification Subject|Safety Cases, Standards & Certification]] → [[02 Concepts/Qualities/Safety & Assurance/Safety & Assurance Index|Safety & Assurance]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Monitors validity of [[02 Concepts/Qualities/Safety & Assurance/Safety Case|Safety Case]]. **Condition:** Each indicator must trace to a specific claim and have a threshold that triggers review.

- Is collected through [[02 Concepts/Lifecycle/MLOps & Operations/Production Monitoring|Production Monitoring]]. **Condition:** Holds when field telemetry captures the events the indicator counts.

- Is computed from events logged by [[02 Concepts/Qualities/Safety & Assurance/Event Data Recorder|Event Data Recorder]]. **Condition:** Field events are recorded consistently.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: SPI.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
