---
title: V4 Machine Learning Background
type: Reference
volume: 4
chapter: 0
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol4/backmatter/appendix_ml.qmd
source_anchor: sec-appendix-ml
source_mode: Source-Correlated Published HTML
tags:
- Type/Reference
- Book/Volume_4
rendered_source_url: https://mlsysbook.ai/vol4/backmatter/appendix_ml.html
---

# V4 Machine Learning Background

[[Home|Home]] · [[01 Books/Volume IV - Physical AI/Volume 4 Overview|Volume Overview]]

^sec-appendix-ml

This appendix supplies the machine learning and statistical tools needed to interpret learned action proposals, size their computation, and evaluate the evidence for their use. It develops uncertainty measures, spatial representations, policy-learning objectives, and rare-event bounds as consultable references for the main text. Each tool separates what a model or test establishes from the physical clearance and timing conditions that the permission path must enforce.

## How to Use This Appendix

^how-to-use-this-appendix

Use the table to enter at the relevant problem. The probability section explains expectations, densities, and uncertainty; spatial representations then connect image arrays to metric geometry. Policy sections distinguish the training objective from runtime execution, and the final sections distinguish statistical evidence from a physical guarantee. The derivations use matrix multiplication, derivatives, and integrals; the prose following each result states the engineering consequence so that a reader can consult the result before working through its proof.

| When you encounter this systems symptom                                             | Consult                                                                                                 | For this quantitative tool                                                                   |
|-------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| A vision-language model hallucinates actions under perceptual ambiguity             | [[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^sec-appendix-ml-probability\|section 1.2]]        | Posterior entropy metrics, Shannon uncertainty, and refusal thresholds                       |
| Overconfident neural outputs command aggressive actions out-of-distribution         | [[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^sec-appendix-ml-calibration\|section 1.2.3]]      | Softmax simplex geometry and Expected Calibration Error (ECE)                                |
| Multi-camera extrinsics, 2D tokenization, or 3D scene geometry drift                | [[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^sec-appendix-ml-spatial\|section 1.3]]            | ${SE(3)}$ transforms, patch embeddings, attention, and metric 3D lifting                     |
| Camera features must be placed in one metric ground-plane grid                      | [[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^sec-appendix-ml-bev-lifting\|section 1.3.3]]      | Lift-Splat depth hypotheses, frustum size, and BEV splatting                                 |
| Differentiable 3D scene reconstruction diverges during real-time tracking           | [[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^sec-appendix-ml-3dgs\|section 1.3.5]]             | 3D Gaussian Splatting parameters and covariance projection                                   |
| Occupancy mapping retains phantom obstacles after objects move                      | [[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^sec-appendix-ml-voxels\|section 1.3.6]]           | Log-odds voxel updates, TSDF fusion, and raycast DRAM traffic                                |
| Small sensor noise produces explosive, unconstrained actuator commands              | [[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^sec-appendix-ml-lipschitz\|section 1.4.2]]        | Lipschitz continuity bounds and spectral normalization                                       |
| A behavioral cloning policy drifts into unrecoverable off-trajectory states         | [[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^sec-appendix-ml-compounding\|section 1.5]]        | ${\mathcal{O}(S^2 \epsilon)}$ compounding error and DAgger linear reduction                  |
| $\ell_2$ regression averages bimodal demonstrations into lethal obstacle collisions | [[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^sec-appendix-ml-multimodal\|section 1.5.1]]       | Conditional expectation proof and multimodal policy decoders                                 |
| A generative decoder cannot finish a chunk within the setpoint period               | [[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^sec-appendix-ml-diffusion\|section 1.5.2]]        | Denoising evaluations ${N_{\text{eval}}}$ latency-expressiveness trade-off and flow matching |
| Offline reinforcement learning selects ungrounded, destructive motor setpoints      | [[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^sec-appendix-ml-affordances\|section 1.6]]        | Bellman value overestimation and SayCan affordance grounding                                 |
| Continuous policy optimization diverges under function approximation error          | [[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^sec-appendix-ml-continuous-rl\|section 1.6.1]]    | DDPG, TD3 clipped double Q-learning, SAC maximum entropy, and PPO clipping                   |
| Sim-to-real transfer fails due to unobservable physical environmental parameters    | [[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^sec-appendix-ml-asymmetric-ac\|section 1.6.6]]    | Asymmetric actor-critic architectures and privileged simulation states                       |
| Comparing policy decoders across latency, compute intensity, and memory footprint   | [[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^sec-appendix-ml-policy-tradeoffs\|section 1.6.9]] | Comparative systems taxonomy (MLP, CNN, ACT, Diffusion, Flow, RL)                            |
| Verifying time-varying physical safety properties across continuous traces          | [[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^sec-appendix-ml-stl\|section 1.7]]                | Signal Temporal Logic (STL) syntax and quantitative robustness degree                        |
| Zero-failure fleet testing encounters the Poisson Exposure Wall                     | [[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^sec-appendix-ml-exposure\|section 1.8]]           | Rule of Three (${T} \ge 3.0/{\lambda}$), Wald breakdown, and Clopper-Pearson bounds          |
| Physical testbed wear explodes during fixed-sample policy qualification             | [[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^sec-appendix-ml-sprt\|section 1.9]]               | Sequential Probability Ratio Test (SPRT) and Wald stopping boundaries                        |
| Contact collision shocks and latency spikes exceed Gaussian $6{\sigma}$ bounds      | [[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^sec-appendix-ml-evt\|section 1.10]]               | Tail-family selection, GEV/GPD fits, and conditional high-quantile sizing                    |

## Probability, Information Theory, and Calibration

^sec-appendix-ml-probability

Commanding an uncalibrated motor torque stresses gearboxes, violates physical clearance envelopes, and risks destructive contact collisions across an irreversible causal boundary, unlike a software prediction error that merely degrades a recommendation or text token. Autonomous machines must therefore reason quantitatively about uncertainty across perception, intent estimation, and world modeling. In closed-loop physical AI, uncertainty quantification determines whether a candidate action proposal is dispatched to motor controllers or intercepted by a safety governor.

### Conditional Probability and Bayes’ Rule

^conditional-probability-and-bayes-rule

When a sensor returns observed evidence ${x}$, the conditional distribution ${p}({y} \mid {x})$ characterizes the updated belief over ${y}$. For continuous parameters, ${p}$ in the following expressions denotes a density; probabilities over regions require integration. By Bayes’ rule:

$$
{p}({\theta} \mid {\mathcal{D}}) = \frac{{p}({\mathcal{D}} \mid {\theta}) {p}({\theta})}{{p}({\mathcal{D}})} = \frac{{p}({\mathcal{D}} \mid {\theta}) {p}({\theta})}{\int_{\Theta} {p}({\mathcal{D}} \mid {\theta'}) {p}({\theta'}) \, d{\theta'}}
$$

 where ${p}({\theta})$ represents prior belief over model parameters or latent states ${\theta} \in {\Theta}$, ${p}({\mathcal{D}} \mid {\theta})$ represents the likelihood of physical dataset or sensor observation sequence ${\mathcal{D}} = \{{\mathbf{x}}_1, \dots, {\mathbf{x}}_{{N}}\}$, and ${p}({\theta} \mid {\mathcal{D}})$ represents the updated posterior belief.

In high-dimensional learning systems, integrating over the parameter manifold ${\Theta}$ to compute the marginal likelihood (evidence) ${p}({\mathcal{D}}) = \int_{\Theta} {p}({\mathcal{D}} \mid {\theta}) {p}({\theta}) \, d{\theta}$ is analytically and computationally intractable. Real-time autonomy resolves this intractability through two complementary paradigms:

1.  **Maximum a posteriori (MAP) estimation:** Replacing posterior integration with point optimization:

$$
{\theta_{\text{MAP}}} = \arg\max_{\theta} \left[ \sum_{i=1}^{N} \ln {p}({\mathbf{x}}_i \mid {\theta}) + \ln {p}({\theta}) \right]
$$

 With conditionally independent observations and a summed log-likelihood, a zero-mean isotropic Gaussian prior ${p}({\theta}) = {\mathcal{N}}({\mathbf{0}}, {\sigma_0}^2 {\mathbf{I}})$ gives the log-prior $\ln {p}({\theta}) = -\frac{\|{\theta}\|_2^2}{2{\sigma_0}^2} - \frac{{d}}{2}\ln(2\pi{\sigma_0}^2)$. Maximizing the posterior objective is mathematically identical to minimizing negative log-likelihood with an explicit $\ell_2$ penalty $\frac{{\lambda_{\text{reg}}}}{2} \|{\theta}\|_2^2$, where ${\lambda_{\text{reg}}} = 1/{\sigma_0}^2$. However, MAP estimation yields only a single deterministic point estimate ${\theta_{\text{MAP}}}$. The point estimate does not report posterior variance; it does not establish that the underlying uncertainty is zero. In continuous control, epistemic uncertainty (ignorance arising from lack of training data in unfamiliar operational domains) must be sharply distinguished from aleatoric uncertainty (stochasticity inherent to sensor noise, turbulent airflow, or non-deterministic contact friction). A point-estimated model can still predict observation noise, but that output alone does not quantify uncertainty about its fitted parameters.
2.  **Variational inference:** Approximating the true posterior ${p}({\theta} \mid {\mathcal{D}})$ with a tractable variational distribution family ${q_\phi}({\theta})$ by maximizing the Evidence Lower Bound (ELBO):

$$
\ln {p}({\mathcal{D}}) = \mathbb{E}_{{\theta} \sim {q_\phi}({\theta})} \left[ \ln \frac{{p}({\mathcal{D}}, {\theta})}{{q_\phi}({\theta})} \right] + {\mathcal{D}_{\text{KL}}}\left( {q_\phi}({\theta}) \,\parallel\, {p}({\theta} \mid {\mathcal{D}}) \right) \ge \mathbb{E}_{{\theta} \sim {q_\phi}({\theta})} [\ln {p}({\mathcal{D}} \mid {\theta})] - {\mathcal{D}_{\text{KL}}}\left( {q_\phi}({\theta}) \,\parallel\, {p}({\theta}) \right)
$$

 Because the Kullback-Leibler divergence is non-negative (${\mathcal{D}_{\text{KL}}} \ge 0$), the lower bound holds, with equality when the variational distribution equals the posterior almost everywhere. Variational inference converts intractable high-dimensional integration into continuous gradient-based optimization over variational parameters ${\phi}$. This formulation provides the analytical foundation for the latent-variable action chunking and generative decoders derived in [[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^sec-appendix-ml-multimodal|section 1.5.1]], where latent variables capture human demonstrator intent and style without collapsing multimodal physical actions into destructive spatial averages.

### Shannon Entropy and Ambiguity Thresholds

^shannon-entropy-and-ambiguity-thresholds

When a perception or intent model spreads probability across several candidate targets, entropy quantifies the average uncertainty or information content contained in that distribution. For a discrete random variable ${X}$ taking values in alphabet ${\mathcal{X}}$:[[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^fn1|¹]]

$$
{H}({X}) = - \sum_{{x} \in {\mathcal{X}}} {p}({x}) \log_2 {p}({x}) = \mathbb{E}_{{x} \sim {p}} \left[ \log_2 \frac{1}{{p}({x})} \right]
$$

 For continuous random variables governing physical state ${\mathbf{x}} \in \mathbb{R}^{d}$ with probability density ${p}({\mathbf{x}})$, the **differential entropy** evaluates to:

$$
{h}({\mathbf{X}}) = - \int_{\mathbb{R}^{d}} {p}({\mathbf{x}}) \ln {p}({\mathbf{x}}) \, d{\mathbf{x}}
$$

 Under a multivariate Gaussian distribution ${\mathbf{x}} \sim {\mathcal{N}}({\boldsymbol{\mu}}, {\boldsymbol{\Sigma}})$ with positive-definite covariance ${\boldsymbol{\Sigma}} \in \mathbb{R}^{{d} \times {d}}$, substituting the Gaussian density ${p}({\mathbf{x}}) = (2\pi)^{-{d}/2} (\det {\boldsymbol{\Sigma}})^{-1/2} \exp(-\frac{1}{2}({\mathbf{x}}-{\boldsymbol{\mu}})^\top {\boldsymbol{\Sigma}}^{-1} ({\mathbf{x}}-{\boldsymbol{\mu}}))$ yields:

$$
\begin{aligned} {h}({\mathbf{X}}) &= -\mathbb{E}\left[ -\frac{{d}}{2}\ln(2\pi) - \frac{1}{2}\ln(\det {\boldsymbol{\Sigma}}) - \frac{1}{2}({\mathbf{x}} - {\boldsymbol{\mu}})^\top {\boldsymbol{\Sigma}}^{-1}({\mathbf{x}} - {\boldsymbol{\mu}}) \right] \\ &= \frac{{d}}{2}\ln(2\pi) + \frac{1}{2}\ln(\det {\boldsymbol{\Sigma}}) + \frac{1}{2}\operatorname{Tr}\left({\boldsymbol{\Sigma}}^{-1} \mathbb{E}[({\mathbf{x}}-{\boldsymbol{\mu}})({\mathbf{x}}-{\boldsymbol{\mu}})^\top]\right) \\ &= \frac{1}{2} \ln\left( (2\pi {e})^{d} \det {\boldsymbol{\Sigma}} \right) \end{aligned}
$$

 Unlike discrete entropy, differential entropy depends on coordinate units and can be negative. Comparisons require the same coordinates and units. For a Gaussian it scales with the logarithmic volume of the physical uncertainty ellipsoid $\det {\boldsymbol{\Sigma}}$. In state estimation, sensor fusion, and Kalman filtering, an informative measurement update shrinks $\det {\boldsymbol{\Sigma}}$, producing an exact physical information gain ${\Delta} {h} = {h_{\text{prior}}} - {h_{\text{post}}} = \frac{1}{2} \ln(\det {\boldsymbol{\Sigma}_{\text{prior}}} / \det {\boldsymbol{\Sigma}_{\text{post}}})$. Under an isotropic Gaussian distribution ${\mathcal{N}}({\boldsymbol{\mu}}, {\sigma}^2 {\mathbf{I}})$, this reduces to ${h}({\mathbf{X}}) = \frac{{d}}{2} \ln(2\pi {e} {\sigma}^2)$. In continuous reinforcement learning, such as Soft Actor-Critic (SAC), the unsquashed diagonal Gaussian policy has entropy ${\mathcal{H}}(\pi(\cdot \mid {s})) = \frac{{d_a}}{2}(1 + \ln(2\pi)) + \sum_{i=1}^{{d_a}} \ln {\sigma^{\pi}}_i({s})$ with ${d_a}$ action dimensions and conditional standard deviations ${\sigma^{\pi}}_i$. Entropy regularization encourages exploration; after bounding actions with a nonlinear transformation, its Jacobian changes this entropy, as the SAC derivation below shows.

To quantify information divergence between an empirical demonstrator distribution ${p}$ and a learned policy distribution ${q}$, information theory defines the **Kullback-Leibler (KL) divergence** (relative entropy):

$$
{\mathcal{D}_{\text{KL}}}({p} \,\parallel\, {q}) = \int_{\mathbb{R}^{d}} {p}({\mathbf{x}}) \ln \left( \frac{{p}({\mathbf{x}})}{{q}({\mathbf{x}})} \right) d{\mathbf{x}}
$$

 where ${\mathcal{D}_{\text{KL}}}({p} \parallel {q}) \ge 0$ by Gibbs’ inequality, with equality if and only if ${p} = {q}$ almost everywhere.

In closed-loop decision making, Shannon entropy provides an instantaneous monitor of policy ambiguity. When a vision-language planner encounters an underspecified scene with two equally probable referents (such as two identical cups), the discrete action entropy approaches its maximum ${H}({X}) \to \log_2 2 = 1.0\text{ bit}$. A calibrated threshold gates actuation, issuing an ambiguity fault (`ERR_GROUNDING_AMBIGUITY`) that commands a stationary hold while active perception collects disambiguating viewpoints. However, because an overfitted neural network can be confidently wrong, entropy alone cannot guarantee semantic correctness; it must operate in tandem with physical clearance monitors.

### Softmax Overconfidence and Calibration Error

^sec-appendix-ml-calibration

A perception classifier that reports a $0.99$ softmax score on a wet-floor reflection or an unfamiliar obstacle is measuring logit separation rather than empirical accuracy. Standard neural classification heads normalize raw logit vectors ${\mathbf{z}} = [{z}_1, \dots, {z}_{{K}}]^\top \in \mathbb{R}^{K}$ into categorical distributions using the softmax function:

$$
{\sigma}({\mathbf{z}})_i = \frac{e^{{z}_i / {T_{\text{cal}}}}}{\sum_{j=1}^{K} e^{{z}_j / {T_{\text{cal}}}}}
$$

 where ${T_{\text{cal}}} > 0$ is a temperature hyperparameter (defaulting to ${T_{\text{cal}}} = 1$). The softmax operator maps logits onto the open probability simplex ${\Delta}^{{K}-1} = \{{\mathbf{p}} \in \mathbb{R}^{K} : \sum_i {p}_i = 1, {p}_i > 0\}$ strictly through algebraic exponentiation.

A cross-entropy training objective does not by itself establish calibration. At ${T_{\text{cal}}}=1$, for target class ${y} \in \{1, \dots, {K}\}$, the cross-entropy loss evaluates to ${\mathcal{L}_{\text{CE}}}({\mathbf{z}}, {y}) = -{z_{c}} + \ln \sum_{j=1}^{K} e^{{z}_j}$. Differentiating with respect to any logit ${z}_i$:

$$
\frac{\partial {\mathcal{L}_{\text{CE}}}}{\partial {z}_i} = \frac{e^{{z}_i}}{\sum_{j=1}^{K} e^{{z}_j}} - {\mathbf{1}}({i} = {y}) = {\sigma}({\mathbf{z}})_i - {\mathbf{1}}({i} = {y})
$$

 For the ground-truth class ${y}$, the derivative is negative until its predicted probability approaches unity. For an individually fitted example, cross-entropy decreases as the correct class separates from the other logits; separable, unregularized training can therefore keep increasing those margins. This is not a proof that every trained network is overconfident or that noisy examples can all be fitted simultaneously. A large softmax output measures relative logit separation, while calibration asks whether predictions with that confidence are correct at the corresponding frequency.

To quantify whether predicted probabilities match empirical physical frequencies, reliability engineering computes the **Expected Calibration Error (ECE)** and **Maximum Calibration Error (MCE)**:[[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^fn2|²]]

$$
\text{ECE} = \sum_{{m}=1}^{{N_{\text{bins}}}} \frac{|{B_m}|}{{N}} \left| \text{acc}({B_m}) - \text{conf}({B_m}) \right|, \qquad \text{MCE} = \max_{{m} \in \{1, \dots, {N_{\text{bins}}}\}} \left| \text{acc}({B_m}) - \text{conf}({B_m}) \right|
$$

 Empty bins contribute zero to ECE and are omitted from MCE; accuracy and confidence averages are defined only for nonempty bins. Here ${B_m}$ is the set of validation examples whose predicted confidence falls in $(({m}-1)/{N_{\text{bins}}},{m}/{N_{\text{bins}}}]$. The size $|{B_m}|$ is the sample count in bin ${m}$, and ${N}$ is the total validation sample count. The mean predicted confidence is $\text{conf}({B_m}) = \frac{1}{|{B_m}|} \sum_{i \in {B_m}} {\hat{p}}_i$, and the empirical accuracy is $\text{acc}({B_m}) = \frac{1}{|{B_m}|} \sum_{i \in {B_m}} {\mathbf{1}}({\hat{y}}_i = {y}_i)$.

To recalibrate an overconfident model post-hoc without altering its classification accuracy, **temperature scaling** optimizes a single scalar parameter ${T_{\text{cal}}} > 0$ on a held-out calibration dataset ${\mathcal{D}_{\text{cal}}}$:

$$
{T_{\text{cal}}}^* = \arg\min_{{T_{\text{cal}}} > 0} \left[ - \sum_{({\mathbf{x}}, {y}) \in {\mathcal{D}_{\text{cal}}}} \ln \left( \frac{e^{{z_{c}}({\mathbf{x}}) / {T_{\text{cal}}}}}{\sum_{j=1}^{K} e^{{z}_j({\mathbf{x}}) / {T_{\text{cal}}}}} \right) \right]
$$

 Because ${T_{\text{cal}}}^*$ scales all logits uniformly, the ranking $\arg\max_i ({z}_i / {T_{\text{cal}}}) = \arg\max_i {z}_i$ remains unchanged for all ${T_{\text{cal}}} > 0$, preserving top-1 accuracy. Temperatures above one soften probabilities, while temperatures below one sharpen them; optimizing calibration loss does not guarantee exact calibration. However, temperature scaling rests on the classical assumption that deployment data is identically distributed to calibration data (${p_{\text{deploy}}} = {p_{\text{cal}}}$). In physical AI, an embodied agent continually encounters non-stationary environmental shifts: lens flare, wet floor reflectance, novel obstacle textures, or altered motor dynamics. Temperature scaling cannot repair or detect out-of-distribution inputs: scaling an out-of-distribution logit vector by scalar ${T_{\text{cal}}}^*$ still yields near-unity confidence if the raw relative logit separation remains large. In safety-critical autonomy, post-hoc calibration requires separately validated uncertainty and clearance checks. Conformal coverage also depends on its sampling assumptions, commonly exchangeability; it does not automatically survive deployment shift.

## Spatial Representations and Scene Parameterization

^sec-appendix-ml-spatial

Detecting a door handle at pixel $(142, 88)$ in a wrist-camera image cannot tell a joint controller where to move until that pixel ray is combined with metric depth and transformed through the camera, wrist, arm, and mobile-base coordinate frames. Unlike language models that operate on discrete semantic tokens, an embodied policy must bind high-dimensional sensor arrays (RGB-D cameras, time-of-flight rangefinders, and lidars) to rigid physical links and Euclidean 3D reference frames.

### Special Euclidean Group ${SE(3)}$ Transforms

^special-euclidean-group-specialeuclideangroup-transforms

Rigid body transformations in 3D Euclidean space belong to the Special Euclidean Lie group ${SE(3)}$, combining a $3 \times 3$ orthonormal rotation matrix ${\mathbf{R}} \in {SO(3)}$ (${\mathbf{R}}^\top {\mathbf{R}} = {\mathbf{I}}$, $\det({\mathbf{R}}) = +1$) with a translation vector ${\mathbf{t}} \in \mathbb{R}^3$:

$$
{\mathbf{T}} = \begin{bmatrix} {\mathbf{R}} & {\mathbf{t}} \\ {\mathbf{0}}^\top & 1 \end{bmatrix} \in {SE(3)} \subset \mathbb{R}^{4 \times 4}
$$

 A homogeneous coordinate vector ${\tilde{\mathbf{p}}} = [{\mathbf{p}}^\top, 1]^\top \in \mathbb{R}^4$ transforms across coordinate frames via matrix-vector multiplication:

$$
{\tilde{\mathbf{p}}'} = {\mathbf{T}} {\tilde{\mathbf{p}}} \iff {\mathbf{p}'} = {\mathbf{R}} {\mathbf{p}} + {\mathbf{t}}
$$

 Let ${\mathbf{T}_{AB}}$ denote the transform mapping coordinates from frame ${B}$ into frame ${A}$. For a kinematic chain comprising world frame ${W}$, mobile base ${B}$, end effector ${E}$, and wrist camera ${C}$, the forward composite transformation evaluates via associative matrix multiplication:

$$
{\mathbf{T}_{WC}} = {\mathbf{T}_{WB}} {\mathbf{T}_{BE}} {\mathbf{T}_{EC}}
$$

 The inverse transform admits an exact closed-form evaluation avoiding general $4 \times 4$ matrix inversion:

$$
{\mathbf{T}}^{-1} = \begin{bmatrix} {\mathbf{R}}^\top & -{\mathbf{R}}^\top {\mathbf{t}} \\ {\mathbf{0}}^\top & 1 \end{bmatrix}
$$

#### Lie Algebra ${\mathfrak{se}(3)}$ and Manifold Perturbation

^lie-algebra-specialeuclideanalgebra-and-manifold-perturbation

Because ${SE(3)}$ forms a smooth, non-Euclidean Riemannian manifold rather than a linear vector space, unconstrained optimization (such as gradient descent during camera pose estimation or neural trajectory generation) cannot directly add matrices (${\mathbf{T}}_1 + {\mathbf{T}}_2 \notin {SE(3)}$). Regressing 3D rotations directly using Euler angles induces topological singularities (gimbal lock at pitch $\pm 90^\circ$) where degrees of freedom collapse. Unconstrained unit quaternions ${\mathbf{q}_{\text{quat}}} \in {S^3}$ suffer from the antipodal double-cover ambiguity (${\mathbf{q}_{\text{quat}}}$ and $-{\mathbf{q}_{\text{quat}}}$ represent the identical physical rotation). In continuous neural policy training, minimizing $\ell_2$ regression loss over quaternions produces severe gradient cancellation when the network predicts opposite hemispheres for nearby states. To ensure topological continuity across continuous rotations, modern spatial policies either output continuous 6D rotation representations (the first two columns of ${\mathbf{R}}$ orthonormalized via Gram-Schmidt) or parameterize local variations in the tangent space at the identity: the Lie algebra ${\mathfrak{se}(3)}$.

For the finite pose increment below, a twist coordinate vector ${\boldsymbol{\xi}} = [{\mathbf{v}}^\top, {\boldsymbol{\omega}}^\top]^\top \in \mathbb{R}^6$ combines integrated translation coordinates ${\mathbf{v}}$ and rotation coordinates ${\boldsymbol{\omega}}$. If these symbols instead denote velocities, multiply the matrix twist by elapsed time before exponentiating. The wedge operator $(\cdot)^{{\wedge}}$ maps ${\boldsymbol{\xi}}$ to its matrix Lie algebra representation:

$$
{\hat{\boldsymbol{\xi}}} = {\boldsymbol{\xi}}^{{\wedge}} = \begin{bmatrix} [{\boldsymbol{\omega}}]_\times & {\mathbf{v}} \\ {\mathbf{0}}^\top & 0 \end{bmatrix} \in {\mathfrak{se}(3)}, \quad \text{where } [{\boldsymbol{\omega}}]_\times = \begin{bmatrix} 0 & -{\omega_z} & {\omega_y} \\ {\omega_z} & 0 & -{\omega_x} \\ -{\omega_y} & {\omega_x} & 0 \end{bmatrix}
$$

 The exponential map $\exp: {\mathfrak{se}(3)} \to {SE(3)}$ computes finite rigid transformations in closed form via Rodrigues’ formula:

$$
\exp({\hat{\boldsymbol{\xi}}}) = \begin{bmatrix} \exp([{\boldsymbol{\omega}}]_\times) & {\mathbf{V}} {\mathbf{v}} \\ {\mathbf{0}}^\top & 1 \end{bmatrix}
$$

 where ${\theta_{\text{rot}}} = \|{\boldsymbol{\omega}}\|$, $\exp([{\boldsymbol{\omega}}]_\times) = {\mathbf{I}} + \frac{\sin{\theta_{\text{rot}}}}{{\theta_{\text{rot}}}} [{\boldsymbol{\omega}}]_\times + \frac{1 - \cos{\theta_{\text{rot}}}}{{\theta_{\text{rot}}}^2} [{\boldsymbol{\omega}}]_\times^2$, and ${\mathbf{V}} = {\mathbf{I}} + \frac{1 - \cos{\theta_{\text{rot}}}}{{\theta_{\text{rot}}}^2} [{\boldsymbol{\omega}}]_\times + \frac{{\theta_{\text{rot}}} - \sin{\theta_{\text{rot}}}}{{\theta_{\text{rot}}}^3} [{\boldsymbol{\omega}}]_\times^2$.

In spatial tracking and state estimation, small pose uncertainties are modeled by perturbing the mean transform with a zero-mean Gaussian twist vector in the local frame: ${\mathbf{T}'} = {\mathbf{T}} \exp({\hat{\boldsymbol{\epsilon}}})$, with ${\boldsymbol{\epsilon}} \sim {\mathcal{N}}({\mathbf{0}}, {\boldsymbol{\Sigma}_{\boldsymbol{\xi}}})$ and covariance ${\boldsymbol{\Sigma}_{\boldsymbol{\xi}}} \in \mathbb{R}^{6 \times 6}$. The exponential keeps the updated pose on ${SE(3)}$. The covariance describes local tangent coordinates, not a Gaussian distribution over matrix entries; its approximation is reliable only while the local perturbation model is adequate. At zero rotation, evaluate the coefficients above by their continuous limits to avoid division by zero.

### Visual Patch Tokenization, Attention, and 3D Metric Lifting

^sec-appendix-ml-patch-embedding

A vision transformer that slices three $224 \times 224$ camera frames into $14 \times 14$-pixel patches produces 768 visual tokens per control step. Yet none of those tokens carries metric 3D distance until camera intrinsics and depth measurements lift the 2D image plane into Euclidean space. Embodied vision-language-action (VLA) models and spatial transformers convert continuous sensory streams into discrete tokens for neural attention, then lift candidate spatial predictions into 3D coordinates for physical reasoning. **[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/03 The Cognitive Brain/V4-03.04 Learned Representations#^sec-brain-learned-representations|Learned Representations]]** and **[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/03 The Cognitive Brain/V4-03.05 The Cost of a Fresh Evaluation#^sec-brain-cognitive-pipeline|The Cost of a Fresh Evaluation]]** use the token counts derived here to size the application processor’s memory traffic.

#### Convolutional Encoders Versus Vision Transformer Tokenization

^convolutional-encoders-versus-vision-transformer-tokenization

Physical AI architectures employ two primary paradigms for encoding raw camera observations into visual features:

1.  **Convolutional Encoders (ConvNets):** Classical visuomotor backbones (such as ResNet-18/34/50 or modern ConvNeXt variants) process images through hierarchical sliding-window convolutions. Convolutions possess an intrinsic inductive bias: **translational equivariance** ($\text{Conv}(\text{Shift}({\mathbf{I}})) = \text{Shift}(\text{Conv}({\mathbf{I}}))$) and local spatial compactness. Because small $3 \times 3$ filter weights are repeatedly applied across thousands of image pixel locations, convolutional feature extraction achieves high arithmetic intensity (FLOPs per byte transferred from DRAM) in early layers. Intermediate feature activations stream through on-chip SRAM line buffers, minimizing off-chip memory bandwidth consumption and reducing traffic when the accelerator mapping and buffer capacity permit reuse. Deterministic latency still requires a timing analysis under contention. However, local receptive fields require deep network stacks to capture global scene context, limiting their ability to resolve long-range semantic relationships (such as attending from a robot gripper to a distant receptacle).
2.  **Vision Transformers (ViTs):** Vision transformers discard local sliding windows in favor of non-overlapping patch tokenization and global multi-head self-attention. While ViTs lack hardwired translational equivariance, they establish global receptive fields across the entire image at layer 1. The operational trade-off is computational complexity and memory bandwidth: self-attention scales quadratically ($\mathcal{O}({N}^2)$) in token count ${N}$. On embedded edge accelerators operating at single-frame batch sizes, materializing full ${N} \times {N}$ attention matrices generates substantial activation memory traffic that stresses shared system memory buses.

#### 2D Vision Transformer Patch Tokenization

^d-vision-transformer-patch-tokenization

Consider an RGB image ${\mathbf{I}} \in \mathbb{R}^{{H} \times {W} \times {C}}$ captured by an onboard camera with spatial resolution ${H} \times {W}$ and ${C}$ color channels. Feeding raw pixels to a multilayer perceptron would discard spatial locality and inflate the parameter count. A vision transformer frontend therefore partitions the image into a non-overlapping sequence of ${N}$ patches of ${p_{\text{patch}}} \times {p_{\text{patch}}}$ pixels, with ${H}$ and ${W}$ divisible by ${p_{\text{patch}}}$ after any chosen crop or padding:

$$
{N} = \frac{{H} \cdot {W}}{{p_{\text{patch}}}^2}
$$

 Each patch, indexed by its row and column $({h}, {w})$ in the camera plane, is flattened into a vector ${\mathbf{x}_p}^{({h}, {w})} \in \mathbb{R}^{{p_{\text{patch}}}^2 {C}}$. A trainable linear projection ${\mathbf{W}_{\text{patch}}} \in \mathbb{R}^{({p_{\text{patch}}}^2 {C}) \times {d}}$ maps each flattened patch into the transformer’s hidden dimension ${d}$. Without positional information or position-dependent masks, self-attention is permutation-equivariant: permuting the input rows permutes the output rows. Therefore the model knows nothing of spatial proximity unless position is added explicitly:

$$
{\mathbf{z}}_0^{({h}, {w})} = {\mathbf{x}_p}^{({h}, {w})} {\mathbf{W}_{\text{patch}}} + {\mathbf{E}_{\text{pos}}^{2D}}({h}, {w}) + {\mathbf{e}_{\text{cam}}}
$$

 The 2D position embedding ${\mathbf{E}_{\text{pos}}^{2D}}({h}, {w})$ decomposes along the vertical axis ${h}$ and the horizontal axis ${w}$, using sinusoidal frequency bands or learned coordinate embeddings. It encodes position in the image plane and carries no metric 3D distance. When several cameras feed one model, such as an overhead camera for scene context and a wrist camera for millimeter-scale alignment, a learned camera identifier ${\mathbf{e}_{\text{cam}}} \in \{{\mathbf{e}_{\text{overhead}}}, {\mathbf{e}_{\text{wrist}}}\}$ distinguishes their reference frames. Some architectures also prepend a summary token ${\mathbf{x}_{\text{class}}} \in \mathbb{R}^{{d}}$ to the sequence.

To make the dimensions concrete, take a square RGB frame 224 pixels on a side (illustrative; see the Reader Guide) with patch size ${p_{\text{patch}}} =$ 14. The frame divides into 16 patches on a side, 256 in all. Each patch holds 196 pixels across 3 color channels, a flattened vector of 588 values, and ${\mathbf{W}_{\text{patch}}}$ maps each such vector into a 4096-dimensional model space. One frame therefore becomes 256 tokens of width 4096. A robot with 3 cameras (two wrist cameras and one overhead) supplies 3 $\times$ 256 = 768 visual tokens per step before any text or proprioceptive token is added.

The visual tokens then join the rest of the input. A natural-language directive such as “grasp the red mug by its handle” is tokenized by byte-pair encoding into text embeddings ${\mathbf{z}_{\text{text}}} \in \mathbb{R}^{{S_{\text{text}}} \times {d}}$. The robot’s configuration (joint angles, joint velocities, and gripper state) passes through a linear layer into proprioceptive tokens ${\mathbf{z}_{\text{proprio}}} \in \mathbb{R}^{{K_s} \times {d}}$. The three streams concatenate into one multimodal input sequence:

$$
{\mathbf{Z}} = [{\mathbf{z}_{\text{vision}}} \,|\, {\mathbf{z}_{\text{text}}} \,|\, {\mathbf{z}_{\text{proprio}}}] \in \mathbb{R}^{{N_{\text{total}}} \times {d}}
$$

#### Self-Attention Over the Combined Sequence

^self-attention-over-the-combined-sequence

The combined sequence ${\mathbf{Z}}$ passes through a stack of transformer layers, each consisting of multi-head self-attention and a feed-forward network. Self-attention projects each token through learned matrices ${\mathbf{W}_{Q}}$, ${\mathbf{W}_{K}}$, and ${\mathbf{W}_{V}}$ into a query ${\mathbf{q}}_i$, a key ${\mathbf{k}}_j$, and a value, and computes pairwise attention weights over the whole sequence:

$$
{A_{ij}} = \frac{\exp\left({\mathbf{q}}_i^\top {\mathbf{k}}_j / \sqrt{{d_{\text{head}}}}\right)}{\sum_{{m}} \exp\left({\mathbf{q}}_i^\top {\mathbf{k}}_{{m}} / \sqrt{{d_{\text{head}}}}\right)}
$$

 A text token such as “handle” can attend to visual patch tokens, but a high attention weight is not a verified grasp location or metric pose. A trained spatial decoder may produce a 2D affordance heatmap, and placing the gripper in 3D still takes depth evidence, camera calibration, and the metric lifting below. A rolling key-value (KV) cache stores prior token states for attention. It neither tracks object permanence nor maintains a 3D position and velocity; an explicit state estimator must associate observations across frames and widen its uncertainty while the mug is occluded.

#### Pinhole Back-Projection and 3D Metric Lifting

^pinhole-back-projection-and-3d-metric-lifting

Standard 2D patch tokens lack metric scale due to projective ambiguity: along any optical ray ${\lambda} [{u}, {v}, 1]^\top$, infinitely many 3D points project to identical pixel coordinates. To interface with physical control barrier filters, kinetic stopping calculators, and obstacle clearance envelopes, 2D visual predictions must be lifted into metric 3D coordinates ${\mathbf{p}_{\text{world}}} \in \mathbb{R}^3$.

Let $[{u}, {v}]^\top$ denote pixel coordinates on the image sensor, and let the calibrated pinhole camera intrinsic matrix be:

$$
{\mathbf{K}} = \begin{bmatrix} {f_x} & 0 & {c_x} \\ 0 & {f_y} & {c_y} \\ 0 & 0 & 1 \end{bmatrix}
$$

 where $({f_x}, {f_y})$ are focal lengths in pixels and $({c_x}, {c_y})$ is the principal point. Given an aligned optical-axis depth measurement ${Z_{\text{meas}}} = {Z_c} > 0$ (obtained from stereo disparity, time-of-flight lidar, or calibrated depth sensors), the 3D position in the camera coordinate frame ${\mathbf{p}_c} \in \mathbb{R}^3$ is recovered via inverse intrinsic projection:

$$
{\mathbf{p}_c} = {Z_{\text{meas}}} \cdot {\mathbf{K}}^{-1} \begin{bmatrix} {u} \\ {v} \\ 1 \end{bmatrix} = \begin{bmatrix} ({u} - {c_x}) \frac{{Z_{\text{meas}}}}{{f_x}} \\ ({v} - {c_y}) \frac{{Z_{\text{meas}}}}{{f_y}} \\ {Z_{\text{meas}}} \end{bmatrix}
$$

 Transforming ${\mathbf{p}_c}$ into the robot base or world frame ${W}$ uses the rigid extrinsic transform ${\mathbf{T}_{WC}} \in {SE(3)}$ defined in this section:

$$
{\tilde{\mathbf{p}}_W} = {\mathbf{T}_{WC}} {\tilde{\mathbf{p}}_C} \implies {\mathbf{p}_{\text{world}}} = {\mathbf{R}_{WC}} {\mathbf{p}_c} + {\mathbf{t}_{WC}}
$$

 A sensor reporting range along a ray must first convert it to optical-axis depth; substituting raw range for ${Z_{\text{meas}}}$ distorts off-axis geometry. The permission path and kinematic reachability evaluators require this metric 3D reconstruction; ungrounded 2D tokens cannot establish whether a proposed trajectory satisfies physical clearance boundaries ${d_{\text{stop}}}$.

### Camera-To-Bird’s-Eye-View Lifting

^sec-appendix-ml-bev-lifting

Checking whether a mobile base can pass a warehouse pillar requires obstacle footprints in meters on the floor plane, whereas each onboard camera observes the aisle in perspective pixels along rays of unknown depth. A bird’s-eye-view (BEV) representation places the features of every camera in one metric grid on the ground plane, the frame in which planners and clearance checks work. [[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^fig-08-ray-frustum-voxel-lifting|Figure 1]] stages this transformation across four sequential processing blocks. Monocular 2D feature extraction works on the raw camera images. Categorical depth distribution estimation lifts each feature ray into a 3D frustum of discrete hypothesis bins. Extrinsic coordinate transformation splats the frustum points into a metric ground-plane grid of vertical pillars. A final permission gate bounds spatial clearance residuals before dispatching commands.

1.  **Feature extraction.** A vision backbone, such as DINOv2 ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-oquab2023dinov2|Oquab et al. 2023]]) or a lightweight convolutional network, maps image ${\mathbf{I}} \in \mathbb{R}^{{H} \times {W} \times 3}$ to a grid of feature vectors:

$$
{\mathbf{f}_{u, v}} = \text{Backbone}({\mathbf{I}})[{u}, {v}] \in \mathbb{R}^{C}
$$

 Forward projection (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/08 Sensor Perception/V4-08.03 Capture Physics and Calibration#^eq-percep-pinhole-projection|equation 8.2]]**) collapses each 3D ray onto one pixel. Consequently, a feature ${\mathbf{f}_{u, v}}$ stands for a whole ray in space while its metric depth remains unknown.

2.  **Lift.** LSS represents that ambiguity rather than resolving it. Along the bearing ray ${\mathbf{K}}^{-1}[{u}, {v}, 1]^\top$ of **[[01 Books/Volume IV - Physical AI/03 Running the Machine/08 Sensor Perception/V4-08.03 Capture Physics and Calibration#^eq-percep-bearing-ray|equation 8.3]]**, the network scores ${D}$ discrete depth bins spanning $[{d_{\min}}, {d_{\max}}]$, for example 64 bins from 0.5 m to 20 m, spaced linearly or logarithmically:

$$
{\boldsymbol{\alpha}_{u, v}} = \text{softmax}({\mathbf{d}_{u, v}}) \in {\Delta}^{{D}-1}
$$

 An outer product lifts each 2D feature into a frustum of 3D points, one per depth hypothesis:

$$
{\mathbf{c}_{u, v, k}} = {\alpha_{u, v}}({k}) \cdot {\mathbf{f}_{u, v}} \in \mathbb{R}^{C} \quad \text{at } {\mathbf{p}_c}({u}, {v}, {d}_k) = {d}_k {\mathbf{K}}^{-1} \begin{bmatrix} {u} \\ {v} \\ 1 \end{bmatrix}
$$

 For a feature map 128 cells on a side, with 64 depth bins and 64 feature channels, the frustum tensor holds about 67.1 million values, 134.2 MB per frame at FP16. This is a materialized tensor footprint for one camera. Actual DRAM traffic depends on whether the runtime materializes, tiles, or fuses lifting with pooling; zero-copy handoff avoids an extra copy but does not eliminate tensor reads and writes.

3.  **Splat.** The calibrated extrinsic transform ${\mathbf{T}_{\text{base}}^{\text{cam}}}\in {SE(3)}$, with rotation ${\mathbf{R}_{\text{base}}^{\text{cam}}}$ and translation ${\mathbf{t}_{\text{base}}^{\text{cam}}}$, maps every frustum point from the camera’s optical frame into the robot base frame:

$$
{\mathbf{p}_{\text{body}}} = {\mathbf{R}_{\text{base}}^{\text{cam}}} {\mathbf{p}_c} + {\mathbf{t}_{\text{base}}^{\text{cam}}}
$$

 The workspace is discretized into a grid of vertical pillars, for example 200 cells on a side covering a 20 m square at 0.1 m resolution. The splat sums every frustum feature that falls within pillar $({X}, {Y})$, using accelerated cumulative sums or point-pillar pooling ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-philion2020lift|Philion and Fidler 2020]]; [[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-liu2023bevfusion|Liu et al. 2023]]):

$$
{\mathbf{V}_{\text{BEV}}}({X}, {Y}) = \sum_{({u}, {v}, k) \in \text{Pillar}({X}, {Y})} {\mathbf{c}_{u, v, k}}
$$

 On parallel GPU accelerators, naive scatter-add operations create severe write-port contention and non-coalesced DRAM transactions when hundreds of frustum points map to the identical BEV pillar. Optimized runtimes eliminate this bottleneck by sorting frustum points by pillar index and executing parallel cumulative-sum prefix scans or precomputed index-table indirection ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-liu2023bevfusion|Liu et al. 2023]]). The splat aligns the cameras’ hypotheses in one metric frame. It cannot fill a region no camera saw or remove depth-scale error, so the footprint it assigns to a pedestrian still depends on the depth hypotheses and the calibration. That dependence is why the clearance panel closing [[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^fig-08-ray-frustum-voxel-lifting|figure 1]] marks depth as estimated and only the inset as checked.

