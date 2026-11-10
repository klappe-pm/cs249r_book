---
title: Error Correcting Code Memory
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Hardware_Faults_Silent_Data_Corruption
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Error-correcting code memory
taxonomy_id: mlsys.ecc-memory
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Error Correcting Code Memory

Memory protected by redundant check bits that correct supported error patterns and report detectable uncorrectable errors, reducing the risk of silent corruption.

## Browsing Home

[[02 Concepts/Qualities/Reliability & Fault Tolerance/Hardware Faults & Silent Data Corruption Subject|Hardware Faults & Silent Data Corruption]] → [[02 Concepts/Qualities/Reliability & Fault Tolerance/Reliability & Fault Tolerance Index|Reliability & Fault Tolerance]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Turns many would-be silent memory corruptions into corrected or reported faults, limiting [[02 Concepts/Qualities/Reliability & Fault Tolerance/Silent Data Corruption|Silent Data Corruption]]. **Condition:** For errors within the code's correction and detection strength, in ECC-protected memory.

- Keeps jobs running through correctable errors, raising [[02 Concepts/Qualities/Reliability & Fault Tolerance/Availability|Availability]]. **Condition:** When correctable memory errors would otherwise crash jobs or corrupt their results.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: ECC; SECDED.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
