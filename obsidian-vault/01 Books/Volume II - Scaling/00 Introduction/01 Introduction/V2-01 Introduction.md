---
title: V2-01 Introduction
type: Chapter
volume: 2
chapter: 1
publication_status: Preview
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol2/01_introduction/01_introduction.qmd
source_anchor: sec-vol2-introduction
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_2
rendered_source_url: https://mlsysbook.ai/vol2/01_introduction/01_introduction.html
---

# V2-01 Introduction

[[Home|Home]] · [[01 Books/Volume II - Scaling/Volume 2 Overview|Volume Overview]]

^sec-vol2-introduction

[Lecture slides](https://mlsysbook.ai/slides/vol2.html#ch-01) for this chapter

![[90 Assets/Volume II/01 Introduction/Cover Introduction Blueprint Labeled 541f9963f4.webp]]

*Isometric fleet-scale blueprint showing a single ML system expanding into racks, network fabric, coordination layers, scaling constraints, and failure domains.*

## Chapter Sections

- [[01 Books/Volume II - Scaling/00 Introduction/01 Introduction/V2-01.01 Purpose|V2-01.01 Purpose]]
- [[01 Books/Volume II - Scaling/00 Introduction/01 Introduction/V2-01.02 The Scale Moment|V2-01.02 The Scale Moment]]
- [[01 Books/Volume II - Scaling/00 Introduction/01 Introduction/V2-01.03 From Single Node to Fleet|V2-01.03 From Single Node to Fleet]]
- [[01 Books/Volume II - Scaling/00 Introduction/01 Introduction/V2-01.04 AI Scaling Laws|V2-01.04 AI Scaling Laws]]
- [[01 Books/Volume II - Scaling/00 Introduction/01 Introduction/V2-01.05 Constraints of Scale|V2-01.05 Constraints of Scale]]
- [[01 Books/Volume II - Scaling/00 Introduction/01 Introduction/V2-01.06 The C³ Taxonomy and Foundations of Scale|V2-01.06 The C³ Taxonomy and Foundations of Scale]]
- [[01 Books/Volume II - Scaling/00 Introduction/01 Introduction/V2-01.07 The Fleet Stack and the Lighthouse Archetypes|V2-01.07 The Fleet Stack and the Lighthouse Archetypes]]
- [[01 Books/Volume II - Scaling/00 Introduction/01 Introduction/V2-01.08 The Structure of This Textbook|V2-01.08 The Structure of This Textbook]]
- [[01 Books/Volume II - Scaling/00 Introduction/01 Introduction/V2-01.09 Fallacies and Pitfalls|V2-01.09 Fallacies and Pitfalls]]
- [[01 Books/Volume II - Scaling/00 Introduction/01 Introduction/V2-01.10 Summary|V2-01.10 Summary]]
- [[01 Books/Volume II - Scaling/00 Introduction/01 Introduction/V2-01.11 Self-Check Answers|V2-01.11 Self-Check Answers]]
- [[01 Books/Volume II - Scaling/00 Introduction/01 Introduction/V2-01.12 Source References|V2-01.12 Source References]]
- [[01 Books/Volume II - Scaling/00 Introduction/01 Introduction/V2-01.13 Footnotes|V2-01.13 Footnotes]]

Next: [[01 Books/Volume II - Scaling/00 Introduction/01 Introduction/V2-01.01 Purpose|V2-01.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/01_introduction/01_introduction.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol2/01_introduction/01_introduction.html#sec-vol2-introduction). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Foundations/Quantitative System Models/Empirical Scaling Laws|Empirical Scaling Laws]]
- [[02 Concepts/Foundations/Quantitative System Models/Parallel Scaling Efficiency|Parallel Scaling Efficiency]]

## Related Themes

- [[03 Themes/Scaling and Coordination|Scaling and Coordination]]

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume II - Scaling/01 The Fleet/02 Compute Infrastructure/V2-02 Compute Infrastructure|V2-02 Compute Infrastructure]] — Bandwidth hierarchy dictates placement; Rack power wall.
- [[01 Books/Volume II - Scaling/01 The Fleet/03 Network Fabrics/V2-03 Network Fabrics|V2-03 Network Fabrics]] — Alpha-beta model.
- [[01 Books/Volume II - Scaling/01 The Fleet/04 Data Storage/V2-04 Data Storage|V2-04 Data Storage]] — Input delivery budget.
- [[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05 Collective Communication|V2-05 Collective Communication]] — Ring AllReduce and the bandwidth bound.
- [[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06 Distributed Training|V2-06 Distributed Training]] — Parallelism plan as joint placement; Sparse embedding sharding; Scaling efficiency and the scaling wall; Alignment training co-location.
- [[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07 Fault Tolerance|V2-07 Fault Tolerance]] — Fleet failure rate; Young-Daly checkpoint interval; Silent data corruption verification.
- [[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08 Fleet Orchestration|V2-08 Fleet Orchestration]] — Gang scheduling.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/09 Fleet Efficiency/V2-09 Fleet Efficiency|V2-09 Fleet Efficiency]] — Program goodput; ML goodput.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10 Serving at Scale|V2-10 Serving at Scale]] — Per-request compute budget.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/11 Edge Intelligence/V2-11 Edge Intelligence|V2-11 Edge Intelligence]] — Local training must earn its place.
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/13 Security & Privacy/V2-13 Security & Privacy|V2-13 Security & Privacy]] — Extraction budgets; Poisoning as a bilevel attack; Differential privacy.
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/14 Robust AI/V2-14 Robust AI|V2-14 Robust AI]] — Shift taxonomy.
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/15 Sustainable AI/V2-15 Sustainable AI|V2-15 Sustainable AI]] — Operational carbon chain.
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/16 Responsible AI/V2-16 Responsible AI|V2-16 Responsible AI]] — Assurance case.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/01_introduction/introduction_concepts.yml)

<!-- Semantic Navigation: End -->
