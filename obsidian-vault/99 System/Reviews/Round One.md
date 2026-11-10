---
title: Round One
tags:
- Type/Review
---

# Round One

## Scope

This review checks YAML, Title Case headings, chapter coverage, Markdown tables, local images, and exact page, heading, and block references. Literal code examples are excluded from prose checks.

## Results

| Check | Count |
| --- | ---: |
| Notes | 2139 |
| Tables | 922 |
| Wiki Links | 32784 |
| External Links | 6878 |
| Image Embeds | 1216 |
| Unique Media | 1169 |
| Source Notes | 2093 |
| Source Heading IDs | 3058 |
| Imported Source Heading IDs | 3024 |
| Chapters | 71 |
| Errors | 1881 |
| Warnings | 0 |

## Findings

### Broken Markdown Link

11 error findings. Representative examples:

- `01 Books/Volume II - Scaling/Frontmatter/V2 Preface.md` — Missing Local Target: ../01_introduction/images/svg/fleet-stack.svg
- `01 Books/Volume II - Scaling/Frontmatter/V2 Preface.md` — Missing Local Target: ../02_compute_infrastructure/images/svg/margin_stack.svg
- `01 Books/Volume II - Scaling/Frontmatter/V2 Preface.md` — Missing Local Target: ../06_distributed_training/images/svg/margin_stack.svg

### Broken Wikilink

5 error findings. Representative examples:

- `06 My Notes/Experiments/Experiment Log.md` — Missing Target: Note Name
- `06 My Notes/Inbox/Inbox.md` — Missing Target: Note Name
- `06 My Notes/Questions/Open Questions.md` — Missing Target: Note Name

### Heading Case

28 error findings. Representative examples:

- `01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10.03 Structural Optimization Changing What the Model Computes.md:213` — Heading Is Not Title Case: optional
- `01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10.03 Structural Optimization Changing What the Model Computes.md:292` — Heading Is Not Title Case: optional
- `01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10.03 Structural Optimization Changing What the Model Computes.md:495` — Heading Is Not Title Case: optional

### Inline Display Math

1520 error findings. Representative examples:

- `01 Books/Volume I - Foundations/00 Introduction/01 Introduction/V1-01.07 When ML Systems Fail Silently.md:29` — Display Math Delimiters Must Be On Separate Lines
- `01 Books/Volume I - Foundations/00 Introduction/01 Introduction/V1-01.08 Iron Law of ML Systems.md:7` — Display Math Delimiters Must Be On Separate Lines
- `01 Books/Volume I - Foundations/00 Introduction/01 Introduction/V1-01.08 Iron Law of ML Systems.md:15` — Display Math Delimiters Must Be On Separate Lines

### Manifest Metadata

270 error findings. Representative examples:

- `02 Concepts/Foundations/Workloads & Requirements/Requirements, SLOs & Baselines Subject.md` — source_path Does Not Match Manifest
- `02 Concepts/Foundations/Workloads & Requirements/Requirements, SLOs & Baselines Subject.md` — source_commit Does Not Match Manifest
- `02 Concepts/Foundations/Workloads & Requirements/Workload Characterization Subject.md` — source_path Does Not Match Manifest

### Quarto Attribute

19 error findings. Representative examples:

- `01 Books/Volume II - Scaling/Frontmatter/V2 Preface.md:53` — Unconverted Quarto Attribute Or Shortcode
- `01 Books/Volume II - Scaling/Frontmatter/V2 Preface.md:70` — Unconverted Quarto Attribute Or Shortcode
- `01 Books/Volume II - Scaling/Frontmatter/V2 Preface.md:74` — Unconverted Quarto Attribute Or Shortcode

### Quarto Div

7 error findings. Representative examples:

- `01 Books/Volume II - Scaling/Frontmatter/V2 Preface.md:74` — Unconverted Quarto Div
- `01 Books/Volume II - Scaling/Frontmatter/V2 Preface.md:76` — Unconverted Quarto Div
- `01 Books/Volume II - Scaling/Frontmatter/V2 Preface.md:89` — Unconverted Quarto Div

### Source Heading Coverage

4 error findings. Representative examples:

- `books/vol1/frontmatter/about.qmd` — 2 Authored Headings Missing: sec-about-companion-resources, sec-book-copyright-licensing-2538
- `books/vol2/frontmatter/about.qmd` — 4 Authored Headings Missing: sec-vol2-about-companion-resources, sec-vol2-about-covers, sec-vol2-about-how-to-read, sec-vol2-about-reading-paths
- `books/vol2/backmatter/appendix_c3.qmd` — 14 Authored Headings Missing: sec-appdx-c3-dam-scorecard, sec-appdx-c3-diagnostic-tree, sec-appdx-c3-diagnostic-tree-details, sec-appdx-c3-taxonomy-bottleneck-table, sec-appdx-c3-taxonomy-case-1, sec-appdx-c3-taxonomy-case-studies, sec-appdx-c3-taxonomy-effective-flops, sec-appdx-c3-taxonomy-rules-of-thumb

### Table Columns

17 error findings. Representative examples:

- `01 Books/Volume I - Foundations/04 Deployment/15 Responsible Engineering/V1-15.08 Summary.md:17` — Expected 3 Cells, Found 2
- `01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06.11 Summary.md:15` — Expected 3 Cells, Found 1
- `01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06.11 Summary.md:16` — Expected 3 Cells, Found 1

## Limits

Structural checks establish link, metadata, table, and asset integrity. Semantic relationship validity and visual rendering require separate review. Source-generated assets without saved image files are tracked by the importer.

## Review Triage and Required Corrections

The initial snapshot exposed inline display equations, table delimiters escaped outside wiki aliases, punctuation-sensitive Title Case failures, missing source headings, and Quarto code-cell parsing defects in repository fallbacks. Those defects require a corrected import before Round Two. Index provenance is also required to match its manifest records.

The reviewer corrected validator false positives for escaped wiki alias pipes and literal inline code examples. Reader-visible heading coverage excludes HTML comments and PDF-only branches. The counts above describe the historical first snapshot; the second review records the corrected final state.
