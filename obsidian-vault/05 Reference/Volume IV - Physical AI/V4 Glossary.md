---
title: V4 Glossary
type: Reference
volume: 4
chapter: 0
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol4/backmatter/glossary/glossary.qmd
source_anchor: sec-glossary
source_mode: Source-Correlated Published HTML
tags:
- Type/Reference
- Book/Volume_4
rendered_source_url: https://mlsysbook.ai/vol4/backmatter/glossary/glossary.html
---

# V4 Glossary

[[Home|Home]] · [[01 Books/Volume IV - Physical AI/Volume 4 Overview|Volume Overview]]

^sec-glossary

This glossary defines key terms used throughout *Physical AI*. Terms are organized alphabetically.

## A

^sec-glossary-vol4-a

**Action Chunking**\
A policy technique in which a model predicts a sequence of future actions rather than one action per inference. Executing part of a chunk amortizes inference latency but leaves that interval open loop with respect to new policy observations. Receding-horizon replanning or temporal ensembling can improve responsiveness and continuity; neither chunking nor blending establishes kinematic feasibility or collision clearance. (**[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/03 The Cognitive Brain/V4-03 The Cognitive Brain#^sec-brain|The Cognitive Brain]]**, **[[01 Books/Volume IV - Physical AI/03 Running the Machine/11 Trajectory Planning/V4-11 Trajectory Planning#^sec-planning|Trajectory Planning]]**, **[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06 Policy Training#^sec-training|Policy Training]]**)

**Active Probing**\
The deliberate application of a small, bounded input that makes two observationally indistinguishable states produce different observations before the response deadline, such as a controlled pull on a latch below its contact ceiling. Its cost is time and an excitation that must itself fit the operating envelope. (**[[01 Books/Volume IV - Physical AI/04 Governing the Machine/18 Engineering Physical AI/V4-18 Engineering Physical AI#^sec-frontier|Engineering Physical AI]]**)

**Administrative Lease (${T_{\text{admin}}}$)**\
The bound, inside an intent lease, on how long the application processor may hold a goal without renewing it. It caps the harm a hung or crashed host can do while its last goal stays active; it is one of the three deadlines whose earliest sets the intent lease’s expiry. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/10 Grounded Intent/V4-10 Grounded Intent#^sec-intent|Grounded Intent]]**)

**Advantage**\
The amount by which taking a particular action in a state beats the policy’s usual choice there, ${A^{\pi}}({s}, {\mathbf{a}}) = {Q^{\pi}}({s}, {\mathbf{a}}) - {V^{\pi}}({s})$. Policy-gradient and advantage-conditioned methods shift probability toward positive-advantage actions. (**[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06 Policy Training#^sec-training|Policy Training]]**)

**Approval Record**\
The record that names, for each decision behind a machine’s admitted actions, the person who approved it and answers for it, together with the human roles the design relies on, the permission stage and its reporting duties, the groups exposed to the machine, the records kept about people, and the labor the deployment moves. The release gate reads it as a standing condition, so a decision with no owner refuses operation. (**[[01 Books/Volume IV - Physical AI/04 Governing the Machine/17 Responsible Physical AI/V4-17.10 The Approval Record#^sec-responsibility-approval-record|The Approval Record]]**, **[[05 Reference/Volume IV - Physical AI/V4 Systems and Hardware#^sec-appendix-systems-wire-responsibility|Approval record]]**)

## B

^sec-glossary-vol4-b

**Back-EMF**\
Back electromotive force, the voltage ${e_{\text{bemf}}} = {K_e} {\omega_m}$ that a spinning motor induces in its own windings in opposition to the supply. In SI units ${K_e}$ equals the torque constant ${K_t}$. At speed, back-EMF can leave the inverter too little voltage headroom to control current, silently lowering the braking torque the drive can deliver. (**[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/02 The Physical Body/V4-02 The Physical Body#^sec-body|The Physical Body]]**)

**Behavioral Cloning (BC)**\
An imitation-learning method that trains a policy by supervised learning to map sensory observations directly to expert control actions, treating sequential decision-making as a regression or classification task. While computationally efficient on static demonstration archives, standard behavioral cloning ignores the closed-loop consequences of its own control outputs. Small single-step errors can therefore move the robot away from the demonstration distribution, where later errors may compound without learned recovery behavior. (**[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06 Policy Training#^sec-training|Policy Training]]**, **[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05 Physical Data#^sec-data|Physical Data]]**)

**Belief State**\
An estimate of a physical quantity carried forward from dated sensor evidence, stated in a reference frame, together with the evidence epoch of the last measurement that constrained it and a declared law for how its error bound ${E}({\Delta} {t})$ grows while no new evidence arrives. The permission path may rely on a belief only until that bound reaches the task tolerance, at its invalidation horizon. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/09 Spatial Memory/V4-09 Spatial Memory#^sec-memory|Spatial Memory]]**)

**Belief State Invalidation Horizon (${T_{\text{inv}}}$)**\
The elapsed time beyond which an unobserved spatial or kinematic state estimate can no longer be certified to lie within a task’s safe tolerance envelope. Derived from disturbance and motion bounds or a declared probabilistic uncertainty model, it limits how long perceptual memory supports the claim. A covariance-based horizon retains the confidence assumptions of that model. Downstream planners that treat spatial beliefs older than this horizon as valid free space risk commanding collisions with dynamic obstacles. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/09 Spatial Memory/V4-09 Spatial Memory#^sec-memory|Spatial Memory]]**, **[[05 Reference/Volume IV - Physical AI/V4 Control and Dynamics#^sec-appendix-control-covariance|Continuous Covariance Propagation and Observability]]**)

**Bumpless Transfer**\
A dynamic control handoff protocol that matches controller state and commanded references across control authorities to avoid abrupt changes in actuator effort. When supervisory control transitions abruptly between an autonomous neural policy and a human operator, unmatched commands can induce mechanical shocks, structural oscillations, or loss of traction. Bumpless transfer employs dynamic transition ramps and feedback state tracking to transfer command authority smoothly; effort and slew limits still require separate checks. (**[[01 Books/Volume IV - Physical AI/04 Governing the Machine/14 Supervisory Intervention/V4-14 Supervisory Intervention#^sec-intervention|Supervisory Intervention]]**, **[[05 Reference/Volume IV - Physical AI/V4 Control and Dynamics#^sec-appendix-control-splines|Smooth Trajectories and Bumpless Transfer]]**)

## C

^sec-glossary-vol4-c

**Causal Boundary**\
The interface through which a digital command produces physical forces, currents, or flows. A proposal can be rejected before it crosses; once executed, it can alter the environment and dissipate energy, and restoring a command in memory does not restore the machine’s prior physical state. Recovery requires another physical action, so a qualified permission check must precede actuation. The permission path sits above this boundary, at the proposal boundary of **[[01 Books/Volume IV - Physical AI/00 Introduction/01 The Causal Boundary/V4-01.08 The Machine in Five Levels#^sec-boundary-machine-model|The Machine in Five Levels]]**. (**[[01 Books/Volume IV - Physical AI/00 Introduction/01 The Causal Boundary/V4-01 The Causal Boundary#^sec-boundary|The Causal Boundary]]**, **[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/02 The Physical Body/V4-02 The Physical Body#^sec-body|The Physical Body]]**)

**Causal Confusion (Causal Misidentification)**\
An imitation learning failure mode where a policy conditions on spurious, non-causal features that correlate with expert actions in training demonstrations rather than the true physical affordances of the task. High-capacity neural models exploit incidental visual cues (such as interface indicators, dashboard lights, or past actions) that disappear or change under physical deployment. When deployment breaks these correlations, the policy can select inappropriate actions even if its demonstration loss was low. (**[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06 Policy Training#^sec-training|Policy Training]]**)

**Chunk Lease (${T_{\text{lease}}}$)**\
The execution lease of the autonomous chunk policy, which bounds how long an admitted chunk may keep driving the actuators before a renewal must arrive. It is chosen, then checked against the ceiling the stopping budget derives, and it enters the pre-brake delay because a stalled proposer is noticed only when its lease expires. (**[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/04 The Nervous System/V4-04 The Nervous System#^sec-nervous|The Nervous System]]**, **[[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12 Safety Enforcement#^sec-enforcement|Safety Enforcement]]**)

**Clearance Inset (${C_{\text{inset}}}$)**\
The separation a consumer holds between an estimated obstacle position and the machine’s envelope so that the true obstacle stays at least the required clearance away, except with a stated tail probability measured under the conditions of use. It rests on residuals measured against ground truth, so it includes the calibration bias and heavy tail that a reported covariance omits. A percentile inset is not a hard bound; only a justified bound on the error or a feasible stop within the remaining delay budget closes the residual tail. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/08 Sensor Perception/V4-08 Sensor Perception#^sec-perception|Sensor Perception]]**, **[[01 Books/Volume IV - Physical AI/03 Running the Machine/11 Trajectory Planning/V4-11 Trajectory Planning#^sec-planning|Trajectory Planning]]**)

**Closed-Loop Evaluation**\
Measuring a policy’s performance, safety, and stability through interactive rollouts on physical hardware or in simulation, rather than through static loss metrics on a held-out dataset. Because an autonomous policy continuously perturbs its own operating environment, evaluation requires logging closed-loop metrics such as task completion rates, safety-margin violations, and mean operating time between interventions. Open-loop validation error alone does not measure the consequences of policy-induced distribution shift. (**[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07 Closed-Loop Evaluation#^sec-evaluation|Closed-Loop Evaluation]]**, **[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06 Policy Training#^sec-training|Policy Training]]**)

**Closure Test**\
The test, declared before any data are collected, whose passing would retire an operating restriction held against an open premise in the residual-claims register, for example a failure-free trial campaign that bounds a new detector’s miss rate. Until it passes, the restriction holds. (**[[01 Books/Volume IV - Physical AI/04 Governing the Machine/18 Engineering Physical AI/V4-18 Engineering Physical AI#^sec-frontier|Engineering Physical AI]]**)

**Common-Cause Analysis**\
Tracing routing, power paths, and clock trees so that no single physical event, such as a shared cable carrier, a shared converter reference, or a common silicon erratum, can disable two paths whose failures an argument treats as independent. (**[[01 Books/Volume IV - Physical AI/04 Governing the Machine/15 Adversarial Verification/V4-15 Adversarial Verification#^sec-verification|Adversarial Verification]]**, **[[01 Books/Volume IV - Physical AI/03 Running the Machine/13 Workload Placement/V4-13 Workload Placement#^sec-placement|Workload Placement]]**)

**Compounding Rollout Error**\
The accumulation of task error when a policy’s actions move it into states poorly represented in expert demonstrations. Under standard finite-horizon imitation-learning assumptions, a per-step expert-distribution error rate ${\epsilon}$ can yield worst-case excess accumulated task cost of order ${\mathcal{O}(S^2 \epsilon)}$ over horizon ${S}$. This is not a universal law for physical displacement, tracking error, or collision probability. (**[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06 Policy Training#^sec-training|Policy Training]]**, **[[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^sec-appendix-ml-compounding|Imitation Learning and Compounding Covariate Shift]]**)

**Configuration Space**\
The set of all configurations of a mechanism; for a manipulator, a configuration is the collection of joint positions $({q}_1, \dots, {q}_n)$. Removing the configurations occupied by obstacles leaves the free space ${\mathcal{C}_{\text{free}}}$. A path through configuration space still lacks timing, which an executable trajectory adds. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/11 Trajectory Planning/V4-11 Trajectory Planning#^sec-planning|Trajectory Planning]]**)

**Conformal Prediction Set**\
The set of candidate answers that a calibrated threshold cannot exclude. Calibrating the threshold on held-out labeled cases gives the set a chosen marginal coverage level across cases, provided new cases are exchangeable with the calibration set. A set with more than one member is a principled trigger for asking a person rather than guessing. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/10 Grounded Intent/V4-10 Grounded Intent#^sec-intent|Grounded Intent]]**)

**Control Barrier Function (CBF)**\
A scalar function ${h}({\mathbf{x}})$ of the plant state whose nonnegative region is the safe set ${\mathcal{C}}$ and whose rate of change the control input can influence, so that admitting only inputs with ${\dot{h}} \ge -{\kappa}({h})$, for an extended class-${\mathcal{K}}$ rate function ${\kappa}$ that vanishes at zero, keeps a state that starts in ${\mathcal{C}}$ inside it (forward invariance) while the model, actuator, and timing assumptions hold. A Lyapunov function certifies convergence toward a point; a barrier function certifies that the state never leaves a region. For a torque-controlled plant, ${h}$ must carry speed and braking authority, because raw distance has relative degree two and gives the input no direct control authority at the boundary. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12 Safety Enforcement#^sec-enforcement|Safety Enforcement]]**, **[[05 Reference/Volume IV - Physical AI/V4 Control and Dynamics#^sec-appendix-control-cbf|Safety and Control Barrier Functions]]**)

**Credible Deceleration (${a_{\text{brake}}}$)**\
The sustained deceleration a machine can actually exert against its environment under stated conditions, a validated low tail rather than a datasheet peak. Traction, tip-over, and the drives’ current-limited torque each bound it, so it changes with payload, floor friction, and arm pose. (**[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/02 The Physical Body/V4-02 The Physical Body#^sec-body|The Physical Body]]**, **[[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12 Safety Enforcement#^sec-enforcement|Safety Enforcement]]**)

**Cross-Embodiment Transfer**\
A learning paradigm in which a single policy or foundation model is trained on sensorimotor data gathered across heterogeneous robot morphologies, kinematic chains, and actuator dynamics to generalize to novel target embodiments. Achieving cross-embodiment generalization requires accounting for differences in observations, action semantics, and body dynamics, for example through shared representations or embodiment-specific adapters. Its primary challenge is preventing negative transfer induced by unmodeled dynamic discrepancies, link inertia variations, and differing joint velocity boundaries. (**[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05 Physical Data#^sec-data|Physical Data]]**, **[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06 Policy Training#^sec-training|Policy Training]]**)

## D

^sec-glossary-vol4-d

**Defeater**\
A physically realizable condition that invalidates a warrant in a safety-case argument, as an oil film can defeat the braking traction a stopping claim assumes. Adversarial review is the systematic search for defeaters. (**[[01 Books/Volume IV - Physical AI/04 Governing the Machine/16 Deployment Release/V4-16 Deployment Release#^sec-release|Deployment Release]]**)

**Diffusion Policy**\
A generative policy that produces continuous action sequences by iteratively denoising a noisy candidate conditioned on observations. It can represent multiple demonstration modes without forcing their average, but generated chunks still require feasibility and clearance checks. The number and cost of denoising steps contribute to inference latency. (**[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06 Policy Training#^sec-training|Policy Training]]**, **[[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^sec-appendix-ml-diffusion|Continuous trajectory diffusion and flow matching]]**)

**Domain Randomization (DR)**\
A sim-to-real transfer methodology that systematically perturbs physical parameters (mass, friction, damping, motor torque limits), sensor characteristics (noise covariance, latency, camera pose), and visual textures across simulated training episodes. By exposing the policy to a broad distribution of simulated environments, domain randomization encourages the neural network to learn invariant representations and feedback behaviors robust to the chosen variation; transfer still depends on whether that variation covers the relevant physical conditions. If randomized too narrowly, the real world falls outside the training hull; if randomized too broadly, learning can become harder or the resulting behavior overly conservative. (**[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06 Policy Training#^sec-training|Policy Training]]**)

**Dynamic Reachability**\
The property that the end effector can move from its measured state to a target pose, within its velocity, acceleration, jerk, and thermal limits, before the evidence supporting that target expires. Static reachability asks only whether some joint configuration reaches the pose; dynamic reachability adds the clock, so a target well inside the workspace can still be unreachable on one capture. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/10 Grounded Intent/V4-10 Grounded Intent#^sec-intent|Grounded Intent]]**)

**Dynamic Stopping Distance (${d_{\text{stop}}}$)**\
The clearance needed to stop from the current state, including pre-brake delay, the selected braking trajectory, and localization and protective allowances. With constant speed ${v}$ during delay and constant braking deceleration ${a_{\text{brake}}}>0$, the model is ${d_{\text{stop}}}={v}{\tau_{\text{delay}}}+{v}^2/(2{a_{\text{brake}}})+{\delta_{\text{loc}}}+{\delta_{\text{margin}}}$. A ramped or jerk-limited stop requires its own profile integral; the permission path must reserve that distance together with the tracking inset and any remaining timing margin. (**[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/02 The Physical Body/V4-02 The Physical Body#^sec-body|The Physical Body]]**, **[[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12 Safety Enforcement#^sec-enforcement|Safety Enforcement]]**)

## E

^sec-glossary-vol4-e

**End-Effector**\
The tool, gripper, or hand at the distal tip of a manipulator that performs the intended interaction with the workpiece. Workspace and keep-out checks are written against its pose rather than against joint angles. (**[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/03 The Cognitive Brain/V4-03 The Cognitive Brain#^sec-brain|The Cognitive Brain]]**)

**Endogenous Covariate Shift**\
A distribution shift in sequential decision-making where an embodied agent’s own execution errors drive its physical body into states unrepresented in its training demonstrations, thereby presenting the policy with novel out-of-distribution observations. An offline action-loss objective does not itself constrain the states visited by the deployed policy, so errors can compound along the trajectory. In physical systems, this shift can cause task failure or boundary violations; corrective data and feedback can improve recovery but require evaluation in the affected states. (**[[01 Books/Volume IV - Physical AI/00 Introduction/01 The Causal Boundary/V4-01 The Causal Boundary#^sec-boundary|The Causal Boundary]]**, **[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05 Physical Data#^sec-data|Physical Data]]**, **[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06 Policy Training#^sec-training|Policy Training]]**)

**Endogenous Experience (The Action–Observation Loop)**\
The closed-loop data generation process in which an agent’s executed actions causally determine its subsequent physical states and sensory observations (${s}_{t+1} \sim {p}({s} \mid {s}_t, {\mathbf{a}}_{t})$). Unlike passive supervised learning on fixed, exogenous datasets, physical AI experience generation forms an irreversible dynamical feedback loop where minor control perturbations alter future data collection trajectories. Consequently, data generation and policy deployment cannot be separated in embodied agents. (**[[01 Books/Volume IV - Physical AI/00 Introduction/01 The Causal Boundary/V4-01 The Causal Boundary#^sec-boundary|The Causal Boundary]]**, **[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05 Physical Data#^sec-data|Physical Data]]**)

**Envelope Trichotomy**\
A three-valued epistemic classification of cyber-physical runtime health that partitions system status relative to its certified operating envelope into *known-true* (verified valid telemetry inside bounds), *known-false* (verified limit breach), and *unknown* (epistemic uncertainty from sensor corruption, frame drops, or estimator divergence). In embodied AI, both *known-false* and *unknown* withhold tracking permission and select the qualified fallback for the current state and surviving hardware. (**[[01 Books/Volume IV - Physical AI/04 Governing the Machine/16 Deployment Release/V4-16 Deployment Release#^sec-release|Deployment Release]]**)

**Evidence Epoch (${t_0}$)**\
The physical time reference of the measurement that last constrained an estimate, such as a camera’s exposure midpoint or the instant a hardware register latches an encoder count. Republishing or predicting a belief advances its publication and estimate epochs, but only a new measurement advances its evidence epoch. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/09 Spatial Memory/V4-09 Spatial Memory#^sec-memory|Spatial Memory]]**, **[[01 Books/Volume IV - Physical AI/03 Running the Machine/08 Sensor Perception/V4-08 Sensor Perception#^sec-perception|Sensor Perception]]**)

**Evidence Horizon**\
The longest time the evidence behind a proposal keeps its target within tolerance. For a tracked target whose residual motion can accelerate at ${a_{\text{slip}}}$, it follows from setting the open-loop drift $\tfrac{1}{2}{a_{\text{slip}}} {\Delta} {t}^2$ equal to the margin ${r_{\text{tol}}} - {e_0}$. It is one of the three deadlines whose earliest sets an intent lease’s expiry. (**[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/03 The Cognitive Brain/V4-03 The Cognitive Brain#^sec-brain|The Cognitive Brain]]**, **[[01 Books/Volume IV - Physical AI/03 Running the Machine/10 Grounded Intent/V4-10 Grounded Intent#^sec-intent|Grounded Intent]]**)

**Execution Lease**\
Authority an admitted command source holds to keep driving the actuators without renewal. It begins at admission, not at dispatch, and its expiry invokes the state-matched fallback rather than the next proposal. The chunk lease and the manual lease are its two instances on the running machine. (**[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/04 The Nervous System/V4-04 The Nervous System#^sec-nervous|The Nervous System]]**, **[[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12 Safety Enforcement#^sec-enforcement|Safety Enforcement]]**, **[[01 Books/Volume IV - Physical AI/04 Governing the Machine/14 Supervisory Intervention/V4-14 Supervisory Intervention#^sec-intervention|Supervisory Intervention]]**)

**Exposure Wall**\
The limit on what failure-free operation alone can establish about a rare failure rate. Under a stationary Poisson failure model, bounding a catastrophic rate ${\lambda} = 10^{-9}$ per hour at 95 percent confidence requires about $-\ln(0.05)/{\lambda} \approx 3.0 \times 10^9$ failure-free hours of exposure from the same configuration, an argument Butler and Finelli made for flight software. The required exposure makes direct demonstration impractical, so claims at that level also need architectural evidence, fault injection, and justified operating premises. (**[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07.10 Verification Ceilings and the Exposure Wall#^sec-evaluation-limits|Verification Ceilings and the Exposure Wall]]**, **[[01 Books/Volume IV - Physical AI/04 Governing the Machine/15 Adversarial Verification/V4-15 Adversarial Verification#^sec-verification|Adversarial Verification]]**, **[[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^sec-appendix-ml-exposure|Zero-Failure Testing and the Exposure Wall]]**)

**Extended Kalman Filter (EKF)**\
A recursive state estimator for nonlinear measurement or motion models that runs the Kalman filter’s predict and update steps on a first-order linearization about the current estimate. When the model curves appreciably across the prior’s spread, the reported covariance can understate the true error, so the filter’s consistency must be tested rather than assumed. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/09 Spatial Memory/V4-09 Spatial Memory#^sec-memory|Spatial Memory]]**)

**Extreme Value Theory (EVT)**\
The statistical theory that supplies limiting distribution families for extremes, much as the central limit theorem supplies one for sums. Its threshold form models every observation above a high threshold with the generalized Pareto distribution; its block-maxima form models one maximum per block with the generalized extreme value distribution. (**[[01 Books/Volume IV - Physical AI/04 Governing the Machine/15 Adversarial Verification/V4-15 Adversarial Verification#^sec-verification|Adversarial Verification]]**, **[[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^sec-appendix-ml-evt|Extreme Value Theory and Tail Risk]]**)

## F

^sec-glossary-vol4-f

**Fallback Ladder**\
The ordered set of responses the permission path selects when a proposal cannot be admitted unchanged or its premises fail. Its rungs are PROJECT (minimal-intervention projection of the proposal onto the safe set), HOLD (a state-matched powered hold), STOP (a controlled, state-matched stop), and INHIBIT (drive torque inhibit with a separately rated brake). Each response requires a validated entry region and surviving hardware; selection must occur while that response remains feasible. An invalid replacement need not revoke an active trajectory whose own premises still hold. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12.10 The Fallback Ladder#^sec-enforcement-fallback-ladder|The Fallback Ladder]]**, **[[01 Books/Volume IV - Physical AI/04 Governing the Machine/14 Supervisory Intervention/V4-14 Supervisory Intervention#^sec-intervention|Supervisory Intervention]]**)

**Flow Matching Policy**\
A generative policy trained to predict a vector field that transports samples from a base distribution toward a conditional action distribution. The training probability path and sample coupling determine the transport construction; straight conditional paths do not imply globally optimal transport or straight learned sample trajectories. Sampling cost depends on the trained field, numerical solver, and required accuracy, so fewer inference steps than diffusion must be demonstrated for the selected policies. (**[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06 Policy Training#^sec-training|Policy Training]]**)

**Force Closure**\
A grasp property: every external force and torque on the held object can be balanced by contact forces that each lie inside its friction cone. Force closure says a balancing set of forces exists, not that the gripper can produce it within its force limit or without crushing the object. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/10 Grounded Intent/V4-10 Grounded Intent#^sec-intent|Grounded Intent]]**, **[[05 Reference/Volume IV - Physical AI/V4 Control and Dynamics#^sec-appendix-control-grasp|Grasp mechanics: Friction cones and force closure]]**)

**Forward Invariance**\
A property of a dynamical system, control policy, and set ${\mathcal{C}}$: every trajectory starting in ${\mathcal{C}}$ remains in ${\mathcal{C}}$ for all future time under the stated assumptions. A barrier certificate can establish this property for a modeled system with feasible controls. Applying the result to hardware requires maintaining the state, disturbance, actuation, and timing premises of the certificate. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12 Safety Enforcement#^sec-enforcement|Safety Enforcement]]**, **[[05 Reference/Volume IV - Physical AI/V4 Control and Dynamics#^sec-appendix-control-cbf|Safety and Control Barrier Functions]]**)

**Forward Occupancy Set**\
The region a tracked actor could occupy a given time after its last measurement, grown from its measured position by its speed bound and its tracking uncertainty. A proposed motion is admitted only if it stays clear of every such set over the motion and its stop. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/10 Grounded Intent/V4-10 Grounded Intent#^sec-intent|Grounded Intent]]**)

**Four-Stream Action Tap**\
The tuple $({a_{\text{req}}}, {a_{\text{cmd}}}, {a_{\text{enf}}}, {a_{\text{meas}}})$ that records one action at each of its four causal stages, the requested action, the mapped command, the enforced command, and the measured response. Keeping all four makes any single choice of training label interpretable, provided the taps are stamped in one hardware-synchronized timebase. (**[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05 Physical Data#^sec-data|Physical Data]]**)

**Free-Space Depth (${d_{\text{free}}}$)**\
The distance from a hull’s surface to the nearest place that no live evidence vouches for, read from a distance field built with every occupied, unknown, or expired cell treated as an obstacle. It is the clearance a map can certify for motion. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/09 Spatial Memory/V4-09 Spatial Memory#^sec-memory|Spatial Memory]]**)

**Freshness Deadline (${\Delta t_{\text{fresh}}}$)**\
The largest age, counted from the capture of a measurement to the onset of the actuator’s response, that a measurement of a moving target may reach before the target’s motion alone spends the allowable position error. It equals the error tolerance divided by the fastest credible velocity of the tracked state, and every stage from exposure to torque onset shares it. (**[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/02 The Physical Body/V4-02 The Physical Body#^sec-body|The Physical Body]]**)

**Friction Cone**\
The set of forces a Coulomb contact can transmit, $\|{\mathbf{f}_{k, \parallel}}\| \le {\mu} {f_{k, \perp}}$, a cone about the contact normal with half-angle $\arctan {\mu}$. A nonadhesive contact can push but not pull, so a gripper holds an object only through forces inside its friction cones. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/10 Grounded Intent/V4-10 Grounded Intent#^sec-intent|Grounded Intent]]**, **[[05 Reference/Volume IV - Physical AI/V4 Control and Dynamics#^sec-appendix-control-grasp|Grasp mechanics: Friction cones and force closure]]**)

**Future-State Conditioning**\
Generating candidate motion plans from the state anticipated at execution time rather than the stale state measured when planning began, which removes the reference jump at trajectory handoff that planning latency would otherwise create. Activation still depends on the permission path checking the seam against the current state estimate and its error bound. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/11 Trajectory Planning/V4-11 Trajectory Planning#^sec-planning|Trajectory Planning]]**)

## G

^sec-glossary-vol4-g

**Generalist Policy**\
A robot policy pretrained on pooled demonstrations from many robots and tasks, then post-trained on demonstrations of the target task. Pretraining supplies broad visual and motor priors; post-training supplies the task, the embodiment, and the evidence the target deployment needs. (**[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06 Policy Training#^sec-training|Policy Training]]**)

**Grounded Affordance**\
An affordance expressed in the robot’s own frame and units, namely a feature pose in the base frame, an approach direction, an aperture, and a contact wrench ceiling, each tied to dated sensor evidence through a calibrated measurement chain. Unlike a detector box or a language label, it says where and how the gripper may make contact. A learned grasp score or a confident detection is not grounding, because neither carries a metric error bound, a wrench limit, or an evidence epoch that the permission path could admit or expire. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/10 Grounded Intent/V4-10 Grounded Intent#^sec-intent|Grounded Intent]]**, **[[01 Books/Volume IV - Physical AI/03 Running the Machine/08 Sensor Perception/V4-08 Sensor Perception#^sec-perception|Sensor Perception]]**)

## H

^sec-glossary-vol4-h

**Hardware Lease**\
A countdown timer on the safety microcontroller that enforces a lease’s expiry without the cooperation of the process that issued the authority. It is the mechanism behind every other lease, since a hung host cannot extend authority that a hardware timer is counting down. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/10 Grounded Intent/V4-10 Grounded Intent#^sec-intent|Grounded Intent]]**, **[[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12 Safety Enforcement#^sec-enforcement|Safety Enforcement]]**)

**Heterogeneous Silicon Partitioning**\
Allocation of learned workloads and time-critical permission or control loops to different compute resources, with hardware protection of memory and peripheral access. Separate processors and dedicated buses can remove specific interference and fault paths, but shared power, clocks, interconnects, or thermal limits can retain common-mode failures. Timing and fault-containment claims therefore require evidence for the actual partition and declared load and fault envelope. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/13 Workload Placement/V4-13 Workload Placement#^sec-placement|Workload Placement]]**, **[[05 Reference/Volume IV - Physical AI/V4 Systems and Hardware#^sec-appendix-systems-ipc|Heterogeneous SoC Mailboxes, Memory Barriers, and Zero-Copy IPC]]**)

**Human-Gated Aggregation**\
An interactive imitation-learning scheme in which the expert decides when to take over and only the takeover segments enter the dataset as labels. It avoids training on the learner’s own failing commands. (**[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05 Physical Data#^sec-data|Physical Data]]**)

**Human Oversight Role**\
A duty that a design assigns to a person, such as stopping the machine, taking over a channel, or approving a motion, and that the safety argument relies on. It counts as a countermeasure only if its holder has the time, the information, and the authority to act within the time the hazard leaves; a remote assistant who serves many machines must also be free when a request arrives. (**[[01 Books/Volume IV - Physical AI/04 Governing the Machine/17 Responsible Physical AI/V4-17.04 Oversight a Person Can Perform#^sec-responsibility-meaningful-oversight|Oversight a Person Can Perform]]**)

## I

^sec-glossary-vol4-i

**Importance Sampling**\
A Monte Carlo method that draws test runs from a proposal distribution that visits the failure region often, then weights each run by the ratio of the operational to the proposal likelihood to remove the bias. It estimates rare failure rates with far fewer runs than plain sampling, but only for the declared operational distribution. (**[[01 Books/Volume IV - Physical AI/04 Governing the Machine/15 Adversarial Verification/V4-15 Adversarial Verification#^sec-verification|Adversarial Verification]]**)

**Inevitable Collision State (ICS)**\
A physical system state ${\mathbf{x}}({t})$ from which no admissible, physically executable control trajectory within actuator and friction limits can prevent impact with environmental obstacles over an infinite time horizon. Unlike geometric obstacle clearance, an ICS explicitly accounts for plant momentum, friction limits, dynamic obstacle trajectories, and finite actuator braking authority. A machine can enter an ICS before contact; insufficient stopping distance establishes this only when no other admissible evasive trajectory avoids impact. (**[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/02 The Physical Body/V4-02 The Physical Body#^sec-body|The Physical Body]]**, **[[01 Books/Volume IV - Physical AI/03 Running the Machine/11 Trajectory Planning/V4-11 Trajectory Planning#^sec-planning|Trajectory Planning]]**, **[[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12 Safety Enforcement#^sec-enforcement|Safety Enforcement]]**)

**Innovation**\
The difference between a measurement and the estimator’s prediction of it, which is what the measurement says that the prediction did not. A zero innovation confirms an estimate only along directions the sensors can observe. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/09 Spatial Memory/V4-09 Spatial Memory#^sec-memory|Spatial Memory]]**)

**Intent Grounding Refusal**\
A typed rejection of a goal itself, returned when the referent is unresolved or no candidate grasp survives the physical checks a learned generator did not perform, such as an inverse-kinematics solution inside joint limits, jaw aperture, and a collision-free approach corridor. Unlike a planning failure, which finds no collision-free path to a valid goal, it rejects the goal before the planner is invoked, so no best guess over unresolved referents reaches trajectory generation. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/10 Grounded Intent/V4-10 Grounded Intent#^sec-intent|Grounded Intent]]**, **[[01 Books/Volume IV - Physical AI/04 Governing the Machine/14 Supervisory Intervention/V4-14 Supervisory Intervention#^sec-intervention|Supervisory Intervention]]**)

**Intent Lease**\
The record, eighth in the record chain, that turns a grounded human goal into a bounded, expiring request that grants a target, a tolerance, and effort ceilings, but never a path. It expires at the earliest of its evidence horizon, its administrative lease, and its stopping deadline, and expiry withdraws the authority based on that intent and requires re-grounding or a qualified state-matched fallback. Unlike an execution lease, it bounds which trajectories may be admitted, not how long an admitted command may run. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/10 Grounded Intent/V4-10 Grounded Intent#^sec-intent|Grounded Intent]]**, **[[01 Books/Volume IV - Physical AI/03 Running the Machine/11 Trajectory Planning/V4-11 Trajectory Planning#^sec-planning|Trajectory Planning]]**)

**Intervention Masking**\
An evaluation distortion in which repeated, proactive interventions by human supervisors intercept a policy before it reaches a boundary failure. Because the supervisor intervenes during nascent drift, assisted success and accident counts alone do not reveal how the unaided policy would have behaved after takeover. Logs must distinguish intervention classes, exposure, and task outcomes. Reporting these separately prevents assisted task completion from being mistaken for evidence of independent policy competence. (**[[01 Books/Volume IV - Physical AI/04 Governing the Machine/14 Supervisory Intervention/V4-14 Supervisory Intervention#^sec-intervention|Supervisory Intervention]]**, **[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07 Closed-Loop Evaluation#^sec-evaluation|Closed-Loop Evaluation]]**)

**Intervention Rate**\
The number of events in a declared intervention class divided by active operating time, or by distance when a distance-based rate is reported. The rate depends on the intervention policy and exposure population; human takeovers and automatic corrections must remain distinguishable. It does not by itself establish safety or stability. (**[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07 Closed-Loop Evaluation#^sec-evaluation|Closed-Loop Evaluation]]**, **[[01 Books/Volume IV - Physical AI/04 Governing the Machine/14 Supervisory Intervention/V4-14 Supervisory Intervention#^sec-intervention|Supervisory Intervention]]**)

## J

^sec-glossary-vol4-j

**Jerk**\
The rate of change of acceleration, ${j} = {\dot{a}} = \dddot{{x}}$, in m/s³. A jerk limit makes a brake ramp its deceleration up instead of stepping it, which spares occupants, payloads, and transmissions a shock but lengthens the stop, because full deceleration arrives later. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/11 Trajectory Planning/V4-11 Trajectory Planning#^sec-planning|Trajectory Planning]]**, **[[01 Books/Volume IV - Physical AI/00 Introduction/01 The Causal Boundary/V4-01 The Causal Boundary#^sec-boundary|The Causal Boundary]]**, **[[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12 Safety Enforcement#^sec-enforcement|Safety Enforcement]]**)

## K

^sec-glossary-vol4-k

**Kinodynamic Feasibility**\
The property that the machine can track a candidate trajectory, including its seams and its stop, while every joint stays within its position, velocity, acceleration, jerk, torque, and current limits; the kinodynamic feasibility envelope is the set of initial states from which this holds. Collision freedom is necessary but not sufficient, and checking only discrete waypoints can miss an interpolant that overshoots a limit between samples. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/11 Trajectory Planning/V4-11 Trajectory Planning#^sec-planning|Trajectory Planning]]**, **[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/02 The Physical Body/V4-02 The Physical Body#^sec-body|The Physical Body]]**)

## L

^sec-glossary-vol4-l

**Learner-Action Contamination**\
A data-collection failure in which the failing policy’s own commands enter the dataset as expert labels, so the retrained policy learns to answer the cues of an approaching hazard with the commands that caused it. (**[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05 Physical Data#^sec-data|Physical Data]]**)

**Legible Intent**\
Motion and signals that let a person who does not know a machine’s goal infer it early enough to get out of the way, as opposed to motion that is predictable only to someone who already knows the plan. It helps the people a machine puts at risk protect themselves, and signals should promise only what measured detection supports. (**[[01 Books/Volume IV - Physical AI/04 Governing the Machine/17 Responsible Physical AI/V4-17.07 Who Bears the Risk#^sec-responsibility-legible-intent|Legible intent]]**)

## M

^sec-glossary-vol4-m

**Manual Lease (${T_{\text{lease,man}}}$)**\
The execution lease of a human operator in manual mode, renewed by authenticated heartbeats. It replaces the chunk lease in the pre-brake delay while the operator drives, so it must fit the stopping reserve of the mode in which it is granted. (**[[01 Books/Volume IV - Physical AI/04 Governing the Machine/14 Supervisory Intervention/V4-14 Supervisory Intervention#^sec-intervention|Supervisory Intervention]]**)

**Mean Time Between Interventions (MTBI)**\
Active operating time divided by the number of events in a declared intervention class. MTBI is the reciprocal of the time-based intervention rate when the count is nonzero; a zero-event run requires an exposure-based statistical bound rather than a claim of infinite reliability. Interrupted trials and the intervention policy affect interpretation, so MTBI alone does not establish safety or stability. (**[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07 Closed-Loop Evaluation#^sec-evaluation|Closed-Loop Evaluation]]**, **[[01 Books/Volume IV - Physical AI/04 Governing the Machine/14 Supervisory Intervention/V4-14 Supervisory Intervention#^sec-intervention|Supervisory Intervention]]**)

**Memory Wall**\
The limit on a workload’s rate that arises when its operands cannot reach the arithmetic units as fast as those units could consume them, so that the bytes moved from off-chip memory, not the operations performed, set the time per evaluation. Faster arithmetic does not move it; only fewer bytes per evaluation (fewer or narrower weights, or weights resident on chip) or more bandwidth does. It is distinct from memory capacity, since a model can fit in memory and still be too slow to stream. (**[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/03 The Cognitive Brain/V4-03 The Cognitive Brain#^sec-brain|The Cognitive Brain]]**)

**Metric 3D Lifting (Spatial Grounding)**\
The construction of a three-dimensional scene representation in physical units and a declared coordinate frame from sensor observations. Metric scale requires calibrated geometry, depth measurements, or another validated scale reference; image features and reconstruction methods alone do not resolve monocular scale ambiguity. The representation supports reachability and collision checks only within its uncertainty, coverage, and information-age bounds. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/08 Sensor Perception/V4-08 Sensor Perception#^sec-perception|Sensor Perception]]**, **[[01 Books/Volume IV - Physical AI/03 Running the Machine/10 Grounded Intent/V4-10 Grounded Intent#^sec-intent|Grounded Intent]]**)

**Minimal Risk Maneuver (MRM)**\
A fallback maneuver intended to reduce risk after a fault or loss of nominal authority, such as a controlled stop or transition to a supported resting configuration. Its feasibility depends on the current state, available clearance, and surviving sensing, actuation, and power. The designation does not guarantee a hazard-free outcome or require every machine to reach an immediate standstill. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12 Safety Enforcement#^sec-enforcement|Safety Enforcement]]**, **[[01 Books/Volume IV - Physical AI/04 Governing the Machine/14 Supervisory Intervention/V4-14 Supervisory Intervention#^sec-intervention|Supervisory Intervention]]**)

**Minimal-Intervention Safety Shield**\
A safety filter that modifies a nominal control proposal only as needed to satisfy modeled safety and actuator constraints. The CBF-QP safety filter solves ${\mathbf{u}^*}=\arg\min_{{\mathbf{u}}}\|{\mathbf{u}}-{\mathbf{u}_{\text{nom}}}\|^2$ subject to barrier and input constraints, potentially acting before the safe-set boundary is reached. Its guarantee depends on feasibility, model and state bounds, and execution timing; minimizing input deviation neither maximizes task performance nor supplies a fallback when the feasible set is empty. Its effect on the system hazard rate is conditional on the proposal rate and its interception coverage, so a shield does not remove the need to bound the proposer’s failure rate. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12 Safety Enforcement#^sec-enforcement|Safety Enforcement]]**, **[[01 Books/Volume IV - Physical AI/04 Governing the Machine/18 Engineering Physical AI/V4-18 Engineering Physical AI#^sec-frontier|Engineering Physical AI]]**, **[[05 Reference/Volume IV - Physical AI/V4 Control and Dynamics#^sec-appendix-control-cbf|Safety and Control Barrier Functions]]**)

**Missing Observable**\
The unmeasured physical quantity on which an open claim depends, such as a friction coefficient or a latch strength, stated in terms of the physical claim rather than as an out-of-distribution latent state. Naming it lets a team choose between adding sensing, establishing a physical bound, and restricting the task. (**[[01 Books/Volume IV - Physical AI/04 Governing the Machine/18 Engineering Physical AI/V4-18 Engineering Physical AI#^sec-frontier|Engineering Physical AI]]**)

**Mode Averaging (Multimodality Catastrophe)**\
A learning failure in which a regression policy averages distinct valid action modes into an unsuitable action, potentially causing a physical hazard. Mean squared error favors the conditional mean, which can lie between valid pathways. When human demonstrators navigate around an obstacle by choosing either a left or right detour, a naive regression model averages the competing action modes, commanding an interpolation that steers the robot directly into the obstacle. Mixture models, discrete strategy choices, or generative decoders can represent distinct modes; their selected actions still require physical feasibility checks. (**[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06 Policy Training#^sec-training|Policy Training]]**, **[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/03 The Cognitive Brain/V4-03 The Cognitive Brain#^sec-brain|The Cognitive Brain]]**)

**Mode Confusion**\
A mismatch between the mode an operator believes the automation is in and the mode it is actually in, so that an action correct for the believed mode is wrong for the actual one. On a machine whose actuator channels change hands separately, the operator’s belief about one channel can be stale while the operator acts on another. Committed channel masks and per-channel announcement address it; correct ownership at the bus does not. (**[[01 Books/Volume IV - Physical AI/04 Governing the Machine/14 Supervisory Intervention/V4-14 Supervisory Intervention#^sec-intervention|Supervisory Intervention]]**)

**Monitored Premise Expiration**\
The withdrawal of operational authority when runtime monitoring finds a required safety-case premise false or unknown, for example because measured temperature exceeds a limit or sensor packets are missing. Linking runtime telemetry to safety case warrants makes detectable premise failures grounds for restricting authority; unmonitored premises still require independent evidence. When a monitored premise expires, the system transitions autonomously into a restricted or refusal operational regime. (**[[01 Books/Volume IV - Physical AI/04 Governing the Machine/16 Deployment Release/V4-16 Deployment Release#^sec-release|Deployment Release]]**)

## O

^sec-glossary-vol4-o

**Observability**\
The property that the history of a machine’s sensor outputs over a finite window, together with its known inputs and dynamics, determines the state uniquely, so that distinct physical trajectories produce distinct measurement sequences. Along an unobservable direction the innovation stays zero whatever the error, so a contracting covariance there reflects the model’s assumptions rather than evidence. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/09 Spatial Memory/V4-09 Spatial Memory#^sec-memory|Spatial Memory]]**, **[[05 Reference/Volume IV - Physical AI/V4 Control and Dynamics#^sec-appendix-control-covariance|Continuous Covariance Propagation and Observability]]**)

**Observation Contract**\
A specification of the spatial, temporal, and semantic claims a perception subsystem supplies downstream, including coordinate frames, capture times, coverage, uncertainty, and validity flags. It distinguishes deterministic bounds from statistical confidence regions and names how detectable violations revoke a claim. A contract cannot make occluded or unmonitored conditions observable; unsupported claims must remain unknown. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/08 Sensor Perception/V4-08 Sensor Perception#^sec-perception|Sensor Perception]]**, **[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/03 The Cognitive Brain/V4-03 The Cognitive Brain#^sec-brain|The Cognitive Brain]]**)

**Observational Indistinguishability**\
The condition in which two physical states that require different responses produce the same observation history, under every input the machine may admissibly apply, until the deadline by which a state-specific response must begin. Unlike classical unobservability, it is tied to a deadline and to the admissible inputs. A more capable classifier on the same channel cannot separate the states; only a new channel, active probing, or a response valid in both states changes the outcome. (**[[01 Books/Volume IV - Physical AI/04 Governing the Machine/18 Engineering Physical AI/V4-18 Engineering Physical AI#^sec-frontier|Engineering Physical AI]]**)

**Operating Envelope**\
The declared set of external conditions and internal execution states, each stated with its units and tolerances, over which a machine’s protective claim must hold and at which every trial of that claim is run. It extends the operational design domain with the machine’s own state, such as processor load, drive bus voltage, and bus traffic. Values that are each in range can combine into a point outside the envelope, so its coupled corners must be tested. (**[[01 Books/Volume IV - Physical AI/04 Governing the Machine/15 Adversarial Verification/V4-15 Adversarial Verification#^sec-verification|Adversarial Verification]]**, **[[01 Books/Volume IV - Physical AI/04 Governing the Machine/16 Deployment Release/V4-16 Deployment Release#^sec-release|Deployment Release]]**)

**Operational Design Domain (ODD)**\
The object poses, surface conditions, payloads, speeds, and disturbances in which a machine is meant to operate, written down as the scenario table. A dataset supports the part of the ODD that its occupancy join covers; the rest is its known absence. The sets nest: the policy manifest claims a declared ODD within the ODD, evaluation samples a target ODD within the declared ODD, and verification extends the target ODD to the machine’s internal conditions as the operating envelope that a release verdict authorizes in whole, in part, or not at all. (**[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05.08 Collection Policy Coverage#^sec-data-policy-coverage|Collection Policy Coverage]]**, **[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06 Policy Training#^sec-training|Policy Training]]**, **[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07 Closed-Loop Evaluation#^sec-evaluation|Closed-Loop Evaluation]]**, **[[01 Books/Volume IV - Physical AI/04 Governing the Machine/15 Adversarial Verification/V4-15 Adversarial Verification#^sec-verification|Adversarial Verification]]**, **[[01 Books/Volume IV - Physical AI/04 Governing the Machine/16 Deployment Release/V4-16 Deployment Release#^sec-release|Deployment Release]]**)

**Operational Independence**\
The property that no activity, fault, or overload in the proposal domain can push the permission path’s execution past its deadline or disable its authority to refuse, through any resource the two share. Unlike spatial isolation, it also covers time, supply, clock, reset, and heat; it is the placement-level form of what functional-safety standards call freedom from interference. A separate core or chip is not independent by construction, since each shared resource is a hypothesis that needs a bound. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/13 Workload Placement/V4-13 Workload Placement#^sec-placement|Workload Placement]]**)

**Moral Crumple Zone**\
The position of a person who absorbs blame for an outcome that a system’s design controlled, typically the operator nearest the event, named by analogy with the crumple zone of a car. A human role without the time, information, or authority to act creates one. (**[[01 Books/Volume IV - Physical AI/04 Governing the Machine/17 Responsible Physical AI/V4-17.04 Oversight a Person Can Perform#^sec-responsibility-meaningful-oversight|Oversight a Person Can Perform]]**)

## P

^sec-glossary-vol4-p

**Paired Probing**\
Validating a simulator component by applying identical open-loop command sequences to the simulator and to the physical hardware, then measuring the difference between the resulting state trajectories against explicit error budgets. A difference beyond the tolerance for the operating envelope makes the simulator defective for that training task. (**[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06 Policy Training#^sec-training|Policy Training]]**)

**Performance Level (PL)**\
The ISO 13849-1 grade, a (lowest) to e (highest), of how reliably a safety-related control function performs, based on its architecture, diagnostic coverage, and component failure rates. Standards for the application set the required level; person detection on a driverless industrial truck, for example, requires PL d. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/08 Sensor Perception/V4-08 Sensor Perception#^sec-perception|Sensor Perception]]**, **[[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12 Safety Enforcement#^sec-enforcement|Safety Enforcement]]**, **[[01 Books/Volume IV - Physical AI/04 Governing the Machine/16 Deployment Release/V4-16 Deployment Release#^sec-release|Deployment Release]]**)

**Permission Path**\
The independent mechanism with bounded latency, which the learned model cannot delay or corrupt, that alone may permit an action to reach an actuator. It checks each proposal against fresh evidence, the stopping envelope, and a fallback feasible from the current state, and refuses when any check fails. (**[[01 Books/Volume IV - Physical AI/00 Introduction/01 The Causal Boundary/V4-01.08 The Machine in Five Levels#^sec-boundary-machine-model|The Machine in Five Levels]]**, **[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/04 The Nervous System/V4-04 The Nervous System#^sec-nervous|The Nervous System]]**, **[[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12 Safety Enforcement#^sec-enforcement|Safety Enforcement]]**)

**Permission Stage**\
A grant that allows a named configuration of a machine to operate in a named domain, among named groups of people, on named evidence, and under named reporting duties, such as testing with a safety driver, driverless testing, or open deployment. A machine leaves a stage on evidence gathered there, and a stage is withdrawn for a configuration change, an incident, or a withheld record. (**[[01 Books/Volume IV - Physical AI/04 Governing the Machine/17 Responsible Physical AI/V4-17.05 Permission in Stages#^sec-responsibility-staged-permission|Permission in Stages]]**)

**Physical Artificial Intelligence (Physical AI)**\
The engineering of closed-loop machines in which learned models influence, without synchronous human approval, physical actions that change subsequent observations. A system is in scope when it combines a learned model, consequential physical feedback, and delegated physical authority. Its actions must fit the plant’s physical limits and the time available to respond, and a useful proposal still needs an independent permission decision. (**[[01 Books/Volume IV - Physical AI/00 Introduction/01 The Causal Boundary/V4-01 The Causal Boundary#^sec-boundary|The Causal Boundary]]**, **[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/03 The Cognitive Brain/V4-03 The Cognitive Brain#^sec-brain|The Cognitive Brain]]**)

**Physical Plant**\
The apparatus being controlled, such as a robot’s wheeled base or arm, whose state keeps changing while the computer calculates. (**[[01 Books/Volume IV - Physical AI/00 Introduction/01 The Causal Boundary/V4-01 The Causal Boundary#^sec-boundary|The Causal Boundary]]**, **[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/02 The Physical Body/V4-02 The Physical Body#^sec-body|The Physical Body]]**)

**Problem of Many Hands**\
The difficulty of assigning responsibility for an outcome that many people each helped produce, so that each can truthfully point to someone else. For a physical machine, the decisions behind one admitted action (policy, enforcer, envelope, crossing rule, staffing) belong to different parties and mostly appear in no runtime log. (**[[01 Books/Volume IV - Physical AI/04 Governing the Machine/17 Responsible Physical AI/V4-17.03 Decisions Behind an Admitted Action#^sec-responsibility-many-hands|Decisions Behind an Admitted Action]]**)

**Proposal Boundary**\
The line between a learned model, which may only propose an action, and the permission path, a mechanism designed to make the actuation decision independently of the model, within a qualified latency and fault envelope. The permission path checks each proposal against fresh evidence, the stopping envelope, and a fallback feasible from the current state, and it refuses when any check fails. The proposal boundary separates the Brain from the Nervous System in the book’s five-level machine. (**[[01 Books/Volume IV - Physical AI/00 Introduction/01 The Causal Boundary/V4-01.08 The Machine in Five Levels#^sec-boundary-machine-model|The Machine in Five Levels]]**, **[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/04 The Nervous System/V4-04 The Nervous System#^sec-nervous|The Nervous System]]**, **[[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12 Safety Enforcement#^sec-enforcement|Safety Enforcement]]**)

## Q

^sec-glossary-vol4-q

**Qualification Ladder**\
The ordering of four qualification environments, software-in-the-loop, processor-in-the-loop (PIL), hardware-in-the-loop (HIL), and physical fault rigs, by how much of the loop from sensing through inference, buses, drives, and plant is real, and therefore by falling trial throughput. The order is not a hierarchy of evidence, because a higher rung cannot subsume a lower one. Each rung yields a distinct category of evidence and stays blind to the physical mechanisms outside its boundary, so extensive software-in-the-loop passes say nothing about clock drift, DMA stalls, interrupt jitter, or supply sag. (**[[01 Books/Volume IV - Physical AI/04 Governing the Machine/15 Adversarial Verification/V4-15 Adversarial Verification#^sec-verification|Adversarial Verification]]**)

**Quantization**\
Storing a model’s weights, and optionally its activations, in fewer bits than training used. Weight-only quantization cuts the bytes a bandwidth-bound decode step must read; it does not speed up compute-bound phases unless the processor has kernels for the lower-precision arithmetic. (**[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/03 The Cognitive Brain/V4-03 The Cognitive Brain#^sec-brain|The Cognitive Brain]]**)

## R

^sec-glossary-vol4-r

**Record Chain**\
The sixteen records, one produced by each chapter of Parts I to IV except the one on the learned proposer and one by the conclusion, that carry the book’s assumptions and evidence from the limit record to the residual-claims register. One strand states what the plant can do and what the proposer has shown it can do; the other carries what the proposer proposes now; they meet in the enforcement record. A record makes a claim inspectable; it does not establish the claim. (**[[01 Books/Volume IV - Physical AI/00 Introduction/01 The Causal Boundary/V4-01.12 The Architecture of This Book#^sec-boundary-book-architecture|The Architecture of This Book]]**, **[[05 Reference/Volume IV - Physical AI/V4 Systems and Hardware#^sec-appendix-systems-record-register|The record register]]**)

**Reflected Rotor Inertia (${J_{\text{ref}}}$)**\
The apparent rotational inertia of an actuator rotor seen at the load-side joint output, ${J_{\text{ref}}} = {N_{\text{gear}}}^2 {J_{\text{rotor}}}$ for transmission ratio ${N_{\text{gear}}}$. In high-reduction joints it dominates the apparent load, caps joint acceleration, and concentrates impact energy on the gear teeth before drive current can be interrupted. (**[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/02 The Physical Body/V4-02 The Physical Body#^sec-body|The Physical Body]]**)

**Relative Degree**\
The number of times a function of the state, such as a barrier function ${h}({\mathbf{x}})$, must be differentiated with respect to time before the control input appears explicitly. Raw distance has relative degree two for torque, so a barrier written on distance alone gives the input no instantaneous control authority at the boundary. (**[[05 Reference/Volume IV - Physical AI/V4 Control and Dynamics#^sec-appendix-control-cbf|Safety and Control Barrier Functions]]**, **[[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12 Safety Enforcement#^sec-enforcement|Safety Enforcement]]**)

**Release Verdict**\
The signed decision that sets how much authority a named machine’s permission path may grant, `UNCOND` for the full assessed operating envelope, `COND` for a separately evidenced restricted envelope, or `REFUSE` when any required premise is missing, contradicted, or unknown, in each case only while its standing conditions hold. It is decided before operation and never moves the proposal boundary; under every verdict the permission path still admits each action. (**[[01 Books/Volume IV - Physical AI/04 Governing the Machine/16 Deployment Release/V4-16 Deployment Release#^sec-release|Deployment Release]]**)

**Replacement Latency (${L}$)**\
The elapsed time from the capture of the observation a new proposal rests on to the admission of that proposal. It is the sum of the capture-to-dispatch observation age and the dispatch-to-admission interval ${\Delta_{\text{da}}}$. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/11 Trajectory Planning/V4-11 Trajectory Planning#^sec-planning|Trajectory Planning]]**, **[[01 Books/Volume IV - Physical AI/03 Running the Machine/13 Workload Placement/V4-13 Workload Placement#^sec-placement|Workload Placement]]**)

**Rolling Shutter**\
An image sensor readout in which rows are reset, exposed, and read out sequentially, each row starting one row period after the previous one, so a single frame samples a moving scene at progressively later times. A global shutter instead exposes every pixel over the same interval. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/08 Sensor Perception/V4-08 Sensor Perception#^sec-perception|Sensor Perception]]**)

**Rule of Three**\
The approximation that zero failures in ${n}$ independent trials bounds the per-trial failure probability below about $3/{n}$ at 95 percent confidence, because $-\ln 0.05 \approx 3$. The bound holds only under the trials’ sampling assumptions. (**[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07 Closed-Loop Evaluation#^sec-evaluation|Closed-Loop Evaluation]]**, **[[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^sec-appendix-ml-exposure|Zero-Failure Testing and the Exposure Wall]]**)

## S

^sec-glossary-vol4-s

**Safe Torque Off (STO)**\
A drive safety function that prevents the drive from generating motor torque through its torque-producing power stage. STO does not itself brake a moving load, hold a gravity-loaded mechanism, or isolate the electrical supply. Its use in a stopping or restraint path requires a plant-specific assessment of coasting, stored energy, and any separately rated mechanical brake. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12 Safety Enforcement#^sec-enforcement|Safety Enforcement]]**, **[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/02 The Physical Body/V4-02 The Physical Body#^sec-body|The Physical Body]]**)

**Safety Case (Claim–Argument–Evidence)**\
A structured argument that a named machine, in a stated operating envelope and under a stated fault model, meets explicit physical criteria, written as claims that decompose through stated arguments into retained evidence. Unlike a test report, it states why the evidence supports a claim about conditions the machine has not yet met and names the assumptions under which the reasoning stops holding. It is written with the design, and in this book’s architecture its verdict decides what the permission path lets the machine do. (**[[01 Books/Volume IV - Physical AI/04 Governing the Machine/16 Deployment Release/V4-16 Deployment Release#^sec-release|Deployment Release]]**)

**Safety Integrity Level (SIL)**\
The IEC 61508 grade, 1 (lowest) to 4 (highest), of the risk reduction a safety function must provide, expressed as a band of tolerable dangerous failure rates. Not to be confused with software-in-the-loop testing, which some texts also abbreviate SIL. (**[[01 Books/Volume IV - Physical AI/04 Governing the Machine/16 Deployment Release/V4-16 Deployment Release#^sec-release|Deployment Release]]**)

**Safety Laser Scanner**\
A planar time-of-flight sensor type-tested as a protective device (IEC 61496-3) whose safety output reports only that something occupies a configured protective field. On a mobile base it carries the certified stop for a person in the path; a perception LiDAR without that rating cannot. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/08 Sensor Perception/V4-08 Sensor Perception#^sec-perception|Sensor Perception]]**, **[[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12 Safety Enforcement#^sec-enforcement|Safety Enforcement]]**)

**Safety Microcontroller**\
The small, independently clocked processor that runs the permission path’s deadline-critical checks, watchdogs, and hardware leases, and commands the drives’ stop functions. On the running machine it sits on its own board link with no memory shared with the application processor. (**[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/04 The Nervous System/V4-04 The Nervous System#^sec-nervous|The Nervous System]]**, **[[01 Books/Volume IV - Physical AI/03 Running the Machine/13 Workload Placement/V4-13 Workload Placement#^sec-placement|Workload Placement]]**)

**Scenario Table**\
The operational design domain divided into cells over low-dimensional task and environment parameters, such as pose offsets, surface friction, payload, and lighting, so that a dataset’s measured occupancy can be joined against it. Cells the join leaves empty are the dataset’s known absences. (**[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05.08 Collection Policy Coverage#^sec-data-policy-coverage|Collection Policy Coverage]]**)

**Sequential Probability Ratio Test (SPRT)**\
Wald’s test that updates a log-likelihood ratio after each trial and stops as soon as it crosses an acceptance or rejection boundary set by the allowed error probabilities. It permits early acceptance without inflating false acceptance, provided hypotheses, outcome, and boundaries are declared before testing. (**[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07 Closed-Loop Evaluation#^sec-evaluation|Closed-Loop Evaluation]]**, **[[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^sec-appendix-ml-sprt|Sequential Probability Ratio Test]]**)

**Shadow Mode Deployment**\
Staging in which a candidate policy runs on the live sensor streams and writes the commands it would have proposed to an isolated buffer with no actuator authority, while the incumbent controller supplies proposals and the enforcer keeps sole output ownership. Because the incumbent’s admitted commands determine the plant trajectory, agreement in shadow mode says nothing about the states the candidate’s own actions would reach. (**[[01 Books/Volume IV - Physical AI/04 Governing the Machine/16 Deployment Release/V4-16 Deployment Release#^sec-release|Deployment Release]]**, **[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07 Closed-Loop Evaluation#^sec-evaluation|Closed-Loop Evaluation]]**)

**Shared Autonomy**\
A collaborative control architecture in which a human supervisor and an autonomous policy concurrently exert control authority over an embodied system’s physical degrees of freedom. Authority allocation may be realized via continuous haptic virtual fixtures, dynamic compliance blending, or task-space privilege partitioning. The central challenge of shared autonomy is maintaining an intuitive, transparent authority distribution that avoids conflicting commands while preserving the qualified safety constraints. (**[[01 Books/Volume IV - Physical AI/04 Governing the Machine/14 Supervisory Intervention/V4-14 Supervisory Intervention#^sec-intervention|Supervisory Intervention]]**)

**Sim-to-Real Contact Exploit**\
A training failure in which a reinforcement learning policy discovers and exploits unphysical numerical artifacts in a simulator’s contact solver, such as interpenetration spring restitution, infinite friction sticking, or instantaneous impulse relaxation, to achieve high simulated reward. Because these mathematical solver relaxations do not exist in the physical world, the learned policy can lose performance or violate constraints when deployed on hardware. Mitigation can include improved contact models, randomized parameters, energy-consistency checks, and physical validation. (**[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06 Policy Training#^sec-training|Policy Training]]**)

**Sim-to-Real Gap (Sim-to-Reality Gap)**\
The systematic discrepancy in dynamics, contact mechanics, sensor transduction, and execution latency that exists between a computational physics simulation and the real physical environment. Policies optimized purely in simulation frequently fail upon physical deployment when the selected models omit or misrepresent effects such as frictional contact, transmission backlash, compliance, or execution delay. Bridging this gap is the central challenge of simulation-based policy training in physical AI. (**[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06 Policy Training#^sec-training|Policy Training]]**, **[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07 Closed-Loop Evaluation#^sec-evaluation|Closed-Loop Evaluation]]**)

**Simultaneous Localization and Mapping (SLAM)**\
Estimating a machine’s pose while building the map it localizes against. Modern systems store past poses as a graph of odometry and scan-match constraints; a loop closure adds a constraint when a place is revisited and can shift every pose and map cell at once, which is why map-anchored beliefs must carry the map revision that placed them. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/09 Spatial Memory/V4-09 Spatial Memory#^sec-memory|Spatial Memory]]**)

**Spatial Information Age (${t_{\text{age}}}$)**\
The time elapsed between the exposure midpoint at the transducer and the consumption of the resulting observation by a policy, state observer, or control loop; running text calls it observation age. Mass keeps moving while the pipeline computes, so the age becomes travel ${v}\,{t_{\text{age}}}$ that enters the stopping budget through the pre-brake delay. A frame’s arrival timestamp in userspace understates it by the capture and transport time already spent. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/08 Sensor Perception/V4-08 Sensor Perception#^sec-perception|Sensor Perception]]**, **[[01 Books/Volume IV - Physical AI/03 Running the Machine/09 Spatial Memory/V4-09 Spatial Memory#^sec-memory|Spatial Memory]]**)

**Speed and Separation Monitoring (SSM)**\
A collaborative-robot safety mode, set out in ISO 10218-2:2025, that slows or stops the robot so that a protective separation distance to a person is never breached. That distance covers the person’s travel over the robot’s reaction and stopping time, the robot’s own travel and stopping distance, and the position uncertainty of both. Power and force limiting, the complementary mode, instead bounds the force of a contact that is allowed to happen. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/10 Grounded Intent/V4-10 Grounded Intent#^sec-intent|Grounded Intent]]**, **[[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12 Safety Enforcement#^sec-enforcement|Safety Enforcement]]**)

**Standing Condition**\
A relied-on premise of a release verdict paired with a detector or site procedure, a checking cadence set by the physical failure mechanism rather than the software release cycle, and a validated response for when the premise becomes false or unknown. Standing conditions make a release revocable. (**[[01 Books/Volume IV - Physical AI/04 Governing the Machine/16 Deployment Release/V4-16.06 The Verdict’s Standing Conditions#^sec-release-standing-conditions|The Verdict's Standing Conditions]]**)

**Stopping Budget**\
The accounting of the distance a moving machine needs to stop, tested against the usable clearance in ${d_{\text{stop}}} \le {D_{\text{clear}}}$. Its elementary form is travel during the pre-brake delay plus braking travel, ${v}{\tau_{\text{delay}}} + {v}^2/(2{a_{\text{brake}}})$; the finished budget adds the allowances and delays that each part of the machine introduces, so added delay consumes clearance in proportion to the machine’s speed. (**[[01 Books/Volume IV - Physical AI/00 Introduction/01 The Causal Boundary/V4-01 The Causal Boundary#^sec-boundary|The Causal Boundary]]**, **[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/02 The Physical Body/V4-02 The Physical Body#^sec-body|The Physical Body]]**, **[[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12.04 Stopping Envelopes#^sec-enforcement-composite-budget|Sizing the composite stopping budget]]**)

**Stopping Envelope**\
The set of plant states, clearance and speed along each direction of travel, from which the resident braking response, begun after the accounted delay, arrests motion before the nearest boundary with the localization, protective, and tracking allowances still reserved. It turns ${d_{\text{stop}}} \le {D_{\text{clear}}}$ into a speed ceiling. Payload, floor friction, and winding temperature move its boundary, so an envelope computed from a datasheet deceleration overstates it when the machine is loaded. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12 Safety Enforcement#^sec-enforcement|Safety Enforcement]]**)

**Stopping Suffix**\
A precomputed braking trajectory reserved with an admitted motion plan to reach a controlled standstill within declared clearance and actuator limits. It is usable only from its validated entry region, with the necessary state continuity, traction, drive authority, and power available. If authority expires from another state, the permission path needs a separately qualified state-matched response. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/11 Trajectory Planning/V4-11 Trajectory Planning#^sec-planning|Trajectory Planning]]**, **[[01 Books/Volume IV - Physical AI/04 Governing the Machine/14 Supervisory Intervention/V4-14 Supervisory Intervention#^sec-intervention|Supervisory Intervention]]**)

**Supervisory Intervention**\
The transfer of the right to propose commands on named actuator channels between a learned policy and an authenticated person, committed on a control tick and bounded by a lease, while every command continues to pass the same permission check. The operator gains only the right to propose, not the actuators, and because the transfer is a delay on a moving machine it is priced in the stopping budget. (**[[01 Books/Volume IV - Physical AI/04 Governing the Machine/14 Supervisory Intervention/V4-14 Supervisory Intervention#^sec-intervention|Supervisory Intervention]]**)

## T

^sec-glossary-vol4-t

**Takeover Reaction Budget (${T_{\Sigma}}$)**\
The supervisory waiting interval from a takeover demand to receipt of the first human command, modeled here as ${T_{\Sigma}}={T_{\text{sensory}}}+{T_{\text{cognitive}}}+{T_{\text{motor}}}+{T_{\text{comm}}}$. The communication term includes transport and the authority handshake; plant response, braking, and any subsequent blending require separate budget terms. A takeover can be credited with preventing harm only if this complete response fits before the last feasible intervention time. (**[[01 Books/Volume IV - Physical AI/04 Governing the Machine/14 Supervisory Intervention/V4-14 Supervisory Intervention#^sec-intervention|Supervisory Intervention]]**)

**Task and Motion Planning (TAMP)**\
Planning that couples a symbolic search over discrete actions, such as grasp and place, with geometric samplers that find the continuous grasp poses, joint configurations, and paths each action needs. Failure to find a valid sample leaves the symbolic step unverified; it does not establish that no feasible configuration exists. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/10 Grounded Intent/V4-10 Grounded Intent#^sec-intent|Grounded Intent]]**)

**Temporal Ensembling**\
A filtering technique for action-chunked policies that combines predictions for the same execution time from overlapping chunks, often through an exponentially weighted average. It can reduce inter-chunk discontinuities but does not guarantee bounded jerk, preserve distinct action modes, or establish feasibility. Weighting older predictions also trades responsiveness for smoothing. (**[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/03 The Cognitive Brain/V4-03 The Cognitive Brain#^sec-brain|The Cognitive Brain]]**, **[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06 Policy Training#^sec-training|Policy Training]]**, **[[01 Books/Volume IV - Physical AI/03 Running the Machine/11 Trajectory Planning/V4-11 Trajectory Planning#^sec-planning|Trajectory Planning]]**)

**Temporal Logic Falsification**\
Verification posed as adversarial optimization, in which an optimizer searches initial conditions and time-varying disturbance trajectories within a bounded budget to minimize the quantitative robustness of a Signal Temporal Logic (STL) requirement, a real-valued measure of how far a trajectory is from violating or satisfying it. A trajectory with negative robustness is a counterexample; an unsuccessful search yields no certificate. (**[[01 Books/Volume IV - Physical AI/04 Governing the Machine/15 Adversarial Verification/V4-15 Adversarial Verification#^sec-verification|Adversarial Verification]]**, **[[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^sec-appendix-ml-stl|Signal Temporal Logic and Continuous Robustness]]**)

**Test Oracle**\
The predicate, fixed in full before a trial runs, that compares each independently witnessed quantity of the trial’s trace with its bound from a declared reference event and returns the trial’s verdict. Each comparison carries a signed margin in its own unit, which lets a near miss inform the next trial. (**[[01 Books/Volume IV - Physical AI/04 Governing the Machine/15 Adversarial Verification/V4-15 Adversarial Verification#^sec-verification|Adversarial Verification]]**)

**Time Parameterization**\
Choosing the timing ${s}({t})$ along a fixed geometric path ${\mathbf{q}}({s})$ so that every joint velocity, acceleration, torque, and jerk stays within the body’s limits, usually to minimize traversal time. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/11 Trajectory Planning/V4-11 Trajectory Planning#^sec-planning|Trajectory Planning]]**)

**Time-to-Harm (${t_{\text{harm}}}$)**\
The predicted interval until a specified harmful event under a stated continuation of the current motion and disturbance assumptions. Comparing it with detection, decision, actuation, and braking time helps assess response urgency, but a scalar timing inequality alone does not prove clearance or forward invariance. A protective response must begin while it remains feasible; once that region is lost, initiating emergency braking cannot guarantee avoidance. (**[[01 Books/Volume IV - Physical AI/04 Governing the Machine/18 Engineering Physical AI/V4-18 Engineering Physical AI#^sec-frontier|Engineering Physical AI]]**)

**Trajectory Spline Blending (${C}^2$ Continuity)**\
Interpolation across trajectory seams that matches position, velocity, and acceleration through ${C}^2$ continuity, using suitably constrained polynomials or splines. Acceleration continuity removes acceleration steps but does not imply continuous jerk, which requires ${C}^3$ continuity, or bound the magnitude of jerk. The blend must separately satisfy velocity, acceleration, jerk, torque, and clearance limits over the entire segment. (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/11 Trajectory Planning/V4-11 Trajectory Planning#^sec-planning|Trajectory Planning]]**, **[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/03 The Cognitive Brain/V4-03 The Cognitive Brain#^sec-brain|The Cognitive Brain]]**)

## V

^sec-glossary-vol4-v

**Vision-Language-Action (VLA) Model**\
A multimodal model that conditions action predictions on visual observations and language, often with robot proprioception. Outputs may be discrete action tokens, continuous controls, or trajectory chunks. Built on high-capacity transformer backbones pretrained on Internet-scale vision-language datasets and fine-tuned on robotics demonstrations, VLA models synthesize open-vocabulary semantic reasoning with spatial affordance grounding. Because their internal weights lack physical safety and stability guarantees, their outputs are treated as unprivileged candidate proposals requiring downstream kinodynamic and barrier filtering. (**[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/03 The Cognitive Brain/V4-03 The Cognitive Brain#^sec-brain|The Cognitive Brain]]**, **[[01 Books/Volume IV - Physical AI/03 Running the Machine/10 Grounded Intent/V4-10 Grounded Intent#^sec-intent|Grounded Intent]]**)

## W

^sec-glossary-vol4-w

**World Model**\
An internal generative model that learns to simulate the forward transition dynamics, contact mechanics, and sensory observations of the physical environment conditioned on the agent’s prospective actions. In physical AI, world models support counterfactual trajectory evaluation and model-predictive rollouts without executing each candidate on hardware. A learned predictive model is not automatically a validated digital twin. Their reliability is limited by epistemic uncertainty over non-smooth contact changes and the sim-to-real gap. (**[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/03 The Cognitive Brain/V4-03 The Cognitive Brain#^sec-brain|The Cognitive Brain]]**, **[[01 Books/Volume IV - Physical AI/03 Running the Machine/11 Trajectory Planning/V4-11 Trajectory Planning#^sec-planning|Trajectory Planning]]**, **[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06 Policy Training#^sec-training|Policy Training]]**)

**Worst-Case Execution Time (WCET)**\
The longest time a task can take to run to completion on a given processor, over every admissible input and every state its caches, pipeline, and buses can be in, with no other task competing for the processor. It is the ${C}$ term of a response bound; blocking and interference from other tasks and interrupts are separate terms with their own bounds, which a shared multicore can inflate. A measured maximum can refute a declared WCET but never establish it. (**[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/04 The Nervous System/V4-04 The Nervous System#^sec-nervous|The Nervous System]]**, **[[01 Books/Volume IV - Physical AI/03 Running the Machine/13 Workload Placement/V4-13 Workload Placement#^sec-placement|Workload Placement]]**)

Back to top

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/backmatter/glossary/glossary.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol4/backmatter/glossary/glossary.html#sec-glossary). Rendering provenance is recorded in the import manifest.
