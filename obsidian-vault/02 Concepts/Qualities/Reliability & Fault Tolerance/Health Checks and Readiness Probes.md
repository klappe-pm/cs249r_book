---
title: Health Checks and Readiness Probes
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Failure_Models_Retries_Degradation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Health checks and readiness probes
taxonomy_id: mlsys.health-checks
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Health Checks and Readiness Probes

Periodic liveness and readiness checks that let an orchestrator or load balancer stop routing traffic to, or restart, a replica that is unhealthy or still loading its model.

## Browsing Home

[[02 Concepts/Qualities/Reliability & Fault Tolerance/Failure Models, Retries & Degradation Subject|Failure Models, Retries & Degradation]] → [[02 Concepts/Qualities/Reliability & Fault Tolerance/Reliability & Fault Tolerance Index|Reliability & Fault Tolerance]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Tells which replicas may receive traffic from [[02 Concepts/Lifecycle/Deployment & Serving/Request Load Balancing|Request Load Balancing]]. **Condition:** Replicas can be unhealthy or still loading weights.

- Keeps traffic away from replicas in [[02 Concepts/Lifecycle/Deployment & Serving/Model Cold Start|Model Cold Start]]. **Condition:** A replica reports ready only after its model is loaded and warmed.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: readiness probe; liveness probe; health endpoint.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
