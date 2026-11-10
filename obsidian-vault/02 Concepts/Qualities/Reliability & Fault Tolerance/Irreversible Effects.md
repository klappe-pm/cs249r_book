---
title: Irreversible Effects
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Failure_Models_Retries_Degradation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Irreversible effects
taxonomy_id: mlsys.irreversible-effects
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Irreversible Effects

External consequences that cannot be fully undone by restoring software state, retrying, or performing a compensating action.

## Browsing Home

[[02 Concepts/Qualities/Reliability & Fault Tolerance/Failure Models, Retries & Degradation Subject|Failure Models, Retries & Degradation]] → [[02 Concepts/Qualities/Reliability & Fault Tolerance/Reliability & Fault Tolerance Index|Reliability & Fault Tolerance]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume IV - Physical AI/00 Introduction/01 The Causal Boundary/V4-01.05 Defining the Causal Boundary#^sec-boundary-thermodynamic-irreversibility|V4-01.05 Defining the Causal Boundary]] — Irreversibility. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/01_boundary/01_boundary.qmd#L665).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Can prevent full reversal by [[02 Concepts/Lifecycle/MLOps & Operations/Rollback|Rollback]]. **Condition:** Restoring software or configuration cannot necessarily undo physical, informational, financial, or human consequences already caused.

- Can remain after [[02 Concepts/Qualities/Reliability & Fault Tolerance/Compensating Action|Compensating Action]]. **Condition:** A remedy may address an obligation or consequence without restoring the original world state.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
