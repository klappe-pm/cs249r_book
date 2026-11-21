---
title: Content Round One
type: Review
tags:
- Type/Review
---

# Content Round One

## Scope

Independent adversarial review of the first complete import and semantic graph. Inspected representative notes from all four volumes, quantitative appendices, source-correlated HTML, tables, local image imports, chapter navigation, practice entry points, and source-reference fallbacks. This records the initial findings before correction.

## Evidence

The initial manifest contained 144 source documents, 71 main chapters, 1,079 imported book notes, and 879 canonical concepts. Of the source documents, 131 used source-correlated published HTML and 13 used repository QMD fallback. The media import recorded 1,169 local assets and no missing image references. The semantic graph retained 2,010 conditional relationships and resolved all 221 recorded alignments, with four chapter-level fallbacks.

## Findings Requiring Correction

1. **Blocker — Table Delimiters Were Escaped.** A broad alias-pipe cleanup escaped ordinary table separators before a later wikilink. The initial output contained 852 rows starting with an escaped pipe. Example: `V3-13.08 Summary.md`. Escape alias pipes only inside actual wikilink spans; keep Markdown table delimiters intact.
2. **Blocker — Quantitative Fallbacks Lost Results.** Whole-document QMD fallback replaced computed values even when the published document matched except for one new heading. Volume IV Chapter 12 lost 156 computed values and the Volume II C3 appendix lost 55. The generated vault contained 219 computed-value labels overall. A section-aware hybrid import should preserve matching rendered content and import new source sections separately.
3. **Blocker — Fallback Links Became Circular.** The generic book-page mapper changed explicit computed-value source links into local links back to the containing chapter. Those links no longer led to the missing result. Preserve explicit external fallbacks when no faithful local result exists and reject residual calculation expressions.
4. **Major — Source Section Coverage Was Incomplete.** Volume IV Chapter 12 has 15 H2 source headings but only four section notes in the first import. The final section note was approximately 117 KB and contained additional H2 headings and unnormalized sentence-case H3 headings. Verify section coverage per source document in addition to the chapter count.
5. **Major — Source References Consumed Sentence Punctuation.** References such as `@sec-model-serving.` and `@sec-fleet-orchestration.` included the sentence full stop in the parsed identifier and fell back unnecessarily. Strip terminal sentence punctuation before lookup.
6. **Major — Leading Articles Were Lowercased After Numeric Prefixes.** Examples included `V4-01 the Causal Boundary`, `V4-12.02 the Per-Tick Gatekeeper`, and `V2 the C 3 Taxonomy`. Apply Title Case to the substantive title separately before adding the volume and chapter prefix.
7. **Major — Block-ID Formatting Could Consume Blank Lines.** A multiline replacement using `\s*$` removed separating newlines after standalone IDs. Tables and figures need an unambiguous final block marker with blank-line separation. Use line-local horizontal whitespace in substitutions.
8. **Major — Sidenotes Interrupted Sentences.** Website footnote and bibliography sidebars were inserted between sentence fragments, with `fnref` markers and HTML superscript labels. Relocate note and reference bodies into a clean end section or proper Markdown footnotes while preserving exact targets.
9. **Major — Mathematics Needed a Reader-Compatible Form.** Custom macros followed by subscripts survived expansion, and display math appeared inside prose paragraphs. Expand the actual macro token boundary and put display delimiters on separate lines.
10. **Usability — Practice Entry Points Needed Reading Connections.** The four practice notes linked companion repository roots and the experiment log but lacked concrete chapter connections. Add curated links to relevant reading and identify the notes as companion entry points.

## Image and Navigation Observations

The inspected images were local attachments with readable names and source provenance. No external Markdown image embeds remained in the initial vault. Home, volume, chapter, and section navigation were present. Practice navigation and the quantitative fallback defects above still needed correction before acceptance.

## Disposition

Round One is not accepted as final. Findings were sent to the primary agent and renderer for correction. Round Two must verify the corrected generated vault and its exact reference targets, not simply rerun a chapter-count check.
