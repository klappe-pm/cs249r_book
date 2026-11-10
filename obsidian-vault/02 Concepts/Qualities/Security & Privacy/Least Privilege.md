---
title: Least Privilege
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Access_Control_Isolation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Least privilege
taxonomy_id: mlsys.least-privilege
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Least Privilege

Granting each component or actor only the permissions its task requires, for only as long as it requires them.

## Browsing Home

[[02 Concepts/Qualities/Security & Privacy/Access Control & Isolation Subject|Access Control & Isolation]] → [[02 Concepts/Qualities/Security & Privacy/Security & Privacy Index|Security & Privacy]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Constrains grants made by [[02 Concepts/Qualities/Security & Privacy/Authorization|Authorization]]. **Condition:** When permissions are scoped to the task and expire or are revoked when the task ends.

- Limits the consequences of [[02 Concepts/Qualities/Security & Privacy/Prompt Injection|Prompt Injection]]. **Condition:** When a model-driven component processes untrusted content and can act only through narrowly scoped credentials and tools.

- Reduces [[02 Concepts/Qualities/Reliability & Fault Tolerance/Blast Radius|Blast Radius]]. **Condition:** When a compromised or faulty component holds only the permissions its task requires.

## Themes

- [[03 Themes/Security and Trust|Security and Trust]]

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