![[90 Assets/Volume IV/Shared Figures/Fig08 Ray Frustum Voxel Lifting 97b8c01fd3.svg]]

*Four stages show image features, a ray with several learned depth hypotheses, a shared bird's-eye-view grid, and a clearance decision. The last panel labels depth as estimated and the inset as checked; learned depth-bin weights alone do not establish a metric error bound.*

Figure 1: **Camera ray frustum lifting and BEV splatting**: LSS ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-philion2020lift|Philion and Fidler 2020]]) places learned depth hypotheses from each camera in a shared metric BEV frame; that coordinate transform does not resolve monocular depth ambiguity. The final clearance inset requires separately validated metric residuals, bias, and a chosen tail quantile or deterministic error bound before permission. (Architecture adapted from Philion and Fidler ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-philion2020lift|2020]]).)

^fig-08-ray-frustum-voxel-lifting

The softmax over depth bins expresses weights the model assigns, and its entropy is not a calibrated metric covariance. The clearance inset of **[[01 Books/Volume IV - Physical AI/03 Running the Machine/08 Sensor Perception/V4-08.07 Spatial Error and Clearance Bounds#^sec-perception-error-clearance|Spatial Error and Clearance Bounds]]** therefore rests on separately validated spatial residuals, not on the lifted weights.

### Inverse-Depth Parameterization

^inverse-depth-parameterization

In visual-inertial odometry and SLAM, representing distant 3D landmarks in standard Cartesian coordinates $({x}, {y}, {z})$ induces extreme non-linearity: small pixel tracking errors produce quadratic depth errors (${\delta} {z} \propto {z}^2$). Under **inverse-depth parameterization**, a 3D feature is parameterized by the 6D vector ${\mathbf{y}} = [{x}_0, {y}_0, {z}_0, {\theta_{\text{az}}}, {\phi}, {\rho}]^\top$. Here $({x}_0, {y}_0, {z}_0)$ is the optical center when first observed, $({\theta_{\text{az}}}, {\phi})$ are azimuth and elevation angles, and ${\rho} = 1/{d}$ is inverse depth:[[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^fn3|³]]

$$
{\mathbf{p}}({d}) = \begin{bmatrix} {x}_0 \\ {y}_0 \\ {z}_0 \end{bmatrix} + \frac{1}{{\rho}} \begin{bmatrix} \cos{\phi} \sin{\theta_{\text{az}}} \\ -\sin{\phi} \\ \cos{\phi} \cos{\theta_{\text{az}}} \end{bmatrix}
$$

 At optical infinity (${d} \to \infty$), inverse depth approaches zero (${\rho} \to 0$). This parameterization can improve estimator conditioning for distant features; covariance shape and numerical stability still depend on the measurement model, noise assumptions, and estimator implementation.

### 3D Gaussian Splatting Parameters

^sec-appendix-ml-3dgs

A neural scene reconstructed from camera images can render a photorealistic view of a workcell while filling unobserved regions with semi-transparent floaters or hollow shells that offer no conservative collision surface. Continuous neural scene representations parameterize physical environments through collections of 3D Gaussians ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-kerbl20233d|Kerbl et al. 2023]]), where each Gaussian ${G}_i({\mathbf{p}})$ is defined by four core physical and radiometric attributes:

1.  **Spatial mean (${\boldsymbol{\mu}}_i \in \mathbb{R}^3$):** The 3D centroid in world coordinates.
2.  **Covariance matrix (${\boldsymbol{\Sigma}}_i \in \mathbb{R}^{3 \times 3}$):** Defining ellipsoidal shape and orientation. To guarantee that ${\boldsymbol{\Sigma}}_i$ remains symmetric and positive semi-definite throughout gradient descent, it is factorized into an orthonormal rotation matrix ${\mathbf{R}}_i \in {SO(3)}$ (parameterized by a unit quaternion ${{\mathbf{q}_{\text{quat}}}}_i$) and a positive scaling diagonal matrix ${\mathbf{S}}_i = \text{diag}({{s_{x}}}_i, {{s_{y}}}_i, {{s_{z}}}_i)$:

$$
{\boldsymbol{\Sigma}}_i = {\mathbf{R}}_i {\mathbf{S}}_i {\mathbf{S}}_i^\top {\mathbf{R}}_i^\top
$$

3.  **Radiance appearance (${c}_i$):** Parameterized via Spherical Harmonics (SH) coefficients up to degree 3 (16 coefficients per color channel) to capture view-dependent specular reflections.
4.  **Opacity (${\alpha}_i \in [0, 1]$):** Modeled via a sigmoid activation ${\alpha}_i = {\sigma}({o}_i) = \frac{1}{1 + e^{-{o}_i}}$ over unbounded logit ${o}_i \in \mathbb{R}$ to bound opacity. Sigmoid gradients can still vanish near saturation.

#### Camera Projection and Screen-Space Covariance

^camera-projection-and-screen-space-covariance

During real-time novel-view synthesis, 3D Gaussians are transformed into the camera optical frame via rigid extrinsic transform ${\mathbf{T}_{CW}}\in {SE(3)}$, where ${\mathbf{R}_{CW}} \in {SO(3)}$ is the rotational component:

$$
{\mathbf{p}_c} = [{x}, {y}, {z}]^\top = {\mathbf{R}_{CW}} {\boldsymbol{\mu}}_i + {\mathbf{t}_{CW}}
$$

 The pinhole camera model projects 3D point ${\mathbf{p}_c}$ to image pixel coordinates $[{u}, {v}]^\top$:

$$
\pi({x}, {y}, {z}) = \begin{bmatrix} {f_x} \frac{{x}}{{z}} + {c_x} \\ {f_y} \frac{{y}}{{z}} + {c_y} \end{bmatrix}
$$

 Because perspective projection is non-linear in depth ${z}$, 3D Gaussian Splatting applies an affine first-order Taylor approximation evaluated at the Gaussian center ${\mathbf{p}_c}$. The projection Jacobian ${\mathbf{J}} \in \mathbb{R}^{2 \times 3}$ evaluates to:

$$
{\mathbf{J}} = \frac{\partial \pi}{\partial {\mathbf{p}_c}} = \begin{bmatrix} \frac{\partial {u}}{\partial {x}} & \frac{\partial {u}}{\partial {y}} & \frac{\partial {u}}{\partial {z}} \\ \frac{\partial {v}}{\partial {x}} & \frac{\partial {v}}{\partial {y}} & \frac{\partial {v}}{\partial {z}} \end{bmatrix} = \begin{bmatrix} \frac{{f_x}}{{z}} & 0 & -\frac{{f_x} {x}}{{z}^2} \\ 0 & \frac{{f_y}}{{z}} & -\frac{{f_y} {y}}{{z}^2} \end{bmatrix}
$$

 The projected 2D screen-space covariance ${\boldsymbol{\Sigma}_{2D}} \in \mathbb{R}^{2 \times 2}$ is then:

$$
{\boldsymbol{\Sigma}_{2D}} = {\mathbf{J}} {\mathbf{R}_{CW}} {\boldsymbol{\Sigma}}_i {\mathbf{R}_{CW}}^\top {\mathbf{J}}^\top
$$

 where a low-pass filter (${\boldsymbol{\Sigma}_{2D}'} = {\boldsymbol{\Sigma}_{2D}} + {s} {\mathbf{I}}_2$ with ${s} \approx 0.3\text{ pixel}^2$) is added to prevent aliasing when a Gaussian projects to sub-pixel footprints.

#### Differentiable Alpha-Blending and Clearance Limits

^differentiable-alpha-blending-and-clearance-limits

To render pixel color ${C}({u}, {v})$, tile-based rasterization bins Gaussians into $16 \times 16$ pixel screen tiles, sorts overlapping Gaussians along the camera optical axis by depth ${z}$, and computes front-to-back alpha-blended volume rendering:

$$
{C} = \sum_{i \in {\mathcal{N}}} {c}_i {\alpha'}_i {T}_i, \quad \text{where } {T}_i = \prod_{j=1}^{{i}-1} (1 - {\alpha'}_j)
$$

 Here ${T}_i$ represents cumulative optical transmittance along the viewing ray, initialized to ${T}_1=1$. In this rendering equation, ${\alpha'}_i$ is the pixel-dependent opacity contribution, including the projected Gaussian footprint, rather than the stored opacity ${\alpha}_i$. An implementation may terminate when the remaining transmittance is sufficiently small; the error tolerance, scene density, and hardware determine the resulting speed.

However, a physical AI systems engineer must recognize the boundary between visual rendering and physical clearance. The 3D Gaussian parameters are optimized strictly against 2D photometric rendering loss (such as $\ell_1$ color difference and SSIM). Gaussians frequently fit unobserved scene regions with semi-transparent “floaters,” hollow shells, or blurred volumetric density. Neither the stored opacity ${\alpha}_i$ nor the spatial gradient $\nabla_{{\mathbf{p}}} {G}_i({\mathbf{p}})$ of its density constitutes a conservative collision surface. [[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^fig-3dgs-slam-splatam|Figure 2]] partitions this architectural handoff across three functional panels. Panel (a) tracks camera poses from an incoming RGB-D stream. Panel (b) maintains the 3D Gaussian memory primitives (mean, covariance ellipsoid, opacity, and spherical-harmonic color) under adaptive splitting, cloning, and pruning. Panel (c) decouples photometric rasterization from physical safety, routing Gaussian primitives through an unvalidated candidate occupancy or signed distance field before an explicit error-bounding step admits the clearance envelope.

![[90 Assets/Volume IV/Shared Figures/Fig09 Canonical 3dgs Memory 219bb2bfb1.svg]]

*Three-panel schematic. Panel a: an RGB-D stream feeds pose tracking, which outputs the camera pose. Panel b: a Gaussian scene memory holding 3D Gaussians with mean, covariance, opacity, and spherical-harmonic color, drawn as three oriented ellipses, above an adaptive density control step that splits, clones, and prunes. Panel c: a rasterize arrow leads to novel-view rendering, a visual output; a convert arrow leads to a dashed candidate occupancy or distance field marked not yet validated, which connects to an error-bound-then-clearance step.*

Figure 2: **Gaussian memory and clearance handoff**: Camera observations update a Gaussian scene for novel-view rendering. Its visual output does not directly supply conservative collision distance; a separately validated geometry or occupancy conversion and permission check are required ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-kerbl20233d|Kerbl et al. 2023]]; [[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-matsuki2024gaussian|Matsuki et al. 2024]]).

^fig-3dgs-slam-splatam

Storage per primitive depends on its packing and spherical-harmonic degree, so a map’s footprint is its primitive count times that packing. A dense cubic grid instead stores $\mathcal{O}({N}^3)$ cells, and a sparse occupancy map stores only allocated structure, whose size depends on the observed geometry and the accuracy target. [[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^fig-09-volumetric-memory-scaling|Figure 3]] plots these three storage scaling regimes on logarithmic axes as grid resolution spans from 10 to $10^4$ cells per dimension. The cubic grid grows steeply as $\mathcal{O}({N}^3)$ and passes gigabytes at modest resolutions. The surface-allocated octree scales along an $\mathcal{O}({N}^2)$ trajectory. The stylized Gaussian scene maintains a flat baseline under an assumed fixed primitive count of 500,000 elements.

![[90 Assets/Volume IV/Shared Figures/Cell 4 Output 1 c732d95edc.png]]

