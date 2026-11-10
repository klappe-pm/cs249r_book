---
title: V2-17 Conclusion
type: Chapter
volume: 2
chapter: 17
publication_status: Preview
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol2/17_conclusion/17_conclusion.qmd
source_anchor: sec-conclusion
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_2
rendered_source_url: https://mlsysbook.ai/vol2/17_conclusion/17_conclusion.html
---

# V2-17 Conclusion

[[Home|Home]] · [[01 Books/Volume II - Scaling/Volume 2 Overview|Volume Overview]]

^sec-conclusion

[Lecture slides](https://mlsysbook.ai/slides/vol2.html#ch-17) for this chapter

![[90 Assets/Volume II/17 Conclusion/Cover Conclusion Blueprint Labeled ee5d5586f6.webp]]

*Blueprint-style fleet-scale ML systems map with labeled areas for infrastructure, fabric, storage, distributed training, serving, operations, security, sustainability, and governance.*

## Chapter Sections

- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/17 Conclusion/V2-17.01 Purpose|V2-17.01 Purpose]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/17 Conclusion/V2-17.02 Distilling Distributed ML Systems|V2-17.02 Distilling Distributed ML Systems]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/17 Conclusion/V2-17.03 Six Principles of Distributed ML Systems|V2-17.03 Six Principles of Distributed ML Systems]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/17 Conclusion/V2-17.04 The Complete Production System|V2-17.04 The Complete Production System]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/17 Conclusion/V2-17.05 Competencies Mastered|V2-17.05 Competencies Mastered]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/17 Conclusion/V2-17.06 Where the Binding Constraint Moves Next|V2-17.06 Where the Binding Constraint Moves Next]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/17 Conclusion/V2-17.07 Fallacies and Pitfalls|V2-17.07 Fallacies and Pitfalls]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/17 Conclusion/V2-17.08 Summary|V2-17.08 Summary]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/17 Conclusion/V2-17.09 Self-Check Answers|V2-17.09 Self-Check Answers]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/17 Conclusion/V2-17.10 Source References|V2-17.10 Source References]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/17 Conclusion/V2-17.11 Footnotes|V2-17.11 Footnotes]]

Next: [[01 Books/Volume II - Scaling/04 The Responsible Fleet/17 Conclusion/V2-17.01 Purpose|V2-17.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/17_conclusion/17_conclusion.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol2/17_conclusion/17_conclusion.html#sec-conclusion). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume II - Scaling/00 Introduction/01 Introduction/V2-01 Introduction|V2-01 Introduction]] — Scale moment; Scaling laws as the demand curve; C3 taxonomy; Fleet Law; Fleet stack; Reliability gap; Communication intensity; Energy accounting boundary.
- [[01 Books/Volume II - Scaling/01 The Fleet/02 Compute Infrastructure/V2-02 Compute Infrastructure|V2-02 Compute Infrastructure]] — Rack power wall.
- [[01 Books/Volume II - Scaling/01 The Fleet/03 Network Fabrics/V2-03 Network Fabrics|V2-03 Network Fabrics]] — Bisection bandwidth and topology economics; Alpha-beta model.
- [[01 Books/Volume II - Scaling/01 The Fleet/04 Data Storage/V2-04 Data Storage|V2-04 Data Storage]] — I/O wall.
- [[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05 Collective Communication|V2-05 Collective Communication]] — Ring AllReduce and the bandwidth bound; Exposed communication under overlap; Gradient compression with error feedback.
- [[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06 Distributed Training|V2-06 Distributed Training]] — Scaling efficiency and the scaling wall; Parallelism plan as joint placement; Synchronization models and stragglers.
- [[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07 Fault Tolerance|V2-07 Fault Tolerance]] — Fleet failure rate; Young-Daly checkpoint interval; Elastic recovery invariants; Graceful degradation ladder.
- [[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08 Fleet Orchestration|V2-08 Fleet Orchestration]] — Gang scheduling; Feasibility before fairness; Topology-aware placement.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/09 Fleet Efficiency/V2-09 Fleet Efficiency|V2-09 Fleet Efficiency]] — Program goodput; ML goodput; Runtime goodput.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10 Serving at Scale|V2-10 Serving at Scale]] — Per-request compute budget; Prefill-decode interference and chunked prefill; Serving cost dominance; SLO goodput and the serving tax; State-aware request routing.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/11 Edge Intelligence/V2-11 Edge Intelligence|V2-11 Edge Intelligence]] — Background adaptation admission; Participation selection; Secure aggregation.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/12 ML Operations at Scale/V2-12 ML Operations at Scale|V2-12 ML Operations at Scale]] — Staged rollout exposure budget; Evaluation contract; SLO vector of budgets.
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/13 Security & Privacy/V2-13 Security & Privacy|V2-13 Security & Privacy]] — Leakage through authorized outputs; Privacy budget account; Provenance bounds trust.
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/14 Robust AI/V2-14 Robust AI|V2-14 Robust AI]] — Adversarial robustness for a named threat model; Shift taxonomy.
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/15 Sustainable AI/V2-15 Sustainable AI|V2-15 Sustainable AI]] — Operational carbon chain; Demand outruns efficiency; Carbon-aware placement and time-shifting.
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/16 Responsible AI/V2-16 Responsible AI|V2-16 Responsible AI]] — Fairness criteria conflict; Sociotechnical feedback and designed oversight.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/17_conclusion/conclusion_concepts.yml)

<!-- Semantic Navigation: End -->
