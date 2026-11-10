---
title: V3-09 Agent Security
type: Chapter
volume: 3
chapter: 9
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol3/09_security/09_security.qmd
source_anchor: sec-vol3-security
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_3
rendered_source_url: https://mlsysbook.ai/vol3/09_security/09_security.html
---

# V3-09 Agent Security

[[Home|Home]] · [[01 Books/Volume III - Agentic Systems/Volume 3 Overview|Volume Overview]]

^sec-vol3-security

[Lecture slides](https://mlsysbook.ai/slides/vol3.html#ch-09) for this chapter

![[90 Assets/Volume III/09 Security/Cover Security Blueprint Labeled b5e201ff16.webp]]

*Blueprint for Agent Security.*

## Chapter Sections

- [[01 Books/Volume III - Agentic Systems/03 Tool Use/09 Agent Security/V3-09.01 Purpose|V3-09.01 Purpose]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/09 Agent Security/V3-09.02 Attacks Through Permitted Operations|V3-09.02 Attacks Through Permitted Operations]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/09 Agent Security/V3-09.03 The Adversarial Threat Model|V3-09.03 The Adversarial Threat Model]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/09 Agent Security/V3-09.04 The Confused Deputy and Task-Scoped Authority|V3-09.04 The Confused Deputy and Task-Scoped Authority]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/09 Agent Security/V3-09.05 Disclosure Through Permitted Tools|V3-09.05 Disclosure Through Permitted Tools]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/09 Agent Security/V3-09.06 Quarantined Readers and Ingestion Isolation|V3-09.06 Quarantined Readers and Ingestion Isolation]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/09 Agent Security/V3-09.07 Information-Flow Policy|V3-09.07 Information-Flow Policy]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/09 Agent Security/V3-09.08 Delegated Identity and Credential Brokering|V3-09.08 Delegated Identity and Credential Brokering]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/09 Agent Security/V3-09.09 Multi-Turn Attacks and State Persistence|V3-09.09 Multi-Turn Attacks and State Persistence]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/09 Agent Security/V3-09.10 Adversarial Robustness and Red-Teaming|V3-09.10 Adversarial Robustness and Red-Teaming]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/09 Agent Security/V3-09.11 Fallacies and Pitfalls|V3-09.11 Fallacies and Pitfalls]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/09 Agent Security/V3-09.12 Summary|V3-09.12 Summary]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/09 Agent Security/V3-09.13 Historical Perspective and Further Reading|V3-09.13 Historical Perspective and Further Reading]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/09 Agent Security/V3-09.14 Exercises|V3-09.14 Exercises]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/09 Agent Security/V3-09.15 Source References|V3-09.15 Source References]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/09 Agent Security/V3-09.16 Footnotes|V3-09.16 Footnotes]]

Next: [[01 Books/Volume III - Agentic Systems/03 Tool Use/09 Agent Security/V3-09.01 Purpose|V3-09.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/09_security/09_security.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol3/09_security/09_security.html#sec-vol3-security). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/System Types/Agentic Systems/Action Approval Gate|Action Approval Gate]]
- [[02 Concepts/Qualities/Security & Privacy/Information Flow Control|Information Flow Control]]
- [[02 Concepts/Qualities/Security & Privacy/Prompt Injection|Prompt Injection]]

## Related Themes

- [[03 Themes/Security and Trust|Security and Trust]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume III - Agentic Systems/00 Introduction/01 Introduction/V3-01 Introduction|V3-01 Introduction]] — Side-effect classes; Invariant closure; Horizon compounding; Cost per accepted task; Lighthouse workloads.
- [[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02 The Foundation Model|V3-02 The Foundation Model]] — Grammar-constrained decoding; Invocation contract.
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04 Context Engineering|V3-04 Context Engineering]] — Context compaction.
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05 KV Cache Management|V3-05 KV Cache Management]] — KV footprint and resident fit; Radix prefix cache.
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/06 Long-Term Memory/V3-06 Long-Term Memory|V3-06 Long-Term Memory]] — Record roles; Memory poisoning; Memory write policy.
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07 Tool Calling|V3-07 Tool Calling]] — Confused deputy; Complete mediation; Discovery is not authority; Bounded observation; Operation identity.
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08 Agent Sandboxes|V3-08 Agent Sandboxes]] — Containment beneath the model; Attenuation and revocation; Egress control; Least privilege; Credential brokering.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/09_security/security_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10 The Agent Harness|V3-10 The Agent Harness]] — Approval escrow; Harness owns continuation.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12 Failure Recovery|V3-12 Failure Recovery]] — Compensation.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13 Agent Evaluation|V3-13 Agent Evaluation]] — Task sampling and score intervals.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/09_security/security_concepts.yml)

<!-- Semantic Navigation: End -->
