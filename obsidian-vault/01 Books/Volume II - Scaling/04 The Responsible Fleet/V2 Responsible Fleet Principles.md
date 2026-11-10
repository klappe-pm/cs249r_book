---
title: V2 Responsible Fleet Principles
type: Part
volume: 2
chapter: 0
publication_status: Preview
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol2/parts/responsible_fleet_principles.qmd
source_anchor: responsible-fleet-principles
source_mode: Source-Correlated Published HTML
tags:
- Type/Part
- Book/Volume_2
rendered_source_url: https://mlsysbook.ai/vol2/parts/responsible_fleet_principles.html
---

# V2 Responsible Fleet Principles

[[Home|Home]] · [[01 Books/Volume II - Scaling/Volume 2 Overview|Volume Overview]]

^responsible-fleet-principles

Parts I through III built the machine learning fleet, coordinated its training, and optimized its deployment. Part IV develops the mechanisms for enforcing the security, privacy, robustness, environmental, and social constraints that have shaped those design decisions from the outset. Their detailed treatment follows deployment because enforcement depends on the infrastructure, training, and operational controls already introduced. Each of these constraints can be stated as a budget, measured, and exceeded, which makes it an engineering constraint in the same sense as bandwidth, power, or latency.

What these constraints share is that the evidence collected in the earlier parts cannot certify them. A fleet can meet its latency targets and pass every release gate while an authenticated caller copies the model’s behavior, an authorized answer reveals a training record, or a poisoned contribution plants a backdoor. Its health signals can stay normal while its predictions degrade under shifted inputs. Its energy per request can fall while its total energy rises, and an accurate, fast model can still concentrate its errors among the people least able to contest them. No single algorithm closes any of these gaps; each requires monitoring, verification, and governance systems that surround the fleet. Ignoring them is not a neutral choice, because a breach, a regulatory action, or a site that cannot supply power can stop a fleet as surely as a hardware failure. The principles below preview the limits that the following chapters make operational. They identify decisions that belong in the initial system requirements even though the mechanisms for evaluating and enforcing them require the full fleet context.

The first boundary is what the fleet can trust. A model’s behavior is shaped by far more parties than the team that trains it.

**Principle 22: The provenance bound on trust**

**Invariant**: A trained model’s behavior is a function of every contributor to its data, code, and weights, including training records and labels, preprocessing and training code, software dependencies, pretrained checkpoints, and the hardware and firmware that executed the run. A contributor that cannot be identified and verified can change that behavior without producing a visible failure, so the provenance record bounds how far the model can be trusted.

**Implication**: Poisoning and supply-chain attacks need not crash anything. A small set of crafted training examples or a backdoored checkpoint can shift a targeted decision while aggregate validation accuracy stays unchanged, so clean evaluation results cannot certify integrity. Trust must be established upstream, through signed artifacts, immutable lineage for data and code, controlled dependencies, and verification before an artifact enters training or deployment, and it extends only as far as that record reaches.

^pri-provenance-bounds-trust

The second boundary is what the fleet can reveal. Even when every upstream artifact is verified, a deployed model can still leak private training records through the predictions it returns to callers.

**Principle 23: The information leakage invariant**

**Invariant**: A privacy claim must name the protected unit and the observations available to an adversary. Let ${R}$ be one protected individual’s training record and ${O}$ an observable model output. Leakage about that record is present when

$$
{I}({R}; {O}) > 0 .
$$

 Here, ${I}(\cdot;\cdot)$ denotes mutual information.

**Implication**: A correctly executing model can disclose its training data through the outputs it is authorized to give, as memorized text, as membership, or as reconstructed inputs, so access control over stored data cannot protect it. Privacy is a budget, not a switch. Post hoc anonymization of input records does not remove sensitive information already memorized in model weights. Systems requiring formal record-level privacy guarantees should use mechanisms such as differential privacy (DP) where appropriate. DP bounds the influence of adding or removing one protected record for a data analysis or training procedure. Interactive query systems must account for composition, and they may stop answering once the system exhausts the allocated privacy budget.

^pri-information-leakage

Privacy defines what the fleet may reveal; robustness defines how reliably it behaves when distributions drift, environments change, or inputs actively probe its weaknesses. Hardening a model against those perturbations is not a free post-processing step, because training against worst-case inputs multiplies the arithmetic required for each update.

**Principle 24: The robustness compute penalty**

**Invariant**: Adversarial training buys intrinsic robustness with training compute. It trains on adversarial examples, inputs perturbed within a stated budget so that the model’s prediction changes. Projected gradient descent (PGD)-style training finds each perturbation with ${K_{\text{PGD}}}$ inner attack steps, so a batch costs roughly ${K_{\text{PGD}}}+1$ forward-backward passes instead of one. The resulting clean-accuracy and robustness effects depend on the attack strength and training procedure.

**Implication**: Robustness is claimed only per stated failure class (distribution shift, adversarial input, poisoning, silent hardware fault), each with its own evidence, because every one of them can keep service-health signals normal while predictions become invalid. Robustness measures consume training or serving resources and must be evaluated against a stated threat model; certified robustness, for example, is paid for in serving samples rather than training passes. External guardrails such as input filtering and output verification can complement adversarial training, but their detection errors and latency costs remain part of the system. They do not establish the same guarantee as robustness of the underlying model.

