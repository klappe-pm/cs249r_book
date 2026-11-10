---
title: Machine Unlearning
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Privacy_Leakage_Differential_Privacy
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Machine unlearning
taxonomy_id: mlsys.machine-unlearning
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Machine Unlearning

Removing the influence of specified training records from a trained model, either exactly by retraining or approximately at lower cost.

## Browsing Home

[[02 Concepts/Qualities/Security & Privacy/Privacy Leakage & Differential Privacy Subject|Privacy Leakage & Differential Privacy]] → [[02 Concepts/Qualities/Security & Privacy/Security & Privacy Index|Security & Privacy]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is a cheaper, approximate alternative to full [[02 Concepts/Lifecycle/MLOps & Operations/Retraining|Retraining]]. **Condition:** Exact unlearning equals retraining without the removed records; approximate methods trade the strength of the guarantee for lower cost.

- Requires [[02 Concepts/Lifecycle/Data Engineering/Data Lineage|Data Lineage]]. **Condition:** To locate every model, shard, and derived artifact that was trained on the records to be removed.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
