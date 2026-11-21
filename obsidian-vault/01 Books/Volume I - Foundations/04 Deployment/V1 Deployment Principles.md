---
title: V1 Deployment Principles
type: Part
volume: 1
chapter: 0
publication_status: Released
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol1/parts/deploy_principles.qmd
source_anchor: deployment-principles
source_mode: Source-Correlated Published HTML
tags:
- Type/Part
- Book/Volume_1
rendered_source_url: https://mlsysbook.ai/vol1/parts/deploy_principles.html
---

# V1 Deployment Principles

[[Home|Home]] · [[01 Books/Volume I - Foundations/Volume 1 Overview|Volume Overview]]

^deployment-principles

The code can be correct and the benchmarks excellent, and yet the system may fail. Part III ended with benchmarks whose load generator decides when each request arrives and whose test data stays fixed. Part IV moves from that controlled environment to production, where ML systems face the additional threat of silent decay. A machine learning system can continue to produce outputs that are confident, well-formatted, and wrong as the world drifts away from its training distribution. At deployment, the data environment escapes the engineer’s control and can stress the trained algorithm and the serving machine in ways no test set anticipated. Reliability is therefore a continuous control loop of D·A·M co-design rather than a one-time check before release. The principles here define the requirements and diagnostic models for that reliability.

**Principle 9: The verification gap**

**Policy**: Statistical verification holds only over a defined deployment population ${p_{\text{deploy}}}$, task distance ${d_{\text{task}}}$, tolerance ${\tau_{\text{tol}}}$, and target error ${\epsilon}$, estimated by a finite-sample procedure at a stated confidence level:

$$
\Pr_{({x},{y})\sim {p_{\text{deploy}}}}\!\left[{d_{\text{task}}}({f}({x}),{y}) \leq {\tau_{\text{tol}}}\right] \geq 1-{\epsilon}
$$

**Implication**: Deployment is not a one-way transfer; it is a control loop. Because no test suite can cover every possible real-world input, production systems must monitor their own uncertainty and fail gracefully when they drift outside their known performance envelope.

^pri-verification-gap

The verification gap means finite evaluation can only estimate behavior on a defined population with uncertainty. Those estimates may erode as production data diverges from the data used to make them.

**Principle 10: The statistical drift diagnostic**

**Fitted model**: Divergence between the production and baseline distributions does not by itself determine whether accuracy changes; over a measured deployment range, labeled outcomes can fit a local linear relationship:

$$
{\text{Accuracy}}({t}) \approx {\text{Accuracy}_0} - {\lambda}\cdot {\mathcal{D}(P_t \| P_0)}
$$

 where ${P_t}$ is the data distribution at time ${t}$ after deployment and ${P_0}$ is the training (baseline) distribution. The term ${\text{Accuracy}_0}$ is the model’s performance on ${P_0}$, ${\mathcal{D}(P_t \| P_0)}$ is the statistical divergence between the current and baseline distributions, and ${\lambda}$ is fitted from labeled outcomes rather than inferred from divergence alone. Consider a credit scoring model trained on 2020 borrower behavior. Two years later, inflation rises, interest rates change, and lending policies shift. The system still produces scores, but the statistical relationship between inputs and outcomes may have changed; labeled outcome monitoring determines whether real accuracy declined while conventional error logs remained quiet. Unlike many traditional software failures, which are often surfaced by crashes, exceptions, or explicit service-health signals, ML systems can fail silently because the environment changes even when the code and infrastructure remain unchanged. This first-order linearization applies only over the measured range; the relationship is model-dependent and may be nonlinear for large drift.

**Implication**: Observability must extend beyond system metrics (latency, errors) to combine statistical drift signals with labeled outcomes. A system can remain operational while prediction quality changes, but drift monitoring alone does not establish degradation.

^pri-statistical-drift

External drift is not the only threat. Even when the world holds still, the serving pipeline itself can diverge from the model validated offline.

**Principle 11: The training-serving skew diagnostic**

**Heuristic**: Training and serving code paths can diverge on identical inputs, and that divergence is measurable without labels. For scalar model scores, define training-serving divergence as the expected absolute difference between the two functions over a stated comparison-input distribution:

$$
{S_{\text{skew}}}= \mathbb{E}[|{f_{\text{serve}}}({x}) - {f_{\text{train}}}({x})|]
$$

 The exact relationship between ${S_{\text{skew}}}$ and accuracy depends on the loss function, decision boundary geometry, and production distribution. Unexplained divergence weakens the assumption that offline validation estimates production behavior and can cause silent accuracy loss, but ${S_{\text{skew}}}$ is not a universal accuracy-loss equation. This divergence arises from inconsistent preprocessing logic, different library implementations, stale feature values, or environmental state changes between the two code paths.

**Implication**: Feature consistency is an architectural requirement, not merely a best practice. Feature stores are more than caches; they can reduce skew by centralizing feature definitions and retrieval. Teams still need validation for freshness, point-in-time correctness, preprocessing, model-runtime, and postprocessing parity. Even subtle differences (PIL vs. OpenCV resize, FP64 vs. FP32 normalization) can compound to produce silent accuracy degradation that standard monitoring may not detect.

