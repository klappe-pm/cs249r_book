---
title: CPU Threading and NUMA Placement
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Runtime_Execution_Dispatch
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: CPU threading and NUMA placement
taxonomy_id: mlsys.cpu-threading-numa
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# CPU Threading and NUMA Placement

Configuring thread pools, core affinity, and memory placement across NUMA domains so CPU operators parallelize without oversubscription or remote-memory penalties.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Runtime Execution & Dispatch Subject|Runtime Execution & Dispatch]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Maps operator work onto the cores and caches of [[02 Concepts/Stack/Hardware & Accelerators/CPU Execution Architecture|CPU Execution Architecture]]. **Condition:** Inference or preprocessing runs on multicore hosts.

- Sets achieved core utilization through [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Resource Utilization|Resource Utilization]]. **Condition:** Thread counts and affinity are configured relative to available cores and NUMA domains.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: thread affinity; intra-op and inter-op threads; NUMA-aware execution.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
