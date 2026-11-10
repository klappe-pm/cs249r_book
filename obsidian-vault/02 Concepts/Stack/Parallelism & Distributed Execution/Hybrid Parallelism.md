---
title: Hybrid Parallelism
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Parallelism_Strategies
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Hybrid parallelism
taxonomy_id: mlsys.hybrid-parallel
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Hybrid Parallelism

Combining data, tensor, pipeline, and other parallelism dimensions, mapped onto the hardware hierarchy so the most communication-intensive dimension uses the fastest links.

## Browsing Home

[[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism Strategies Subject|Parallelism Strategies]] → [[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism & Distributed Execution Index|Parallelism & Distributed Execution]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Assigns parallel dimensions to the axes of [[02 Concepts/Stack/Parallelism & Distributed Execution/Device Mesh|Device Mesh]]. **Condition:** Each parallelism dimension corresponds to a named mesh axis.

- Sets, per parallelism dimension, the [[02 Concepts/Foundations/Quantitative System Models/Communication to Computation Ratio|Communication to Computation Ratio]]. **Condition:** When the parallel plan fixes which tensors cross which links on each step.

## Themes

- [[03 Themes/Scaling and Coordination|Scaling and Coordination]]

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: 3D parallelism.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
