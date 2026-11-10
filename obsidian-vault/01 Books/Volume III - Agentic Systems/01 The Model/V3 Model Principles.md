---
title: V3 Model Principles
type: Part
volume: 3
chapter: 0
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol3/parts/model_principles.qmd
source_anchor: model-principles
source_mode: Repository QMD
tags:
- Type/Part
- Book/Volume_3
rendered_source_url: https://mlsysbook.ai/vol3/parts/model_principles.html
---

# V3 Model Principles

[[Home|Home]] · [[01 Books/Volume III - Agentic Systems/Volume 3 Overview|Volume Overview]]

^model-principles

The introduction defined the trajectory, mapped its horizon, state, and authority exposures, and established that a model’s output is a proposal rather than a verified result. Before an agent loops across turns, retains memory, or invokes tools, every trajectory begins at the origin of the H·S·A space with a single model call. In the repair task, that first call reads a failure report and proposes an inspection or a patch. Because an isolated call has no horizon beyond itself, carries no state forward, and holds zero ambient authority, it forms the baseline from which the later parts measure each departure. Neither a longer reasoning trace nor a larger pool of candidate patches alters that baseline: extra tokens, parallel samples, and verification checks consume the decision’s budget, while sequential feedback rounds begin to extend its horizon. Part I therefore governs the cost and evidence of one model decision before the runtime acts on what it proposes.

A request can include a long source excerpt and ask for a short edit, or ask the model to reproduce the entire changed file. Those choices impose different amounts of input processing and output generation. Autoregressive output conditions each token on the preceding sequence; in the ordinary token-by-token implementation, each additional token adds another generation step. The time per step depends on the serving configuration, so the engineering rule concerns a measured cost rather than a universal ratio.

**Invariant**: Under a fixed serving configuration with approximately stable generation time per token, output-generation latency grows approximately with output length. For unbatched decoding of a dense model with ${P}$ parameters stored at ${s_{\text{elem}}}$ bytes each, where weight reads dominate, memory bandwidth ${\text{BW}}$ bounds each output token’s step time from below:

$$
{t_{\text{decode}}} \ge \frac{{P}\,{s_{\text{elem}}}}{{\text{BW}}}
$$

 The bound describes neither every serving configuration nor the whole call’s latency, which also includes preparation, queueing, prefill, and postprocessing.

**Implication**: When generation dominates the call, an interface that expresses the same useful proposal in fewer tokens can reduce latency. Input processing, queueing, and checks must still fit the task’s deadline. Compare interfaces at a matched task budget rather than assuming that shorter output is always better. [[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02.09 The Cost of a Model Call#^sec-vol3-foundation-model-cost|Sec — V3-02.09 The Cost of a Model Call]] develops the bound ([[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02.09 The Cost of a Model Call#^eq-vol3-fm-token-floors|Eq — V3-02.09 The Cost of a Model Call]]) and prices a concrete call; [[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^sec-vol3-appendix-inference-roofline|Sec — V3 Inference Cost Foundations]] derives the hardware estimate and its assumptions.

^pri-vol3-memory-bandwidth-decoding

Bounding output length prices a call, but the runtime must also distinguish time spent from work completed. A call interrupted by a token limit, a cancellation, or a dropped connection may leave a truncated payload that still parses, so [[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02.06 The Invocation Contract#^sec-vol3-foundation-model-contract|Sec — V3-02.06 The Invocation Contract]] requires a mechanical completion-status check before treating any output as a finished candidate. Even a complete candidate, however, is only a plausible proposal. When one call misses the repair, spending additional inference to sample several candidate patches raises two separate questions: whether a valid patch sits in the pool and whether the runtime’s check can identify it. A static build or type check can reject broken syntax, and a visible regression test can filter out patches that fail existing cases, yet neither proves every property of the intended fix. Because selection over many candidates exploits whatever false acceptances the check allows, the precision of the check bounds the value of extra compute.

**Invariant**: Producing a valid candidate, selecting it, and establishing that it satisfies the task are different events. Additional sampling can raise the chance that a candidate set contains a valid result; the check that selects from the set bounds how far a pass can be trusted. For a valid-candidate rate ${p_{\text{valid}}}$, a false-reject rate ${\epsilon_{\text{FR}}}$, and a false-accept rate ${\epsilon_{\text{FA}}}$, the precision of a passing verdict is

$$
{\Pi_{V}} = \frac{{p_{\text{valid}}}(1-{\epsilon_{\text{FR}}})}{{p_{\text{valid}}}(1-{\epsilon_{\text{FR}}})+(1-{p_{\text{valid}}})\,{\epsilon_{\text{FA}}}}
$$

 A checker can be exact for a stated property and still leave open whether that property captures the task.

**Implication**: At a low valid rate, a small false-accept rate fills the passing set with invalid candidates, and the effect grows when a check becomes an optimization target, whether a selection rule over many samples or a training reward. Allocate a task’s budget across generation, assessment, and feedback; compare the complete policy against a single-candidate baseline at matched cost, counting unsuccessful attempts and checks; and stop when marginal acceptance per unit cost falls below a threshold. State what each check supports, protect its criteria and observations from the actions it judges, and preserve unresolved requirements in the acceptance decision. Learned assessments can rank or revise candidates but supply neither permission to act nor an independent guarantee. [[01 Books/Volume III - Agentic Systems/01 The Model/03 Test-Time Compute/V3-03 Test-Time Compute#^sec-vol3-test-time-compute|Sec — V3-03 Test-Time Compute]] develops the precision ([[01 Books/Volume III - Agentic Systems/01 The Model/03 Test-Time Compute/V3-03.05 Verifying Candidates#^eq-vol3-verifier-precision|Eq — V3-03.05 Verifying Candidates]]) and the stopping rule ([[01 Books/Volume III - Agentic Systems/01 The Model/03 Test-Time Compute/V3-03.07 Bounded Search#^eq-vol3-marginal-stopping|Eq — V3-03.07 Bounded Search]]).

^pri-vol3-verification-asymmetry

Together, these two principles connect the price of a model decision to the evidence behind its result under invariant closure (principle ). [[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02 The Foundation Model#^sec-vol3-foundation-model|Sec — V3-02 The Foundation Model]] establishes what a single request supplies, how the response reports completion, and how input processing and output generation contribute to latency and cost. [[01 Books/Volume III - Agentic Systems/01 The Model/03 Test-Time Compute/V3-03 Test-Time Compute#^sec-vol3-test-time-compute|Sec — V3-03 Test-Time Compute]] then analyzes when longer generation, parallel candidates, and check-and-revise rounds improve the selected result within a fixed budget. With a bounded call contract and a rule for pricing extra inference in place, Part II turns to what the runtime carries from one call to the next.

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/parts/model_principles.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol3/parts/model_principles.html#model-principles). Rendering provenance is recorded in the import manifest.