*Log-scale plot of calculated storage against grid cells per dimension for a dense cubic voxel grid, an assumed surface-allocated octree, and a Gaussian scene held at a fixed primitive count. The fixed Gaussian line is an assumption, not a claim of constant cost at equal geometric fidelity.*

Figure 3: **Constructed spatial-memory storage scenarios**: A dense cube uses four bytes per voxel, the octree allocates one 32-byte surface cell per squared grid dimension, and the Gaussian scene holds a fixed count and packing while grid resolution varies. These are storage models, not equal-fidelity or measured runtime benchmarks; Gaussian count must rise if a stricter geometry target requires it.

^fig-09-volumetric-memory-scaling

For the Gaussian packing in the plot, 500,000 primitives at 56 bytes each require 28 MB. A deployment chooses its representation after measuring map completeness, update time, query time, and the conversion needed for conservative clearance.

### Log-Odds Occupancy and Signed-Distance Fusion

^sec-appendix-ml-voxels

When a pallet jack moves out of a warehouse aisle, an occupancy map that records only range hits leaves a phantom obstacle blocking the path unless subsequent sensor rays actively clear the empty sightlines. Discrete volumetric grids model 3D occupancy uncertainty through recursive Bayesian estimation. Let ${m}_i \in \{0, 1\}$ denote the binary occupancy state of voxel ${i}$ (${m}_i = 1$ occupied, ${m}_i = 0$ free). Given a temporal sequence of range observations ${z_{1:t}} = ({z}_1, \dots, {z}_t)$, Bayes’ rule expresses the posterior occupancy:

$$
{p}({m}_i \mid {z_{1:t}}) = \frac{{p}({z}_t \mid {m}_i, {z_{1:t-1}}) {p}({m}_i \mid {z_{1:t-1}})}{{p}({z}_t \mid {z_{1:t-1}})}
$$

 Assuming that observation ${z}_t$ is conditionally independent of past observations given the true static occupancy ${m}_i$ (${p}({z}_t \mid {m}_i, {z_{1:t-1}}) = {p}({z}_t \mid {m}_i)$), and writing the identical relation for the unoccupied state $\neg {m}_i$ (${m}_i = 0$):

$$
{p}(\neg {m}_i \mid {z_{1:t}}) = \frac{{p}({z}_t \mid \neg {m}_i) {p}(\neg {m}_i \mid {z_{1:t-1}})}{{p}({z}_t \mid {z_{1:t-1}})}
$$

 Dividing the two equations cancels the common evidence normalizer ${p}({z}_t \mid {z_{1:t-1}})$:

$$
\frac{{p}({m}_i \mid {z_{1:t}})}{{p}(\neg {m}_i \mid {z_{1:t}})} = \frac{{p}({z}_t \mid {m}_i)}{{p}({z}_t \mid \neg {m}_i)} \frac{{p}({m}_i \mid {z_{1:t-1}})}{{p}(\neg {m}_i \mid {z_{1:t-1}})}
$$

 Applying Bayes’ rule to the measurement likelihood ${p}({z}_t \mid {m}_i) = \frac{{p}({m}_i \mid {z}_t) {p}({z}_t)}{{p}({m}_i)}$ gives the measurement odds ratio:

$$
\frac{{p}({z}_t \mid {m}_i)}{{p}({z}_t \mid \neg {m}_i)} = \frac{{p}({m}_i \mid {z}_t)}{1 - {p}({m}_i \mid {z}_t)} \frac{1 - {p}({m}_i)}{{p}({m}_i)}
$$

 Taking the natural logarithm of the odds ratio defines the log-odds quantity ${L}({x}) = \ln \frac{{p}({x})}{1 - {p}({x})}$. Substituting yields the canonical **additive log-odds update**:[[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^fn4|⁴]]

$$
{L}_t({m}_i) = {L}_{t-1}({m}_i) + \underbrace{\ln \frac{{p}({m}_i \mid {z}_t)}{1 - {p}({m}_i \mid {z}_t)}}_{\text{inverse sensor model } {L_{\text{sensor}}}} - \underbrace{\ln \frac{{p}({m}_i)}{1 - {p}({m}_i)}}_{\text{prior belief } {L}_0}
$$

 where ${p}({m}_i \mid {z}_t)$ is the calibrated inverse sensor model. When prior belief is uninformative (${p}({m}_i) = 0.5 \implies {L}_0 = 0$), the update reduces to simple addition: ${L}_t({m}_i) = {L}_{t-1}({m}_i) + {L_{\text{sensor}}}$.

Along a range sensor ray, voxels traversed before the hit receive negative log-odds evidence (${L_{\text{free}}} < 0$), while the voxel containing the return receives positive evidence (${L_{\text{occ}}} > 0$). Voxels beyond the return receive no update. With the uninformative prior used here, zero evidence corresponds to ${L_{\text{sensor}}}=0$. To prevent numerical saturation lockup where an obstacle that was observed occupied hundreds of times requires hundreds of empty observations before clearing, updates are clamped within finite bounds $[{L_{\min}}, {L_{\max}}]$ (e.g., $[-2.0, +3.5]$).

#### Octree Occupancy and Free-Space Raycasting

^octree-occupancy-and-free-space-raycasting

Occupancy grid mapping ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-elfes1989using|Elfes 1989]]) tessellates space into cells and applies this update to every cell a ray touches. A volumetric raycast walks each return’s sightline with the three-dimensional digital differential analyzer (3D-DDA) traversal ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-amanatides1987fast|Amanatides and Woo 1987]]). Hierarchical stores such as OctoMap ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-hornung2013octomap|Hornung et al. 2013]]) and OpenVDB ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-museth2013vdb|Museth 2013]]) allocate cells only where rays have passed, so storage follows the observed volume rather than the bounding cube. [[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^fig-09-octomap-volumetric-mapping|Figure 4]] traces this spatial-memory pipeline across three successive representations during an indoor mobile robot traversal. Panel (a) shows the unorganized, noisy 3D point cloud acquired by a tilting range scanner. Panel (b) shows the hierarchical 8-ary octree that adaptively clusters occupied volumes. Panel (c) shows the explicit ternary classification that differentiates confirmed free-space voxels (white) and occupied obstacle cells (dark) from unobserved unknown volumes. Free-space evidence recorded along ray sightlines lets the map retire a phantom obstacle once the same region is seen empty, while a never-observed cell stays unknown however long the map runs. **[[01 Books/Volume IV - Physical AI/03 Running the Machine/09 Spatial Memory/V4-09.07 Certified Spatial Assertions in Scene Memory#^sec-memory-scene-attention-buffers|Certified Spatial Assertions in Scene Memory]]** applies this rule to the aisle, where only fresh free-space evidence can vouch that a path is clear.

![[90 Assets/Volume IV/Shared Figures/Fig09 Real Octomap Volumetric Mapping cf336abfba.png]]

*Probabilistic 3D Volumetric Mapping and Hierarchical Octree Space Subdivision. Empirical 3D spatial memory representation reconstructed from a physical mobile robot traversing an indoor corridor with a tilting lidar scanner. (a) Raw 3D point cloud acquired during robot motion, subject to sensor noise and finite field-of-view occlusions. (b) Volumetric OctoMap voxel representation modeling 3D space as an 8-ary hierarchical tree, where occupied volumes are probabilistically updated and stored across variable resolutions. (c) Explicit free-space raycasting and lossless octree pruning, differentiating observed free cells (white voxels) from occupied obstacles (dark voxels) and unobserved unknown regions; free evidence alone does not certify traversability for a particular robot. By maintaining explicit free-space evidence along sensor sightlines, spatial memory actively invalidates phantom obstacle tracks without waiting for arbitrary software timeouts.*

Figure 4: **Probabilistic octree volumetric mapping**: A corridor traversal reconstructed from raw point cloud into a probabilistic octree and then into explicit free, occupied, and unknown space ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-hornung2013octomap|Hornung et al. 2013]]). The third panel is what distinguishes spatial memory from an accumulated point cloud, because raycasting records evidence of emptiness along sightlines, letting the map actively retire a phantom obstacle track instead of waiting for a timeout to expire it. (Credit: Autonomous Intelligent Systems Lab, University of Freiburg ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-hornung2013octomap|Hornung et al. 2013]]).)

^fig-09-octomap-volumetric-mapping

#### Truncated Signed Distance Fusion

^truncated-signed-distance-fusion

A truncated signed distance field (TSDF), fused volumetrically at camera rate by KinectFusion ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-newcombe2011kinectfusion|Newcombe et al. 2011]]) and incrementally on robots by Voxblox ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-oleynikova2017voxblox|Oleynikova et al. 2017]]), stores in each voxel ${\mathbf{p}_{\text{vox}}}$ a *metric projective distance* ${D}({\mathbf{p}_{\text{vox}}}) \in [-{\mu_{\text{tsdf}}}, +{\mu_{\text{tsdf}}}]$. This distance is positive in front of an observed return along its sensing ray. Each voxel also stores a dimensionless fusion weight ${W}({\mathbf{p}_{\text{vox}}})$. For a calibrated depth image, transform the voxel center into camera coordinates ${\mathbf{p}_c} = [{X_c}, {Y_c}, {Z_c}]^\top$ and project it to pixel $({u}, {v})$. Its projective sample is ${s} = {Z_{\text{meas}}}({u}, {v}) - {Z_c}$. For a range ray, the equivalent along-ray sample is ${s} = {r_{\text{hit}}} - {r_{\text{voxel}}}$; both are positive before the hit. Near the return, the sample is clamped in meters and fused into the running weighted average:

$$
{d_{\mu}}({\mathbf{p}_{\text{vox}}}) = \max(-{\mu_{\text{tsdf}}}, \min({\mu_{\text{tsdf}}}, {s})), \qquad {D}_t({\mathbf{p}_{\text{vox}}}) = \frac{{W}_{t-1}({\mathbf{p}_{\text{vox}}}) {D}_{t-1}({\mathbf{p}_{\text{vox}}}) + {w}_t {d_{\mu}}({\mathbf{p}_{\text{vox}}})}{{W}_{t-1}({\mathbf{p}_{\text{vox}}}) + {w}_t}
$$

 where ${w}_t$ is the dimensionless observation weight and the stored weight ${W}_t = {W}_{t-1} + {w}_t$ is capped at ${W_{\max}}$. Fusion uses a valid capture-time pose and refuses a sample older than the voxel’s last evidence epoch. A negative sample just behind the measured return contributes to the local zero crossing under the surface model; it does not certify an unseen obstacle interior.

Interpolating observed samples gives an approximate gradient near a zero crossing, limited by unknown voxels, projective bias, discretization, and moving objects. A projective TSDF is therefore not the nearest-surface Euclidean distance a clearance decision needs. A clearance query therefore reads a validated occupancy or Euclidean signed distance field (ESDF) with an unknown-space policy, the conversion **[[01 Books/Volume IV - Physical AI/03 Running the Machine/09 Spatial Memory/V4-09.07 Certified Spatial Assertions in Scene Memory#^sec-memory-scene-attention-buffers|Certified Spatial Assertions in Scene Memory]]** requires of every scene representation before the permission path relies on it.

#### One Frame’s Update and Its Memory Traffic

^one-frames-update-and-its-memory-traffic

Each incoming depth frame must pass a freshness gate before updating occupancy along its rays and fusing TSDF samples inside the truncation band ([algorithm 1](https://mlsysbook.ai/vol4/backmatter/appendix_ml.html#algo-volumetric-tsdf-raycast)), and the notebook after the pseudocode prices the resulting update traffic that **[[01 Books/Volume IV - Physical AI/03 Running the Machine/09 Spatial Memory/V4-09.07 Certified Spatial Assertions in Scene Memory#^sec-memory-scene-attention-buffers|Certified Spatial Assertions in Scene Memory]]** charges against the memory bus. The update procedure rejects the frame before touching the map when its capture epoch is too old or older than the last evidence of any cell it would update. It then clears and marks occupancy along each ray and fuses TSDF samples only inside the truncation band. Every updated cell takes the capture epoch, not the update time, so a later consumer can judge each cell’s freshness.

$\mathcal{P}$

**Napkin Math 1.1: DRAM bandwidth of 3D TSDF voxel grids**

**Practical Engineering Question**: What are the distance-and-weight payload and modeled DRAM bandwidth of sparse vs. dense TSDF representations?

*1. Dense allocation.* A manipulation workcell of 10 m $\times$ 10 m $\times$ 3 m (300 m³) at 1 cm pitch holds 300,000,000 voxels. At 4 bytes per voxel (16-bit distance plus 16-bit fusion weight), excluding occupancy, per-cell evidence epochs, and allocator overhead, the distance-and-weight payload is 1.20 GB. Refining the pitch to 5 mm for tool contact raises the count to 2,400,000,000 voxels and the partial payload to 9.60 GB, which alone exceeds an illustrative 8 GB memory budget.

*2. Sparse allocation.* Surfaces occupy a thin manifold within the volume. Grouping voxels into 512-voxel leaf blocks and allocating only within the truncation band, assumed to be 3 percent of the volume, gives 17,579 blocks. With a 32-byte leaf header, the payload is 36.6 MB at 1 cm and 292.5 MB at 5 mm. A full map must also budget the separate occupancy layer, per-cell epochs, block lookup and allocator metadata, and capacity for the unknown-space policy.

*3. Traversal and DRAM traffic.* A 640 $\times$ 480 depth stream at 60 Hz supplies 18.432 million rays per second. Along a 3 m ray at 1 cm pitch the traversal visits 300 cells. The 294 cells before the hit receive occupancy free-ray updates, and the 6 cells near the return receive TSDF fusion. Sparse TSDF allocation saves map capacity; it removes neither the traversal nor the occupancy updates. At 8 bytes of assumed read/write traffic per update, sending every update to DRAM costs 44.2 GB/s. At an assumed 95 percent cache hit fraction for both occupancy and TSDF updates, the modeled DRAM demand falls to 2.21 GB/s, a 20× reduction. The hit rate depends on ray overlap, atomics, evictions, and writeback on the chosen hardware; it is an input to measure, not a property of the map structure.

**Systems insight**: Sparse allocation yields 33× less modeled TSDF payload in this surface-fraction scenario, while bus demand depends on measured locality and on all traversed-cell work. Whether that demand fits beside policy inference on a shared bus is the contention question of **[[01 Books/Volume IV - Physical AI/03 Running the Machine/13 Workload Placement/V4-13.04 Contention for Shared Resources#^sec-placement-resource-contention|Contention for Shared Resources]]**.

## Function Approximation and Sensitivity Bounds

^sec-appendix-ml-sensitivity

A sensor perturbation can change a neural action proposal even when the physical scene has barely moved. A sensitivity bound limits that change relative to the input error and supplies a quantity to compare with available actuator headroom. The bound concerns the proposal; the permission path must still check the plant state and enforce current limits.

### Multilayer Perceptrons in Continuous Control

^sec-appendix-ml-mlp

For high-rate proprioceptive feedback loops (such as $500\text{--}1000\text{ Hz}$ quadruped balance, bipedal locomotion, and arm impedance control), physical policies frequently employ **Multilayer Perceptrons (MLPs)** rather than deep spatial transformers. A canonical continuous MLP policy takes a low-dimensional proprioceptive vector ${\mathbf{x}} \in \mathbb{R}^{{d}}$ (joint positions ${\mathbf{q}}$, velocities ${\dot{\mathbf{q}}}$, IMU angular rates, projected gravity, and previous action history). It then evaluates a sequence of ${N_L}$ affine transformations interleaved with element-wise non-linear activations:

$$
{\mathbf{h}}_0 = {\mathbf{x}}, \quad {\mathbf{h}}_{{\ell}} = {f}_{{\ell}}({\mathbf{W}}_{{\ell}} {\mathbf{h}}_{{\ell}-1} + {\mathbf{b}}_{{\ell}}) \quad \text{for } {\ell}=1, \dots, {N_L}, \quad \pi({\mathbf{x}}) = {\mathbf{W}_{\text{out}}} {\mathbf{h}}_{{N_L}} + {\mathbf{b}_{\text{out}}}
$$

 where ${\mathbf{W}}_{{\ell}} \in \mathbb{R}^{{n}_{{\ell}} \times {n}_{{\ell}-1}}$ are weight matrices and ${\mathbf{b}}_{{\ell}} \in \mathbb{R}^{{n}_{{\ell}}}$ are bias vectors.

#### Systems Profile and Roofline Limits of MLP Policies

^systems-profile-and-roofline-limits-of-mlp-policies

A compact MLP can keep its weights and activations in on-chip memory, reducing interference from camera direct memory access and other DRAM clients. Capacity alone does not establish residency: cache replacement, shared clients, scheduling, and accelerator transfers determine the memory level that supplies each layer.

For a dense layer with ${d_{\text{in}}}{d_{\text{out}}}$ weights, a single input vector requires approximately $2{d_{\text{in}}}{d_{\text{out}}}$ floating-point operations. If each weight occupies ${s_{\text{elem,W}}}$ bytes and is read once from the memory level being analyzed, the weight-only arithmetic intensity is

$$
{I_{\text{MLP}}} \approx \frac{2}{{s_{\text{elem,W}}}}\;\text{FLOP/byte}.
$$

 Activation traffic lowers this ratio; weight reuse across inputs raises it. The relevant roofline compares this intensity with compute throughput divided by bandwidth at that same memory level. Cache-resident weights therefore change the applicable bandwidth, not the amount of arithmetic.

A deployment budgets weights, scratch buffers, and hidden activations together, preallocates runtime storage, and measures or bounds worst-case execution under interference. A short average forward pass does not by itself justify placing inference in an interrupt handler or guarantee a control deadline.

### Lipschitz Continuity and Spectral Normalization

^sec-appendix-ml-lipschitz

Bounding how strongly a network amplifies input perturbations requires a global sensitivity constant. A neural policy $\pi: {\mathcal{X}} \to {\mathcal{U}}$ is ${L_{\text{lip}}}$-Lipschitz continuous if there exists a non-negative scalar constant ${L_{\text{lip}}}$ such that for all ${\mathbf{x}}_1, {\mathbf{x}}_2 \in {\mathcal{X}}$:

$$
\| \pi({\mathbf{x}}_1) - \pi({\mathbf{x}}_2) \|_{{\mathcal{U}}} \le {L_{\text{lip}}} \| {\mathbf{x}}_1 - {\mathbf{x}}_2 \|_{{\mathcal{X}}}
$$

 For a feedforward network with ${N_L}$ layers $\pi({\mathbf{x}}) = {f}_{{N_L}}({\mathbf{W}}_{{N_L}} \dots {f}_1({\mathbf{W}}_1 {\mathbf{x}}))$, let ${{L_{\phi}}}_k$ bound each activation’s slope over the input domain. The composed Lipschitz bound is:

$$
{L_{\text{lip}}} \le \prod_{k=1}^{{N_L}} {{L_{\phi}}}_k \| {\mathbf{W}}_k \|_2
$$

 where $\|{\mathbf{W}}_k\|_2 = {\sigma_{\max}}({\mathbf{W}}_k)$ is the spectral norm (the largest singular value of weight matrix ${\mathbf{W}}_k$). Standard activations such as ReLU and Tanh are 1-Lipschitz in their scalar forms; exact GeLU has maximum derivative about $1.1289$, so assigning it a factor of one would understate the bound.

The product is an upper bound, not necessarily the smallest Lipschitz constant. Its physical interpretation depends on normalization. A network receiving position and velocity in different units needs declared input scales; converting its normalized output to torque introduces another scale factor. Without those conversions, multiplying a position error by a dimensionless network bound cannot yield a torque error.

To bound policy sensitivity directly during training, **spectral normalization** reparameterizes each weight matrix by its spectral norm:

$$
{\overline{\mathbf{W}}}_k = \frac{{\mathbf{W}}_k}{{\sigma_{\max}}({\mathbf{W}}_k)}
$$

 where ${\sigma_{\max}}({\mathbf{W}}_k)$ is estimated efficiently via power iteration during forward passes. Division by the exact nonzero spectral norm gives $\|{\overline{\mathbf{W}}}_k\|_2=1$. Finite power iteration generally gives an estimate, not a certified upper bound; a safety argument must account for its error. Even an exact network sensitivity bound does not prove closed-loop plant stability.

### Perturbation Amplification and Supervisory Clamping

^perturbation-amplification-and-supervisory-clamping

In physical systems, input state ${\mathbf{x}}$ is corrupted by sensor measurement noise ${\delta} {\mathbf{x}}$ bounded by $\|{\delta} {\mathbf{x}}\| \le {\epsilon}$. The resulting deviation in commanded control action is bounded by:

$$
\| {\delta} {\mathbf{u}_{\text{nom}}} \| = \| \pi({\mathbf{x}} + {\delta} {\mathbf{x}}) - \pi({\mathbf{x}}) \| \le {L_{\text{lip}}} {\epsilon}
$$

 The constant has output-units per input-unit once normalization is included. Compare ${L_{\text{lip}}}{\epsilon}$ with the actuator headroom at the current operating state. Spectral normalization bounds the network, while stability, safe torque, and sensor validity require a plant model and a state-dependent permission check.

## Imitation Learning and Compounding Covariate Shift

^sec-appendix-ml-compounding

Behavioral cloning fits a policy to demonstrator state-action pairs. Two different failures need different remedies: ambiguous demonstrations can make a point predictor average incompatible actions, while feedback can carry even an accurate predictor into states missing from its training data. The decoder derivations address the first problem; the coupling bound and DAgger address the second.

### Mode Averaging and the Decoders That Avoid It

^sec-appendix-ml-multimodal

When human demonstrators steer left around a central pillar half the time (${\mathbf{a}} = +1.0$) and right the other half (${\mathbf{a}} = -1.0$), a policy trained with mean squared error averages the two commands to ${\mathbf{a}} = 0.0$ and drives dead center into the pillar. To see why squared-error regression produces that collision, consider an imitation learning objective minimizing mean squared error ($\ell_2$ loss) over demonstration distribution ${\mathcal{D}_{\text{demo}}}$:

$$
\min_\pi \mathbb{E}_{({\mathbf{o}}, {\mathbf{a}}) \sim {\mathcal{D}_{\text{demo}}}} \left[ \| {\mathbf{a}} - \pi({\mathbf{o}}) \|_2^2 \right]
$$

 By the law of total expectation, decomposing the error around the conditional mean $\mathbb{E}[{\mathbf{a}} \mid {\mathbf{o}}]$ yields an orthogonal variance decomposition:

$$
\begin{aligned} \mathbb{E}_{{\mathbf{a}} \mid {\mathbf{o}}} \left[ \| {\mathbf{a}} - \pi({\mathbf{o}}) \|_2^2 \mid {\mathbf{o}} \right] &= \mathbb{E}_{{\mathbf{a}} \mid {\mathbf{o}}} \left[ \| ({\mathbf{a}} - \mathbb{E}[{\mathbf{a}} \mid {\mathbf{o}}]) + (\mathbb{E}[{\mathbf{a}} \mid {\mathbf{o}}] - \pi({\mathbf{o}})) \|_2^2 \mid {\mathbf{o}} \right] \\ &= \mathbb{E}_{{\mathbf{a}} \mid {\mathbf{o}}} \left[ \| {\mathbf{a}} - \mathbb{E}[{\mathbf{a}} \mid {\mathbf{o}}] \|_2^2 \mid {\mathbf{o}} \right] + \| \mathbb{E}[{\mathbf{a}} \mid {\mathbf{o}}] - \pi({\mathbf{o}}) \|_2^2 \\ &\quad + 2 \left\langle \mathbb{E}_{{\mathbf{a}} \mid {\mathbf{o}}}[{\mathbf{a}} - \mathbb{E}[{\mathbf{a}} \mid {\mathbf{o}}] \mid {\mathbf{o}}], \, \mathbb{E}[{\mathbf{a}} \mid {\mathbf{o}}] - \pi({\mathbf{o}}) \right\rangle \end{aligned}
$$

 Because $\mathbb{E}_{{\mathbf{a}} \mid {\mathbf{o}}}[{\mathbf{a}} - \mathbb{E}[{\mathbf{a}} \mid {\mathbf{o}}] \mid {\mathbf{o}}] = {\mathbf{0}}$, the cross-term vanishes identically, leaving:

$$
\mathbb{E}_{({\mathbf{o}}, {\mathbf{a}}) \sim {\mathcal{D}_{\text{demo}}}} \left[ \| {\mathbf{a}} - \pi({\mathbf{o}}) \|_2^2 \right] = \mathbb{E}_{{\mathbf{o}}} \left[ \operatorname{Tr}(\operatorname{Cov}({\mathbf{a}} \mid {\mathbf{o}})) \right] + \mathbb{E}_{{\mathbf{o}}} \left[ \| \mathbb{E}[{\mathbf{a}} \mid {\mathbf{o}}] - \pi({\mathbf{o}}) \|_2^2 \right]
$$

 The first term is the irreducible conditional variance of demonstrator behavior. The second term is non-negative and strictly minimized if and only if the policy evaluates to the **conditional expectation**:

$$
\pi^*({\mathbf{o}}) = \mathbb{E}[{\mathbf{a}} \mid {\mathbf{o}}] = \int_{{\mathcal{A}}} {\mathbf{a}}\, {p}({\mathbf{a}} \mid {\mathbf{o}}) \, d{\mathbf{a}}
$$

 In digital machine learning tasks (such as computer vision regression), predicting the conditional expectation over ambiguous targets produces a blurry reconstruction, a soft pixel average that remains safely confined to software memory. In physical AI systems, commanded actions cross the causal boundary into continuous Euclidean space governed by non-convex obstacles, joint limits, and irreversible contact dynamics.

Demonstrator behavior in physical manipulation and navigation is inherently multimodal:

- Dodging an obstacle: an expert steers left (${\mathbf{a}} = +1.0$) or right (${\mathbf{a}} = -1.0$) around a central pillar with equal probability $\Pr({\mathbf{a}} = +1 \mid {\mathbf{o}}) = \Pr({\mathbf{a}} = -1 \mid {\mathbf{o}}) = 0.5$.
- Symmetrical manipulation: an end effector approaches a cylindrical object from azimuth ${\theta_{\text{az}}} = 0^\circ$ or ${\theta_{\text{az}}} = 180^\circ$.
- Assembly routing: threading a flexible cable clockwise or counter-clockwise around a structural fastener.

Because demonstration density ${p}({\mathbf{a}} \mid {\mathbf{o}})$ is supported on disjoint, disconnected modes separated by an obstacle, the conditional expectation computes the arithmetic mean:

$$
\pi^*({\mathbf{o}}) = 0.5(+1.0) + 0.5(-1.0) = 0.0
$$

 This mean action lies in a region of zero demonstration probability ($\Pr({\mathbf{a}} = 0.0 \mid {\mathbf{o}}) = 0$). In the physical workspace, the coordinate ${\mathbf{a}} = 0.0$ corresponds precisely to the geometric position of the central obstacle. Commanding $\pi^*({\mathbf{o}}) = 0.0$ instructs the steering actuator to hold dead center at full cruising speed, driving the physical robot directly into the pillar. In physical autonomy, regression mode averaging does not produce a cosmetic blur; it can propose a collision unless the permission path rejects it.

#### Decoder Families

^decoder-families

A probabilistic decoder can avoid mode averaging by parameterizing the conditional action distribution ${p}({\mathbf{a}} \mid {\mathbf{o}})$ rather than its expectation. The families below trade inference cost against distributional expressiveness; none of them supplies recovery states that the demonstrations lack. **[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06.03 Policy Training Regimes#^sec-training-synthesis-regimes|Policy Training Regimes]]** compares them by the network evaluations each chunk costs, which is where the choice reaches the control deadline.

1.  **Deterministic direct regression (MLP).** A feedforward network trained with squared error predicts one action per observation and, with sufficient capacity and ideal optimization, fits the conditional mean. The restriction comes from the point-output objective, not from MLPs as a network family; an MLP can also parameterize a mixture or stochastic policy. One evaluation avoids iterative sampling cost but does not resolve ambiguous demonstrations.

2.  **Mixture density networks.** A Gaussian mixture head predicts nonnegative weights summing to one, means, and positive-definite covariances:

$$
\pi({\mathbf{a}}\mid {\mathbf{o}})=\sum_{{m}=1}^{M} {w_m}({\mathbf{o}})\,{\mathcal{N}}({\mathbf{a}};{\boldsymbol{\mu}_m}({\mathbf{o}}),{\boldsymbol{\Sigma}_m}({\mathbf{o}})).
$$

 Sampling a component or selecting a mode preserves alternatives in one network evaluation. Computing the mixture mean would restore the original averaging problem. Covariance regularization and component coverage matter because likelihood optimization can collapse a component onto a few observations.

3.  **Implicit behavioral cloning.** Implicit behavioral cloning (IBC) ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-florence2022implicit|Florence et al. 2022]]) learns an energy-based model ${E_\theta}({\mathbf{o}}, {\mathbf{a}}) \in \mathbb{R}$, trained with contrastive or InfoNCE objectives to assign low energy to demonstrated state-action pairs and high energy to counterfactual actions. Inference solves

$$
{\mathbf{a}}^* = \arg\min_{{\mathbf{a}}} {E_\theta}({\mathbf{o}}, {\mathbf{a}})
$$

 An energy function can have several separated minima, and selecting its minimizing action can change discontinuously even when the energy network is continuous. Inference requires iterative derivative-free or gradient-based optimization whose latency and convergence depend on sample counts and accelerator parallelism, with risks of settling into suboptimal local energy minima.

4.  **Conditional diffusion and flow matching.** Diffusion Policy ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-chi2024diffusionpolicy|Chi et al. 2025]]) and flow-matching decoders generate entire action trajectory chunks via iterative denoising or ordinary differential equation (ODE) integration. Their training targets injected noise vectors or continuous velocity fields conditioned on corrupted states, observations, and timesteps rather than clean actions, allowing multimodal sampling instead of directly regressing a clean action mean. Approximation error and the sampling procedure still affect whether distinct modes survive. [[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^sec-appendix-ml-diffusion|Section 1.5.2]] derives both objectives and prices their sampling steps.

5.  **Latent-variable chunking.** Action Chunking with Transformers (ACT) ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-zhao2023learning|Zhao et al. 2023]]) predicts an action trajectory chunk ${\mathbf{A}}_t = ({\mathbf{a}}_{t}, {\mathbf{a}}_{t+1}, \dots, {\mathbf{a}}_{t+{H}-1}) \in \mathbb{R}^{{H} \times {d_a}}$ from observation ${\mathbf{o}}_{t}$ using a Conditional Variational Autoencoder (CVAE). The true objective is to maximize the conditional log-marginal likelihood of demonstrated chunks across dataset ${\mathcal{D}_{\text{demo}}}$:

