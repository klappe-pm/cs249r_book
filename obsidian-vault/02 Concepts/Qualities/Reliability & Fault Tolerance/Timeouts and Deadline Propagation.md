---
title: Timeouts and Deadline Propagation
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Failure_Models_Retries_Degradation
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Timeouts and deadline propagation
taxonomy_id: mlsys.request-timeout
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Timeouts and Deadline Propagation

A caller's time limit propagated to dependencies so they can stop work after the remaining budget expires, bounding caller wait and reducing abandoned work when cancellation is enforced.

## Browsing Home

[[02 Concepts/Qualities/Reliability & Fault Tolerance/Failure Models, Retries & Degradation Subject|Failure Models, Retries & Degradation]] → [[02 Concepts/Qualities/Reliability & Fault Tolerance/Reliability & Fault Tolerance Index|Reliability & Fault Tolerance]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Cancels abandoned work that would otherwise sustain [[02 Concepts/Qualities/Reliability & Fault Tolerance/Metastable Failure|Metastable Failure]]. **Condition:** When deadlines are propagated so downstream services stop serving requests the client no longer waits for.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: request deadline; deadline propagation; timeout budget.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
