---
title: Quality Filtering
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Data_Selection_Curation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Quality filtering
taxonomy_id: mlsys.quality-filtering
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Quality Filtering

Removing or down-weighting training examples judged low quality by heuristics, classifiers, or model scores.

## Browsing Home

[[02 Concepts/Lifecycle/Data Engineering/Data Selection & Curation Subject|Data Selection & Curation]] → [[02 Concepts/Lifecycle/Data Engineering/Data Engineering Index|Data Engineering]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Implements [[02 Concepts/Lifecycle/Data Engineering/Data Selection|Data Selection]]. **Condition:** The quality score must correlate with downstream value; filtering on a narrow proxy can remove useful diversity.

- Raises average [[02 Concepts/Lifecycle/Data Engineering/Data Quality|Data Quality]]. **Condition:** Holds when the filter's notion of quality matches the target task; filters can also remove useful diversity.

- Runs at corpus scale on [[02 Concepts/Lifecycle/Data Engineering/Distributed Batch Data Processing|Distributed Batch Data Processing]]. **Condition:** Applies to web-scale pretraining corpora.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