$$
\ln {p_\theta}({\mathbf{A}}_t \mid {\mathbf{o}}_{t}) = \ln \int_{{\mathcal{Z}}} {p_\theta}({\mathbf{A}}_t, {\mathbf{z}} \mid {\mathbf{o}}_{t}) \, {d}{\mathbf{z}}
$$

 Because this marginalization is intractable, ACT introduces a variational posterior ${q_\phi}({\mathbf{z}} \mid {\mathbf{o}}_{t}, {\mathbf{A}}_t)$ parameterized by a transformer encoder. Expanding the identity with ${p_\theta}({\mathbf{A}}_t, {\mathbf{z}} \mid {\mathbf{o}}_{t}) = {p_\theta}({\mathbf{A}}_t \mid {\mathbf{o}}_{t}, {\mathbf{z}}) {p_\theta}({\mathbf{z}})$:

$$
\begin{aligned} \ln {p_\theta}({\mathbf{A}}_t \mid {\mathbf{o}}_{t}) &= \int_{{\mathcal{Z}}} {q_\phi}({\mathbf{z}} \mid {\mathbf{o}}_{t}, {\mathbf{A}}_t) \ln {p_\theta}({\mathbf{A}}_t \mid {\mathbf{o}}_{t}) \, {d}{\mathbf{z}} \\ &= \int_{{\mathcal{Z}}} {q_\phi}({\mathbf{z}} \mid {\mathbf{o}}_{t}, {\mathbf{A}}_t) \ln \left( \frac{{p_\theta}({\mathbf{A}}_t, {\mathbf{z}} \mid {\mathbf{o}}_{t})}{{q_\phi}({\mathbf{z}} \mid {\mathbf{o}}_{t}, {\mathbf{A}}_t)} \cdot \frac{{q_\phi}({\mathbf{z}} \mid {\mathbf{o}}_{t}, {\mathbf{A}}_t)}{{p_\theta}({\mathbf{z}} \mid {\mathbf{o}}_{t}, {\mathbf{A}}_t)} \right) {d}{\mathbf{z}} \\ &= \int_{{\mathcal{Z}}} {q_\phi}({\mathbf{z}} \mid {\mathbf{o}}_{t}, {\mathbf{A}}_t) \ln \frac{{p_\theta}({\mathbf{A}}_t, {\mathbf{z}} \mid {\mathbf{o}}_{t})}{{q_\phi}({\mathbf{z}} \mid {\mathbf{o}}_{t}, {\mathbf{A}}_t)} \, {d}{\mathbf{z}} + \int_{{\mathcal{Z}}} {q_\phi}({\mathbf{z}} \mid {\mathbf{o}}_{t}, {\mathbf{A}}_t) \ln \frac{{q_\phi}({\mathbf{z}} \mid {\mathbf{o}}_{t}, {\mathbf{A}}_t)}{{p_\theta}({\mathbf{z}} \mid {\mathbf{o}}_{t}, {\mathbf{A}}_t)} \, {d}{\mathbf{z}} \\ &= \mathbb{E}_{{\mathbf{z}} \sim {q_\phi}({\mathbf{z}} \mid {\mathbf{o}}_{t}, {\mathbf{A}}_t)} \left[ \ln \frac{{p_\theta}({\mathbf{A}}_t \mid {\mathbf{o}}_{t}, {\mathbf{z}}) {p_\theta}({\mathbf{z}})}{{q_\phi}({\mathbf{z}} \mid {\mathbf{o}}_{t}, {\mathbf{A}}_t)} \right] + {\mathcal{D}_{\text{KL}}}\left( {q_\phi}({\mathbf{z}} \mid {\mathbf{o}}_{t}, {\mathbf{A}}_t) \,\parallel\, {p_\theta}({\mathbf{z}} \mid {\mathbf{o}}_{t}, {\mathbf{A}}_t) \right) \\ &\ge \mathbb{E}_{{\mathbf{z}} \sim {q_\phi}({\mathbf{z}} \mid {\mathbf{o}}_{t}, {\mathbf{A}}_t)} \left[ \ln {p_\theta}({\mathbf{A}}_t \mid {\mathbf{o}}_{t}, {\mathbf{z}}) \right] - {\mathcal{D}_{\text{KL}}}\left( {q_\phi}({\mathbf{z}} \mid {\mathbf{o}}_{t}, {\mathbf{A}}_t) \,\parallel\, {p_\theta}({\mathbf{z}}) \right) \equiv {\mathcal{L}_{\text{ELBO}}}({\theta}, {\phi}) \end{aligned}
$$

 Assuming standard isotropic Gaussian prior ${p_\theta}({\mathbf{z}}) = {\mathcal{N}}({\mathbf{0}}, {\mathbf{I}})$ and diagonal Gaussian variational posterior ${q_\phi}({\mathbf{z}} \mid {\mathbf{o}}_{t}, {\mathbf{A}}_t) = {\mathcal{N}}({\boldsymbol{\mu}_\phi}, \operatorname{diag}({\boldsymbol{\sigma}_\phi}^2))$, the Kullback-Leibler divergence evaluates in closed form:

$$
{\mathcal{D}_{\text{KL}}}\left( {q_\phi}({\mathbf{z}} \mid {\mathbf{o}}_{t}, {\mathbf{A}}_t) \,\parallel\, {\mathcal{N}}({\mathbf{0}}, {\mathbf{I}}) \right) = \frac{1}{2} \sum_{j=1}^{{d_z}} \left( {\sigma_{\phi, j}}^2 + {\mu_{\phi, j}}^2 - 1 - \ln({\sigma_{\phi, j}}^2) \right)
$$

 Sampling directly as ${\mathbf{z}} \sim {q_\phi}$ is a stochastic operation that prevents backpropagation because the node has no analytical derivatives with respect to encoder parameters ${\phi}$. ACT resolves this via the **reparameterization trick**: isolating stochasticity into parameter-free standard normal noise ${\boldsymbol{\epsilon}} \sim {\mathcal{N}}({\mathbf{0}}, {\mathbf{I}})$:

$$
{\mathbf{z}} = {\boldsymbol{\mu}_\phi}({\mathbf{o}}_{t}, {\mathbf{A}}_t) + {\boldsymbol{\sigma}_\phi}({\mathbf{o}}_{t}, {\mathbf{A}}_t) \odot {\boldsymbol{\epsilon}}, \quad \text{yielding } \frac{\partial {\mathbf{z}}}{\partial {\boldsymbol{\mu}_\phi}} = {\mathbf{I}}, \quad \frac{\partial {\mathbf{z}}}{\partial {\boldsymbol{\sigma}_\phi}} = \operatorname{diag}({\boldsymbol{\epsilon}})
$$

 To parameterize the reconstruction likelihood, ACT models ${p_\theta}({\mathbf{A}}_t \mid {\mathbf{o}}_{t}, {\mathbf{z}})$ as an isotropic Laplace distribution:

$$
{p_\theta}({\mathbf{A}}_t \mid {\mathbf{o}}_{t}, {\mathbf{z}}) = \frac{1}{(2{b})^{{H} {d_a}}} \exp\left( -\frac{\|{\mathbf{A}}_t - {\pi_\theta}({\mathbf{o}}_{t}, {\mathbf{z}})\|_1}{{b}} \right)
$$

 Maximizing the log-likelihood is equivalent to minimizing the $\ell_1$ norm $\|{\mathbf{A}}_t - {\pi_\theta}({\mathbf{o}}_{t}, {\mathbf{z}})\|_1$. Away from zero residual, $\ell_1$ loss gives constant-magnitude gradients with respect to each predicted action component, whereas $\ell_2$ loss gives greater influence to large residuals. Neither loss alone filters demonstrator tremor or guarantees freedom from overfitting; those outcomes depend on the data, regularization, and temporal model. Weighting the KL regularizer by hyperparameter ${\beta} > 0$ yields the full training loss:

$$
{\mathcal{L}_{\text{ACT}}}({\theta}, {\phi}) = \mathbb{E}_{({\mathbf{o}}_{t}, {\mathbf{A}}_t) \sim {\mathcal{D}_{\text{demo}}}, {\boldsymbol{\epsilon}} \sim {\mathcal{N}}({\mathbf{0}}, {\mathbf{I}})} \left[ \|{\mathbf{A}}_t - {\pi_\theta}({\mathbf{o}}_{t}, {\boldsymbol{\mu}_\phi} + {\boldsymbol{\sigma}_\phi} \odot {\boldsymbol{\epsilon}})\|_1 + {\beta} {\mathcal{D}_{\text{KL}}}\left( {q_\phi}({\mathbf{z}} \mid {\mathbf{o}}_{t}, {\mathbf{A}}_t) \,\parallel\, {\mathcal{N}}({\mathbf{0}}, {\mathbf{I}}) \right) \right]
$$

    The latent variable ${\mathbf{z}} \in \mathbb{R}^{{d_z}}$ can encode variation among demonstrations, while the decoder predicts all ${H}$ actions together. Neither separated latent clusters nor kinematic smoothness follows from the architecture alone. Executing ${H_{\text{exec}}}$ actions before replanning reduces policy interventions, but increases the time before new observations can alter the proposal. Substituting ${S}/{H}$ into the single-step compounding bound is not justified without new chunk-level error and cost assumptions.

    At test time the variational encoder, which requires the future demonstration chunk, is discarded. Setting ${\mathbf{z}}={\mathbf{0}}$ evaluates the decoder at the prior mean in one forward pass. That latent point is not guaranteed to select the most probable demonstrated mode. Sampling the prior can expose additional modes but also poorly trained latent regions. ACT combines overlapping chunk predictions through **temporal ensembling**; for example, an exponentially recency-weighted convention is:

$$
{\mathbf{a}}_{t} = \frac{\sum_{i=0}^{\min({t},{H}-1)} {w_i}\,{\mathbf{A}}_{t-i}[{i}]}{\sum_{i=0}^{\min({t},{H}-1)}{w_i}},
$$

 Each weight ${w_i}$ decays exponentially with the offset ${i}$, so this convention favors recent predictions. Averaging incompatible chunks can still create an invalid action; the admitted command must satisfy current limits.

6.  **Discrete action tokens.** Vision-language-action models such as RT-1, RT-2, and OpenVLA ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-brohan2023rt1|Brohan, Brown, Carbajal, Chebotar, Dabis, et al. 2023]]; [[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-brohan2023rt2|Brohan, Brown, Carbajal, Chebotar, Chen, et al. 2023]]; [[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-kim2024openvla|Kim et al. 2024]]) discretize continuous action dimensions into ${B}$ uniform bins (commonly 256) and emit categorical tokens:

$$
\text{bin}({a}_k) = \min\!\left({B}-1,\left\lfloor {B}\frac{{a}_k-{a_{\min}}}{{a_{\max}}-{a_{\min}}}\right\rfloor\right)
$$

 For an action clipped to the declared range, this assigns one of ${B}$ equal-width bins, including the upper endpoint. Decoding to bin centers gives maximum scalar quantization error $({a_{\max}}-{a_{\min}})/(2{B})$. Categorical sampling or mode selection preserves alternatives; taking their mean reintroduces averaging. A decoder that emits one token per action dimension autoregressively needs ${d_a}$ sequential predictions, although other tokenizations and parallel heads have different costs.

### Continuous Trajectory Diffusion and Flow Matching

^sec-appendix-ml-diffusion

Sampling one distinct trajectory around an obstacle avoids the collision caused by averaging two paths, but running 16 sequential denoising passes through a 48-million-parameter U-Net takes $40.4\text{ ms}$ and overruns a $25\text{ ms}$ synchronous setpoint deadline. Continuous trajectory diffusion treats policy synthesis as generative denoising over continuous multi-step action trajectory chunks ${\mathbf{A}} \in \mathbb{R}^{{H} \times {d_a}}$ conditioned on visual and proprioceptive observation histories ${\mathbf{O}}$ ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-chi2024diffusionpolicy|Chi et al. 2025]]). Here ${H}$ counts physical action steps, ${d_a}$ counts action dimensions, and the later ${N_{\text{eval}}}$ counts inference evaluations; diffusion time is not physical execution time. Rather than predicting an unconstrained point estimate via mean squared error, diffusion models represent complex multimodal action distributions without collapsing into mode averaging.

The closed-loop visuomotor diffusion pipeline has three coordinated architectural columns ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^fig-diffusion-policy-architecture|figure 5]]). The left observation column encodes visual camera streams and proprioceptive joint history into a conditioning vector. The center denoising column applies a noise network across ${N_{\text{eval}}}$ sequential reverse-diffusion steps to refine Gaussian noise into a candidate action chunk. The right dispatch column extracts an execution prefix from the prediction horizon and routes those candidate actions across the proposal boundary into the $1\text{ kHz}$ permission path. It also discards the unexecuted tail before re-planning. The noise-prediction backbone ${\boldsymbol{\epsilon}_\theta}$ is typically implemented using either a 1D Temporal Convolutional (Conv1D) U-Net or a Diffusion Transformer (DiT):

- **1D temporal convolutional U-Net:** Convolutions across the action horizon reuse filters at many positions. Feature-wise linear modulation (FiLM) supplies observation and diffusion-step conditioning. Layer widths, intermediate tensors, and accelerator tiling determine whether activations stay on chip.
- **Diffusion transformer (DiT):** Attention connects action tokens and visual conditioning. The action horizon and conditioning length determine attention work, while kernel fusion determines how much intermediate storage reaches DRAM. Neither backbone implies a fixed parameter count or per-step latency; the worked budget below declares one illustrative configuration.

![[90 Assets/Volume IV/Shared Figures/Fig06 Canonical Diffusion Policy 19e01bd348.svg]]

*Three-column block diagram. Observation: camera images and robot state pass through an encoder to a conditioning history. Denoising: Gaussian noise enters a noise network run for a number of sequential steps, producing a dashed candidate action chunk. Dispatch: a bracket marks the prediction horizon; the first segment is sent and the rest discarded. The sent prefix crosses a dashed proposal boundary into a 1 kHz permission path, which passes an admitted command to the drives.*

Figure 5: **Diffusion policy architecture**: A continuous trajectory diffusion policy for visuomotor control, denoising a candidate action chunk from Gaussian noise across ${N_{\text{eval}}}$ iterations and dispatching only a prefix of it before re-planning. Asynchronous buffering and an independent high-rate permission path can separate slower chunk generation from actuation. Conditional denoising can represent alternative demonstrated paths without taking their direct-regression mean. (Adapted from Chi et al. ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-chi2024diffusionpolicy|2025]])).

^fig-diffusion-policy-architecture

#### Forward Diffusion and Variance Scheduling

^forward-diffusion-and-variance-scheduling

The forward diffusion process progressively corrupts a ground-truth demonstrated action chunk ${\mathbf{A}}^0 \sim {p_{\text{data}}}({\mathbf{A}})$ with Gaussian noise across ${N}$ discrete timesteps (or continuous diffusion time ${t_{\text{diff}}} \in [0, 1]$):

$$
{q}({\mathbf{A}^k} \mid {\mathbf{A}}^{k-1}) = {\mathcal{N}}\left({\mathbf{A}^k}; \sqrt{1 - {\beta}_k} {\mathbf{A}}^{k-1}, {\beta}_k {\mathbf{I}}\right)
$$

 where $\{{\beta}_k \in (0, 1)\}_{k=1}^{N}$ denotes a predefined variance schedule. Defining ${\alpha}_k = 1 - {\beta}_k$, the one-step transition evaluates to:

$$
{\mathbf{A}^k} = \sqrt{{\alpha}_k} {\mathbf{A}}^{k-1} + \sqrt{1 - {\alpha}_k} {\boldsymbol{\epsilon}}_{k-1}, \quad {\boldsymbol{\epsilon}}_{k-1} \sim {\mathcal{N}}({\mathbf{0}}, {\mathbf{I}})
$$

 Unrolling this recursion for ${k} = 2$:

$$
\begin{aligned} {\mathbf{A}}^2 &= \sqrt{{\alpha}_2} \left( \sqrt{{\alpha}_1} {\mathbf{A}}^0 + \sqrt{1 - {\alpha}_1} {\boldsymbol{\epsilon}}_0 \right) + \sqrt{1 - {\alpha}_2} {\boldsymbol{\epsilon}}_1 \\ &= \sqrt{{\alpha}_2 {\alpha}_1} {\mathbf{A}}^0 + \sqrt{{\alpha}_2(1 - {\alpha}_1)} {\boldsymbol{\epsilon}}_0 + \sqrt{1 - {\alpha}_2} {\boldsymbol{\epsilon}}_1 \end{aligned}
$$

 Because the linear combination of two independent zero-mean Gaussian random variables ${\mathcal{N}}({\mathbf{0}}, {\sigma_a}^2 {\mathbf{I}})$ and ${\mathcal{N}}({\mathbf{0}}, {\sigma_b}^2 {\mathbf{I}})$ is itself a Gaussian with variance $({\sigma_a}^2 + {\sigma_b}^2){\mathbf{I}}$, the combined variance of the noise terms simplifies algebraically:

$$
{\alpha}_2(1 - {\alpha}_1) + (1 - {\alpha}_2) = {\alpha}_2 - {\alpha}_1 {\alpha}_2 + 1 - {\alpha}_2 = 1 - {\alpha}_1 {\alpha}_2
$$

 Defining the cumulative variance product ${\bar{\alpha}}_{k} = \prod_{{s}=1}^{k} {\alpha}_{{s}}$, mathematical induction establishes the closed-form marginal distribution at any arbitrary diffusion step ${k}$ directly from clean action chunk ${\mathbf{A}}^0$:

$$
{q}({\mathbf{A}^k} \mid {\mathbf{A}}^0) = {\mathcal{N}}\left({\mathbf{A}^k}; \sqrt{{\bar{\alpha}}_{k}} {\mathbf{A}}^0, (1 - {\bar{\alpha}}_{k}) {\mathbf{I}}\right)
$$

 allowing immediate sampling of noisy trajectories during training without simulating intermediate Markov chain transitions:

$$
{\mathbf{A}^k} = \sqrt{{\bar{\alpha}}_{k}} {\mathbf{A}}^0 + \sqrt{1 - {\bar{\alpha}}_{k}} {\boldsymbol{\epsilon}}, \quad {\boldsymbol{\epsilon}} \sim {\mathcal{N}}({\mathbf{0}}, {\mathbf{I}})
$$

#### Reverse Denoising and Score-Matching Objective

^reverse-denoising-and-score-matching-objective

The generative reverse process synthesizes an action trajectory from pure Gaussian noise ${\mathbf{A}^N} \sim {\mathcal{N}}({\mathbf{0}}, {\mathbf{I}})$ by parameterizing the conditional reverse transition distribution ${p_\theta}({\mathbf{A}}^{k-1} \mid {\mathbf{A}^k}, {\mathbf{O}})$:

$$
{p_\theta}({\mathbf{A}}^{k-1} \mid {\mathbf{A}^k}, {\mathbf{O}}) = {\mathcal{N}}\left({\mathbf{A}}^{k-1}; {\boldsymbol{\mu}_\theta}({\mathbf{A}^k}, {\mathbf{O}}, {k}), {\boldsymbol{\Sigma}}_k\right)
$$

 By Bayes’ rule, the true reverse posterior conditioned on the clean trajectory ${\mathbf{A}}^0$ is tractable and Gaussian: ${q}({\mathbf{A}}^{k-1} \mid {\mathbf{A}^k}, {\mathbf{A}}^0) = {\mathcal{N}}({\mathbf{A}}^{k-1}; {\tilde{\boldsymbol{\mu}}}_k({\mathbf{A}^k}, {\mathbf{A}}^0), {\tilde{\beta}}_k {\mathbf{I}})$, where:

$$
{\tilde{\boldsymbol{\mu}}}_k({\mathbf{A}^k}, {\mathbf{A}}^0) = \frac{\sqrt{{\bar{\alpha}}_{k-1}} {\beta}_k}{1 - {\bar{\alpha}}_{k}} {\mathbf{A}}^0 + \frac{\sqrt{{\alpha}_k}(1 - {\bar{\alpha}}_{k-1})}{1 - {\bar{\alpha}}_{k}} {\mathbf{A}^k}
$$

 Because ${\mathbf{A}}^0$ is unobserved at test time, the reverse process substitutes an estimate of ${\mathbf{A}}^0$ derived from Tweedie’s formula. For any Gaussian perturbation ${\mathbf{x}} \sim {\mathcal{N}}({\mathbf{x}}_0, {\sigma}^2 {\mathbf{I}})$ with prior density ${p}({\mathbf{x}}_0)$, the conditional observation density is:

$$
{p}({\mathbf{x}} \mid {\mathbf{x}}_0) = \frac{1}{(2\pi {\sigma}^2)^{{D}/2}} \exp\left( -\frac{\|{\mathbf{x}} - {\mathbf{x}}_0\|^2}{2{\sigma}^2} \right)
$$

 Differentiating with respect to the noisy measurement ${\mathbf{x}}$:

$$
\nabla_{{\mathbf{x}}} {p}({\mathbf{x}} \mid {\mathbf{x}}_0) = -\frac{{\mathbf{x}} - {\mathbf{x}}_0}{{\sigma}^2} {p}({\mathbf{x}} \mid {\mathbf{x}}_0)
$$

 The marginal density of noisy observations evaluates to ${p}({\mathbf{x}}) = \int_{\mathbb{R}^{D}} {p}({\mathbf{x}} \mid {\mathbf{x}}_0) {p}({\mathbf{x}}_0) \, {d}{\mathbf{x}}_0$. Differentiating under the integral sign:

$$
\nabla_{{\mathbf{x}}} {p}({\mathbf{x}}) = \int_{\mathbb{R}^{D}} \nabla_{{\mathbf{x}}} {p}({\mathbf{x}} \mid {\mathbf{x}}_0) {p}({\mathbf{x}}_0) \, {d}{\mathbf{x}}_0 = -\frac{1}{{\sigma}^2} \int_{\mathbb{R}^{D}} ({\mathbf{x}} - {\mathbf{x}}_0) {p}({\mathbf{x}} \mid {\mathbf{x}}_0) {p}({\mathbf{x}}_0) \, {d}{\mathbf{x}}_0
$$

 Dividing both sides by the marginal density ${p}({\mathbf{x}})$:

$$
\frac{\nabla_{{\mathbf{x}}} {p}({\mathbf{x}})}{{p}({\mathbf{x}})} = \nabla_{{\mathbf{x}}} \ln {p}({\mathbf{x}}) = -\frac{1}{{\sigma}^2} \left( {\mathbf{x}} - \int_{\mathbb{R}^{D}} {\mathbf{x}}_0 \frac{{p}({\mathbf{x}} \mid {\mathbf{x}}_0) {p}({\mathbf{x}}_0)}{{p}({\mathbf{x}})} \, {d}{\mathbf{x}}_0 \right) = -\frac{{\mathbf{x}} - \mathbb{E}[{\mathbf{x}}_0 \mid {\mathbf{x}}]}{{\sigma}^2}
$$

 Multiplying by ${\sigma}^2$ and isolating $\mathbb{E}[{\mathbf{x}}_0 \mid {\mathbf{x}}]$ proves **Tweedie’s formula**:

$$
\mathbb{E}[{\mathbf{x}}_0 \mid {\mathbf{x}}] = {\mathbf{x}} + {\sigma}^2 \nabla_{{\mathbf{x}}} \ln {p}({\mathbf{x}})
$$

 Tweedie’s formula reveals that the Bayes-optimal reconstruction of clean state ${\mathbf{x}}_0$ equals the corrupted measurement ${\mathbf{x}}$ shifted along the marginal Stein score $\nabla_{{\mathbf{x}}} \ln {p}({\mathbf{x}})$ scaled by noise variance ${\sigma}^2$. Rewriting the forward diffusion marginal ${\mathbf{A}^k} = \sqrt{{\bar{\alpha}}_{k}} {\mathbf{A}}^0 + \sqrt{1 - {\bar{\alpha}}_{k}} {\boldsymbol{\epsilon}}$ as $\frac{{\mathbf{A}^k}}{\sqrt{{\bar{\alpha}}_{k}}} = {\mathbf{A}}^0 + \frac{\sqrt{1 - {\bar{\alpha}}_{k}}}{\sqrt{{\bar{\alpha}}_{k}}} {\boldsymbol{\epsilon}}$, the effective noise variance is ${\sigma}^2 = \frac{1 - {\bar{\alpha}}_{k}}{{\bar{\alpha}}_{k}}$. At the population optimum of the noise-prediction objective, Tweedie’s formula equates the estimated clean trajectory ${\hat{\mathbf{A}}}^0$ and the Stein score $\nabla_{{\mathbf{A}^k}} \ln {p}({\mathbf{A}^k} \mid {\mathbf{O}})$:

