---
title: Optimal Checkpoint Interval
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Checkpointing_Elastic_Recovery
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Optimal checkpoint interval
taxonomy_id: mlsys.checkpoint-interval
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Optimal Checkpoint Interval

The checkpoint period that minimizes expected lost time, balancing checkpoint write cost against expected rework, approximately the square root of twice the write cost times MTBF.

## Browsing Home

[[02 Concepts/Qualities/Reliability & Fault Tolerance/Checkpointing & Elastic Recovery Subject|Checkpointing & Elastic Recovery]] → [[02 Concepts/Qualities/Reliability & Fault Tolerance/Reliability & Fault Tolerance Index|Reliability & Fault Tolerance]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Maximizes, when well chosen, [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Training Goodput|Training Goodput]]. **Condition:** Under a stated MTBF and checkpoint write cost, the interval trades checkpoint overhead against expected lost work.

## Themes

- [[03 Themes/Reliability and Recovery|Reliability and Recovery]]

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: Young-Daly interval.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
