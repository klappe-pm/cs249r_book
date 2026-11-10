---
title: V3 Trajectory Learning Principles
type: Part
volume: 3
chapter: 0
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol3/parts/learning_principles.qmd
source_anchor: trajectory-learning-principles
source_mode: Repository QMD
tags:
- Type/Part
- Book/Volume_3
rendered_source_url: https://mlsysbook.ai/vol3/parts/learning_principles.html
---

# V3 Trajectory Learning Principles

[[Home|Home]] · [[01 Books/Volume III - Agentic Systems/Volume 3 Overview|Volume Overview]]

^trajectory-learning-principles

Parts II through IV built closure around a fixed model. [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13 Agent Evaluation#^sec-vol3-evaluation|Sec — V3-13 Agent Evaluation]] measured task acceptance and compared configurations, and [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/14 Operating Agents/V3-14 Operating Agents#^sec-vol3-operations|Sec — V3-14 Operating Agents]] ended Part IV by testing explanations for failures under declared conditions and releasing changes in stages behind a gate. Part V changes the model itself: training alters the proposals the runtime receives, while moving none of the H·S·A exposures, granting no authority, and removing none of the runtime’s enforcement obligations. Because a changed policy can still alter realized trajectory length, state use, and requested effects, held-out evaluation and release policies still govern whether the resulting model may replace the one in service. The intervention ladder of [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/15 Trajectory Curation/V3-15.03 Capability Gap Diagnosis#^sec-vol3-flywheel-intervention-order|Sec — V3-15.03 Capability Gap Diagnosis]] therefore places weight updates after cheaper and more reversible changes to context, tools, and the runtime, as a default order that diagnostic evidence can shorten rather than a sequence every failure must climb. Once evidence justifies a weight update, however, training cannot simply fit every token of a passing trace, because an agent transcript interleaves model proposals with environment observations and intermediate mistakes that the policy should condition on rather than imitate.

**Invariant**: A recorded outcome does not determine how a trajectory should be used for learning. Curation relates the evidence to a proposed behavior change, admits records for a declared use, and distinguishes admissible targets from contextual or rejected actions. For imitation, delivered observations condition the selected responses but are not themselves targets. The objective applies to examples with at least one admitted target token. With a mask ${m}_{t}$ that equals one only at the admitted policy-token positions of a serialized example ${x}_1,\ldots,{x}_{{S}}$ and ${N_{\text{active}}}=\sum_t {m}_{t}$, the objective makes that selection exact:

$$
{\mathcal{L}_{\text{SFT}}}({\theta}) = -\frac{1}{{N_{\text{active}}}}\sum_{t=2}^{{S}} {m}_{t} \log {\pi_\theta}({x}_t \mid {x_{<t}})
$$

 Masked context still shapes gradients through the predictions that depend on it.

**Implication**: Passing a task check does not make every action in its trace a suitable demonstration, and recovery demonstrations cover post-error states that an error-free corpus lacks. The active-token fraction sets the supervision each trajectory supplies. Construct the mask from the admitted target spans and the actual serialized input, not from authorship alone, and evaluate the resulting policy under the intended serving format. Predicting observation tokens would add a different objective; it would not turn generated text into authentic tool evidence. [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/15 Trajectory Curation/V3-15.03 Capability Gap Diagnosis#^sec-vol3-flywheel-gap|Sec — V3-15.03 Capability Gap Diagnosis]] and [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/15 Trajectory Curation/V3-15.07 Recovery Demonstration Curation#^sec-vol3-flywheel-curation|Sec — V3-15.07 Recovery Demonstration Curation]] develop admission, and [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/16 Trajectory Fine-Tuning/V3-16.05 Observation Loss Masking#^sec-vol3-fine-tuning-loss-masking|Sec — V3-16.05 Observation Loss Masking]] develops the objective ([[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/16 Trajectory Fine-Tuning/V3-16.05 Observation Loss Masking#^eq-vol3-sft-masked-objective|Eq — V3-16.05 Observation Loss Masking]]).

^pri-vol3-trajectory-post-training

Imitation learns from selected responses, while preference learning compares assessed alternatives. Reinforcement learning instead collects new interactions and uses their rewards to guide policy updates, which turns a check into an optimization target. The verification asymmetry (principle ) governs that step. When true success is rare, a small false-accept rate in the verifier makes rewarded failures a large share of the rewarded rollouts ([[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/17 Reinforcement Learning from Verifiable Rewards/V3-17.04 Verifiable Rewards#^eq-vol3-rlvr-false-accept-share|Eq — V3-17.04 Verifiable Rewards]]), so the assessment must stay protected from the candidate and scoped to what it checks.

The three chapters build from evidence selection to policy updates without prescribing a mandatory sequence of training methods. [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/15 Trajectory Curation/V3-15 Trajectory Curation#^sec-vol3-trajectory-curation|Sec — V3-15 Trajectory Curation]] establishes which records and fixtures support a declared learning use. [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/16 Trajectory Fine-Tuning/V3-16 Trajectory Fine-Tuning#^sec-vol3-fine-tuning|Sec — V3-16 Trajectory Fine-Tuning]] turns admitted material into selected prediction targets or justified preference comparisons and an identified candidate policy. [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/17 Reinforcement Learning from Verifiable Rewards/V3-17 Reinforcement Learning from Verifiable Rewards#^sec-vol3-rlvr|Sec — V3-17 Reinforcement Learning from Verifiable Rewards]] adds fresh reward-scored interactions on states no demonstration covers, and develops the reward, the credit assigned across turns, the isolation of the verifier, and the rollout fleet that together decide what the update learns and what it costs. Across all three methods, the policy improves only as far as the scope and protection of its check allow, while the runtime retains every enforcement boundary around the updated model. That measured single-agent configuration then serves as the baseline in Part VI when deciding whether multi-agent coordination earns its added cost.

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/parts/learning_principles.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol3/parts/learning_principles.html#trajectory-learning-principles). Rendering provenance is recorded in the import manifest.