$$
\nabla_{{\mathbf{A}^k}} \ln {p}({\mathbf{A}^k} \mid {\mathbf{O}}) = -\frac{{\boldsymbol{\epsilon}_\theta}({\mathbf{A}^k}, {\mathbf{O}}, {k})}{\sqrt{1 - {\bar{\alpha}}_{k}}}
$$

 Substituting ${\hat{\mathbf{A}}}^0 = \frac{1}{\sqrt{{\bar{\alpha}}_{k}}} \left( {\mathbf{A}^k} - \sqrt{1 - {\bar{\alpha}}_{k}} {\boldsymbol{\epsilon}_\theta}({\mathbf{A}^k}, {\mathbf{O}}, {k}) \right)$ into the posterior mean ${\tilde{\boldsymbol{\mu}}}_k$ reparameterizes the reverse transition mean:

$$
{\boldsymbol{\mu}_\theta}({\mathbf{A}^k}, {\mathbf{O}}, {k}) = \frac{1}{\sqrt{{\alpha}_k}} \left( {\mathbf{A}^k} - \frac{{\beta}_k}{\sqrt{1 - {\bar{\alpha}}_{k}}} {\boldsymbol{\epsilon}_\theta}({\mathbf{A}^k}, {\mathbf{O}}, {k}) \right)
$$

 The noise-prediction network ${\boldsymbol{\epsilon}_\theta}$ is optimized via the simplified $\ell_2$ denoising score-matching objective:

$$
{\mathcal{L}_{\text{diff}}}({\theta}) = \mathbb{E}_{k \sim {\mathcal{U}}\{1, {N}\}, {\boldsymbol{\epsilon}} \sim {\mathcal{N}}({\mathbf{0}}, {\mathbf{I}}), ({\mathbf{O}}, {\mathbf{A}}^0) \sim {\mathcal{D}_{\text{demo}}}} \left[ \left\| {\boldsymbol{\epsilon}} - {\boldsymbol{\epsilon}_\theta}\left(\sqrt{{\bar{\alpha}}_{k}}{\mathbf{A}}^0 + \sqrt{1 - {\bar{\alpha}}_{k}}{\boldsymbol{\epsilon}}, {\mathbf{O}}, {k}\right) \right\|^2 \right]
$$

 By following the score function $\nabla_{{\mathbf{A}^k}} \ln {p}({\mathbf{A}^k} \mid {\mathbf{O}})$, reverse diffusion steers stochastic sampling toward high-density demonstration modes rather than averaging incompatible modes into an obstacle collision. Each denoising step commits further to a single mode of the conditional action distribution.

#### Continuous Flow Matching and Vector Field Regression

^continuous-flow-matching-and-vector-field-regression

While standard diffusion models formulate generation as reverse stochastic differential equations (SDEs), **continuous flow matching** ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-lipman2022flow|Lipman et al. 2022]]) generates trajectories along deterministic probability flows defined by ordinary differential equations (ODEs):

$$
\frac{{d}{\mathbf{y}}_t}{d{t}} = {v_\theta}({\mathbf{y}}_t, {t}, {\mathbf{O}})
$$

 The continuous vector field ${v_\theta}$ drives a source noise distribution ${\rho}_0({\mathbf{y}}) = {\mathcal{N}}({\mathbf{0}}, {\mathbf{I}})$ to the empirical demonstration target distribution ${\rho}_1({\mathbf{y}}) = {p_{\text{data}}}({\mathbf{y}})$ across continuous time ${t} \in [0, 1]$, governed by the **continuity equation**:

$$
\frac{\partial {\rho}_t({\mathbf{y}})}{\partial {t}} + \nabla \cdot \left( {\rho}_t({\mathbf{y}}) {u}_t({\mathbf{y}}) \right) = 0
$$

 For a straight conditional interpolation path, the continuous trajectory interpolates linearly between source noise ${\mathbf{y}}_0 \sim {\mathcal{N}}({\mathbf{0}}, {\mathbf{I}})$ and demonstration chunk ${\mathbf{y}}_1 \sim {\mathcal{D}_{\text{demo}}}$:

$$
{\psi}_t({\mathbf{y}}_0) = (1 - {t}) {\mathbf{y}}_0 + {t} {\mathbf{y}}_1, \quad {t} \in [0, 1]
$$

 The conditional velocity along each paired-sample path is constant across time:

$$
{v}_t({\mathbf{y}} \mid {\mathbf{y}}_1) = \frac{{d}}{d{t}} {\psi}_t({\mathbf{y}}_0) = {\mathbf{y}}_1 - {\mathbf{y}}_0
$$

 and the trajectory acceleration vanishes identically: $\frac{{d}^2}{d{t}^2} {\psi}_t({\mathbf{y}}_0) = {\mathbf{0}}$. The **Conditional Flow Matching (CFM) theorem** ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-lipman2022flow|Lipman et al. 2022]]) proves a gradient identity. Regressing the neural vector field ${v_\theta}$ against this conditional vector field over paired samples $({\mathbf{y}}_0, {\mathbf{y}}_1)$ gives the same gradients as regressing it against the intractable marginal velocity field ${u}_t({\mathbf{y}})$:

$$
\nabla_{\theta} \mathbb{E}_{t, {\mathbf{y}}_0, {\mathbf{y}}_1} \left[ \| {v_\theta}({\psi}_t({\mathbf{y}}_0), {t}, {\mathbf{O}}) - ({\mathbf{y}}_1 - {\mathbf{y}}_0) \|^2 \right] = \nabla_{\theta} \mathbb{E}_{t, {\mathbf{y}} \sim {\rho}_t} \left[ \| {v_\theta}({\mathbf{y}}, {t}, {\mathbf{O}}) - {u}_t({\mathbf{y}}) \|^2 \right]
$$

 The network is therefore trained via direct mean squared regression:

$$
{\mathcal{L}_{\text{FM}}}({\theta}) = \mathbb{E}_{t \sim {\mathcal{U}}[0, 1], {\mathbf{y}}_0 \sim {\mathcal{N}}({\mathbf{0}}, {\mathbf{I}}), {\mathbf{y}}_1 \sim {\mathcal{D}_{\text{demo}}}} \left[ \left\| {v_\theta}\left((1 - {t}){\mathbf{y}}_0 + {t}{\mathbf{y}}_1, {t}, {\mathbf{O}}\right) - ({\mathbf{y}}_1 - {\mathbf{y}}_0) \right\|^2 \right]
$$

 The conditional paths above are straight for each sampled pair, but the learned marginal velocity averages over pairs that reach the same intermediate point. Its integrated trajectories need not remain straight, and their numerical error need not vanish. Independent noise/data pairing also does not establish globally optimal transport. Flow matching can support fewer evaluations in a measured task, but the step count must satisfy an action-quality criterion; it is not a universal consequence of the interpolation formula.

#### Denoising Steps Against the Control Deadline

^denoising-steps-against-the-control-deadline

In continuous generative policies, the number of reverse evaluation steps ${N_{\text{eval}}}$ is the governing systems lever trading off policy expressiveness at the physical plant against computational latency on accelerator hardware. The reverse trajectory discretizes a continuous probability flow ODE or reverse SDE. Discretizing this path across ${N_{\text{eval}}}$ finite steps introduces numerical integration errors:

- **Sampling accuracy:** Reducing the number of evaluations increases numerical approximation error for a fixed solver and learned field. How that error changes multimodal coverage, collision rate, or setpoint smoothness depends on the learned distribution and solver. The architecture alone supplies no minimum acceptable step count.
- **Computational latency and roofline limits:** Reverse diffusion is an inherently sequential Markov chain: evaluation ${k}-1$ requires the tensor output of evaluation ${k}$. Denoising steps cannot be parallelized across the time dimension on GPU or NPU accelerators. Total chunk generation latency scales linearly with ${N_{\text{eval}}}$:[[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^fn5|⁵]]

$$
{t_{\text{infer}}} = {t_{\text{vis}}} + {N_{\text{eval}}} \cdot {t_{\text{pass}}}
$$

 where ${t_{\text{vis}}}$ is the one-time visual feature extraction latency per chunk and ${t_{\text{pass}}}$ is the forward execution time of noise-prediction network ${\boldsymbol{\epsilon}_\theta}$. A weight-transfer lower bound is ${t_{\text{stream}}}={M_{\text{weights}}}/{\text{BW}_{\text{mem}}}$ when every evaluation reloads those weights. The roofline intensity must count all operations and traffic, including convolutional or token reuse and activation spills. Batch size alone does not make every decoder memory bound. The worked budget below evaluates this transfer bound separately from its assumed execution time.

A setpoint producer that must finish synchronously within ${\Delta t_{\text{ctrl}}}$ misses its contract when ${t_{\text{infer}}}>{\Delta t_{\text{ctrl}}}$. The consequence depends on the controller’s defined hold, interpolation, and fallback behavior; a deadline miss does not inherently imply a torque drop. Physical AI architectures resolve this latency-expressiveness trade-off through three coordinated mechanisms:

1.  **Action chunking:** The policy predicts a multi-step trajectory chunk ${\mathbf{A}} \in \mathbb{R}^{{H} \times {d_a}}$ spanning prediction horizon ${H}$. Executing an execution horizon ${H_{\text{exec}}} \le {H}$ amortizes the ${N_{\text{eval}}}$-step generation latency over ${H_{\text{exec}}} {\Delta t_{\text{ctrl}}}$ of physical robot motion.
2.  **Fewer solver evaluations:** Flow matching, improved solvers, or distillation can reduce sequential evaluations when validation shows that the resulting action quality remains adequate. Reduced compute buys timing slack at the cost of a new approximation and validation obligation.
3.  **Dual-rate asynchronous decoupling:** The application processor runs the generative denoising loop asynchronously at a relaxed rate ($10\text{--}20\text{ Hz}$), sending each action chunk across the proposal boundary over a black-channel link that carries a checksum and sequence number. A discrete safety microcontroller, which shares no memory with the application processor, receives the chunk into its own double buffer and executes synchronously at $1\text{ kHz}$. It interpolates spline knots, enforces slew-rate limits, and gates commands through deterministic control barrier functions (**[[01 Books/Volume IV - Physical AI/00 Introduction/01 The Causal Boundary/V4-01.08 The Machine in Five Levels#^sec-boundary-machine-model|The Machine in Five Levels]]**).

The numerical execution of this dual-rate pipeline spans both processors ([algorithm 2](https://mlsysbook.ai/vol4/backmatter/appendix_ml.html#algo-diffusion-policy-trajectory)), and its geometry, denoising trajectory, and hardware split appear across the three panels of [[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^fig-diffusion-denoising-process|figure 6]]. Panel (a) demonstrates multimodal action selection. It contrasts direct MSE regression, which averages divergent paths into an obstacle collision, against conditional diffusion, which samples distinct valid trajectory modes. Panel (b) traces the reverse-diffusion denoising sequence from isotropic Gaussian noise ${\mathbf{A}}^{{N_{\text{eval}}}}$ to a coherent action chunk ${\mathbf{A}}^0$. Panel (c) shows the asynchronous dual-rate hardware split, where the application processor streams candidate chunks over a black-channel serial link to a discrete $1\text{ kHz}$ safety microcontroller running double-buffering, freshness checks, and spline interpolation. **[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06.03 Policy Training Regimes#^sec-training-synthesis-regimes|Policy Training Regimes]]** uses the timing budget below to evaluate which sampler fits the control deadline. The pseudocode assumes the microcontroller’s receive path has already validated the proposal’s capture epoch, clock conversion, configuration, validity interval, and handoff continuity. An absent, expired, or rejected chunk selects the defined fallback; spline interpolation and slew clamping alone do not implement that permission decision. The transmitted action must also pass the actuator interface that converts its declared units to drive commands.

$\mathbf{O}_t = ({\mathbf{o}}_{t-{H_{\text{hist}}}}, \dots, {\mathbf{o}}_{t})$

![[90 Assets/Volume IV/Shared Figures/Appx ML Diffusion Dual Rate cf0b1766fd.svg]]

*Three-panel schematic. Panel a: direct regression averages two demonstrated paths around an obstacle into a mean path that runs into it, while conditional diffusion samples from noise toward one of two mode regions. Panel b: three stacked boxes go from a noisy zigzag to a coarse dashed curve to a smooth candidate action chunk. Panel c: an application processor sampler at 15 Hz sends a chunk through a dashed black-channel link with CRC and sequence number to a safety microcontroller with its own memory, holding an active and a filling buffer and running a freshness check, spline, and slew clamp at a 1 kHz tick; it passes an admitted command to the drives.*

Figure 6: **Diffusion policy action chunk denoising and receding-horizon decoupling**: (a) Multimodal resolution: direct regression with mean squared error averages divergent demonstrations into an invalid obstacle collision, whereas conditional diffusion can sample alternative demonstrated modes; generated paths still require clearance checks. (b) Iterative trajectory denoising: starting from Gaussian noise ${\mathbf{A}}^{{N_{\text{eval}}}} \sim {\mathcal{N}}({\mathbf{0}}, {\mathbf{I}})$, reverse diffusion progressively resolves a coarse trajectory into a smooth action chunk ${\mathbf{A}}^0$. (c) Dual-rate decoupling: an asynchronous sampler on the application processor sends each chunk over a black-channel link to a discrete $1\,\text{kHz}$ safety microcontroller, which holds it in its own double buffer and runs the freshness check, spline interpolation, and slew clamping. The two processors share no memory. (Adapted from Chi et al. ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-chi2024diffusionpolicy|2025]])).

^fig-diffusion-denoising-process

Consider a 7-DoF arm with a two-finger gripper (${d_a} = 8$) whose policy generates chunks of 16 setpoints at a chosen 25 ms setpoint period (40 Hz), a 400 ms horizon. The noise-prediction network is a 1D temporal convolutional U-Net with 48 million parameters, 96 MB at FP16. Its timings below are illustrative inputs, not measurements of any device. The budget has three parts.

1.  **Perception.** A visual encoder processes two synchronized RGB streams (wrist-mounted and over-the-shoulder) into the conditioning embedding ${\mathbf{E}}_t$ in ${t_{\text{vis}}} =$ 14 ms per chunk. Because the features are extracted once per chunk before denoising begins, ${t_{\text{vis}}}$ is a fixed cost whatever the sampling schedule.
2.  **Denoising.** Each reverse step evaluates ${\boldsymbol{\epsilon}_\theta}$ at 14.2 GFLOP. At a peak bandwidth of 204.8 GB/s, streaming the weights once takes at least 0.469 ms, and the arithmetic intensity is about 147.9 FLOP/byte. With kernel launch overhead and activation spills, the time per evaluation is ${t_{\text{pass}}} =$ 1.65 ms, and the sampler then sets the cost. A standard DDIM sampler with 16 steps denoises in 26.4 ms, for a total inference latency of 40.4 ms. A flow-matching decoder integrated with 2 Euler evaluations, assuming two steps meet the task’s action-quality criterion, needs 3.3 ms, for a total of 17.3 ms.
3.  **The deadline.** Run synchronously against the 25 ms period, the DDIM sampler overruns by 61.6 percent before any scheduling overhead. The two-evaluation flow decoder fits with 7.7 ms (30.8 percent) of compute-only slack, and it may run in lockstep only if its measured tail latency, bus transfer, and operating-system scheduling also fit. Run asynchronously at 15 Hz (a 66.7 ms period), the DDIM sampler refreshes the chunk buffer with 26.3 ms to spare. The permission path, at 1 kHz in the two-processor implementation, meanwhile interpolates the 400 ms chunk and checks its freshness, falling back when the chunk expires.

### Compounding Quadratic Error in Behavioral Cloning

^compounding-quadratic-error-in-behavioral-cloning

A $1\text{ mm}$ wrist-pose error on step 1 shifts the wrist camera viewpoint on step 2 into a slightly off-center state that the human demonstrator never visited. Whereas offline supervised evaluation samples from a fixed demonstration distribution, in closed-loop execution the current action ${\mathbf{a}}_{t}$ alters the subsequent physical state ${s}_{t+1}$ and the next observation distribution, creating **compounding covariate shift**.

Let $\pi^*$ denote the expert demonstrator policy and ${\hat{\pi}}$ denote the learned policy. Suppose the single-step error probability under the expert’s state distribution is bounded by ${\epsilon}$ for all timesteps ${t} \in \{1, \dots, {S}\}$:

$$
\forall {t} \le {S}:\quad \mathbb{E}_{{s} \sim {d_{\pi^*}}^t} [ {\mathbf{1}}({\hat{\pi}}({s}) \ne \pi^*({s})) ] \le {\epsilon}
$$

 In digital supervised learning (such as fixed-image classification), evaluation inputs are held fixed, so the expected count of prediction errors scales as $\mathcal{O}({S} {\epsilon})$. In closed-loop physical AI, an action error alters the physical state of the robot, transporting it into states ${s} \notin \text{supp}({d_{\pi^*}})$ that the demonstrator rarely or never visited. Offline training provides no valid statistical guarantee on action error in these learner-induced states.

To derive the compounding error bound, we construct a formal trajectory coupling argument ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-ross2011reduction|Ross et al. 2011]]). Let ${\mathcal{E}}_t$ denote the event that the policy makes its first mistake at time ${t}$ (${\hat{\pi}}({s}_t) \ne \pi^*({s}_t)$ and ${\hat{\pi}}({s}_{{t'}}) = \pi^*({s}_{{t'}})$ for all ${t'} < {t}$). Couple learner and expert trajectories with the same initial state and transition randomness. Until their first disagreement they coincide, so ${\mathcal{E}}_t$ is a subset of the disagreement event on the unconditioned expert trajectory and $\Pr({\mathcal{E}}_t)\le{\epsilon}$. Conditioning on earlier agreement need not preserve the expert state marginal.

The probability that at least one error has occurred at or before step ${t}$ is bounded by a union bound:[[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^fn6|⁶]]

$$
\Pr(\text{error by step } {t}) = \Pr\left( \bigcup_{{t'}=1}^{t} {\mathcal{E}}_{{t'}} \right) \le \sum_{{t'}=1}^{t} \Pr({\mathcal{E}}_{{t'}}) \le {t} {\epsilon}
$$

 Once an error occurs, the robot diverges into unmodeled states where downstream incremental cost is bounded by at most ${C_{\max}}$ per step. Summing over the entire finite execution horizon ${S}$:

$$
\begin{aligned} {J}({\hat{\pi}}) - {J}(\pi^*) &\le \sum_{t=1}^{{S}} {C_{\max}} \Pr(\text{error by step } {t}) \\ &\le {C_{\max}} \sum_{t=1}^{{S}} {t} {\epsilon} \\ &= {C_{\max}} {\epsilon} \frac{{S}({S}+1)}{2} = {\mathcal{O}(S^2 \epsilon)} \end{aligned}
$$

 The quadratic expression is a worst-case upper bound on excess cumulative cost, not a prediction of geometric trajectory error or a probability. Since $\Pr(\text{error by step }{t})\le1$, a tighter bound replaces ${t}{\epsilon}$ by $\min(1,{t}{\epsilon})$. For continuous actions, the disagreement indicator needs a specified tolerance or a surrogate loss tied to a cost bound; exact equality is generally too restrictive.

### Interactive Dataset Aggregation (DAgger) Linear Reduction

^interactive-dataset-aggregation-dagger-linear-reduction

The **DAgger** (Dataset Aggregation) algorithm ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-ross2011reduction|Ross et al. 2011]]) addresses this distribution shift by collecting training data under the learner’s induced state distribution ${d_{\hat{\pi}_i}}$. At each training iteration ${i}$, the loop proceeds in four steps:

1.  Execute policy ${\hat{\pi}}_i$ under the applicable safety envelope to collect trajectories ${\mathcal{T}}_i = \{{s}_1, {s}_2, \dots, {s}_{{S}}\}$.
2.  Query the expert to label every visited state ${s}_t \in {\mathcal{T}}_i$ with the optimal recovery action ${a}^* = \pi^*({s}_t)$.
3.  Aggregate the recovery dataset ${\mathcal{D}} \leftarrow {\mathcal{D}} \cup \{({s}_t, {a}^*)\}$.
4.  Retrain policy ${\hat{\pi}}_{i+1}$ on the aggregated dataset.

For the DAgger bound, make a stronger assumption than the earlier per-step ${C_{\max}}$: one wrong action followed by the expert changes expected remaining cost by at most ${u}$, independent of horizon. With expert labels on learner-visited states, a no-regret online learner, sufficient hypothesis capacity, and a valid finite-sample bound ${\delta_N}$, a selected policy can satisfy a bound of the form

$$
{J}({\hat{\pi}})-{J}(\pi^*) \le {S} {u}({\epsilon_N}+{\gamma_N}+{\delta_N}),
$$

 where ${\epsilon_N}$ is best-in-class loss on the induced-state distribution, ${\gamma_N}$ is average online-learning regret, and ${\delta_N}$ covers finite-sample generalization and policy selection. It scales linearly in ${S}$ only when ${u}=\mathcal{O}(1)$ and those errors remain controlled. The drift states need expert corrective labels; appending recovery trajectories alone does not supply them.

### Closed-Loop Trajectory Distributions and Evaluation Estimands

^sec-appendix-ml-trajectory-distribution

Scoring a candidate policy on a static disk of recorded human demonstrations tests the policy on states the human visited, not on the states that the candidate’s own motor commands and the permission path will drive the robot into. Let a physical rollout be parameterized by initial state ${s}_0$, environmental parameters ${e}$ (lighting, surface friction, obstacle geometry), plant parameters ${m}$ (payload mass, link inertias), and permission-path parameters ${\kappa}$ (lease durations, barrier thresholds). Together these form a trial condition ${c} = ({s}_0, {e}, {m}, {\kappa}) \sim {\mathcal{D}}$ drawn from the operating domain. Under candidate policy ${\pi_\theta}$ and physical plant transition dynamics ${p_m}({s}_{t+1} \mid {s}_t, {\mathbf{u}}_t)$, the joint probability density of an executed trajectory ${\tau} = ({s}_0, {\mathbf{u}}_0, {s}_1, {\mathbf{u}}_1, \dots, {s}_{T})$ over horizon ${T}$ is:

$$
{p_{\text{cl}}}({\tau}\mid{\pi_\theta},{e},{m},{\kappa})={\rho_0}({s}_0\mid {e},{m},{\kappa})\prod_{t=0}^{{T}-1}\left[\int {\pi_\theta}({\mathbf{a}}_{t}\mid {\mathbf{o}_{0:t}})\,{G_\kappa}({\mathbf{u}}_t\mid {s}_t,{\mathbf{a}}_{t})\,d{\mathbf{a}}_{t}\right]{p_m}({s}_{t+1}\mid {s}_t,{\mathbf{u}}_t).
$$

 Here ${\mathbf{o}}_{t}={g}({s}_t,{e})$ is the observation, ${\mathbf{a}}_{t}$ is a proposal, and ${G_\kappa}$ maps proposals to admitted commands or fallback actions. The state includes the controller and permission-path memory needed to make the transition Markov. A deterministic permission map is represented by a point-mass kernel; marginalizing over operating conditions gives the deployment trajectory distribution.

The discounted state visitation distribution (state marginal) ${d}^{{\pi_\theta}}({s})$ induced by policy ${\pi_\theta}$ is:

$$
{d}^{{\pi_\theta}}({s}) = (1 - {\gamma}) \sum_{t=0}^\infty {\gamma}^{t} \Pr({s}_t = {s} \mid {\pi_\theta})
$$

 or in the finite-horizon unweighted setting: ${\bar{d}}^{{\pi_\theta}}({s}) = \frac{1}{{T}} \sum_{t=0}^{{T}-1} \Pr({s}_t = {s} \mid {\pi_\theta})$. Given a binary task success indicator ${\phi}({\tau}) \in \{0, 1\}$ (e.g., reaching a target receptacle without exceeding torque or clearance limits), the true closed-loop task success probability across operating domain ${\mathcal{D}}$ is the formal expectation over trial conditions, including policy and transition randomness inside $\text{Traj}$:

$$
{p}({\mathcal{D}}) = \mathbb{E}_{{c} \sim {\mathcal{D}}}[{\phi}(\text{Traj}({c}))]
$$

 Because the distribution of visited states ${d}^{{\pi_\theta}}$ depends directly on policy proposals and their admission, offline evaluations over fixed logged datasets ${\mathcal{D}_{\text{demo}}}$ evaluate predictions under ${d^{\pi^*}}$. Static validation scores therefore give no statistical bound over ${d}^{{\pi_\theta}}$ when candidate commands deviate from demonstrator actions.

## Value Functions and Continuous Reinforcement Learning

^sec-appendix-ml-affordances

When a latch policy learns by trial and error rather than from demonstrations, no expert label tells it which torque vector to apply at each millisecond. It must discover actions that maximize cumulative reward from interaction, making the reward definition, exploration conditions, and simulator fidelity central assumptions. The following derivations use a fully observed Markov state; a deployed actor with partial observations may require an estimator or history encoder. The transition model includes any fixed permission mechanism, while ${J}$ here denotes reward to maximize rather than the imitation cost minimized above. **[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06.03 Policy Training Regimes#^sec-training-rl-primer|The latch task as a reward problem]]** builds reward, return, value, and the Bellman relation from the machine’s latch task; the derivations below assume that primer and extend it to continuous actions and off-policy learning.

### Continuous Markov Decision Processes and Policy Gradients

^sec-appendix-ml-continuous-rl

Continuous physical control is formalized as a Markov Decision Process (MDP) defined by the tuple ${\mathcal{M}} = ({\mathcal{S}}, {\mathcal{A}}, {p}, {r}, {\gamma}, {\rho_0})$, whose six components are:

- State space ${\mathcal{S}} \subseteq \mathbb{R}^{{d_s}}$ represents continuous physical states (joint angles, angular velocities, base pose, linear velocity);
- Action space ${\mathcal{A}} \subseteq \mathbb{R}^{{d_a}}$ represents continuous actuator commands (joint torques, motor phase currents, or impedance setpoints);
- Transition dynamics ${p}({s}_{t+1} \mid {s}_t, {\mathbf{a}}_{t})$ govern continuous plant kinematics and contact physics;
- Reward function ${r}({s}_t, {\mathbf{a}}_{t}) \in \mathbb{R}$ quantifies task performance, energy efficiency, and actuator regularization;
- Discount factor ${\gamma} \in [0, 1)$ establishes the effective temporal planning horizon;
- Initial state distribution ${\rho_0}({s}_0)$ characterizes starting configurations.

The goal is to learn a parameterized policy ${\pi_\theta}({\mathbf{a}} \mid {s})$ that maximizes the expected discounted cumulative return:

$$
{J}({\pi_\theta}) = \mathbb{E}_{{\tau} \sim {\pi_\theta}} \left[ {R}({\tau}) \right] = \int {p_\theta}({\tau}) {R}({\tau}) \, d{\tau}
$$

 where trajectory ${\tau} = ({s}_0, {\mathbf{a}}_0, {s}_1, {\mathbf{a}}_1, \dots)$ has cumulative return ${R}({\tau}) = \sum_{t=0}^\infty {\gamma}^{t} {r}({s}_t, {\mathbf{a}}_{t})$ and probability density:

$$
{p_\theta}({\tau}) = {\rho_0}({s}_0) \prod_{t=0}^\infty {\pi_\theta}({\mathbf{a}}_{t} \mid {s}_t) {p}({s}_{t+1} \mid {s}_t, {\mathbf{a}}_{t})
$$

 Differentiating expected return ${J}({\pi_\theta})$ directly with respect to policy parameters ${\theta}$ yields:

$$
\nabla_{\theta} {J}({\pi_\theta}) = \int \nabla_{\theta} {p_\theta}({\tau}) {R}({\tau}) \, d{\tau}
$$

 Applying the score-function log-derivative identity $\nabla_{\theta} {p_\theta}({\tau}) = {p_\theta}({\tau}) \nabla_{\theta} \ln {p_\theta}({\tau})$:

$$
\nabla_{\theta} {J}({\pi_\theta}) = \int {p_\theta}({\tau}) \nabla_{\theta} \ln {p_\theta}({\tau}) {R}({\tau}) \, d{\tau} = \mathbb{E}_{{\tau} \sim {\pi_\theta}} \left[ \nabla_{\theta} \ln {p_\theta}({\tau}) {R}({\tau}) \right]
$$

 Taking the natural logarithm of the trajectory probability density decomposes it into initial, policy, and plant components:

$$
\ln {p_\theta}({\tau}) = \ln {\rho_0}({s}_0) + \sum_{t=0}^\infty \ln {\pi_\theta}({\mathbf{a}}_{t} \mid {s}_t) + \sum_{t=0}^\infty \ln {p}({s}_{t+1} \mid {s}_t, {\mathbf{a}}_{t})
$$

 Differentiating with respect to ${\theta}$:

$$
\nabla_{\theta} \ln {p_\theta}({\tau}) = \sum_{t=0}^\infty \nabla_{\theta} \ln {\pi_\theta}({\mathbf{a}}_{t} \mid {s}_t)
$$

 Neither the initial state distribution ${\rho_0}({s}_0)$ nor the plant transition dynamics ${p}({s}_{t+1} \mid {s}_t, {\mathbf{a}}_{t})$ depend on policy weights ${\theta}$, causing their gradients to vanish identically. In physical systems engineering, this property matters because continuous contact dynamics, dry friction stick-slip transitions, and impact collisions are non-differentiable or discontinuous, which makes analytic trajectory derivatives $\nabla_{{\mathbf{a}}} {s}_{t+1}$ ill-conditioned or undefined. The policy gradient formulation bypasses differentiating through plant physics.

By causality (future actions cannot alter past rewards) and subtracting a state-dependent baseline ${V}({s}_t)$ to reduce variance without introducing bias, the **Policy Gradient Theorem** ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-sutton2018reinforcement|Sutton and Barto 2018]]) evaluates the gradient over the state visitation distribution:

