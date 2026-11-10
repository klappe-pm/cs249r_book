---
title: Stopping Envelope
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Runtime_Assurance_Safety_Filters
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Stopping envelope
taxonomy_id: mlsys.stopping-envelope
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Stopping Envelope

The state and clearance conditions within which a specified stopping response remains feasible.

## Browsing Home

[[02 Concepts/Qualities/Safety & Assurance/Runtime Assurance & Safety Filters Subject|Runtime Assurance & Safety Filters]] → [[02 Concepts/Qualities/Safety & Assurance/Safety & Assurance Index|Safety & Assurance]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12.04 Stopping Envelopes#^sec-enforcement-stopping-envelopes|V4-12.04 Stopping Envelopes]] — Stopping envelope. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/12_enforcement/12_enforcement.qmd#L248).

- [[01 Books/Volume IV - Physical AI/00 Introduction/01 The Causal Boundary/V4-01.05 Defining the Causal Boundary#^sec-boundary-kinematic-roofline|V4-01.05 Defining the Causal Boundary]] — Stopping distance. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/01_boundary/01_boundary.qmd#L401).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Bounds reachability of [[02 Concepts/Qualities/Safety & Assurance/Minimal Risk Condition|Minimal Risk Condition]]. **Condition:** A stop-type fallback is feasible only while the state remains inside its stopping envelope.

- Is defined from forward reachable sets computed by [[02 Concepts/Qualities/Safety & Assurance/Reachability Analysis|Reachability Analysis]]. **Condition:** When the envelope is the set of states from which a stopping maneuver stays clear of everything reachable by others.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: safe stopping region.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
