---
title: V4 The Machine Anatomy
type: Part
volume: 4
chapter: 0
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol4/parts/anatomy_principles.qmd
source_anchor: the-machine-anatomy
source_mode: Source-Correlated Published HTML
tags:
- Type/Part
- Book/Volume_4
rendered_source_url: https://mlsysbook.ai/vol4/parts/anatomy_principles.html
---

# V4 The Machine Anatomy

[[Home|Home]] · [[01 Books/Volume IV - Physical AI/Volume 4 Overview|Volume Overview]]

^the-machine-anatomy

Every physical AI system acts through a body with limited capacity to move, stop, exert force, and dissipate heat. The first law of **[[01 Books/Volume IV - Physical AI/00 Introduction/01 The Causal Boundary/V4-01.11 The Four Bedrock Laws#^sec-boundary-bedrock-laws|The Four Bedrock Laws]]** holds that this apparatus cannot take back the work it delivers, and Part I turns that law into numbers. It asks how quickly the machine’s evidence ages, how far the machine travels before it stops, how much torque its drives can deliver, and how much winding heat and supply-voltage drop they tolerate. The Body establishes what motion the hardware can physically support. The Brain, the learned proposer, establishes what computation can supply and how long its answers stay true. The Nervous System must therefore connect them within the time the stopping budget allows. Following this physical order lets the engineer derive an architectural requirement before selecting its implementation.

**Principle 1: The irreversibility law**

**Invariant**: Once a permitted command crosses the causal boundary, the energy it delivers becomes motion, strain, or heat that no software action can recall. At steady speed, during a pre-brake delay ${\tau_{\text{delay}}}$ the machine travels ${v}\,{\tau_{\text{delay}}}$ before any response begins. A stop therefore requires ${d_{\text{stop}}} \le {D_{\text{clear}}}$, with every term of ${d_{\text{stop}}}$ taken from a measured limit of this machine under stated conditions (**[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/02 The Physical Body/V4-02.04 Kinetic Momentum#^sec-body-kinetic-momentum|Kinetic Momentum]]**).

**Implication**: Each part of the machine carries budgets in time, distance, torque, heat, and voltage. The checks needed to admit a command must finish before its execution and inside those budgets. A design is admissible only when it can say which budget binds first, how that budget was established, and what the machine does when it is exhausted.

^pri-vol4-irreversibility

- **The Physical Body (**[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/02 The Physical Body/V4-02 The Physical Body#^sec-body|The Physical Body]]**):** Decides which physical budget binds first and how its value was established, and produces the limit record from which every later record descends.
- **The Cognitive Brain (**[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/03 The Cognitive Brain/V4-03 The Cognitive Brain#^sec-brain|The Cognitive Brain]]**):** Decides what a learned proposer can deliver on time and what memory and latency that costs, and derives the machine’s two-speed split, a slow intent model above a fast chunk policy. It produces no record of its own; its proposer limits, and the payload every proposal must carry, enter the handoff record.
- **The Nervous System (**[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/04 The Nervous System/V4-04 The Nervous System#^sec-nervous|The Nervous System]]**):** Decides where the permission path must run to stay independent of the proposer, how often it must check, and how long a proposal may drive the actuators. It produces the handoff record together with the header that every proposal carries. The independence it requires leads it to adopt a two-processor split as the hypothesis the machine is built on; whether that split holds on real silicon is decided in **[[01 Books/Volume IV - Physical AI/03 Running the Machine/13 Workload Placement/V4-13 Workload Placement#^sec-placement|Workload Placement]]**.

Part I hands forward three linked artifacts across these chapters. On the physical side, **[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/02 The Physical Body/V4-02 The Physical Body#^sec-body|The Physical Body]]** establishes the limit record, the six-element form in which every budget that can end in damage states its operating conditions and its evidence category. The chapter then fills that form on the running machine for the credible deceleration behind the stopping distance, the drive torque that must deliver it, and the input lockout of the converter on the shared drive bus. Against those physical bounds, **[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/03 The Cognitive Brain/V4-03 The Cognitive Brain#^sec-brain|The Cognitive Brain]]** characterizes the proposer’s supply by pricing how many future setpoints one chunk covers, how long a new chunk takes, and how quickly the evidence behind it ages, showing why a chunk keeps the arm supplied without keeping that evidence fresh. Joining demand and supply, **[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/04 The Nervous System/V4-04 The Nervous System#^sec-nervous|The Nervous System]]** produces the handoff record: the lease the permission path derives from the stopping budget, the tick at which it checks, the handoffs between proposer and permission path, and a worked budget that couples all three chapters on the running machine. That worked example selects a candidate configuration. Qualification still requires bounds on each interval, including dispatch to admission, evidence that the protective response remains physically available, and loaded tests showing that the permission path’s isolation from the proposer holds. Part II inherits both records as preconditions on the demonstrations the machine collects while its permission path is watching.

Back to top

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/parts/anatomy_principles.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol4/parts/anatomy_principles.html#the-machine-anatomy). Rendering provenance is recorded in the import manifest.
