# Experimental Verification Protocols

This document details the standardized calibration steps, synthetic test rigs, and validation metrics required to empirically isolate the resolution horizon on the laboratory bench.

---

## 1. Synthetic Benchmarks Class Hierarchy

To evaluate the framework without confounding structural limits with model specification errors, testing must progress through three isolated calibration rigs:

### Rig 1: Canonical Linear Oscillator
* **System:** $H = \frac{1}{2}p^2 + \frac{1}{2}\omega^2 x^2$
* **Purpose:** Establishes the ideal numerical baseline. The stabilizer $\hat{G}^{(k)}$ should map clean rotation symmetries ($SO(2)$) with zero gauge coordinate deformation error.

### Rig 2: Nonlinear Coordinate-Warped Oscillator
* **System:** Rig 1 subjected to an explicit, highly non-linear diffeomorphism injection:
    $$y_1 = x + \gamma p^2, \quad y_2 = p + \gamma x^3$$
* **Purpose:** Separates representation learning capacity from gauge invariance. Tests whether the quotient engine maps identical structural coordinates across distorted vantage points.

### Rig 3: The Classical Rigid Body (Euler Top)
* **System:** Symmetries and conservation laws on the $SO(3)$ Lie algebra group.
* **Purpose:** Evaluates performance against systems containing genuine non-linear bracket structures and non-trivial curvature.

---

## 2. Parameter Sweep Protocols

To map out the empirical response surface $k^* = f(N, \sigma, E_{\mathrm{cov}}, \Gamma)$, the operator must perform three isolated resource sweeps:

[ EMISSIVE EXPERIMENTAL MATRIX ]
                             │
 ┌───────────────────────────┼───────────────────────────┐
 ▼                           ▼                           ▼
 [ Sweep I: Data Volume ]    [ Sweep II: Noise Floor ]   [ Sweep III: Regularization ]
N: 10^3 ──► 10^6            σ: 0.00 ──► 0.50            λ_N: 0.1 ──► 10.0
Prediction: ∂k*/∂N > 0      Prediction: ∂k*/∂σ < 0      Purpose: Bypass Diagnostic

---

## 3. Execution of the Regularization Bypass Control

The Regularization Bypass protocol is the primary tool for testing the causal origin of the discovery limit.

1.  **Freeze Environment:** Lock dataset footprint constraints exactly at $N = 100000$, $\sigma = 0.02$, with fixed state-space coverage profiles.
2.  **Execute Step Intervention:** Evaluate the system across an explicit shift in filter scale:
    $$\lambda_N^{(1)} = 1.0 \quad \longrightarrow \quad \lambda_N^{(2)} = 8.0$$
3.  **Evaluate Causal Fork:**
    * **Observer-Limited Branch:** If the information efficiency peak $k^*$ changes positions along the depth axis ($\partial k^* / \partial \lambda_N \neq 0$), the limit is driven by the observer's derivative reconstruction instability.
    * **Structure-Limited Branch:** If $k^*$ remains pinned at a static depth ($\partial k^* / \partial \lambda_N \approx 0$), the boundary reflects a structural property of the system—either the exhaustion of true invariants or an incorrect choice of invariant class vocabulary.