$$
\nabla_{\theta} {J}({\pi_\theta}) = \frac{1}{1-{\gamma}}\mathbb{E}_{{s} \sim {d}^{{\pi_\theta}}, {\mathbf{a}} \sim {\pi_\theta}(\cdot \mid {s})} \left[ \nabla_{\theta} \ln {\pi_\theta}({\mathbf{a}} \mid {s}) {Q}^{{\pi_\theta}}({s}, {\mathbf{a}}) \right]
$$

 The factor $1/(1-{\gamma})$ is required because the state visitation distribution is normalized. An action-independent baseline may replace ${Q}$ by ${Q}-{V}$ without changing the expectation. Here ${d}^{{\pi_\theta}}({s}) = (1 - {\gamma}) \sum_{t=0}^\infty {\gamma}^{t} \Pr({s}_t = {s} \mid {\pi_\theta})$ is the discounted state visitation distribution, and ${Q}^{{\pi_\theta}}({s}, {\mathbf{a}}) = \mathbb{E}_{{\tau} \sim {\pi_\theta}} \left[ \sum_{k=0}^\infty {\gamma}^{k} {r}({s}_{t+k}, {\mathbf{a}}_{t+k}) \mid {s}_t = {s}, {\mathbf{a}}_{t} = {\mathbf{a}} \right]$ is the continuous state-action value function.

### Deep Deterministic Policy Gradient (DDPG)

^deep-deterministic-policy-gradient-ddpg

For high-dimensional continuous actuator spaces, stochastic sampling in policy gradients introduces substantial variance. The **Deterministic Policy Gradient (DPG)** theorem (introduced by Silver and colleagues in 2014) establishes a closed form for a deterministic policy ${\mu_{\theta}}: {\mathcal{S}} \to {\mathcal{A}}$. The policy gradient is the expected gradient of the action-value function along the policy’s chosen direction:

$$
\nabla_{\theta} {J}({\mu_{\theta}}) = \frac{1}{1-{\gamma}}\mathbb{E}_{{s} \sim {d}^{{\mu_{\theta}}}} \left[ \nabla_{{\mathbf{a}}} {Q}^{{\mu_{\theta}}}({s}, {\mathbf{a}})\Big|_{{\mathbf{a}}={\mu_{\theta}}({s})} \nabla_{\theta} {\mu_{\theta}}({s}) \right]
$$

 Here ${d}^{{\mu_{\theta}}}$ is the normalized discounted visitation distribution and the theorem uses the true policy value ${Q}^{{\mu_{\theta}}}$; DDPG substitutes a learned critic. In discrete Q-learning (such as DQN), selecting the optimal greedy action requires solving an exhaustive search $\arg\max_{a} {Q}({s}, {a})$. In continuous control where action space ${\mathcal{A}} \subseteq \mathbb{R}^{{d_a}}$ has many dimensions (such as a 7-DoF arm or 12-DoF quadruped), solving an inner non-convex optimization at every control cycle is potentially too costly for the control deadline. DPG circumvents this bottleneck by replacing the inner argmax with a differentiable continuous actor network ${\mu_{\theta}}({s})$. Applying the chain rule, the actor is updated directly in the direction of the critic’s action gradient $\nabla_{{\mathbf{a}}} {Q_{\phi}}({s}, {\mathbf{a}})$.

Deep Deterministic Policy Gradient (DDPG, introduced by Lillicrap and colleagues in 2015) parameterizes both actor ${\mu_{\theta}}$ and critic ${Q_{\phi}}$ with deep neural networks. The continuous critic ${Q_{\phi}}({s}, {\mathbf{a}})$ is trained via off-policy temporal difference learning by minimizing Bellman residual error on transitions $({s}, {\mathbf{a}}, {r}, {s'})$ sampled from an experience replay buffer ${\mathcal{D}}$:

$$
{\mathcal{L}}({\phi}) = \mathbb{E}_{({s}, {\mathbf{a}}, {r}, {s'}) \sim {\mathcal{D}}} \left[ \left( {Q_{\phi}}({s}, {\mathbf{a}}) - \left( {r} + {\gamma} {Q_{\phi'}}({s'}, {\mu_{\theta'}}({s'})) \right) \right)^2 \right]
$$

 Target networks $({\phi'}, {\theta'})$ track active networks via slow Polyak averaging ${\phi'} \leftarrow {\tau} {\phi} + (1 - {\tau}){\phi'}$ with tracking rate ${\tau} \ll 1$ (e.g., ${\tau} = 0.005$). Polyak tracking converts an unstable, moving regression target into a quasi-stationary target, slowing target drift without guaranteeing convergence under function approximation.

### Twin Delayed DDPG (TD3) and Overestimation Bias

^twin-delayed-ddpg-td3-and-overestimation-bias

Standard continuous actor-critic algorithms like DDPG suffer from **overestimation bias**. Because the critic uses deep function approximation, target values evaluate with nonzero approximation error ${\epsilon}({s'}, {\mathbf{a}'})$. In continuous Q-learning, the policy maximizes over estimated values.

The **Maximization Bias Lemma** formalizes this phenomenon: let ${Q_{\phi_1}}({s'}, {\mathbf{a}'})$ and ${Q_{\phi_2}}({s'}, {\mathbf{a}'})$ be two noisy estimators of true value ${Q}^*({s'}, {\mathbf{a}'})$ subject to zero-mean estimation error $\mathbb{E}[{\epsilon}_i] = 0$. Because the maximum operator is convex, Jensen’s inequality proves:

$$
\mathbb{E}\left[ \max_{{\mathbf{a}'}} {Q_{\phi_i}}({s'}, {\mathbf{a}'}) \right] \ge \max_{{\mathbf{a}'}} \mathbb{E}\left[ {Q_{\phi_i}}({s'}, {\mathbf{a}'}) \right] = \max_{{\mathbf{a}'}} {Q}^*({s'}, {\mathbf{a}'})
$$

 The bias is nonnegative, and can be zero; strict positivity requires errors that sometimes change which action wins. When present, maximization bias can propagate through recursive Bellman backups: overestimating value at step ${t}+1$ inflates target values at step ${t}$ and can favor suboptimal, physically destructive actuator proposals.

Introduced by Fujimoto and colleagues in 2018, **Twin Delayed DDPG (TD3)** reduces overestimation through three architectural mechanisms:

1.  **Clipped Double Q-learning:** TD3 maintains two separately parameterized critic networks ${Q_{\phi_1}}$ and ${Q_{\phi_2}}$, computing the Bellman target using the minimum of both critics:

$$
{y} = {r} + {\gamma} \min_{i=1, 2} {Q_{\phi'_i}}({s'}, {\tilde{\mathbf{a}}'})
$$

 Because the expected minimum satisfies $\mathbb{E}[\min({X}, {Y})] \le \min(\mathbb{E}[{X}], \mathbb{E}[{Y}])$, taking the minimum introduces a conservative *underestimation bias*. A lower reward estimate is not a clearance or stability bound. Underestimation can change which action wins without making that action physically safer.
2.  **Target policy smoothing:** To prevent the policy from exploiting sharp, non-physical peaks in the learned critic, TD3 injects clipped Gaussian noise into the target action:

$$
{\tilde{\mathbf{a}}'} = \text{clip}\left( {\mu_{\theta'}}({s'}) + \text{clip}({\boldsymbol{\epsilon}}, -{c}, {c}), \, {\mathbf{a}_{\min}}, \, {\mathbf{a}_{\max}} \right), \quad {\boldsymbol{\epsilon}} \sim {\mathcal{N}}({\mathbf{0}}, {\sigma}^2 {\mathbf{I}})
$$

 This regularizes value estimation over a local actuator ball. Doing so enforces the physical prior that similar motor commands should yield similar expected returns while smoothing the optimization landscape.
3.  **Delayed policy updates:** Updating the policy network on every critic step causes the actor to chase an inaccurate, rapidly shifting value landscape. TD3 updates actor parameters ${\theta}$ and target networks once every ${d}$ critic updates (typically delay ratio ${d} = 2$), giving the critics additional updates before actor weights shift, without guaranteeing stabilization.

### Soft Actor-Critic (SAC) and Maximum Entropy Control

^soft-actor-critic-sac-and-maximum-entropy-control

While TD3 provides a deterministic policy, physical autonomy requires stochastic exploration to discover viable contact modes and avoid getting trapped in local contact minima (such as a quadruped foot wedged against an obstacle). **Soft Actor-Critic (SAC, developed by Haarnoja and colleagues in 2018)** formulates continuous control under the **Maximum Entropy Reinforcement Learning** framework. The objective augments task rewards with the differential entropy of the policy:

$$
{J}({\pi_\theta}) = \sum_{t=0}^\infty \mathbb{E}_{({s}_t, {\mathbf{a}}_{t}) \sim {\rho_{\pi_\theta}}} \left[ {\gamma}^{t} \left( {r}({s}_t, {\mathbf{a}}_{t}) + {\alpha} {\mathcal{H}}({\pi_\theta}(\cdot \mid {s}_t)) \right) \right]
$$

 where ${\mathcal{H}}({\pi_\theta}(\cdot \mid {s}_t)) = -\mathbb{E}_{{\mathbf{a}} \sim {\pi_\theta}}[\ln {\pi_\theta}({\mathbf{a}} \mid {s}_t)]$ is the policy entropy, and temperature parameter ${\alpha} > 0$ controls the trade-off between reward maximization and stochastic exploration.

#### Soft Bellman Backups and Squashed Gaussian Policy

^soft-bellman-backups-and-squashed-gaussian-policy

The soft state-action value satisfies the soft Bellman equation:

$$
{Q}({s}, {\mathbf{a}}) = {r}({s}, {\mathbf{a}}) + {\gamma} \mathbb{E}_{{s'} \sim {p}} \left[ {V}({s'}) \right], \quad \text{where } {V}({s}) = \mathbb{E}_{{\mathbf{a}} \sim \pi} \left[ {Q}({s}, {\mathbf{a}}) - {\alpha} \ln \pi({\mathbf{a}} \mid {s}) \right]
$$

 To enforce physical actuator limits ${\mathbf{a}} \in [-{a_{\max}}, {a_{\max}}]^{{d_a}}$, SAC parameterizes the policy as an invertible squashed Gaussian distribution. The network outputs mean ${\boldsymbol{\mu}_{\theta}}({s})$ and log-standard-deviation $\ln {\boldsymbol{\sigma}_{\theta}}({s})$. An unbounded latent action is sampled via the reparameterization trick:

$$
{\mathbf{u}} = {\boldsymbol{\mu}_{\theta}}({s}) + {\boldsymbol{\sigma}_{\theta}}({s}) \odot {\boldsymbol{\epsilon}}, \quad {\boldsymbol{\epsilon}} \sim {\mathcal{N}}({\mathbf{0}}, {\mathbf{I}})
$$

 The following density is for normalized actions. Applying the non-linear squashing function ${\mathbf{a}} = \tanh({\mathbf{u}})$ bounds actions strictly within $(-1, 1)^{{d_a}}$.

By the change-of-variables theorem for probability densities, the log-likelihood of the bounded action ${\mathbf{a}}$ requires correcting for the Jacobian determinant of the tanh mapping:

$$
{\pi_\theta}({\mathbf{a}} \mid {s}) = {\mu}({\mathbf{u}} \mid {s}) \left| \det \frac{{d}{\mathbf{a}}}{{d}{\mathbf{u}}} \right|^{-1}
$$

 Because the squashing operator acts element-wise (${a}_i = \tanh({u}_i)$), the Jacobian matrix is diagonal: $\frac{d{a}_i}{d{u}_i} = 1 - \tanh^2({u}_i)$. The determinant factors into a product:

$$
\det \frac{{d}{\mathbf{a}}}{{d}{\mathbf{u}}} = \prod_{i=1}^{{d_a}} \left( 1 - \tanh^2({u}_i) \right)
$$

 Taking the natural logarithm yields the exact closed-form log-density correction:

$$
\ln {\pi_\theta}({\mathbf{a}} \mid {s}) = \ln {\mu}({\mathbf{u}} \mid {s}) - \sum_{i=1}^{{d_a}} \ln\left( 1 - \tanh^2({u}_i) \right)
$$

 Physical limits require a further scale and offset; their Jacobian must also be included if densities are expressed in physical units. Here $\ln {\mu}({\mathbf{u}} \mid {s}) = -\frac{1}{2} \sum_{i=1}^{{d_a}} \left( \left(\frac{{u}_i - {\mu^{\pi}}_i({s})}{{\sigma^{\pi}}_i({s})}\right)^2 + 2\ln {\sigma^{\pi}}_i({s}) + \ln(2\pi) \right)$.

#### Dual Gradient Descent for Automatic Entropy Tuning

^dual-gradient-descent-for-automatic-entropy-tuning

Fixed temperature ${\alpha}$ fails across phases of robot learning: early exploration requires high entropy (${\alpha} \gg 0$), while fine precision assembly requires low entropy (${\alpha} \to 0$). SAC formulates temperature adaptation as a constrained optimization problem: maximizing expected return subject to a minimum average entropy constraint $\mathbb{E}[{\mathcal{H}}(\pi_t)] \ge {\overline{\mathcal{H}}}$, where target entropy is commonly set to ${\overline{\mathcal{H}}} = -{d_a}$.

Solving the dual Lagrangian formulation yields the exact update for temperature ${\alpha}$:

$$
{\mathcal{L}}({\alpha}) = \mathbb{E}_{{s}_t \sim {\mathcal{D}}, {\mathbf{a}}_{t} \sim \pi_t} \left[ -{\alpha} \ln \pi_t({\mathbf{a}}_{t} \mid {s}_t) - {\alpha} {\overline{\mathcal{H}}} \right]
$$

 Differentiating with respect to ${\alpha}$ gives the dual gradient update rule:

$$
{\alpha} \leftarrow {\alpha} - {\lambda_{\alpha}} \nabla_{\alpha} {\mathcal{L}}({\alpha}) = {\alpha} - {\lambda_{\alpha}} \left( -\ln \pi_t({\mathbf{a}}_{t} \mid {s}_t) - {\overline{\mathcal{H}}} \right)
$$

 When expected policy entropy drops below target ${\overline{\mathcal{H}}}$, $\mathbb{E}[-\ln\pi_t]<{\overline{\mathcal{H}}}$, the expected gradient is negative and gradient descent raises ${\alpha}$. Individual samples need not have that sign. Implementations preserve ${\alpha}>0$, for example by optimizing its logarithm. When entropy exceeds target, ${\alpha}$ decreases to sharpen exploitation.

### Proximal Policy Optimization (PPO) and GPU Simulation

^sec-appendix-ml-ppo

While off-policy algorithms (TD3, SAC) maximize sample efficiency from replay buffers, on-policy **Proximal Policy Optimization (PPO)** ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-schulman2017ppo|Schulman et al. 2017]]) is the common choice when thousands of simulated robots run in parallel on one GPU. The Isaac Gym benchmarks and legged-locomotion training that learns to walk in minutes both follow this pattern ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-makoviychuk2021isaac|Makoviychuk et al. 2021]]; [[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-rudin2022learning|Rudin et al. 2022]]). PPO clips the incentive for large probability-ratio changes in its surrogate objective; clipping does not impose a hard trust region on the resulting policy:

$$
{\mathcal{L}^{\text{CLIP}}}({\theta}) = {\hat{\mathbb{E}}}_t \left[ \min\left( {\rho}_t({\theta}) {\hat{A}}_t, \, \text{clip}({\rho}_t({\theta}), 1 - {\epsilon_{\text{clip}}}, 1 + {\epsilon_{\text{clip}}}) {\hat{A}}_t \right) \right]
$$

 where the probability ratio is ${\rho}_t({\theta}) = \frac{{\pi_\theta}({\mathbf{a}}_{t} \mid {s}_t)}{\pi_{{\theta_{\text{old}}}}({\mathbf{a}}_{t} \mid {s}_t)}$, clipping parameter ${\epsilon_{\text{clip}}} \approx 0.2$, and advantage estimates ${\hat{A}}_t$ are computed via Generalized Advantage Estimation (GAE):

$$
{\widehat{A}^{\text{GAE}}}_t = \sum_{{l}=0}^\infty ({\gamma} {\lambda})^{l} {\delta}_{t+{l}}^{{V}}, \quad \text{where } {\delta}_t^{V} = {r}({s}_t, {\mathbf{a}}_{t}) + {\gamma} {V_{\phi}}({s}_{t+1}) - {V_{\phi}}({s}_t)
$$

 The parameter ${\lambda}\in[0,1]$ trades bootstrapping against longer sampled returns. At ${\lambda}=0$ the estimate is a one-step TD residual and depends directly on critic error. At ${\lambda}=1$, a complete episode gives the discounted Monte Carlo return minus the baseline; truncated rollouts retain bootstrap error. Terminal transitions omit the continuation value in all Bellman targets above.

#### Massively Parallel GPU Simulation Physics and Memory Hierarchy

^massively-parallel-gpu-simulation-physics-and-memory-hierarchy

On-policy training consumes fresh rollouts, while off-policy methods reuse a replay buffer. Parallel simulation can make fresh experience inexpensive by keeping physics state, observations, policy inference, and rollout storage on the same accelerator. This reduces host-device copies when the complete pipeline supports device-resident execution.

The storage comparison depends on transition size as well as count. If each stored transition takes ${b_{\text{tr}}}$ bytes, a rollout with ${n_{\text{env}}}$ environments and ${h}$ steps needs approximately ${n_{\text{env}}} {h} {b_{\text{tr}}}$ bytes, while a replay buffer with ${n_{\text{replay}}}$ transitions needs ${n_{\text{replay}}} {b_{\text{tr}}}$. Images, privileged state, and training scratch space can dominate either budget. No utilization percentage or training duration follows from choosing PPO; simulation fidelity, contact workload, network shape, and convergence requirements determine throughput and total cost.

### Asymmetric Actor-Critic for Sim-To-Real Transfer

^sec-appendix-ml-asymmetric-ac

Deploying policies trained in physics simulators to physical hardware encounters the **reality gap**: unmodeled actuator latency, mechanical compliance, gear backlash, motor thermal derating, and sensor noise cause policies to stumble or destabilize on physical testbeds. An **asymmetric actor-critic** gives the training critic more information than the deployed actor. A related but distinct technique, Rapid Motor Adaptation (RMA) ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-kumar2021rma|Kumar et al. 2021]]), trains a privileged actor and then predicts its environment latent from onboard history. The distinction determines what must run on the robot:

1.  **Privileged centralized critic:** In training simulation, the critic network ${V_{\phi}}({s_{\text{priv}}})$ or ${Q_{\phi}}({s_{\text{priv}}}, {\mathbf{a}})$ conditions on the complete, privileged simulation state ${s_{\text{priv}}} \in \mathbb{R}^{{d_{\text{priv}}}}$. This privileged vector can contain quantities that are unavailable or measured only imperfectly onboard:
    - True surface contact friction coefficients ${\mu}$;
    - Exact link masses, payload inertia matrices, and center-of-mass offsets ${\Delta} {\mathbf{c}}$;
    - Ground-truth contact force vectors ${\mathbf{f}}$ and normal impulses at each foot/finger;
    - Unoccluded 3D ground-truth obstacle positions and complete terrain heightmaps;
    - Motor winding temperatures and dynamic back-EMF constants.

    A sufficiently complete privileged state can make the critic’s prediction problem Markov and reduce estimation uncertainty. It does not make the actor’s observation complete or remove model error.
2.  **Two-phase adaptation and onboard actor:** To transfer privileged knowledge to physical hardware where ${s_{\text{priv}}}$ cannot be measured, modern architectures use a two-phase distillation pipeline:
    - *Phase 1 (Privileged policy training):* The actor ${\pi_\theta}({\mathbf{a}}_{t} \mid {\mathbf{o}}_{t}, {\mathbf{z}}_t)$ receives deployable onboard observations ${\mathbf{o}}_{t}$ and an environment latent vector ${\mathbf{z}}_t = {E}({s_{\text{priv}}})$, where encoder ${E}$ compresses the privileged state into a low-dimensional manifold (${d_z} \approx 8\text{--}16$).
    - *Phase 2 (Temporal adaptation module):* A lightweight 1D temporal convolutional or MLP adaptation module ${g_{\psi}}({\mathbf{o}_{t-H_{\text{hist}}:t}})$ is trained via supervised regression to predict the latent vector ${\hat{\mathbf{z}}}_t$ purely from a sliding window history of recent proprioceptive observations (joint positions ${\mathbf{q}}$, velocities ${\dot{\mathbf{q}}}$, and commanded actions ${\mathbf{a}}$).
3.  **Deployment cost:** A plain asymmetric actor-critic discards the privileged critic at deployment and runs only the actor. An RMA-style design also runs its history encoder or adaptation module. That module has a real compute and memory cost and can infer hidden parameters only when the observation history makes them identifiable. Critic access to simulator state does not give the actor access to that state.

Domain randomization varies physical parameters during training to expose the policy to a broader range of dynamics. It can improve transfer within the represented conditions, but neither randomization nor privileged training guarantees successful deployment on new terrain.

### Bellman Optimality and Out-Of-Distribution Overestimation

^bellman-optimality-and-out-of-distribution-overestimation

The optimal state-action value function ${Q}^*({s}, {\mathbf{a}})$ satisfies the Bellman optimality equation:

$$
{Q}^*({s}, {\mathbf{a}}) = {r}({s}, {\mathbf{a}}) + {\gamma} \mathbb{E}_{{s'} \sim {p}(\cdot \mid {s}, {\mathbf{a}})} \left[ \max_{{\mathbf{a}'} \in {\mathcal{A}}} {Q}^*({s'}, {\mathbf{a}'}) \right]
$$

 When learning offline from static pre-collected datasets ${\mathcal{D}_{\text{offline}}}$ without interactive physical exploration, evaluating the maximization $\max_{{\mathbf{a}'} \in {\mathcal{A}}} {Q}^*({s'}, {\mathbf{a}'})$ queries the learned critic on counterfactual actions that were never attempted in the dataset. Outside the dataset’s state-action support, function approximation errors can produce value overestimation on out-of-distribution (OOD) actions. An offline policy can favor these spuriously high values and propose destructive motor setpoints unless the permission path rejects them.

Modern offline continuous RL counters this instability through **Conservative Q-Learning (CQL)** ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-kumar2020conservative|Kumar et al. 2020]]), which adds an explicit regularization term that penalizes Q-values on out-of-distribution actions while maximizing Q-values on logged demonstrator actions:

$$
\min_{{Q_{\phi}}} {\alpha_{\text{CQL}}} \left( \mathbb{E}_{{s} \sim {\mathcal{D}_{\text{offline}}}, {\mathbf{a}} \sim {\mu}(\cdot \mid {s})}[{Q_{\phi}}({s}, {\mathbf{a}})] - \mathbb{E}_{({s}, {\mathbf{a}}) \sim {\mathcal{D}_{\text{offline}}}}[{Q_{\phi}}({s}, {\mathbf{a}})] \right) + \frac{1}{2} {\mathcal{L}_{\text{Bellman}}}({Q_{\phi}})
$$

 Under its stated coverage, estimation, and regularization assumptions, CQL provides lower-bound results for expected policy value. The displayed regularizer does not guarantee a pointwise bound below ${Q}^*$ for every unseen state-action pair, and reward conservatism does not prevent actuator runaway. Policy proposals still require runtime permission checks.

### SayCan Affordance-Grounded Skill Selection

^saycan-affordance-grounded-skill-selection

The SayCan framework ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-ahn2022saycan|Ahn et al. 2022]]) integrates semantic knowledge from high-capacity language models with physical affordance constraints from trained policies. Let ${c_{\text{instr}}}$ represent high-level language instruction and ${a}$ represent an available low-level skill. SayCan ranks candidate skills by multiplying a language relevance score and an estimated skill-success score, then normalizing if a selection distribution is needed:

$$
{p}({a} \mid {s}, {c_{\text{instr}}}) \propto {p_{\text{LLM}}}({a} \mid {c_{\text{instr}}}) \cdot {V_{\text{policy}}}({s}, {a})
$$

 Here the two factors separate semantic relevance from physical feasibility:

- ${p_{\text{LLM}}}({a} \mid {c_{\text{instr}}})$ represents the **semantic prior**, evaluating whether skill ${a}$ contributes logically to completing instruction ${c_{\text{instr}}}$.
- ${V_{\text{policy}}}({s}, {a}) \in [0, 1]$ represents the **physical affordance probability**, modeled by a learned value function that predicts the probability of successfully executing skill ${a}$ from current state ${s}$.

If the learned value correctly assigns a near-zero score to an unavailable skill, the product deprioritizes it. The learned score estimates success; it bounds no path, contact force, or clearance, so a separate motion-permission check is needed.

### Comparing Policy Architectures by Compute and Distribution

^sec-appendix-ml-policy-tradeoffs

An MLP point regressor computes one action in a single forward pass but averages ambiguous demonstrations into a single path; a diffusion decoder preserves separate path modes at the cost of ${N_{\text{eval}}}$ sequential network evaluations per chunk. Deploying continuous control policies on physical robots requires selecting an architecture whose computational profile, memory traffic, and latency fit the control loop deadlines of the physical plant ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^tbl-policy-systems-taxonomy|table 1]]).

