# Resolution Horizon

> Measuring the limits of invariant discovery under bounded observation.

## Overview

**Resolution Horizon** is an experimental research framework for studying how much mathematical structure can be recovered from finite, noisy observations of dynamical systems.

Rather than treating discoverable structure as an intrinsic property of a system, the framework proposes that structural recovery is jointly determined by the dynamics, the observer, and the available computational resources. 

The central hypothesis is that every observation process possesses a measurable **resolution horizon** ($k^*$): a finite level of structural complexity beyond which additional analysis no longer reveals genuine invariants and instead begins to model observational uncertainty.

The project combines differential geometry, dynamical systems, statistical estimation, and information theory into a unified empirical framework for studying this boundary.

---

## Central Hypothesis

Given finite observations of a dynamical system, increasing structural depth initially improves invariant discovery, but beyond a critical depth, estimation uncertainty dominates, producing an experimentally measurable resolution horizon.

The primary empirical quantity is the information efficiency exchange rate $\eta(k)$, balancing compression value against structural ambiguity:

$$\eta(k) = \frac{\Delta L(k)}{C_G(k)} = \frac{L(\mathcal{D}_N \mid \text{Baseline}) - L\left(\mathcal{D}_N \ \Big\vert{}\  \frac{\text{Lie}_k(\hat{F})}{\hat{G}^{(k)}}\right)}{L(\theta_G) + \log N\left(\delta, \ \hat{G}^{(k)}(\epsilon_k) \cap B_R, \ d_{C^{k+1}}\right)}$$

The optimal discovery horizon is defined as:
$$k^* = \arg\max_k \eta(k)$$

### The Resource Response Surface
The horizon is an emergent response surface shaped by data and environmental constraints:
$$k^* = f\left(N, \sigma, E_{\mathrm{cov}}, \lambda_{\min}(\Gamma)\right)$$

| Symbol | Meaning | Predicted Sign |
| :--- | :--- | :--- |
| $N$ | Number of observations | $\frac{\partial k^*}{\partial N} > 0$ |
| $\sigma$ | Observation noise | $\frac{\partial k^*}{\partial \sigma} < 0$ |
| $E_{\mathrm{cov}}$ | State-space coverage deficit | $\frac{\partial k^*}{\partial E_{\mathrm{cov}}} < 0$ |
| $\lambda_{\min}(\Gamma)$ | Excitation/intervention diversity | $\frac{\partial k^*}{\partial \lambda_{\min}(\Gamma)} > 0$ |

These directional predictions form the primary falsifiable claims of the project.

---

## The Three-Regime Phase Footprint

The interaction between the twin informational curves produces a distinctive coupled geometric signature across algebraic depth $k$:

* **Regime I (Discovery):** $\Delta L(k) \uparrow$ and $C_G(k) \downarrow$. Structural compression rises efficiently while coordinate ambiguity contracts.
* **Regime II (Horizon):** $\eta(k)$ achieves its global maximum. This is the optimal structural resolution boundary ($k = k^*$).
* **Regime III (Misresolution):** $\Delta L(k) \downarrow$ and $C_G(k) \uparrow$. The instrument overfits the equivalence relation itself, parsing high-order derivative noise as false background symmetry.

---

## Repository Structure

```text
├── instrument.py      # Quantitative measurement core & metric calculators
├── experiment.py      # Regularization Bypass protocol & causal interventions
├── test_suite.py      # Automated topological verification harness
└── README.md          # Project specification and deployment guide
```

Execution & DiagnosticsTo run the Regularization Bypass Experiment—applying a causal intervention on the smoothing parameter ($\lambda_N$) to isolate observer-limited horizons from system-limited ceilings:

#!/bin/bash
echo "Running Regularization Bypass Experiment..."
python experiment.py

To execute the automated test suite verifying the paired curve phase signatures and directional derivative signs:

echo "Running Verification Test Suite..."
python -m unittest test_suite.py

Philosophy
Resolution Horizon treats scientific discovery itself as a measurable computational process. Instead of asking:

What mathematical structure exists?

The framework asks:

What mathematical structure is recoverable by a bounded observer with finite data, finite precision, and finite computation?

License
Released under the MIT License.
