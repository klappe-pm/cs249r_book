---
title: Data Protection Regulation
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/AI_Governance_Audit_Regulation
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Data protection regulation
taxonomy_id: mlsys.data-protection-regulation
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Data Protection Regulation

Law governing the collection, use, retention, and automated use of personal data, which imposes obligations such as consent, purpose limitation, deletion, impact assessment, and rights over automated decisions that an ML system must implement in its data pipeline, models, and decision flow.

## Browsing Home

[[02 Concepts/Qualities/Responsible AI/AI Governance, Audit & Regulation Subject|AI Governance, Audit & Regulation]] → [[02 Concepts/Qualities/Responsible AI/Responsible AI Index|Responsible AI]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Mandates a lawful basis and purpose limitation enforced through [[02 Concepts/Lifecycle/Data Engineering/Consent and Purpose Limitation|Consent and Purpose Limitation]]. **Condition:** When personal data of covered people is processed for training or inference.

- Creates erasure obligations fulfilled by [[02 Concepts/Lifecycle/MLOps & Operations/Data Deletion Propagation|Data Deletion Propagation]]. **Condition:** When a legally effective erasure obligation covers the retained personal data and its derived copies.

- Sets the legal floor for [[02 Concepts/Qualities/Security & Privacy/Privacy Requirements|Privacy Requirements]]. **Condition:** Within the jurisdictions whose law applies to the people in the data.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: GDPR; CCPA; privacy law.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
