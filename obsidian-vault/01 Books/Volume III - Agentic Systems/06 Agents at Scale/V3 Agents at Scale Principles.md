---
title: V3 Agents at Scale Principles
type: Part
volume: 3
chapter: 0
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol3/parts/scale_principles.qmd
source_anchor: agents-at-scale-principles
source_mode: Repository QMD
tags:
- Type/Part
- Book/Volume_3
rendered_source_url: https://mlsysbook.ai/vol3/parts/scale_principles.html
---

# V3 Agents at Scale Principles

[[Home|Home]] · [[01 Books/Volume III - Agentic Systems/Volume 3 Overview|Volume Overview]]

^agents-at-scale-principles

Parts I through V built a bounded agent runtime, established how to measure it, and introduced ways to learn from its trajectories. Learning produces candidates for assessment, not a mandatory prerequisite for scale. Part VI changes the count in two directions. One task may be split across separately managed child trajectories joined by handoffs, the temptation the repair agent meets when its next assignment, migrating an authentication module, reaches every caller of the module’s interface. Many tasks also run at once on shared models, quotas, and sandboxes, so each competes for capacity. Delegation extends the H·S·A exposures across these boundaries: an unsupported result can become another worker’s premise, copied state can become stale, and descendant operations can exceed the intended scope unless the runtime constrains them. Trajectory-level encapsulation (principle ) already requires that derived grants only narrow and that concurrent holders reserve against one shared allowance. The controls required for one agent must continue to hold when work is distributed, and the additional coordination must earn its cost under the task’s requirements.

Splitting one task across several agents is tempting whenever a repository-wide change touches many files, but parallel workers do not divide wall-clock time for free. Every handoff serializes context, every child trajectory consumes its own tokens and sandboxes, and reconciling conflicting edits sits back on the critical path.

**Invariant**: Delegation adds work for handoffs, context delivery, coordination, and integration. The portion on the critical path reduces any elapsed-time gain from parallel work; aggregate resource use also includes work off that path. For a fixed set of work with parallel fraction ${f_{\text{parallel}}}$ divisible among ${N_{\text{workers}}}$ equally fast workers and added elapsed overhead ${h}({N_{\text{workers}}})$, normalized by the serial time,

$$
\text{Speedup}({N_{\text{workers}}}) = \frac{1}{(1-{f_{\text{parallel}}}) + {f_{\text{parallel}}}/{N_{\text{workers}}} + {h}({N_{\text{workers}}})}
$$

 The serial fraction caps speedup at $1/(1-{f_{\text{parallel}}})$, and growing overhead can make added workers slower. A delegation decision therefore rests on three measures together: accepted-task rate, elapsed time, and cost per accepted task, under a declared objective.

