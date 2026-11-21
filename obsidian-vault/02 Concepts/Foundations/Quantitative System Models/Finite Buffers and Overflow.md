---
title: Finite Buffers and Overflow
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Queueing_Capacity_Models
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Finite buffers and overflow
taxonomy_id: mlsys.finite-buffer
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Finite Buffers and Overflow

A queue with bounded capacity drops or blocks arrivals once full, so its size trades memory and added delay against the loss rate under bursty input.

## Browsing Home

[[02 Concepts/Foundations/Quantitative System Models/Queueing & Capacity Models Subject|Queueing & Capacity Models]] → [[02 Concepts/Foundations/Quantitative System Models/Quantitative System Models Index|Quantitative System Models]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Caps, by dropping or blocking arrivals once full, the [[02 Concepts/Foundations/Quantitative System Models/Queueing Delay|Queueing Delay]]. **Condition:** When the buffer bound is reached under bursty input; blocked or dropped arrivals pay loss or upstream delay instead of waiting.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: buffer overflow; bounded queue; finite-capacity queue; backlog.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
