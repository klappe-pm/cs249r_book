---
title: V4 Teaching the Machine
type: Part
volume: 4
chapter: 0
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol4/parts/teaching_principles.qmd
source_anchor: teaching-the-machine
source_mode: Source-Correlated Published HTML
tags:
- Type/Part
- Book/Volume_4
rendered_source_url: https://mlsysbook.ai/vol4/parts/teaching_principles.html
---

# V4 Teaching the Machine

[[Home|Home]] · [[01 Books/Volume IV - Physical AI/Volume 4 Overview|Volume Overview]]

^teaching-the-machine

Part I gave the warehouse mobile manipulator a measured body, a chunked proposer slot, and a permission path that bounds every motion segment by a chunk lease. Teaching that proposer a contact skill, such as unlatching a spring-latched cage door, exposes a difficulty that offline machine learning benchmarks never face. In a static benchmark, a classifier reads held-out examples drawn from a fixed distribution (${x} \sim {p_{\text{data}}}$) whose next stored example never changes when the model predicts. On a physical machine, every action the permission path admits moves the arm, alters the contact state, and shapes the observations that follow. That closed-loop dependency is the second bedrock law of **[[01 Books/Volume IV - Physical AI/00 Introduction/01 The Causal Boundary/V4-01.11 The Four Bedrock Laws#^sec-boundary-bedrock-laws|The Four Bedrock Laws]]**, a systems design principle that turns covariate shift into an evidentiary discipline across data collection, training, and evaluation.

**Principle 2: Endogenous data**

**Invariant**: A physical agent’s actions choose its next observations (${s}_{t+1} \sim {p}({s} \mid {s}_{t}, {\mathbf{a}}_{t})$), so the states a deployed policy visits need not be the states it was trained or tested on. For behavioral cloning, the worst-case cost of that drift can grow with the square of the horizon ([[01 Books/Volume IV - Physical AI/02 Teaching the Machine/V4 Teaching the Machine#^ref-ross2011reduction|Ross et al. 2011]]), as **[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05.04 Recovery and Compounding Error#^eq-data-quadratic-drift|equation 5.1]]** states.

**Implication**: A learned proposer’s competence is a claim about a declared region of states, established in closed loop with the permission path in place. Visiting a state during collection, recording an attributable training target for it, and testing competence there in closed loop are three separate steps. Missing states call for more collection, and a finite set of trials bounds the resulting claim rather than proving it outright.

^pri-vol4-endogenous-drift

Part II traces the cage-door policy across the machine Part I built. During collection the permission path can clamp or refuse an operator’s command, and the body can deliver motion that differs from the admitted one. A demonstration must therefore show what was requested, what the permission path allowed, and what the body actually did. Part I’s limit and handoff records become preconditions on the data. Training then turns the supported behavior into candidate policies, one cloned from the demonstrations and one distilled from a simulator teacher, each of which improves its training score while hiding a dependency the hardware can expose. Closed-loop trials test a candidate under declared conditions, showing how data collection, training, and evaluation fit together. When a displaced latch plate breaks the nominal policy, a recovery campaign collects attributable corrections, trains an updated candidate, and tests both nominal regression and the wider latch range (using stipulated trial counts rather than measurements from a physical robot).

- **Physical Data (**[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05 Physical Data#^sec-data|Physical Data]]**):** Decides which conditions the demonstrations support and what they cost to collect, and produces the provenance record of the demonstrations, which lists the conditions the data does not cover as known absences.
- **Policy Training (**[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06 Policy Training#^sec-training|Policy Training]]**):** Decides which training regime fits the available experience and which dependency each regime leaves hidden, and produces the policy manifest, whose declared operating domain cannot exceed the conditions the provenance record supports.
- **Closed-Loop Evaluation (**[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07 Closed-Loop Evaluation#^sec-evaluation|Closed-Loop Evaluation]]**):** Decides what a finite set of closed-loop trials supports about the proposer, and produces the evaluation record for a target operational design domain (ODD) inside the manifest’s declared one, separating proposer autonomy, whole-machine task completion, and protective outcomes.

Part II hands forward an evaluation record: a claim about the learned proposer confined to a target ODD, the finite-sample bound that supports it, a catalog of the conditions it does not cover, and the runtime monitors the rest of the machine must supply. With it, the first of the record chain’s two strands, plant limits and evaluated competence, is complete. That record identifies the candidate from **[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06 Policy Training#^sec-training|Policy Training]]**, the experience and labels documented in **[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05 Physical Data#^sec-data|Physical Data]]**, and the independent trials supporting its evaluated domain. While the initial archive bounds what the current evidence can support, new collection and re-qualification can widen that domain later. Part III relies on the current evaluation record rather than assuming that a policy manifest alone establishes competence. Its permission path checks the physical premises for each action and restricts or refuses proposals when those premises lack support. Any fallback still requires a response the machine can physically execute.

Back to top

## Source References

^source-references

Ross, Stéphane, Geoffrey Gordon, and J. Andrew Bagnell. 2011. “A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning.” *Proceedings of the Fourteenth International Conference on Artificial Intelligence and Statistics (AISTATS)* 15: 627–35.

^ref-ross2011reduction

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/parts/teaching_principles.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol4/parts/teaching_principles.html#teaching-the-machine). Rendering provenance is recorded in the import manifest.
