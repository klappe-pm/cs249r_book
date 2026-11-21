---
title: Data Locality
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Roofline_Performance_Models_Simulation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Data locality
taxonomy_id: mlsys.locality
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Data Locality

Reuse of data near its consumers across time or execution locations.

## Browsing Home

[[02 Concepts/Foundations/Quantitative System Models/Roofline, Performance Models & Simulation Subject|Roofline, Performance Models & Simulation]] → [[02 Concepts/Foundations/Quantitative System Models/Quantitative System Models Index|Quantitative System Models]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/01 Foundations/02 System Paradigms/V1-02.07 Edge ML Latency and Privacy#^sec-ml-systems-data-locality-invariant|V1-02.07 Edge ML Latency and Privacy]] — Data locality. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/02_system_paradigms/02_system_paradigms.qmd#L2331).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Can increase [[02 Concepts/Foundations/Quantitative System Models/Arithmetic Intensity|Arithmetic Intensity]]. **Condition:** When reuse reduces transfers across the measured memory boundary.

- Reduces [[02 Concepts/Foundations/Quantitative System Models/Data Movement Energy|Data Movement Energy]]. **Condition:** Reused data is served from nearer, lower-energy storage levels.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: temporal locality; spatial locality; data reuse.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