^pri-training-serving-skew

Preserving statistical accuracy against drift and skew is only half of the production contract; the prediction must also arrive before the decision window closes. A medical imaging system that detects tumors with 99 percent accuracy but takes 30 seconds per scan may miss its clinical workflow deadline, and an autonomous vehicle perception model that classifies obstacles correctly in 200 ms instead of 50 ms may miss its braking deadline. Latency-sensitive deployed models operate under a strict time budget: if a correct prediction arrives too late, it has no operational value and is functionally equivalent to returning no prediction at all.

**Principle 12: The latency budget principle**

**Policy**: Under serial request-path accounting, end-to-end latency is the sum of network, preprocessing, inference, postprocessing, and queueing delays, and a deployment meets its deadline only at a stated completion quantile:

$$
{L_{\text{lat,total}}}= {L_{\text{lat,network}}}+ {L_{\text{lat,pre}}}+ {L_{\text{lat,infer}}}+ {L_{\text{lat,post}}}+ {L_{\text{lat,queue}}}, \qquad \Pr[{L_{\text{lat,total}}}\leq {T_{\text{deadline}}}] \geq {q}
$$

**Implication**: In latency-sensitive serving, the product selects the deadline and the acceptable completion quantile, such as 0.95, 0.99, or 0.999, and throughput is optimized within that constraint. Serving systems must implement tail-latency controls (for example, bounded-delay dynamic batching or hedged requests). Serving systems must be willing to sacrifice overall throughput to meet the latency deadline of the oldest request in the queue.

^pri-latency-budget

A system can satisfy its latency SLOs, detect measured distributional shifts, and maintain training-serving consistency while still causing systematic harm. The previous principles address silent failures in correctness and service quality; this one addresses failures that degrade equity through silent amplification.

**Principle 13: The bias feedback model**

**Fitted model**: When outputs influence future inputs, today’s disparity becomes an input to the next training cycle, so disparity evolves as a dynamical system rather than staying fixed. Let ${\Delta_g}({k}) \geq 0$ denote the disparity magnitude for group ${g}$ relative to a specified reference group after ${k}$ fixed feedback intervals. With no effective intervention and an approximately constant dimensionless feedback factor ${\alpha_{\text{fb}}}> 0$, disparity may evolve as:

$$
{\Delta_g}({k}) \approx {\Delta_g}(0) \cdot {\alpha_{\text{fb}}}^{k}
$$

 where ${\Delta_g}(0)$ is the initial disparity magnitude relative to that reference group and ${\alpha_{\text{fb}}}$ is fitted per feedback interval. Consider a loan approval model that denies credit at higher rates to applicants from historically underserved communities. Denied applicants cannot build credit history, which makes future applications weaker, which increases future denial rates. The model’s accuracy on its training distribution remains stable, but the population it serves has been reshaped by its own decisions. When ${\alpha_{\text{fb}}}> 1$ under these assumptions, the feedback loop is self-reinforcing; when ${\alpha_{\text{fb}}}\leq 1$, the modeled dynamics are stable or damped. Real deployments may also be nonlinear, saturating, or changed by intervention.

**Implication**: Fairness is not a postdeployment audit; it is a stability constraint on the deployment control loop. Where consequential impact warrants it and collecting or using group attributes is lawful and justified, systems must monitor disaggregated performance metrics across relevant demographic groups with the same rigor applied to latency percentiles. The reason is that a bias regression can be invisible to aggregate accuracy just as a tail-latency violation can be invisible to mean latency.

^pri-bias-feedback

Together, the five principles define a deployment control loop. The loop establishes what offline evidence supports, observes the live system and its environment, acts only when a measured failure warrants intervention, and re-evaluates the relevant service, predictive, or subgroup criterion. These principles separate diagnosis from response. A monitoring signal narrows the investigation, but it neither prescribes an automatic intervention nor proves by itself that end-to-end quality has already degraded.

Part IV makes that control loop concrete. **[[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13 Model Serving#^sec-model-serving|Model Serving]]** builds infrastructure that meets latency budgets under variable traffic and checks training-serving parity on the request path. **[[01 Books/Volume I - Foundations/04 Deployment/14 ML Operations/V1-14 ML Operations#^sec-ml-operations|ML Operations]]** detects drift and skew over the model’s operating lifetime while preserving the evidence needed for diagnosis and response. **[[01 Books/Volume I - Foundations/04 Deployment/15 Responsible Engineering/V1-15 Responsible Engineering#^sec-responsible-engineering|Responsible Engineering]]** treats fairness and feedback as measurable deployment dynamics rather than a one-time compliance check. **[[01 Books/Volume I - Foundations/04 Deployment/16 Conclusion/V1-16 Conclusion#^sec-conclusion|Conclusion]]** then closes the book by gathering these production controls and the quantitative bounds and models of the preceding parts into one framework for reasoning across the whole stack.

Back to top

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/parts/deploy_principles.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol1/parts/deploy_principles.html#deployment-principles). Rendering provenance is recorded in the import manifest.
