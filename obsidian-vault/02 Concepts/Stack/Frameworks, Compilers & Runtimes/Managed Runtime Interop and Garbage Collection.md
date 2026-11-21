---
title: Managed Runtime Interop and Garbage Collection
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Runtime_Execution_Dispatch
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Managed-runtime interop and garbage collection
taxonomy_id: mlsys.managed-runtime-interop
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Managed Runtime Interop and Garbage Collection

Crossing between a managed language runtime (Java, Kotlin, Swift, C#) and native inference code, where buffer copies, object pinning, and garbage-collection pauses add latency and memory.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Runtime Execution & Dispatch Subject|Runtime Execution & Dispatch]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Adds copy and pause overhead to [[02 Concepts/Lifecycle/Deployment & Serving/On Device Inference Runtime|On Device Inference Runtime]]. **Condition:** The app calls native inference from a managed language.

- Adds garbage-collection pauses to [[02 Concepts/Lifecycle/Deployment & Serving/Tail Latency|Tail Latency]]. **Condition:** Large buffers are allocated on the managed heap per request.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: JNI overhead; GC pauses; native interop.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
