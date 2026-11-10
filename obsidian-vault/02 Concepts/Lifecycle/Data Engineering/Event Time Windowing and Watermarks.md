---
title: Event Time Windowing and Watermarks
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Data_Pipelines_Storage_Formats
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Event-time windowing and watermarks
taxonomy_id: mlsys.event-time-windowing
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Event Time Windowing and Watermarks

Grouping stream events into windows by when they occurred, using watermarks to estimate completeness and explicit policies for events arriving after a window closes.

## Browsing Home

[[02 Concepts/Lifecycle/Data Engineering/Data Pipelines & Storage Formats Subject|Data Pipelines & Storage Formats]] → [[02 Concepts/Lifecycle/Data Engineering/Data Engineering Index|Data Engineering]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is a mechanism within [[02 Concepts/Lifecycle/Data Engineering/Stream Processing|Stream Processing]]. **Condition:** Events carry timestamps and can arrive out of order.

- Sets the staleness of streaming features through [[02 Concepts/Lifecycle/Data Engineering/Feature Freshness|Feature Freshness]]. **Condition:** Window size and allowed lateness bound when an aggregate is emitted.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: stream watermarks; late data handling; windowed aggregation.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
