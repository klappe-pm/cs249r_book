---
title: Cross Stack Profiling
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Profiling_Utilization
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Cross-stack profiling
taxonomy_id: mlsys.cross-stack-profiling
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Cross Stack Profiling

Profiling that correlates timestamped events and calling contexts from model code, frameworks, native libraries, and accelerator kernels, so that device time and stalls can be attributed to the operations that launched them.

## Browsing Home

[[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Profiling & Utilization Subject|Profiling & Utilization]] → [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Performance, Efficiency & Benchmarking Index|Performance, Efficiency & Benchmarking]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.04 Request Lifecycle#^sec-model-serving-serving-tax-bill-dc6c|V1-13.04 Request Lifecycle]] — Host-path overhead. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/13_model_serving/13_model_serving.qmd#L1728).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is the cross-layer form of [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Profiling|Profiling]]. **Condition:** When the profiler records events at more than one software layer and can link each device event to the host call that issued it.

- Exposes host-side gaps between device kernels caused by [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Host Dispatch Overhead|Host Dispatch Overhead]]. **Condition:** When host and device events share a clock or are aligned by correlation identifiers.

- Attributes device idle gaps to the host-side stages of [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Training Input Pipeline|Training Input Pipeline]]. **Condition:** Host and device timelines are correlated on one clock.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: framework-to-kernel attribution; host-device trace correlation.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
