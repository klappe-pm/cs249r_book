---
title: V4 Governing the Machine
type: Part
volume: 4
chapter: 0
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol4/parts/governing_principles.qmd
source_anchor: governing-the-machine
source_mode: Source-Correlated Published HTML
tags:
- Type/Part
- Book/Volume_4
rendered_source_url: https://mlsysbook.ai/vol4/parts/governing_principles.html
---

# V4 Governing the Machine

[[Home|Home]] · [[01 Books/Volume IV - Physical AI/Volume 4 Overview|Volume Overview]]

^governing-the-machine

Demonstrating a physical AI model in a controlled laboratory is a milestone. Outside the workbench, dust obscures lenses, lighting changes, wireless networks drop packets, gearboxes wear, and human coworkers share the machine’s path. Each change can invalidate a premise used to permit motion. Part III leaves the running machine with conditional answers rather than settled ones: its stopping margin holds only while the unmeasured dispatch-to-admission interval stays inside its allocation, passing a blind rack corner (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/09 Spatial Memory/V4-09.08 Forward State Propagation and Occlusion Decay#^sec-memory-belief-through-occlusion|Forward State Propagation and Occlusion Decay]]**) rests on an unverified procedural restriction of aisle crossings, and the placement record’s loaded field remains empty. Part IV turns those open questions into intervention rules, fault tests, an operating decision, and a named owner for each decision behind it, beginning with the one delay that no test on the chassis can bound, a person’s. The engineer must be able to explain both the useful work the machine may perform and the conditions that require restricting or stopping it.

**Principle 4: Permission must be earned**

**Invariant**: Authority to operate is granted per operating condition by evidence whose age, provenance, and limits are recorded, and it expires when that evidence does. Zero failures in ${n}$ independent, stationary trials place an approximate upper bound of $3/{n}$ on the per-trial failure probability at 95 percent confidence (**[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07.07 Confidence from a Finite Campaign#^sec-evaluation-closed-loop-survival|Confidence from a Finite Campaign]]**).

**Implication**: The operating decision joins evidence of useful task completion with evidence that the machine contains the specified faults and hazards. Who may command it, what the tests challenged, and which conditions it may enter are decided on that record, not on a demonstration. A premise that evidence cannot settle restricts operation through a reduced envelope, a passive limit, or refusal, and it stays open until a declared test closes it.

^pri-vol4-evidence-bounds-authority

- **Supervisory Intervention (**[[01 Books/Volume IV - Physical AI/04 Governing the Machine/14 Supervisory Intervention/V4-14 Supervisory Intervention#^sec-intervention|Supervisory Intervention]]**):** Decides who holds authority over each actuator at each instant when a person and a learned proposer share the machine, and produces the authority record.
- **Adversarial Verification (**[[01 Books/Volume IV - Physical AI/04 Governing the Machine/15 Adversarial Verification/V4-15 Adversarial Verification#^sec-verification|Adversarial Verification]]**):** Decides which fault tests challenge each claim and how their outcomes count, and produces the fault record.
- **Deployment Release (**[[01 Books/Volume IV - Physical AI/04 Governing the Machine/16 Deployment Release/V4-16 Deployment Release#^sec-release|Deployment Release]]**):** Decides whether the machine may operate and under which standing conditions, and produces the release manifest.
- **Responsible Physical AI (**[[01 Books/Volume IV - Physical AI/04 Governing the Machine/17 Responsible Physical AI/V4-17 Responsible Physical AI#^sec-responsibility|Responsible Physical AI]]**):** Decides who answers for each decision behind an admitted action, which human roles a person can actually perform, and which people bear the machine’s risk and appear in its records. It produces the approval record.

Part IV hands forward a release manifest, an approval record, and the premises they could not close. The release exercise preserves refusal for the illustrative machine with missing qualification evidence, then uses a separately stipulated evidence packet to show how restricted useful service could be supported. Neither branch invents completed tests. The manifest binds the evaluation record, the fault records, the placement record, and the authority record into claims with a verdict (unconditional operation, conditional operation, or refusal) and standing conditions that revoke it. The approval record names the person who approved each decision behind them, so that a decision with no owner refuses operation like an unknown premise. The conclusion in **[[01 Books/Volume IV - Physical AI/04 Governing the Machine/18 Engineering Physical AI/V4-18 Engineering Physical AI#^sec-frontier|Engineering Physical AI]]** synthesizes what the engineer can now build and justify, then transfers the method to an unfamiliar machine. Open premises enter a residual-claims register with their restrictions, owners, and closure tests; they guide the next measurement, learning experiment, architectural change, or narrower task.

Back to top

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/parts/governing_principles.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol4/parts/governing_principles.html#governing-the-machine). Rendering provenance is recorded in the import manifest.
