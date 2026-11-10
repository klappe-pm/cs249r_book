---
title: Failure Injection
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Fault_Injection_Resilience_Testing
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Failure injection
taxonomy_id: mlsys.failure-injection
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Failure Injection

Deliberately introducing selected faults or disruptive conditions to observe system response under controlled experimental boundaries.

## Browsing Home

[[02 Concepts/Qualities/Reliability & Fault Tolerance/Fault Injection & Resilience Testing Subject|Fault Injection & Resilience Testing]] → [[02 Concepts/Qualities/Reliability & Fault Tolerance/Reliability & Fault Tolerance Index|Reliability & Fault Tolerance]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/15 Adversarial Verification/V4-15.02 The Claim a Fault Trial Must Test#^sec-verification-fault-injection|V4-15.02 The Claim a Fault Trial Must Test]] — Fault injection. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/15_verification/15_verification.qmd#L64).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Exercises [[02 Concepts/Lifecycle/MLOps & Operations/Incident Response|Incident Response]]. **Condition:** A controlled scenario can test detection and response paths; success does not demonstrate preparedness for every incident.

- Requires observable acceptance criteria from [[02 Concepts/Lifecycle/Model Evaluation & Testing/Test Oracle|Test Oracle]]. **Condition:** Criteria may evaluate latency, error rates, recovery behavior, or invariants; injecting a fault without assessing outcomes is not sufficient evidence.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
