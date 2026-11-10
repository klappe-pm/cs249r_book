---
title: AI Bill of Materials
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Model_Supply_Chain_Security
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: AI bill of materials
taxonomy_id: mlsys.ai-bill-of-materials
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# AI Bill of Materials

An inventory of the datasets, base weights, libraries, and build steps that produced a model, with versions and hashes, so consumers can check every component against vulnerability and trust lists before depending on the model.

## Browsing Home

[[02 Concepts/Qualities/Security & Privacy/Model & Supply Chain Security Subject|Model & Supply Chain Security]] → [[02 Concepts/Qualities/Security & Privacy/Security & Privacy Index|Security & Privacy]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Lets consumers find known-bad components behind [[02 Concepts/Qualities/Security & Privacy/ML Supply Chain Compromise|ML Supply Chain Compromise]]. **Condition:** When the manifest is complete and machine-readable and components flagged against advisories are rejected, replaced, or contained; the inventory alone reveals but does not prevent a compromise.

- Is compiled from [[02 Concepts/Lifecycle/Data Engineering/Data Lineage|Data Lineage]]. **Condition:** When data lineage records the sources and transformations the manifest lists.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: AIBOM; ML-BOM; SBOM for ML; model provenance manifest.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
