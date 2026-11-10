---
title: Statistical Power
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Evaluation_Design_Experiments
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Statistical power
taxonomy_id: mlsys.statistical-power
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Statistical Power

The probability that an experiment detects an effect of a stated size, fixed by sample size, outcome variance, and the significance level, which decides how much traffic or how many evaluation items a comparison needs before its answer can be trusted.

## Browsing Home

[[02 Concepts/Lifecycle/Model Evaluation & Testing/Evaluation Design & Experiments Subject|Evaluation Design & Experiments]] → [[02 Concepts/Lifecycle/Model Evaluation & Testing/Model Evaluation & Testing Index|Model Evaluation & Testing]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Sets the traffic share and duration required by [[02 Concepts/Lifecycle/Model Evaluation & Testing/Online Experimentation|Online Experimentation]]. **Condition:** When the launch decision must detect an effect of a stated minimum size at stated error rates; metric variance and the number of independent units fix the answer.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: power analysis; sample size calculation; sample size.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