^pri-robustness-compute-penalty

Efficiency gains can also change demand, so lower energy per request does not by itself establish lower fleet energy consumption. When cheaper inference invites broader deployment, longer contexts, or more test-time search, aggregate power draw can climb even as each operation becomes leaner.

**Principle 25: The Jevons paradox of AI (efficiency trap)**

**Invariant**: Efficiency improvements can lower unit cost and stimulate demand. In this comparison, total resource consumption rises only when usage grows by a larger factor than resource efficiency improves. The following schematic depicts that rebound scenario, not an inevitable consequence of efficiency:

$$
\text{Efficiency} \uparrow \implies \text{Cost} \downarrow \implies \text{Demand} \uparrow\uparrow
$$

**Implication**: Making models 10$\times$ more efficient can increase total usage enough to erase or even exceed the expected energy savings. Rebound is not the only path. Scaling laws price each further loss reduction in multiplicative compute, so demand can outrun efficiency even without a demand response to lower cost. Sustainability strategies must focus on absolute limits (carbon budgets, renewable sourcing) rather than rate efficiency (FLOP/s per watt) alone.

^pri-jevons-paradox

Responsible operation also requires making social objectives explicit. Calibration asks whether predicted probabilities match observed frequencies. Score balance compares average scores across groups separately among positive and negative outcomes; equalized odds instead compares thresholded error rates. These criteria can conflict, so a fairness requirement must specify which guarantee the system should enforce.

**Principle 26: The fairness impossibility theorem**

**Invariant**: For imperfect risk scores across groups with different base rates, groupwise calibration and equal mean scores across groups within each outcome class cannot all hold simultaneously.

$$
\Pr({Y}=1 \mid {G}={a}) \neq \Pr({Y}=1 \mid {G}={b}) \implies \text{Trade-off Required}
$$

 Here, ${Y}$ is the outcome and ${G} \in \{{a},{b}\}$ is the group attribute; the implication assumes imperfect prediction and refers specifically to the three score criteria above. Equalized odds at one chosen decision threshold is a different condition.

**Implication**: Under the theorem’s conditions, fairness requires an explicit trade-off; there is no criterion-free optimum that selects among incompatible metrics. Engineers must treat fairness metrics like latency budgets: explicit trade-offs chosen by stakeholders, enforced by the system, and monitored for violation. **[[01 Books/Volume II - Scaling/04 The Responsible Fleet/16 Responsible AI/V2-16 Responsible AI#^sec-responsible-ai|Responsible AI]]** provides the full treatment of when the impossibility result applies, including the equal-base-rate and perfect-prediction exceptions.

^pri-fairness-impossibility

Those trade-offs cannot be evaluated once and frozen, because deployed systems alter the data and incentives they later observe. Once a model’s predictions steer user behavior, ranking exposure, or eligibility decisions, the incoming distribution shifts in response to the system itself.

**Principle 27: The sociotechnical feedback invariant**

**Invariant**: When a deployed model’s decisions affect its environment, the probability distribution of future data ${p}_{t+1}({x})$ depends on the model’s past decisions ${f}_t({x})$.

$$
{p}_{t+1}({x}) = {g}({p}_t({x}), {f}_t({x}))
$$

 Here, ${g}$ is the environment’s response function, which maps the current data distribution and the model’s decisions into the next data distribution. Settings with this feedback, where predictions change the outcomes they predict, are called performative.

**Implication**: Systems whose decisions affect their environments require closed-loop governance. A model that maximizes accuracy on static test data can still degrade the future data distribution it operates on, amplify incentives that bias the next round of data, or destabilize the environment being monitored. Reliability in these settings requires modeling the *feedback loop*, not the *feed-forward inference* alone.

^pri-sociotechnical-feedback

Part IV develops these previews in dependency order. Security and privacy come first, because they decide who may reach the model, what its releases may disclose, and which contributors it may trust; the threat model for data poisoning begins there. Access controls cannot show that the model’s answers stay valid, so robustness follows. It asks whether behavior remains acceptable when inputs, environments, hardware, or adversaries depart from validated conditions, and it develops the evidence and defenses that each failure class requires. Both are paid for in compute, which brings sustainability next. It treats planetary-scale infrastructure as an energy and carbon system whose grid power and facility overhead bound how much of that compute the fleet can run. Responsible AI closes the part by asking whether a fleet that is secure, robust, and within its resource budget is fit to deploy, through an assurance case that an accountable owner can block. It also connects those technical controls to institutional governance. None of these controls is free in C$^3$ terms. Security and robustness spend compute and serving latency on verification. Sustainability prices every powered second of the Fleet Law’s computation, communication, and synchronization terms. Governance is the coordination that decides when the fleet may run at all. Together, these chapters complete the engineering discipline that turns a capable fleet into a trustworthy one.

Back to top

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/parts/responsible_fleet_principles.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol2/parts/responsible_fleet_principles.html#responsible-fleet-principles). Rendering provenance is recorded in the import manifest.