**Implication**: Compare against a single-agent runtime with the same available tools, search opportunities, and resource limits, counting failed, discarded, and canceled work and retaining uncertainty in the outcome estimates. Improving one measure without worsening the others is a sufficient gain, not the only useful trade-off, since a tighter deadline can justify higher spend when the design still meets its acceptance and budget requirements. Represent dependencies, carry explicit control fields and bounded evidence across handoffs, and remember that natural-language task content does not replace runtime-enforced boundaries. [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/18 Multi-Agent Coordination/V3-18.03 The Delegation Trade-Off#^sec-vol3-multiagent-need|Sec — V3-18.03 The Delegation Trade-Off]] develops the bound ([[01 Books/Volume III - Agentic Systems/06 Agents at Scale/18 Multi-Agent Coordination/V3-18.03 The Delegation Trade-Off#^eq-vol3-multiagent-speedup|Eq — V3-18.03 The Delegation Trade-Off]]), and [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/18 Multi-Agent Coordination/V3-18.10 Benchmarking Against a Single Agent#^sec-vol3-multiagent-evaluation|Sec — V3-18.10 Benchmarking Against a Single Agent]] the comparison.

^pri-vol3-coordination-tax

Bounding what a fleet may spend leaves the question of what its spending buys. The answer is the accepted task, the unit that agent evaluation already counts as success ([[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13.03 The Task Acceptance Contract#^sec-vol3-evaluation-contract|Sec — V3-13.03 The Task Acceptance Contract]]), priced by the cost per accepted task introduced in [[01 Books/Volume III - Agentic Systems/00 Introduction/01 Introduction/V3-01.07 Reliability and Cost Over a Horizon#^sec-vol3-intro-horizon-arithmetic|Sec — V3-01.07 Reliability and Cost Over a Horizon]].

**Invariant**: Cost per accepted task charges all initiated work within a declared accounting boundary to the distinct tasks accepted under the same assessment contract. With expected attempt cost $\mathbb{E}[{C_{\text{attempt}}}]$ and acceptance probability ${p_{\text{acc}}}$,

$$
{C_{\text{eff}}} = \frac{\mathbb{E}[{C_{\text{attempt}}}]}{{p_{\text{acc}}}}
$$

 Failed and canceled work remains in the numerator; pending verdicts and unsettled liabilities remain explicit. The account includes every resource a trajectory holds, and each is sized by its own residence: for admission rate ${\lambda_{\text{traj}}}$ and mean residence $\mathbb{E}[{T_{\text{traj}}}]$ at that resource, a stable population holds ${N_{\text{traj}}} = {\lambda_{\text{traj}}}\mathbb{E}[{T_{\text{traj}}}]$ on average.

**Implication**: Raising acceptance can cut cost more than cheaper tokens. A trajectory can retain a sandbox while releasing model-service capacity, so long tool waits raise held sandboxes in proportion; the mean alone gives neither peak occupancy nor deadline capacity, so test burst and completion-time behavior at the intended load. Compare complete policies under consistent outcome, cost, deadline, and authority requirements, including assessment, cleanup, shared capacity, and any human work inside the boundary. Measure the bottleneck before choosing model, cache, routing, or execution changes. [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/19 Agent Economics/V3-19.03 Cost per Accepted Task#^sec-vol3-agent-economics-accounting|Sec — V3-19.03 Cost per Accepted Task]] develops the account, and [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/19 Agent Economics/V3-19.07 Capacity for Trajectories#^sec-vol3-agent-economics-capacity|Sec — V3-19.07 Capacity for Trajectories]] the capacity form ([[01 Books/Volume III - Agentic Systems/06 Agents at Scale/19 Agent Economics/V3-19.07 Capacity for Trajectories#^eq-vol3-trajectory-concurrency|Eq — V3-19.07 Capacity for Trajectories]]).

^pri-vol3-trajectory-goodput

The first principle decides whether splitting a task across agents is worth running and how it is judged; the second decides what one agent or a fleet costs and how much capacity it needs. The two chapters of Part VI take those questions in order. [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/18 Multi-Agent Coordination/V3-18 Multi-Agent Coordination#^sec-vol3-multi-agent|Sec — V3-18 Multi-Agent Coordination]] compares delegation with a single-agent runtime given comparable resources, including parallel search and tools; it judges accepted-task rate, makespan, and cost under a declared objective, then develops typed handoffs, bounded returns, concurrent integration, descendant cancellation, and authority control. [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/19 Agent Economics/V3-19 Agent Economics#^sec-vol3-agent-economics|Sec — V3-19 Agent Economics]] then builds the full cost and capacity account for one agent or many: it turns cost per accepted task into a cohort measurement, prices context reuse, retries, reasoning budgets, critical-path acceleration, and model routing against it, sizes the capacity that concurrent trajectories hold, keeps spending reservations intact across delegated children, and shows that each lighthouse workload is bound by a different term of that account. With every subsystem built and priced, Part VII runs them together on one trajectory.

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/parts/scale_principles.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol3/parts/scale_principles.html#agents-at-scale-principles). Rendering provenance is recorded in the import manifest.
