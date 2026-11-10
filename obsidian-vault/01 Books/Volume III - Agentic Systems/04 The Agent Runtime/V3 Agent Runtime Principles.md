---
title: V3 Agent Runtime Principles
type: Part
volume: 3
chapter: 0
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol3/parts/runtime_principles.qmd
source_anchor: agent-runtime-principles
source_mode: Repository QMD
tags:
- Type/Part
- Book/Volume_3
rendered_source_url: https://mlsysbook.ai/vol3/parts/runtime_principles.html
---

# V3 Agent Runtime Principles

[[Home|Home]] · [[01 Books/Volume III - Agentic Systems/Volume 3 Overview|Volume Overview]]

^agent-runtime-principles

Part III developed tool, containment, and security contracts that already span jobs, leases, approvals, and uncertain effects. Part IV gives their continuing obligations a common trajectory-level owner, then develops crash persistence, effect recovery, evaluation, and live operation. The runtime carries one trajectory across its horizon, bounding the horizon exposure of H·S·A. A long horizon also reshapes the other two exposures: it turns state into a durability problem, because the evidence needed to continue must survive the process that holds it, and it turns authority into an ordering problem, because some effects cannot be undone once later steps depend on them. Governing those obligations across turns begins by encapsulating every call, lease, and budget reservation inside a single runtime-owned trajectory record.

**Invariant**: The runtime governs each model call as part of a whole trajectory. Its runtime-owned record tracks identity, lifecycle state, actual and reserved consumption, grants and leases, continuation references, observation eligibility, and unresolved effect obligations. The trajectory advances only through transitions and admissions that the runtime’s guards permit, because it cannot be relied on to yield, to stop, or to notice that it has stopped making progress. For each cumulative resource dimension, admission requires

$$
\text{actual} + \text{reserved} + \text{proposed liability} + \text{finalization reserve} \le \text{allowance}
$$

 A derived grant or allowance handed to another worker can only narrow what its holder has, and concurrent holders reserve against one shared allowance.

