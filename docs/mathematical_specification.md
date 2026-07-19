# Mathematical Specification

This document provides the formal mathematical definitions governing the Resolution Horizon framework, mapping the continuous geometric objects to their information-theoretic representations.

---

## 1. The Dynamic Generator and Bracket Tree

Let $\mathcal{M}$ be a smooth $d$-dimensional manifold, and let $F \in \mathfrak{X}(\mathcal{M})$ be the true, unobserved vector field generating the system dynamics. The observer reconstructs an empirical estimate $\hat{F}_{N,\lambda_N}$ from a dataset $\mathcal{D}_N^\sigma$ of $N$ trajectories corrupted by noise scalar $\sigma$.

The algebraic depth space $\text{Lie}_k(\hat{F})$ is defined as the filtered Lie algebra subspace spanned by iterated Lie brackets up to depth $k$:

$$\text{Lie}_0(\hat{F}) = \text{span}\{\hat{F}\}$$
$$\text{Lie}_k(\hat{F}) = \text{span}\left(\{ [\hat{X}, \hat{Y}] : \hat{X} \in \text{Lie}_{k-1}(\hat{F}), \, \hat{Y} \in \text{Lie}_0(\hat{F}) \}\right)$$

---

## 2. The Finite-Observation Invariant Class

The set of estimated continuous invariants at algebraic depth $k$, denoted by $\widehat{\text{Inv}}_k$, is the kernel of the Lie derivative operator determined by the algebra elements:

$$\widehat{\text{Inv}}_k = \{ \phi \in C^\infty(\mathcal{M}) : \mathcal{L}_{\hat{X}}\phi = 0, \ \forall \hat{X} \in \text{Lie}_k(\hat{F}) \}$$

---

## 3. The Confidence-Filtered Gauge Stabilizer

Symmetries are formalized not as absolute mathematical transformations, but as a statistical stabilizer region over a compact transformation domain $B_R \subset \text{Diff}^{k+1}(\mathcal{M})$. 

Given a data-dependent metric tolerance $\epsilon_k(N, \sigma, \lambda_N)$ and the jet metric $d_{C^{k+1}}$, the empirical gauge group is defined as:

$$\hat{G}^{(k)}(\epsilon_k) \cap B_R = \left\{ g \in B_R : \sup_{\phi \in \widehat{\text{Inv}}_k} d_{C^{k+1}}(\phi, \, g^*\phi) < \epsilon_k \right\}$$

where the evaluation tolerance scales with high-order derivative variance:

$$\epsilon_k = C_k \left( \frac{\sigma^2}{N} \right)^{1/2} + \epsilon_{\mathrm{model}}$$

---

## 4. The Unified Information Currency

The informational properties of the discovery loop are calculated using a two-part Minimum Description Length (MDL) code layout.

### Invariant Compression Gain
The compression capacity bought by the recovered structural invariants is the reduction in data description length relative to a generic baseline model:

$$\Delta L(k) = L(\mathcal{D}_N^\sigma \mid \text{Baseline}) - L\left(\mathcal{D}_N^\sigma \ \Big|\  \frac{\text{Lie}_k(\hat{F})}{\hat{G}^{(k)}}\right)$$

### Symmetry Ambiguity Cost
The description cost of the remaining coordinate ambiguity is the bit requirements of specifying the parameter grid boundaries $\theta_G$ and the log of the $\delta$-covering number of the stabilizer under the jet metric:

$$C_G(k) = L(\theta_G) + \log N\left(\delta, \ \hat{G}^{(k)}(\epsilon_k) \cap B_R, \ d_{C^{k+1}}\right)$$

---

## 5. The Structural Efficiency Optimization

The operational resolution horizon $k^*$ is the global maximum of the structural efficiency functional $\eta(k)$, indicating the exact transition point before the onset of the misresolution regime:

$$k^* = \arg\max_k \eta(k) = \arg\max_k \left[ \frac{\Delta L(k)}{C_G(k)} \right]$$
