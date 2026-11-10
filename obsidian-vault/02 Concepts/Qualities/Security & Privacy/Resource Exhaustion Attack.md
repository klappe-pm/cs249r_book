---
title: Resource Exhaustion Attack
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Threat_Models_Adversarial_Attacks
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Resource-exhaustion attack
taxonomy_id: mlsys.resource-exhaustion-attack
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Resource Exhaustion Attack

Crafting inputs that maximize a model service's compute, energy, output length, or tool calls, degrading service for other users or running up the operator's cost.

## Browsing Home

[[02 Concepts/Qualities/Security & Privacy/Threat Models & Adversarial Attacks Subject|Threat Models & Adversarial Attacks]] → [[02 Concepts/Qualities/Security & Privacy/Security & Privacy Index|Security & Privacy]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Inflates [[02 Concepts/Qualities/Sustainability & Cost/Energy per Inference|Energy per Inference]]. **Condition:** When inputs are chosen to defeat sparsity, early exit, or bounded output length.

- Takes completed useful work away from [[02 Concepts/Lifecycle/Deployment & Serving/SLO Goodput|SLO Goodput]]. **Condition:** When attacker-amplified requests contend for shared compute, KV-cache memory, or tool-execution slots.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: sponge examples; denial of wallet; model denial of service; unbounded consumption; reasoning slowdown attack.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
