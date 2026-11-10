---
title: Network Egress Control
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Access_Control_Isolation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Network egress control
taxonomy_id: mlsys.egress-control
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Network Egress Control

Restricting which external network destinations a workload or sandbox may contact, typically through default-deny allowlists, to block exfiltration and unintended remote actions.

## Browsing Home

[[02 Concepts/Qualities/Security & Privacy/Access Control & Isolation Subject|Access Control & Isolation]] → [[02 Concepts/Qualities/Security & Privacy/Security & Privacy Index|Security & Privacy]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08.08 Egress Control#^sec-vol3-sandboxes-egress-enforcement|V3-08.08 Egress Control]] — Egress control. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/08_sandboxes/08_sandboxes.qmd#L859).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Applies to network access [[02 Concepts/Qualities/Security & Privacy/Least Privilege|Least Privilege]]. **Condition:** Only destinations the task needs are allowed.

- Blocks exfiltration channels for [[02 Concepts/Qualities/Security & Privacy/Privacy Leakage|Privacy Leakage]]. **Condition:** Leakage would otherwise travel over outbound connections.

- Blocks the outbound channels used for [[02 Concepts/Qualities/Security & Privacy/Model Weight Theft|Model Weight Theft]]. **Condition:** When weights can leave only through network paths the allowlist controls.

- Removes the exfiltration channel exploited by [[02 Concepts/Qualities/Security & Privacy/Prompt Injection|Prompt Injection]]. **Condition:** Allow-listed destinations; injected instructions can still act within the sandbox.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: egress filtering; outbound allowlist.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
