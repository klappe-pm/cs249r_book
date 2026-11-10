---
title: Data Curriculum and Annealing
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Data_Selection_Curation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Data curriculum and annealing
taxonomy_id: mlsys.data-curriculum
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Data Curriculum and Annealing

Changing the training data distribution over a run, such as raising the share of high-quality or long-sequence data during the final learning-rate decay, to improve final capability per unit of compute.

## Browsing Home

[[02 Concepts/Lifecycle/Data Engineering/Data Selection & Curation Subject|Data Selection & Curation]] → [[02 Concepts/Lifecycle/Data Engineering/Data Engineering Index|Data Engineering]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Schedules over the course of training [[02 Concepts/Lifecycle/Data Engineering/Data Mixture|Data Mixture]]. **Condition:** When the curriculum changes source proportions between training phases.

- Raises sequence length late in pretraining to support [[02 Concepts/Foundations/Models & Architectures/Context Length Extension|Context Length Extension]]. **Condition:** When positional handling supports the longer lengths and evaluation verifies useful behavior at them.

- Structures the data schedule of [[02 Concepts/Lifecycle/Training & Adaptation/Pretraining|Pretraining]]. **Condition:** When pretraining runs in phases with different data distributions.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: curriculum learning; data annealing; sequence-length warmup.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