| Policy component         | Evaluations per proposal                             | Main resource question                                     | Distribution and execution limit                                        |
|:-------------------------|:-----------------------------------------------------|:-----------------------------------------------------------|:------------------------------------------------------------------------|
| MLP point regressor      | One                                                  | Do weights and scratch buffers remain resident?            | Squared-error output averages ambiguous targets                         |
| ConvNet with action head | One encoder and head evaluation                      | How much spatial reuse survives the memory mapping?        | The head, not convolution, determines multimodality                     |
| ACT decoder              | One decoder evaluation after observation encoding    | What do visual tokens and action queries cost?             | Fixed latent selects one output; chunk execution delays feedback        |
| Diffusion decoder        | ${N_{\text{eval}}}$ sequential denoising evaluations | Are weights and activations transferred each step?         | Sampling quality depends on model, solver, and ${N_{\text{eval}}}$      |
| Flow-matching decoder    | Solver-dependent sequential evaluations              | How many field evaluations meet the action-quality target? | Straight conditional paths do not guarantee an exact low-step solution  |
| RL actor                 | Usually one actor evaluation                         | What actor, history encoder, and preprocessing execute?    | RL is a training method; the selected head determines the output family |

Table 1: **Architectural Trade-offs Across Continuous Control Policies**: These are mechanisms, not hardware benchmark ranges. Observation encoding and permission checks add costs beyond the proposal decoder.

^tbl-policy-systems-taxonomy

For a concrete choice, count model parameters and activations, identify the memory level serving each operation, and compare the complete measured execution path with the deadline. The worked decoder budget in [[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^sec-appendix-ml-diffusion|section 1.5.2]] makes those assumptions explicit. Sample efficiency also depends on task coverage and recovery data; it cannot be ranked from the decoder family alone.

## Signal Temporal Logic and Continuous Robustness

^sec-appendix-ml-stl

A boolean pass/fail flag tells an engineer whether a mobile base stayed at least $0.30\text{ m}$ from an aisle rack during a $10\text{ s}$ run, but not whether it cleared the rack by $0.25\text{ m}$ or $0.2\text{ mm}$. Verifying whether a physical autonomous system satisfies dynamic safety requirements requires moving beyond instantaneous boolean assertions to continuous temporal specifications that score how much margin remained across the interval.

### Syntax and Semantics of Signal Temporal Logic

^syntax-and-semantics-of-signal-temporal-logic

A **Signal Temporal Logic (STL)** specification evaluates a continuous-time physical signal ${s}({t})$ against temporal requirements defined over time intervals $[{a}, {b}]$:

$$
{\phi} ::= \top \mid \pi \mid \neg {\phi} \mid {\phi}_1 \wedge {\phi}_2 \mid \square_{[{a}, {b}]} {\phi} \mid \lozenge_{[{a}, {b}]} {\phi} \mid {\phi}_1 {\mathcal{U}_{[a, b]}} {\phi}_2
$$

 where $\pi = ({f}({s}({t})) \ge 0)$ is an atomic predicate (e.g., clearance ${d}({t}) - {d_{\text{safe}}} \ge 0$), $\square_{[{a}, {b}]}$ denotes the **Always** operator, $\lozenge_{[{a}, {b}]}$ denotes the **Eventually** operator, and ${\mathcal{U}_{[a, b]}}$ denotes the **Until** operator. The symbols match those of **[[01 Books/Volume IV - Physical AI/04 Governing the Machine/15 Adversarial Verification/V4-15.10 Searching Beyond the First Trial#^sec-verification-stl-robustness|Signal temporal logic and quantitative robustness]]**.

### Quantitative Robustness Degree

^quantitative-robustness-degree

Beyond a boolean satisfaction verdict (${s} \models {\phi}$), STL admits a signed **quantitative robustness metric** ${\rho}({\phi}, {s}, {t})$.[[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^fn7|⁷]] For a formula combining pressure, speed, and force, first define dimensionless atomic margins ${\bar{f}}_i({s})={f}_i({s})/{c}_i$, where each positive scale ${c}_i$ has the same SI unit as its predicate. Then the minimum and maximum below compare like quantities:

$$
\begin{aligned} {\rho}(\pi, {s}, {t}) &= {\bar{f}}({s}({t})) \\ {\rho}(\neg {\phi}, {s}, {t}) &= -{\rho}({\phi}, {s}, {t}) \\ {\rho}({\phi}_1 \wedge {\phi}_2, {s}, {t}) &= \min\left( {\rho}({\phi}_1, {s}, {t}), {\rho}({\phi}_2, {s}, {t}) \right) \\ {\rho}(\square_{[{a}, {b}]} {\phi}, {s}, {t}) &= \min_{t' \in [t+{a}, t+{b}]} {\rho}({\phi}, {s}, {t'}) \\ {\rho}(\lozenge_{[{a}, {b}]} {\phi}, {s}, {t}) &= \max_{t' \in [t+{a}, t+{b}]} {\rho}({\phi}, {s}, {t'}) \end{aligned}
$$

 A strictly positive ${\rho}$ establishes satisfaction and a negative value establishes violation under the stated semantics. Zero is a boundary case that needs the predicate convention. The normalized magnitude is dimensionless and depends on the declared scales. Preserve each raw physical margin and unit separately in the fault record; a single minimum of meters, newtons, and kilopascals has no physical meaning.

The until operator requires ${\phi}_1$ to hold until a time when ${\phi}_2$ holds. Its robustness is

$$
{\rho}({\phi}_1{\mathcal{U}_{[a, b]}}{\phi}_2, {s}, {t}) =\sup_{t'\in[t+{a},t+{b}]}\min\!\left({\rho}({\phi}_2, {s}, {t'}),\inf_{t''\in[t,t')}{\rho}({\phi}_1, {s}, {t''})\right),
$$

 with the infimum over an empty interval taken as $+\infty$. Infimum and supremum replace minimum and maximum when extrema are not attained. A sampled trace establishes continuous-time satisfaction only with a justified interpolation or intersample variation bound and sufficient margin for measurement error.

## Zero-Failure Testing and the Exposure Wall

^sec-appendix-ml-exposure

In digital software machine learning, validation benchmarks evaluate millions of inference queries or generated tokens in parallel across cloud accelerators within minutes. In physical AI systems, one hour of physical robot operation takes one hour of real wall-clock time and inflicts mechanical wear on actuators, gearboxes, and structural linkages. **[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07.07 Confidence from a Finite Campaign#^sec-evaluation-closed-loop-survival|Confidence from a Finite Campaign]]** uses the zero-failure bound and the Rule of Three to price the running machine’s evaluation campaigns. This section derives the discrete and continuous forms that chapter cites. It also shows why the normal approximation fails when zero failures have been observed.

### Derivation of the Discrete Rule of Three

^derivation-of-the-discrete-rule-of-three

Consider an operational test consisting of ${n}$ independent, identically distributed Bernoulli trials (such as autonomous navigation missions or pick-and-place cycles), where each trial has an unknown catastrophic failure probability ${p_{\text{fail}}} \in [0, 1]$. Let the test observe zero catastrophic failures (${k} = 0$). Under the hypothesis of failure probability ${p_{\text{fail}}}$, the probability of observing zero failures across ${n}$ independent trials is:

$$
\Pr(\text{zero failures} \mid {p_{\text{fail}}}) = (1 - {p_{\text{fail}}})^{n}
$$

 To exclude hypothesis ${p_{\text{fail}}}$ at a one-sided confidence level $1 - {\alpha_{\text{sig}}}$ (e.g., 95 percent confidence with ${\alpha_{\text{sig}}} = 0.05$), the likelihood of observing zero failures under that hypothesis must not exceed ${\alpha_{\text{sig}}}$:

$$
(1 - {p_{\text{fail}}})^{n} \le {\alpha_{\text{sig}}}
$$

 Taking the natural logarithm of both sides:

$$
{n} \ln(1 - {p_{\text{fail}}}) \le \ln {\alpha_{\text{sig}}}
$$

 For rare catastrophic events where failure probability is small (${p_{\text{fail}}} \ll 1$), the first-order Taylor series expansion $\ln(1 - {p_{\text{fail}}}) = -{p_{\text{fail}}} - \frac{{p_{\text{fail}}}^2}{2} - \dots \approx -{p_{\text{fail}}}$ yields:[[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^fn8|⁸]]

$$
-{n} {p_{\text{fail}}} \le \ln {\alpha_{\text{sig}}} \iff {p_{\text{fail}}} \ge \frac{-\ln {\alpha_{\text{sig}}}}{{n}} = \frac{\ln(1/{\alpha_{\text{sig}}})}{{n}}
$$

 Inverting this approximation gives a conservative sample count ${n}$ required to bound the failure probability below ${p_{\text{fail}}}$ at confidence $1 - {\alpha_{\text{sig}}}$:

$$
{n} \ge \frac{\ln(1/{\alpha_{\text{sig}}})}{{p_{\text{fail}}}}
$$

 For standard 95 percent confidence (${\alpha_{\text{sig}}} = 0.05$):

$$
{n} \ge \frac{-\ln(0.05)}{{p_{\text{fail}}}} = \frac{2.99573}{{p_{\text{fail}}}} \approx \frac{3}{{p_{\text{fail}}}}
$$

 This classical result is the **discrete Rule of Three**: observing zero failures across ${n}$ trials bounds the per-trial failure probability to ${p_{\text{fail}}} \le 3/{n}$ at 95 percent confidence. The exact inversion without Taylor approximation is ${p_{\text{fail, upper}}} = 1 - {\alpha_{\text{sig}}}^{1/{n}}$; for small ${p_{\text{fail, upper}}}$, the approximation $-\ln({\alpha_{\text{sig}}})/{n}$ slightly exceeds ${p_{\text{fail, upper}}}$, making the approximation conservative. For a target ${p_{*}}$, the exact required integer count is $\lceil\ln{\alpha_{\text{sig}}}/\ln(1-{p_{*}})\rceil$.

### Full Derivation of the Continuous Poisson Exposure Wall

^full-derivation-of-the-continuous-poisson-exposure-wall

Autonomous robots operate continuously in time rather than in discrete trials. Let catastrophic events follow a stationary homogeneous Poisson process with constant failure rate ${\lambda} > 0$ (failures per operating hour), which emerges naturally from the discrete Bernoulli model via the **Poisson Limit Theorem** (the law of rare events). Subdividing total fleet operating duration ${T}$ into ${n}$ infinitesimal intervals of duration ${\Delta} {t} = {T}/{n}$, the per-interval failure probability is ${p} = {\lambda} {\Delta} {t} = {\lambda} {T} / {n}$. In the limit as ${\Delta} {t} \to 0$ (${n} \to \infty$), the binomial probability of observing exactly ${k}$ failures converges to the Poisson distribution:

$$
\lim_{n \to \infty} \binom{{n}}{{k}} \left(\frac{{\lambda} {T}}{{n}}\right)^{k} \left(1 - \frac{{\lambda} {T}}{{n}}\right)^{{n} - {k}} = \frac{({\lambda} {T})^{k} e^{-{\lambda} {T}}}{{k}!}
$$

 Let ${N}({T})$ denote the cumulative count of catastrophic incidents observed across cumulative fleet operating duration ${T} = \sum_{j=1}^{{N_{\text{fleet}}}} {T}_j$ across ${N_{\text{fleet}}}$ robots. The probability of recording exactly ${k}$ incidents in duration ${T}$ is:

$$
\Pr({N}({T}) = {k}) = \frac{({\lambda} {T})^{k} e^{-{\lambda} {T}}}{{k}!}
$$

 Equivalently, the inter-arrival time ${t_1}$ to the first catastrophic incident follows an exponential distribution ${t_1} \sim \text{Exponential}({\lambda})$ with survival probability $\Pr({t_1} > {T}) = e^{-{\lambda} {T}}$. When a physical fleet qualification campaign completes with zero observed incidents (${k} = 0$):

$$
\Pr({N}({T}) = 0) = \frac{({\lambda} {T})^0 e^{-{\lambda} {T}}}{0!} = e^{-{\lambda} {T}}
$$

 To test whether the operational failure rate is below an acceptable target rate ${\lambda_{\text{target}}}$, we formulate the statistical hypothesis test:

$$
{H}_0: {\lambda} \ge {\lambda_{\text{target}}} \quad \text{versus} \quad {H}_1: {\lambda} < {\lambda_{\text{target}}}
$$

 Under null hypothesis ${H}_0$ with rate ${\lambda_{\text{target}}}$, the probability of observing the zero-failure test outcome is $\Pr({N}({T}) = 0 \mid {\lambda_{\text{target}}}) = e^{-{\lambda_{\text{target}}} {T}}$. To reject ${H}_0$ at significance level ${\alpha_{\text{sig}}}$ (achieving confidence level $1 - {\alpha_{\text{sig}}}$):

$$
{p}\text{-value} = \Pr({N}({T}) \le 0 \mid {\lambda_{\text{target}}}) = e^{-{\lambda_{\text{target}}} {T}} \le {\alpha_{\text{sig}}}
$$

 Taking the natural logarithm of both sides:

$$
-{\lambda_{\text{target}}} {T} \le \ln {\alpha_{\text{sig}}} \iff {T} \ge \frac{-\ln {\alpha_{\text{sig}}}}{{\lambda_{\text{target}}}} = \frac{\ln(1/{\alpha_{\text{sig}}})}{{\lambda_{\text{target}}}}
$$

 For standard 95 percent confidence (${\alpha_{\text{sig}}} = 0.05$), $-\ln(0.05) = \ln(20) \approx 2.99573227$. This yields the **continuous Rule of Three**:

$$
{T} \ge \frac{2.99573}{{\lambda_{\text{target}}}} \approx \frac{3.0}{{\lambda_{\text{target}}}}
$$

 Unlike the discrete Bernoulli derivation which required a Taylor approximation for $\ln(1 - {p_{\text{fail}}})$, the continuous Poisson bound ${T} \ge \frac{\ln(1/{\alpha_{\text{sig}}})}{{\lambda_{\text{target}}}}$ is **mathematically exact** across all values of ${\lambda_{\text{target}}} > 0$.

#### Systems Arithmetic of the Exposure Wall

^systems-arithmetic-of-the-exposure-wall

For an illustrative target of 1 × 10⁻⁹ failures per operating hour, the one-sided 95 percent bound requires 2.996 × 10⁹ zero-failure operating hours. At the less stringent hypothetical target of 1 × 10⁻⁶ per hour, it still requires 2.996 × 10⁶ hours. These are scenario targets, not rates assigned by a software assurance level or a functional-safety classification.

Parallelism reduces calendar time but not total exposure. Even 1,000 independent, configuration-equivalent robots operating continuously need 342.0 365-day calendar years at the stricter target. Shared environmental hazards and common software faults can invalidate that independence assumption. Pooling fleet hours requires a justified common rate and representative exposure.

The **Poisson Exposure Wall** limits what zero-event testing alone can establish. A change to policy weights, firmware, sensors, or the operating domain can alter the event process, so earlier hours do not automatically qualify the changed configuration. Reuse requires evidence that the relevant event rate and conditions remain applicable.

Architectural constraints, fault analysis, and runtime monitors therefore carry evidence that a feasible test campaign cannot supply. They are not unconditional guarantees either: a barrier filter or interlock depends on its plant model, sensing validity, fault assumptions, and timing contract. **[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07.08 Trial Budgets, Stopping Rules, and Comparisons#^sec-evaluation-trial-limits|Trial Budgets, Stopping Rules, and Comparisons]]** uses the exposure bound to separate these evidence obligations.

### Wald Normal Confidence Interval Breakdown and Clopper-Pearson Exact Bounds

^wald-normal-confidence-interval-breakdown-and-clopper-pearson-exact-bounds

In standard machine learning benchmarks, empirical success or failure rates are commonly summarized using the asymptotic Wald normal approximation. For ${k}$ observed failures across ${N}$ independent Bernoulli trials, the sample failure proportion is ${\hat{p}} = {k}/{N}$. The two-sided $(1-{\alpha_{\text{sig}}})$ Wald confidence interval is:

$$
\text{CI}_{\text{Wald}} = {\hat{p}} \pm {z_{1-\alpha_{\text{sig}}/2}} \sqrt{\frac{{\hat{p}}(1 - {\hat{p}})}{{N}}}
$$

 where ${z_{1-\alpha_{\text{sig}}/2}}$ is the standard normal critical value (${z_{1-\alpha_{\text{sig}}/2}} \approx 1.96$ for 95 percent confidence).

#### The Asymptotic Collapse at Zero Failures (${k} = 0$)

^the-asymptotic-collapse-at-zero-failures-observedtrialfailurecount-0

In physical autonomy qualification, candidate systems undergo zero-failure validation tests (${k} = 0$). When ${k} = 0$, the sample proportion is ${\hat{p}} = 0$, causing the estimated variance ${\hat{p}}(1-{\hat{p}})/{N}$ to collapse to zero:

$$
\text{CI}_{\text{Wald}}\Big|_{k=0} = 0 \pm {z_{1-\alpha_{\text{sig}}/2}} \sqrt{\frac{0(1 - 0)}{{N}}} = [0, 0]
$$

 The Wald interval asserts, at 95 percent confidence, that the failure probability is exactly zero after a finite test run. It ignores finite-sample uncertainty, and this particular interval excludes every nonzero failure rate. Repeated-sampling coverage of the Wald procedure is not identically zero, but can fall far below its nominal level near the boundary.

For a small nonzero true failure probability, $(1-{p_{\text{fail}}})^{n}$ can remain substantial, so a zero-failure campaign is not evidence of impossibility. The degenerate Wald interval confuses an estimated zero variance with zero uncertainty. Near the opposite boundary it has the same defect, and interior intervals can extend outside the valid probability range.

#### Clopper-Pearson Exact Binomial Inversion

^clopper-pearson-exact-binomial-inversion

To maintain non-asymptotic statistical rigor, physical autonomy qualification can use **Clopper-Pearson exact binomial confidence intervals** ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-clopper1934use|Clopper and Pearson 1934]]). The Clopper-Pearson interval $[{p_{L}}, {p_{U}}]$ inverts the exact binomial cumulative distribution function without normal approximations:

$$
\sum_{{x}=k}^{N} \binom{{N}}{{x}} {p_{L}}^{x} (1 - {p_{L}})^{{N} - {x}} = \frac{{\alpha_{\text{sig}}}}{2}, \quad \sum_{{x}=0}^{k} \binom{{N}}{{x}} {p_{U}}^{x} (1 - {p_{U}})^{{N} - {x}} = \frac{{\alpha_{\text{sig}}}}{2}
$$

 By the identity connecting binomial sums to the regularized incomplete Beta function ${I}_{{p_{\text{fail}}}}({a}, {b})$:

$$
\sum_{{x}=k}^{N} \binom{{N}}{{x}} {p_{\text{fail}}}^{x} (1 - {p_{\text{fail}}})^{{N} - {x}} = {I}_{{p_{\text{fail}}}}({k}, {N} - {k} + 1) = \frac{1}{\text{B}({k}, {N} - {k} + 1)} \int_0^{{p_{\text{fail}}}} {t}^{{k}-1}(1 - {t})^{{N} - {k}} \, d{t}
$$

 for $0<{k}<{N}$, these exact boundaries can be computed using quantiles of the Beta distribution:

$$
{p_{L}} = \text{BetaQuantile}\left(\frac{{\alpha_{\text{sig}}}}{2}; \, {k}, \, {N} - {k} + 1\right), \quad {p_{U}} = \text{BetaQuantile}\left(1 - \frac{{\alpha_{\text{sig}}}}{2}; \, {k} + 1, \, {N} - {k}\right)
$$

 At the endpoints, set ${p_{L}}=0$ for ${k}=0$ and ${p_{U}}=1$ for ${k}={N}$; the corresponding Beta distribution with a zero shape parameter is not defined.

#### Exact Bounds at Zero Failures (${k} = 0$)

^exact-bounds-at-zero-failures-observedtrialfailurecount-0

When zero failures occur in physical testing (${k} = 0$), the lower bound is ${p_{L}} = 0$. For a one-sided $(1 - {\alpha_{\text{sig}}})$ upper confidence bound, the exact binomial condition simplifies to:

$$
\Pr({X} = 0) = \binom{{n}}{0} {p_{U}}^0 (1 - {p_{U}})^{n} = (1 - {p_{U}})^{n} = {\alpha_{\text{sig}}}
$$

 Solving directly for ${p_{U}}$:

$$
1 - {p_{U}} = {\alpha_{\text{sig}}}^{1/{n}} \iff {p_{U}} = 1 - {\alpha_{\text{sig}}}^{1/{n}} = 1 - \exp\left(\frac{1}{{n}} \ln {\alpha_{\text{sig}}}\right)
$$

 Applying the Taylor expansion $e^{u} = 1 + {u} + \frac{{u}^2}{2} + \dots$ with ${u} = \frac{\ln {\alpha_{\text{sig}}}}{{n}}$:

$$
{p_{U}} = 1 - \left( 1 + \frac{\ln {\alpha_{\text{sig}}}}{{n}} + \mathcal{O}({n}^{-2}) \right) = \frac{-\ln {\alpha_{\text{sig}}}}{{n}} + \mathcal{O}({n}^{-2})
$$

 For ${\alpha_{\text{sig}}} = 0.05$, $-\ln(0.05) \approx 2.99573$, rigorously recovering the discrete Rule of Three: ${p_{U}} \approx 3/{n}$. For a two-sided 95 percent interval (${\alpha_{\text{sig}}} = 0.05$, tail probability ${\alpha_{\text{sig}}}/2 = 0.025$):

$$
{p_{U}} = 1 - (0.025)^{1/{n}} \approx \frac{-\ln(0.025)}{{n}} = \frac{3.68888}{{n}} \approx \frac{3.69}{{n}}
$$

 Unlike the degenerate Wald interval, the Clopper-Pearson interval guarantees exact non-asymptotic coverage of at least $1 - {\alpha_{\text{sig}}}$ for every finite sample size ${N} \ge 1$.

## Sequential Probability Ratio Test

^sec-appendix-ml-sprt

Evaluating embodied physical policies on physical hardware is expensive and induces mechanical wear. A fixed-sample design predeclares sample count ${N}$ for its planned acceptance decision and inference. A predeclared rejection rule may stop a failing campaign early, and physical safety can require termination at any time; neither decision requires continued exposure to an unsafe candidate. Early acceptance is different. Stopping when an accumulating result looks favorable and reporting the fixed-sample error guarantee can inflate false acceptance. Valid early acceptance requires a stopping rule with its own error calibration.

Abraham Wald’s **Sequential Probability Ratio Test (SPRT)** ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-wald1945sequential|Wald 1945]]) handles optional stopping for two predeclared simple hypotheses by updating a likelihood ratio after each rollout and comparing it with stopping boundaries. **[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07.08 Trial Budgets, Stopping Rules, and Comparisons#^sec-evaluation-sequential-sprt|Sequential probability ratio testing]]** applies the test to the running machine’s campaign in the same convention used here. The convention uses per-trial failure probability ${p}$, ${k}$ failures in ${m}$ trials, statistic ${\Lambda_m}$, null hypothesis the unacceptable ${p}_0$, and error allowances ${\alpha_{\text{sig}}}$ and ${\beta}$.

### Log-Likelihood Ratio and Bernoulli Updates

^log-likelihood-ratio-and-bernoulli-updates

Across consecutive physical rollouts with independent trial outcomes ${x}_1, {x}_2, \dots, {x}_{{m}}$, sequential testing compares two competing operational hypotheses:

- Null hypothesis ${H}_0$: The system failure probability is unacceptable (${p} = {p}_0$).
- Alternative hypothesis ${H}_1$: The system failure probability meets the safety target (${p} = {p}_1 < {p}_0$).

After observing ${m}$ trials, the cumulative log-likelihood ratio ${\Lambda_m}$ is:

$$
{\Lambda_m} = \sum_{i=1}^{m} \ln \frac{\Pr({x}_i \mid {H}_1)}{\Pr({x}_i \mid {H}_0)}
$$

 For discrete Bernoulli trials where ${x}_i \in \{0, 1\}$ (with ${x}_i = 1$ denoting task failure and ${x}_i = 0$ denoting task success), let ${k} = \sum_{i=1}^{m} {x}_i$ be the cumulative failure count across ${m}$ runs. The log-likelihood ratio simplifies to the exact closed-form evaluation:

$$
{\Lambda_m} = {k} \ln \left(\frac{{p}_1}{{p}_0}\right) + ({m} - {k}) \ln \left(\frac{1 - {p}_1}{1 - {p}_0}\right)
$$

### Wald Stopping Boundaries and Decision Rules

^wald-stopping-boundaries-and-decision-rules

Wald’s stopping rule rests on declared error rates. The Type I error rate ${\alpha_{\text{sig}}}$ is the maximum allowable probability of falsely accepting ${H}_1$ when ${H}_0$ is true. The Type II error rate ${\beta}$ is the maximum allowable probability of falsely rejecting ${H}_1$ when ${H}_1$ is true. Testing then proceeds according to Wald’s stopping rule:

$$
{\Lambda_{\text{lo}}} < {\Lambda_m} < {\Lambda_{\text{up}}}
$$

 where the usual Wald boundary approximations are:

$$
{\Lambda_{\text{up}}} = \ln \left(\frac{1 - {\beta}}{{\alpha_{\text{sig}}}}\right), \quad {\Lambda_{\text{lo}}} = \ln \left(\frac{{\beta}}{1 - {\alpha_{\text{sig}}}}\right)
$$

 At each evaluation step ${m}$:

1.  If ${\Lambda_m} \ge {\Lambda_{\text{up}}}$: Halt and favor ${H}_1$ over the specified ${H}_0$ under the trial model; this is not a general safety certification.
2.  If ${\Lambda_m} \le {\Lambda_{\text{lo}}}$: Halt and favor ${H}_0$ over the specified ${H}_1$; do not release on this evidence.
3.  If ${\Lambda_{\text{lo}}} < {\Lambda_m} < {\Lambda_{\text{up}}}$: The accumulated evidence remains inconclusive; execute rollout ${m}+1$.

Wald’s approximate thresholds need calibration because the discrete log-likelihood increments can overshoot a boundary. Conservative alternatives are ${\Lambda_{\text{up}}}=\ln(1/{\alpha_{\text{sig}}})$ and ${\Lambda_{\text{lo}}}=\ln{\beta}$: the likelihood-ratio martingale under ${H}_0$ bounds false acceptance by ${\alpha_{\text{sig}}}$, and the reciprocal under ${H}_1$ bounds false rejection by ${\beta}$. These guarantees apply to the declared simple hypotheses and observation model, not arbitrary deployment shifts.

### Average Sample Number Optimality

^average-sample-number-optimality

For Bernoulli failure probability ${p}$, the expected log-likelihood increment is

$$
{m}({p})={p}\ln\frac{{p}_1}{{p}_0}+(1-{p})\ln\frac{1-{p}_1}{1-{p}_0}.
$$

 Let ${N_{\text{stop}}}$ be the stopping sample count. Ignoring boundary overshoot and using the nominal endpoint error rates gives Wald’s approximate average sample numbers

$$
\mathbb{E}_{{p}_0}[{N_{\text{stop}}}]\approx\frac{{\alpha_{\text{sig}}} {\Lambda_{\text{up}}}+(1-{\alpha_{\text{sig}}}){\Lambda_{\text{lo}}}}{{m}({p}_0)},\qquad \mathbb{E}_{{p}_1}[{N_{\text{stop}}}]\approx\frac{(1-{\beta}){\Lambda_{\text{up}}}+{\beta} {\Lambda_{\text{lo}}}}{{m}({p}_1)}.
$$

 The denominators are the evidence gained per trial, negative under ${H}_0$ and positive under ${H}_1$. As the hypotheses approach each other, their magnitudes shrink and the required exposure grows. For calibrated boundaries, use the actual operating characteristics and terminal overshoot rather than substituting nominal errors. A predeclared trial cap also changes the protocol and requires an explicit inconclusive outcome or recalibrated terminal rule.

For independent identically distributed outcomes under these two simple hypotheses, SPRT has an average-sample-number efficiency result relative to comparable tests.[[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^fn9|⁹]] Actual machine-hour savings depend on the two event probabilities, error allowances, overshoot at the stopping boundaries, and trial cost. The displayed thresholds are approximations; a finite-sample operating-characteristic calculation or calibrated simulation is needed for the chosen protocol.

## Extreme Value Theory and Tail Risk

^sec-appendix-ml-evt

Average behavior does not determine the largest disturbance or latency spike a controller will encounter. The central limit theorem concerns normalized sums under conditions such as finite variance; it does not imply that individual observations or their far tails are Gaussian. Even a good Gaussian fit near the center can misstate rare exceedances.

For a genuinely Gaussian variable, a one-sided exceedance above ${k}$ standard deviations has probability $1-{\Phi}({k})$, where ${\Phi}$ is the standard normal cumulative distribution function. Under independent samples at rate ${f}$, its mean waiting time is $1/[{f}(1-{\Phi}({k}))]$. Correlation changes the clustering and waiting-time distribution, so a control-loop frequency alone does not establish an independent-trial rate.

### Physical Mechanisms That Motivate Tail Analysis

^physical-mechanisms-that-motivate-tail-analysis

Disturbances affecting structural survival and controller timing can arise from nonlinear or correlated mechanisms that a Gaussian sensor-noise model does not represent:

1.  **Contact impact dynamics:** When an autonomous manipulator or mobile robot collides unexpectedly with a rigid obstacle, Hertzian contact mechanics govern the compressive force along the normal of each contact. This force is ${f_{k, \perp}} = {k_{c}} {\delta}^{3/2}$, where ${\delta}$ is deformation and the subscripts name the contact and its normal direction. When compliant protective covers bottom out against rigid metal chassis, contact stiffness shoots up discontinuously (${k_{c}} \to {k_{\infty}}$), converting residual kinetic energy into sharp loads. The relation ${F_{\text{unbraked}}}={v}\sqrt{{m} {k_{\text{contact}}}}$ applies to an ideal linear spring of stiffness ${k_{\text{contact}}}$ absorbing kinetic energy, not to the Hertzian stiffness coefficient ${k_{c}}$.
2.  **Mechanical friction transitions:** Stick-slip friction instability, drivetrain gear backlash, and structural resonance modes inject multiplicative, non-Gaussian torque transients into actuator gearboxes during rapid reversals.
3.  **Real-time execution jitter:** On embedded systems, shared PCIe buses, memory cache thrashing, interrupt storms, and memory reclamation pauses produce tail latency spikes in control loops that break temporal determinism. Head-of-line blocking can amplify latency tails, but a Pareto service-time model requires evidence; bounded service times and arrival processes can produce different waiting-time tails.

These mechanisms motivate inspecting the measured tail; they do not prove a Pareto law. Bounded disturbances, exponential tails, lognormal tails, and power-law tails are all possible. **Extreme Value Theory (EVT)** supplies limiting models for maxima and threshold exceedances, with tail family and parameter uncertainty estimated from representative data. A positive shape parameter supports a power-law model over the validated range, not an assertion that every physical shock has infinite variance.

### The Fisher-Tippett-Gnedenko Theorem

^the-fisher-tippett-gnedenko-theorem

While the Central Limit Theorem describes the limiting behavior of normalized sums, the **Fisher-Tippett-Gnedenko theorem** ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-coles2001introduction|Coles 2001]]) establishes the asymptotic behavior of normalized block maxima:

