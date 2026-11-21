---
title: Action Approval Gate
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Agent_Harness_Control_Loop
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Action approval gate
taxonomy_id: mlsys.approval-gate
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Action Approval Gate

A harness checkpoint that holds a specific proposed action until an authorized human or policy approves it, binding the approval to that exact action.

## Browsing Home

[[02 Concepts/System Types/Agentic Systems/Agent Harness & Control Loop Subject|Agent Harness & Control Loop]] → [[02 Concepts/System Types/Agentic Systems/Agentic Systems Index|Agentic Systems]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume III - Agentic Systems/03 Tool Use/09 Agent Security/V3-09.08 Delegated Identity and Credential Brokering#^sec-vol3-security-action-bound-approval|V3-09.08 Delegated Identity and Credential Brokering]] — Action-bound approval. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/09_security/09_security.qmd#L684).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Implements [[02 Concepts/Qualities/Responsible AI/Human Oversight|Human Oversight]]. **Condition:** Effective only if approvals bind to the exact action and reviewers can judge it; see automation bias.

- Guards against [[02 Concepts/Qualities/Reliability & Fault Tolerance/Irreversible Effects|Irreversible Effects]]. **Condition:** Holds when the gate is placed before dispatch of actions classified irreversible.

- Records approvals as [[02 Concepts/Qualities/Responsible AI/Decision Accountability Record|Decision Accountability Record]]. **Condition:** Each approval is logged with approver identity.

- Is the undispatched hold within [[02 Concepts/System Types/Agentic Systems/Agent Harness|Agent Harness]]. **Condition:** When the harness holds the proposed action, bound by digest and expiry, until an authorized decision, and re-runs admission after approval.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: human-in-the-loop approval.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
