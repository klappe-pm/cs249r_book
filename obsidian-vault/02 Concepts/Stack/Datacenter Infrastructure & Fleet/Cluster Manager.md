---
title: Cluster Manager
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Cluster_Scheduling_Orchestration
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Cluster manager
taxonomy_id: mlsys.cluster-manager
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Cluster Manager

The control plane that admits jobs, places their tasks on machines, enforces quotas and priorities, and reconciles running state toward declared intent across a cluster.

## Browsing Home

[[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Cluster Scheduling & Orchestration Subject|Cluster Scheduling & Orchestration]] → [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Infrastructure & Fleet Index|Datacenter Infrastructure & Fleet]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Places tasks with [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Bin Packing|Bin Packing]]. **Condition:** Machines have multidimensional resource capacity.

- Enforces [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Resource Quota|Resource Quota]]. **Condition:** Multiple teams share the cluster.

- Honors priorities through [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Job Preemption|Job Preemption]]. **Condition:** Higher-priority work arrives while capacity is full.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: cluster orchestrator; cluster control plane; Kubernetes.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