$$
{M}_n = \max\{{X}_1, {X}_2, \dots, {X}_n\}
$$

 Let ${X}_1, {X}_2, \dots, {X}_n$ be a sequence of independent and identically distributed random variables with cumulative distribution function ${F}({x})$. If there exist normalizing sequences of real constants ${a}_n > 0$ and ${b}_n \in \mathbb{R}$ such that the normalized block maximum converges to a non-degenerate limiting distribution ${G}({z})$:

$$
\lim_{n \to \infty} \Pr\left( \frac{{M}_n - {b}_n}{{a}_n} \le {z} \right) = \lim_{n \to \infty} {F}^{n}({a}_n {z} + {b}_n) = {G}({z})
$$

 then ${G}({z})$ belongs exclusively to the **Generalized Extreme Value (GEV)** family:[[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^fn10|¹⁰]]

$$
{G}({z}) = \exp\left( -\left[ 1 + {\xi} \left(\frac{{z} - {\mu}}{{\sigma}}\right) \right]^{-1/{\xi}} \right)
$$

 defined on $\{{z} : 1 + {\xi}({z} - {\mu})/{\sigma} > 0\}$, with location parameter ${\mu} \in \mathbb{R}$, scale parameter ${\sigma} > 0$, and shape parameter ${\xi} \in \mathbb{R}$. The shape parameter ${\xi}$ partitions extreme behavior into three distinct tail regimes:

1.  **Gumbel (Type I, ${\xi} = 0$):** The continuous limit as ${\xi} \to 0$:

$$
{G}({z}) = \exp\left( -\exp\left(-\frac{{z} - {\mu}}{{\sigma}}\right) \right)
$$

 including several unbounded tail forms, rather than only exponential tails. The maximum domain of attraction $\text{MDA}(\text{Gumbel})$ includes Gaussian, exponential, lognormal, and Gamma distributions.

2.  **Fréchet (Type II, ${\xi} > 0$, with tail index ${\alpha_{\text{tail}}} = 1/{\xi}$):** The heavy-tailed regime where survival probabilities decay according to a polynomial power law: $\Pr({X} > {x}) \sim {x}^{-{\alpha_{\text{tail}}}}$. The domain of attraction $\text{MDA}(\text{Fréchet})$ includes Pareto, Cauchy, and Student’s ${t}$ distributions. For a power-law density ${p}({x}) \sim {\alpha_{\text{tail}}} {x}^{-{\alpha_{\text{tail}}}-1}$, the ${k}$-th raw moment evaluates to:

$$
\mathbb{E}[{X}^{k}] = \int_{{x}_0}^\infty {x}^{k} {p}({x}) \, d{x} \sim {\alpha_{\text{tail}}} \int_{{x}_0}^\infty {x}^{{k} - {\alpha_{\text{tail}}} - 1} \, d{x}
$$

 This integral converges if and only if ${k} - {\alpha_{\text{tail}}} - 1 < -1 \iff {k} < {\alpha_{\text{tail}}} = 1/{\xi}$. For any moment order ${k} \ge 1/{\xi}$, the moment diverges to infinity ($\mathbb{E}[{X}^{k}] = \infty$). A direct mathematical consequence is that for ${\xi} \ge 0.5$ (${\alpha_{\text{tail}}} \le 2$), the unbounded power-law model has **infinite variance** ($\operatorname{Var}({X}) = \infty$). The usual finite-variance central limit theorem then does not apply, and sample variance cannot converge to a finite population variance. For ${\xi} \ge 1.0$, the distribution has infinite mean. These are properties of an unbounded fitted model. Finite physical limits can truncate the tail, and a finite dataset cannot establish literal infinite moments.

3.  **Weibull (Type III, ${\xi} < 0$):** Bounded distributions with a finite physical upper endpoint (${z} \le {\mu} - {\sigma}/{\xi}$). The domain $\text{MDA}(\text{Weibull})$ includes Uniform and Beta distributions, applicable when hard physical limits (such as mechanically positive endstops) strictly bound the disturbance.

### Peaks-Over-Threshold and Generalized Pareto Distribution

^peaks-over-threshold-and-generalized-pareto-distribution

Block maxima analysis discards valuable extreme observations occurring within the same block (e.g., secondary collision shocks) and retains uninformative low maxima from quiescent blocks. The **Peaks-Over-Threshold (POT)** approach, formalized by the Pickands-Balkema-de Haan theorem ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-coles2001introduction|Coles 2001]]), analyzes all excess values ${Y} = {X} - {u}$ exceeding a sufficiently high physical threshold ${u}$:

$$
{F_{u}}({y}) = \Pr({X} - {u} \le {y} \mid {X} > {u}) = \frac{{F}({u} + {y}) - {F}({u})}{1 - {F}({u})}, \quad {y} \ge 0
$$

 The **Pickands-Balkema-de Haan theorem** proves that for a broad class of underlying physical distributions ${F} \in \text{MDA}(\text{GEV}_{\xi})$, as threshold ${u}$ approaches the right endpoint ${x_F}$:

$$
\lim_{{u} \to {x_F}} \sup_{0 \le {y} < {x_F} - {u}} \left| {F_{u}}({y}) - {H}({y}; {\tilde{\sigma}}({u}), {\xi}) \right| = 0
$$

 where, for ${\xi}\ne0$, ${H}({y})$ is the **Generalized Pareto Distribution (GPD)**:

$$
{H}({y}) = 1 - \left( 1 + \frac{{\xi} {y}}{{\tilde{\sigma}}} \right)^{-1/{\xi}}
$$

 defined for ${y}\ge0$ with $1+{\xi} {y}/{\tilde{\sigma}}>0$, with scale parameter ${\tilde{\sigma}} > 0$ and shape parameter ${\xi}$ identical to the GEV shape parameter. For ${\xi}=0$, take the continuous limit ${H}({y})=1-\exp(-{y}/{\tilde{\sigma}})$; for ${\xi}<0$, the upper endpoint is $-{\tilde{\sigma}}/{\xi}$.

#### Threshold Stability and Mean Residual Life

^threshold-stability-and-mean-residual-life

A key property of the GPD is **threshold stability**. If the exceedances over threshold ${u}_0$ follow $\text{GPD}({\tilde{\sigma}}_0, {\xi})$, then for any higher threshold ${u}>{u}_0$ below the upper endpoint, the exceedances over ${u}$ also follow a GPD with the *same* shape ${\xi}$ and linearly shifted scale:

$$
{\tilde{\sigma}}({u}) = {\tilde{\sigma}}_0 + {\xi} ({u} - {u}_0)
$$

 The **Mean Residual Life (MRL)** evaluates the expected excess conditional on exceeding threshold ${u}$:

$$
\mathbb{E}[{X}-{u}\mid {X}>{u}]=\int_0^{{y_{\max}}}[1-{H}({y})]\,d{y}=\frac{{\tilde{\sigma}}({u})}{1-{\xi}}\quad({\xi}<1),
$$

 where ${y_{\max}}=\infty$ for ${\xi}\ge0$ and ${y_{\max}}=-{\tilde{\sigma}}({u})/{\xi}$ for ${\xi}<0$. The exponential limit at ${\xi}=0$ has mean ${\tilde{\sigma}}({u})$.

Substituting the threshold stability relation yields a strictly linear function of threshold ${u}$:

$$
\mathbb{E}[{X} - {u} \mid {X} > {u}] = \frac{{\tilde{\sigma}}_0 + {\xi}({u} - {u}_0)}{1 - {\xi}}
$$

 Systems engineers plot empirical mean excess against candidate thresholds ${u}$ (the MRL plot); approximate linearity helps choose a candidate threshold, alongside parameter stability, dependence diagnostics, and uncertainty. It does not certify a unique mathematically valid threshold.

Given ${N_u}$ exceedances $\{{y}_1, \dots, {y}_{{N_u}}\}$ where ${y}_i = {x}_i - {u} > 0$, parameters $({\tilde{\sigma}}, {\xi})$ can be estimated via Maximum Likelihood Estimation (MLE), with the following expression for ${\xi}\ne0$ and valid support:

$$
\ln {L}({\tilde{\sigma}}, {\xi}) = -{N_u} \ln {\tilde{\sigma}} - \left( 1 + \frac{1}{{\xi}} \right) \sum_{i=1}^{{N_u}} \ln \left( 1 + \frac{{\xi} {y}_i}{{\tilde{\sigma}}} \right)
$$

 Under the GPD model and regularity conditions, including ${\xi}>-1/2$, maximum-likelihood estimates have asymptotic normality and efficiency properties. Finite-sample bias, threshold choice, and clustered exceedances still affect the estimate.

### Hardware Margin and High-Quantile Sizing

^hardware-margin-and-high-quantile-sizing

Sizing physical hardware margins against an ultra-rare catastrophic event probability ${\epsilon}$ (e.g., ${\epsilon} = 10^{-7}$ per control cycle) requires extrapolating from ${N}$ total operational cycles and ${N_u}$ recorded threshold exceedances (${X} > {u}$). With empirical exceedance fraction ${\hat{\zeta}_{u}} = {N_u} / {N} > {\epsilon}$, the **high-quantile return level** ${z_\epsilon}$ satisfies $\Pr({X} > {z_\epsilon}) = {\epsilon}$:

$$
\begin{aligned} \Pr({X} > {z_\epsilon}) &= \Pr({X} > {u}) \Pr({X} > {z_\epsilon} \mid {X} > {u}) \\ &= {\hat{\zeta}_{u}} \left[ 1 - {H}({z_\epsilon} - {u}) \right] \\ &= \frac{{N_u}}{{N}} \left( 1 + \frac{{\xi} ({z_\epsilon} - {u})}{{\tilde{\sigma}}} \right)^{-1/{\xi}} = {\epsilon} \end{aligned}
$$

 Inverting this relation for ${z_\epsilon}$:

$$
\left( 1 + \frac{{\xi} ({z_\epsilon} - {u})}{{\tilde{\sigma}}} \right)^{-1/{\xi}} = \frac{{N} {\epsilon}}{{N_u}} \iff 1 + \frac{{\xi} ({z_\epsilon} - {u})}{{\tilde{\sigma}}} = \left( \frac{{N_u}}{{N} {\epsilon}} \right)^{\xi}
$$

 Rearranging yields the closed-form return level formula:

$$
{z_\epsilon} = {u} + \frac{{\tilde{\sigma}}}{{\xi}} \left[ \left(\frac{{N_u}}{{N} {\epsilon}}\right)^{{\xi}} - 1 \right] \quad ({\xi} \ne 0)
$$

 Taking the continuous limit as ${\xi} \to 0$ using L’Hôpital’s rule ($\lim_{{\xi} \to 0} \frac{{a}^{\xi} - 1}{{\xi}} = \ln {a}$):

$$
{z_\epsilon} = {u} + {\tilde{\sigma}} \ln \left( \frac{{N_u}}{{N} {\epsilon}} \right) \quad ({\xi} = 0)
$$

#### Systems Engineering Sizing Rules

^systems-engineering-sizing-rules

For a fitted positive shape parameter, the return level grows as a power of $1/{\epsilon}$; the exponential limit grows logarithmically. Those rates do not yield a numerical ratio between shock loads without matching thresholds, scales, and exceedance frequencies. Report parameter and model uncertainty with the return level, and keep the target unit explicit: a probability per sampled cycle is not a rate per operating hour.

A force quantile can inform spring travel through ${\delta}={z_\epsilon}/{k_{\text{spring}}}$ only under a valid linear spring model; energy capacity and bottoming-out dynamics still require separate checks. A latency quantile can inform availability analysis, but a watchdog timeout must remain inside the plant’s maximum tolerable delay even when some valid computations exceed it. If that interval is infeasible, the scheduling or fallback design must change.

Queue depth requires an arrival-and-service model converting a delay into accumulated packets or frames; taking the ceiling of a time-valued quantile is dimensionally invalid. Thermal sizing likewise needs the energy and repetition rate of braking events, not a peak-force quantile alone. EVT estimates a tail under stated assumptions; it supplies neither a deterministic maximum nor a guarantee against all future physical failures.

## Further Reading

^further-reading

For a deeper foundational understanding of machine learning theory, sequential statistics, and extreme value modeling, consult the following authoritative references:

- **Deep Learning** ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-goodfellow2016deep|Goodfellow et al. 2016]]) provides a comprehensive treatment of neural network optimization, regularized representation learning, and Lipschitz sensitivity bounds.
- **An Introduction to Statistical Modeling of Extreme Values** ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-coles2001introduction|Coles 2001]]) establishes the definitive mathematical foundations for GEV, GPD, and tail risk quantification.
- **Sequential Tests of Statistical Hypotheses** ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-wald1945sequential|Wald 1945]]) develops the first-principles mathematical framework and average sample number optimality proofs for the Sequential Probability Ratio Test.
- **A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning** ([[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^ref-ross2011reduction|Ross et al. 2011]]) establishes the theoretical foundations of compounding error in imitation learning and derives the DAgger algorithm.

Back to top

## Source References

^source-references

Oquab, Maxime, Timothée Darcet, Théo Moutakanni, Huy Vo, Marc Szafraniec, Vasil Khalidov, Pierre Fernandez, et al. 2023. “Dinov2: Learning Robust Visual Features Without Supervision.” *arXiv Preprint arXiv:2304.07193*.

^ref-oquab2023dinov2

Liu, Zhijian, Haotian Tang, Alexander Amini, Xinyu Yang, Huizi Mao, Daniela Rus, and Song Han. 2023. “BEVFusion: Multi-Task Multi-Sensor Fusion with Unified Bird’s-Eye View Representation.” *IEEE International Conference on Robotics and Automation (ICRA)*, 2774–81.

^ref-liu2023bevfusion

Philion, Jonah, and Sanja Fidler. 2020. “Lift, Splat, Shoot: Encoding Images from Arbitrary Cameras by Predicting Depth.” *Proceedings of the European Conference on Computer Vision (ECCV)*, 272–85.

^ref-philion2020lift

Kerbl, Bernhard, Georgios Kopanas, Thomas Leimk"uhler, and George Drettakis. 2023. “3D Gaussian Splatting for Real-Time Radiance Field Rendering.” *ACM Transactions on Graphics* 42 (4): 139:1–14.

^ref-kerbl20233d

Matsuki, Hidenobu, Ryo Murai, Paul H. J. Kelly, and Andrew J. Davison. 2024. “Gaussian Splatting SLAM.” *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, 18039–48.

^ref-matsuki2024gaussian

Elfes, Alberto. 1989. “Using Occupancy Grids for Mobile Robot Perception and Navigation.” *Computer* 22 (6): 46–57. https://doi.org/10.1109/2.30720.

^ref-elfes1989using

Amanatides, John, and Andrew Woo. 1987. “A Fast Voxel Traversal Algorithm for Ray Tracing.” *Eurographics ’87*, 3–10.

^ref-amanatides1987fast

Museth, Ken. 2013. “VDB: High-Resolution Sparse Volumes with Dynamic Topology.” *ACM Transactions on Graphics* 32 (3): 1–22. https://doi.org/10.1145/2487228.2487235.

^ref-museth2013vdb

Hornung, Armin, Kai M Wurm, Maren Bennewitz, Cyrill Stachniss, and Wolfram Burgard. 2013. “OctoMap: An Efficient Probabilistic 3D Mapping Framework Based on Octrees.” *Autonomous Robots* 34 (3): 189–206.

^ref-hornung2013octomap

Newcombe, Richard A, Shahram Izadi, Otmar Hilliges, David Molyneaux, David Kim, Andrew J Davison, Pushmeet Kohi, Jamie Shotton, Steve Hodges, and Andrew Fitzgibbon. 2011. “KinectFusion: Real-Time Dense Surface Mapping and Tracking.” *IEEE International Symposium on Mixed and Augmented Reality (ISMAR)*, 127–36.

^ref-newcombe2011kinectfusion

Oleynikova, Helen, Zachary Taylor, Marius Fehr, Roland Siegwart, and Juan Nieto. 2017. “Voxblox: Incremental 3D Euclidean Signed Distance Fields for on-Board MAV Planning.” *IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)*, 1366–73.

^ref-oleynikova2017voxblox

Florence, Pete, Corey Lynch, Feryal Behbahani, Tianhe Yu, Wenlong Huang, Fei Xia, et al. 2022. “Implicit Behavioral Cloning.” *Conference on Robot Learning (CoRL)*, 158–68.

^ref-florence2022implicit

Zhao, Tony Z., Vikash Kumar, Sergey Levine, and Chelsea Finn. 2023. “Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware.” *Robotics: Science and Systems (RSS)*. https://doi.org/10.15607/RSS.2023.XIX.016.

^ref-zhao2023learning

Brohan, Anthony, Noah Brown, Justice Carbajal, Yevgen Chebotar, Joseph Dabis, Chelsea Finn, Keerthana Gopalakrishnan, et al. 2023. “RT-1: Robotics Transformer for Real-World Control at Scale.” *Robotics: Science and Systems (RSS)*. https://doi.org/10.15607/RSS.2023.XIX.025.

^ref-brohan2023rt1

Brohan, Anthony, Noah Brown, Justice Carbajal, Yevgen Chebotar, Xi Chen, Krzysztof Choromanski, Tianli Ding, et al. 2023. “RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control.” *arXiv Preprint arXiv:2307.15818*.

^ref-brohan2023rt2

Kim, Moo Jin, Karl Pertsch, Siddharth Karamcheti, Ted Xiao, Ashwin Balakrishna, Suraj Nair, Rafael Rafailov, et al. 2024. “OpenVLA: An Open-Source Vision-Language-Action Model.” *arXiv Preprint arXiv:2406.09246*.

^ref-kim2024openvla

Lipman, Yaron, Ricky TQ Chen, Heli Ben-Hamu, Maximilian Nicklas, and Matt Le. 2022. “Flow Matching for Generative Modeling.” *arXiv Preprint arXiv:2210.02747*.

^ref-lipman2022flow

Chi, Cheng, Zhenjia Xu, Siyuan Feng, Eric Cousineau, Yilun Du, Benjamin Burchfiel, Russ Tedrake, and Shuran Song. 2025. “Diffusion Policy: Visuomotor Policy Learning via Action Diffusion.” *The International Journal of Robotics Research* 44 (10-11): 1684–704. https://doi.org/10.1177/02783649241273668.

^ref-chi2024diffusionpolicy

Sutton, Richard S., and Andrew G. Barto. 2018. *Reinforcement Learning: An Introduction*. 2nd ed. MIT Press.

^ref-sutton2018reinforcement

Schulman, John, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. 2017. “Proximal Policy Optimization Algorithms.” *arXiv Preprint arXiv:1707.06347*.

^ref-schulman2017ppo

Makoviychuk, Viktor, Lukasz Wawrzyniak, Yunrong Guo, Michelle Lu, Kier Storey, Miles Macklin, David Hoeller, et al. 2021. “Isaac Gym: High Performance GPU-Based Physics Simulation for Robot Learning.” *arXiv Preprint arXiv:2108.10470*.

^ref-makoviychuk2021isaac

Rudin, Nikita, David Hoeller, Philipp Reist, and Marco Hutter. 2022. “Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning.” *Proceedings of the 5th Conference on Robot Learning*, Proceedings of machine learning research, vol. 164: 91–100.

^ref-rudin2022learning

Kumar, Ashish, Zipeng Fu, Deepak Pathak, and Jitendra Malik. 2021. “RMA: Rapid Motor Adaptation for Legged Robots.” *Robotics: Science and Systems XVII*. https://doi.org/10.15607/RSS.2021.XVII.011.

^ref-kumar2021rma

Kumar, Aviral, Aurick Zhou, George Tucker, and Sergey Levine. 2020. “Conservative q-Learning for Offline Reinforcement Learning.” *Advances in Neural Information Processing Systems (NeurIPS)* 33: 1179–91.

^ref-kumar2020conservative

Ahn, Michael, Anthony Brohan, Yevgen Chebotar, et al. 2022. “Do as I Can, Not as I Say: Grounding Language in Robotic Affordances.” *Proceedings of the 6th Conference on Robot Learning (CoRL)*, Proceedings of machine learning research, vol. 205: 287–318.

^ref-ahn2022saycan

Clopper, C. J., and Egon S. Pearson. 1934. “The Use of Confidence or Fiducial Limits Illustrated in the Case of the Binomial.” *Biometrika* 26 (4): 404–13.

^ref-clopper1934use

Goodfellow, Ian, Yoshua Bengio, and Aaron Courville. 2016. *Deep Learning*. MIT Press.

^ref-goodfellow2016deep

Coles, Stuart. 2001. *An Introduction to Statistical Modeling of Extreme Values*. Springer.

^ref-coles2001introduction

Wald, Abraham. 1945. “Sequential Tests of Statistical Hypotheses.” *The Annals of Mathematical Statistics* 16 (2): 117–86. https://doi.org/10.1214/aoms/1177731118.

^ref-wald1945sequential

Ross, Stéphane, Geoffrey Gordon, and J. Andrew Bagnell. 2011. “A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning.” *Proceedings of the Fourteenth International Conference on Artificial Intelligence and Statistics (AISTATS)* 15: 627–35.

^ref-ross2011reduction

## Footnotes

^footnotes

<sup>1</sup> **Shannon Information Entropy**: Entropy quantifies average uncertainty within a specified discrete distribution. Its physical meaning depends on whether that distribution is calibrated to the relevant referents and observations.

^fn1

<sup>2</sup> **Expected Calibration Error**: Binned calibration metrics quantify the divergence between neural prediction confidence and realized empirical accuracy across confidence intervals. Separable, unregularized cross-entropy training can keep increasing logit margins; whether a fitted network is overconfident must be assessed on representative held-out data. Relying on uncalibrated confidence scores to gate safety fallbacks permits undetected distribution shifts to corrupt closed-loop actuation.

^fn2

<sup>3</sup> **Inverse-Depth Parameterization**: Civera and colleagues used inverse depth to represent distant visual landmarks in monocular estimation.

^fn3

<sup>4</sup> **Recursive Log-Odds Occupancy**: The log-odds formulation maps probability values from the bounded unit interval to the unbounded real line, turning nonlinear Bayesian product updates into fast additions. Dynamic ranges are clamped by upper and lower saturation bounds to prevent saturation lockup. Failure to clamp log-odds values delays the clearing of dynamic obstacles when physical objects vacate the workspace.

^fn4

<sup>5</sup> **Diffusion Denoising Latency Budget**: Sequential reverse diffusion cannot parallelize across sampling steps because each input requires the previous step’s output. Total inference time ${t_{\text{infer}}} = {t_{\text{vis}}} + {N_{\text{eval}}} {t_{\text{pass}}}$ scales linearly with step count ${N_{\text{eval}}}$, making step reduction or asynchronous chunking essential for real-time actuation.

^fn5

<sup>6</sup> **Compounding Error in Imitation Learning**: Ross and colleagues analyzed how learner actions shift the state distribution. Expert corrective labels on learner-visited states can reduce this exposure.

^fn6

<sup>7</sup> **Signal Temporal Logic Robustness**: Quantitative semantics map a trace and formula to a signed score. Its magnitude inherits the atomic predicate’s units only when all combined predicates use commensurate units; otherwise a declared normalization gives a dimensionless score. Negative scores identify violations for falsification searches, subject to sampled-time and measurement limits.

^fn7

<sup>8</sup> **Statistical Rule of Three**: Zero events in ${n}$ independent Bernoulli trials yield the exact one-sided 95 percent upper probability $1 - 0.05^{1/{n}} \approx 3/{n}$ for small probabilities. In continuous time, a stationary Poisson process requires ${T} \ge 3.0/{\lambda}$. Neither bound covers retrained models, modified firmware, or unobserved hazard classes without configuration-equivalence proofs.

^fn8

<sup>9</sup> **Wald Sequential Probability Ratio Test**: The efficiency result assumes the specified simple hypotheses and independent, identically distributed outcomes. A sequential design can stop an unpromising test early without claiming a fixed percentage of saved robot hours.

^fn9

<sup>10</sup> **Tail Family Is an Empirical Claim**: A positive fitted GEV shape parameter (${\xi} > 0$) provides formal evidence of heavy-tailed physical risk. It does not replace physical instrumentation: block size, temporal autocorrelation, threshold selection, and parameter uncertainty must be validated against real machine rollouts.

^fn10

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/backmatter/appendix_ml.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol4/backmatter/appendix_ml.html#sec-appendix-ml). Rendering provenance is recorded in the import manifest.
