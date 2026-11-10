---
title: Sources of Bias in the Pipeline
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Fairness_Bias
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Sources of bias in the pipeline
taxonomy_id: mlsys.bias-sources
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Sources of Bias in the Pipeline

The distinct points at which disparity enters an ML system, from the world the data records, who is sampled, how labels and features are measured, pooling heterogeneous groups into one model, an unrepresentative evaluation set, and use outside the intended context, each of which calls for a different remedy.

## Browsing Home

[[02 Concepts/Qualities/Responsible AI/Fairness & Bias Subject|Fairness & Bias]] → [[02 Concepts/Qualities/Responsible AI/Responsible AI Index|Responsible AI]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Selects which stage of intervention is appropriate in [[02 Concepts/Qualities/Responsible AI/Bias Mitigation|Bias Mitigation]]. **Condition:** When the dominant source is identified, since reweighting cannot fix a measurement problem and a constraint cannot fix a deployment mismatch.

- Can produce, through correlated features, [[02 Concepts/Qualities/Responsible AI/Proxy Discrimination|Proxy Discrimination]]. **Condition:** When historical or measurement bias is encoded in features correlated with protected attributes and those features drive decisions.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: historical bias; representation bias; measurement bias; aggregation bias; evaluation bias; deployment bias.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
