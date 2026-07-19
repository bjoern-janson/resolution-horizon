# Reference Symbols and Notation

This document provides a definitive structural reference for all variable assignments, geometric metrics, and information-theoretic identifiers utilized across the Resolution Horizon framework.

---

## 1. Geometric and Dynamic Primitive Objects

| Symbol | Definition | Mathematical Class |
| :--- | :--- | :--- |
| $\mathcal{M}$ | State-space manifold of the target dynamical system | Smooth Manifold |
| $F$ | Underlying unobserved vector field (Generator) | $\mathfrak{X}(\mathcal{M})$ |
| $\mathcal{D}_N^\sigma$ | Observation trajectory dataset with size $N$ and noise scale $\sigma$ | Discrete Data Matrix |
| $\hat{F}_{N,\lambda_N}$ | Empirically reconstructed vector field with smoothing factor $\lambda_N$ | Estimated Vector Field |
| $\text{Lie}_k(\cdot)$ | Subspace spanned by iterated Lie brackets at depth $k$ | Filtered Lie Subalgebra |
| $\widehat{\text{Inv}}_k$ | Extracted continuous invariant coordinate equations at depth $k$ | Subspace of $C^\infty(\mathcal{M})$ |

---

## 2. Statistical Metric Estimators

| Symbol | Definition | Mathematical Class |
| :--- | :--- | :--- |
| $\epsilon_k$ | Confidence evaluation tolerance threshold at algebraic depth $k$ | $\mathbb{R}^+$ Scalar |
| $d_{C^{k+1}}$ | Standard jet metric bounding coordinate evaluation up to order $k+1$ | Differential Metric |
| $B_R$ | Compact workspace boundary constraining transformation scale | Bounded Diffeomorphism Subset |
| $\hat{G}^{(k)}(\epsilon_k)$ | Empirical confidence-filtered stabilizer gauge family | Statistical Lie Group Subset |
| $V(k)$ | Variance amplification envelope of the $k$-th derivative operator | Stochastic Boundary Vector |

---

## 3. Information Currency Metrics

| Symbol | Definition | Unit / Scale |
| :--- | :--- | :--- |
| $\Delta L(k)$ | Invariant compression capacity gain over generic baseline | Bits (Description Length) |
| $C_G(k)$ | Symmetry ambiguity cost required to specify the stabilizer domain | Bits (Description Length) |
| $\theta_G$ | Minimal parameter description grid modeling the stabilizer family | Parameter Coordinate Matrix |
| $N(\delta, \cdot)$ | Covering number required to map the confidence ball with grid resolution $\delta$ | Integer Cardinality Counting |
| $\eta(k)$ | Structural efficiency exchange function at resolution depth $k$ | Bits Saved / Bits Spent Ratio |
| $k^*$ | Operational resolution horizon critical point | Discrete Index Axis ($\mathbb{N}^+$) |