**Implication**: Model output proposes changes; the runtime admits them through current state, authority, and budget checks, so spend stays within the allowance even when final usage arrives late, and final checks stay funded. Control requests are recorded independently of model output, so the runtime can stop new admission and abort supported local work while preserving unresolved external obligations; a loop that passes every per-call limit still halts at the dispatch ceiling or deadline. Progress checks use task-scoped observations rather than heartbeats or the model’s own reports, and can miss a loop or flag useful repetition. Per-worker ceilings alone would let ${N_{\text{workers}}}$ concurrent workers spend up to ${N_{\text{workers}}}$ times the budget, and a parent stopping does not prove that its children or their external operations have stopped. Waiting can release a worker while cache state, workspaces, credentials, or effect obligations retain their own lifetimes ([[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05.08 Paused-State Policies#^sec-vol3-kvcache-swapping|Sec — V3-05.08 Paused-State Policies]]). [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10.10 Budgets and Ceilings#^sec-vol3-harness-multidim-budgets|Sec — V3-10.10 Budgets and Ceilings]] develops the admission test ([[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10.10 Budgets and Ceilings#^eq-vol3-bounded-liability-admission|Eq — V3-10.10 Budgets and Ceilings]]).

^pri-vol3-trajectory-encapsulation

A record held only in memory dies with the process that holds it, and the environment’s state is not restored by recovering the runtime’s own. When an action crosses the process boundary into an external service, the runtime must therefore record what it intends to do before the effect can occur.

**Invariant**: Before dispatching an external effect, the runtime obtains a durable acknowledgment of the authorized intent, its admission state, and its recovery template. For an attempt that proceeds to dispatch and later produces an observation, the required order is

$$
{e_{\text{prop}}} \prec {e_{\text{auth}}} \prec {e_{\text{flush}}} \prec {a_{\text{ext}}} \prec {e_{\text{obs}}}
$$

 so, provided every external effect passes through the runtime and the log is durable, a crash before the flush leaves no effect, and after it the log names every operation that still needs settlement. Recovery then works forward from that record. A snapshot restores selected local state, and compensation is a new operation that establishes declared conditions. Neither erases external history, incurred charges, or unresolved effects, and an irreversible commitment ends the compensable region.

**Implication**: An intent without adequate terminal outcome evidence remains unresolved; a timeout or recorded result label does not settle it. Compensations have their own admission, outcome, and repeat contracts, and uncertainty or failure retains a responsible owner. The expected irreversible loss of a plan, ${L_A} = \sum_{a} \Pr(\text{bad}\ {a})\cdot \text{consequence}({a})\cdot(1-{\rho_{a}})$ with ${\rho_{a}}$ the recoverable fraction, favors reversible, information-gathering steps before the pivot, since past it only forward recovery remains. [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11.04 Durable Intent Before Dispatch#^sec-vol3-persistence-wal|Sec — V3-11.04 Durable Intent Before Dispatch]] develops the ordering ([[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11.04 Durable Intent Before Dispatch#^eq-vol3-wal-ordering|Eq — V3-11.04 Durable Intent Before Dispatch]]), and [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12.06 Irreversible Commitments#^sec-vol3-sagas-pivot|Sec — V3-12.06 Irreversible Commitments]] develops commitment regions and the loss ([[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12.06 Irreversible Commitments#^eq-vol3-expected-irreversible-loss|Eq — V3-12.06 Irreversible Commitments]]).

^pri-vol3-intent-before-effect

These principles organize supervision, reconstruction, and recovery for one agent. They do not establish task acceptance, and a population reliability claim cannot rest on one successful run.

**Invariant**: Activity signals alone do not establish task acceptance. Acceptance requires evidence for declared outcome, process, resource, and residual-duty criteria, with the coverage and limits of each check stated. Comparing system versions requires a declared task population, comparable trials, and uncertainty appropriate to the design. For two independent arms with average acceptance probability ${\bar{p}}$, a target difference ${\Delta}$, two-sided significance ${\alpha_{\text{sig}}}$, and power $1-{\beta}$, the tasks needed per arm are approximately

$$
{N_{\text{arm}}} \approx \frac{2\,({z_{1-\alpha_{\text{sig}}/2}}+{z_{1-\beta}})^2\,{\bar{p}}(1-{\bar{p}})}{{\Delta}^2}
$$

 Trace records connect observed decisions and outcomes without proving a unique cause.

**Implication**: Halving the detectable difference quadruples the tasks per arm, so a small suite cannot rank close systems. A biased or contaminated measurement invalidates any sample size. The evaluation harness therefore protects graders from the agent and from untrusted submitted artifacts, calibrates fallible judgments where the rubric uses them, and preserves task, configuration, candidate, operation, and attempt identities so that reconstruction, captured-input replay tests, and new experimental runs remain distinct. A release then advances under a prespecified evidence and exposure policy, while runtime authority, budgets, and unresolved-effect obligations remain in force. [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13.06 Statistical Evaluation Rigor#^sec-vol3-evaluation-paired|Sec — V3-13.06 Statistical Evaluation Rigor]] develops the planning estimate ([[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13.06 Statistical Evaluation Rigor#^eq-vol3-eval-planning-power|Eq — V3-13.06 Statistical Evaluation Rigor]]).

^pri-vol3-release-evidence

The five chapters of Part IV build these principles in order, each on the one before. [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10 The Agent Harness#^sec-vol3-agent-harness|Sec — V3-10 The Agent Harness]] gives each trajectory a record and a harness that can pause, approve, budget, and stop it without the model’s cooperation, which is trajectory-level encapsulation. [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11 Durable Execution#^sec-vol3-durable-execution|Sec — V3-11 Durable Execution]] specifies the recorded history, storage acknowledgment, checkpoints, and ownership needed to reconstruct selected state and admit continuation under stated failure conditions; it also distinguishes reconstruction from replay tests and new execution. [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12 Failure Recovery#^sec-vol3-failure-recovery|Sec — V3-12 Failure Recovery]] uses recorded evidence to choose bounded repair, compensation, containment, or escalation, governs declared commitment regions, and adds fallible task-progress checks, which together complete intent before effect. [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13 Agent Evaluation#^sec-vol3-evaluation|Sec — V3-13 Agent Evaluation]] then measures the single-agent system, defining the accepted task and the evidence a comparison of configurations requires, and [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/14 Operating Agents/V3-14 Operating Agents#^sec-vol3-operations|Sec — V3-14 Operating Agents]] carries that evidence into live operation through traces, controlled diagnosis, and staged release under a declared gate. Those evaluation and operational records do not by themselves certify that training on them is safe, but when cheaper fixes no longer resolve a measured failure, they supply the evidence Part V needs to curate trajectories and update the model’s weights under the same runtime contracts.

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/parts/runtime_principles.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol3/parts/runtime_principles.html#agent-runtime-principles). Rendering provenance is recorded in the import manifest.
