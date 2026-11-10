---
title: Dataset Deduplication
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Data_Selection_Curation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Dataset deduplication
taxonomy_id: mlsys.deduplication
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Dataset Deduplication

Finding and managing exact or near-duplicate examples within a corpus and overlaps with evaluation data to control sample weighting, redundant compute, memorization, and contamination.

## Browsing Home

[[02 Concepts/Lifecycle/Data Engineering/Data Selection & Curation Subject|Data Selection & Curation]] → [[02 Concepts/Lifecycle/Data Engineering/Data Engineering Index|Data Engineering]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is a curation stage of [[02 Concepts/Lifecycle/Data Engineering/Data Selection|Data Selection]]. **Condition:** Removing duplicates changes sample weights and must preserve required coverage.

- Reduces [[02 Concepts/Lifecycle/Model Evaluation & Testing/Benchmark Contamination|Benchmark Contamination]]. **Condition:** Holds when deduplication is run against evaluation sets, not only within the training corpus.

- Lowers extractable memorization by removing the repeated sequences behind [[02 Concepts/Qualities/Security & Privacy/Training Data Extraction|Training Data Extraction]]. **Condition:** When near-duplicates are removed from the pretraining corpus.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
