# Nonuniformity required for fast erasure

The [endpoint bottleneck inequality](control_obstruction.md#u1-bottleneck-inequality) gives necessary resources for locally randomizing the far end of the chain. This section develops its consequences for the system's largest eigenvalue, for a sequence of endpoint channels, and for a finite coherent controller. The Hamiltonian, target state, and half trace distance are fixed by [the model](model.md); their role in the full result is described in [the overview](overview.md).

Use the product input from Result U1 and write

```math
r=3^{L-1},\qquad d_S=3^L,\qquad
0\leq\varepsilon<\frac13,\qquad
\delta=\frac13-\varepsilon>0.
```

The success condition in this section is only

```math
D\!\left(\rho_L(T),\frac{I_3}{3}\right)\leq\varepsilon.
```

A uniform global erasure guarantee implies this condition, but the lower bounds require only this one input and one final local marginal. All logarithms in this section are natural unless a base is indicated.

## R1. Temporary system nonuniformity

For a density matrix $`\rho`$ on dimension $`d`$, define its min-entropy and min-entropy deficit by

```math
H_{\min}(\rho)=-\log\|\rho\|_\infty,
\qquad
P_\infty(\rho)=\log d-H_{\min}(\rho)
=\log\bigl(d\|\rho\|_\infty\bigr).
```

**Result R1.** Every endpoint protocol satisfying the stated local success condition obeys

```math
{
\boxed{
\int_0^T\|\rho_t\|_\infty\,dt\geq\frac{\delta}{J},
\qquad
\sup_{0\leq t\leq T}\|\rho_t\|_\infty
\geq\frac{\delta}{JT}.
}
}
\tag{R1}
```

Equivalently,

```math
\inf_{0\leq t\leq T}H_{\min}(\rho_t)
\leq\log\frac{JT}{\delta}.
```

For piecewise continuous finite-pulse protocols the extrema can be attained among the trajectory and its one-sided pulse states. The supremum and infimum formulation also covers limits of such protocols.

### Proof and scaling

The local success condition forces $`p_\downarrow(L,T)\geq1/3-\varepsilon=\delta`$. Apply U1 to obtain the integral inequality, then bound the integral by $`T\sup_t\|\rho_t\|_\infty`$. Taking the negative logarithm proves the min-entropy formulation.

Initially, the nonzero eigenvalues of $`\rho_0`$ are all $`1/r`$, so

```math
H_{\min}(\rho_0)=(L-1)\log3,
\qquad
P_\infty(\rho_0)=\log3.
```

Consequently

```math
\sup_{0\leq t\leq T}
\bigl[P_\infty(\rho_t)-P_\infty(\rho_0)\bigr]
\geq(L-1)\log3-\log\frac{JT}{\delta}.
```

At fixed $`J`$ and fixed error $`\varepsilon<1/3`$, a polynomial upper bound on $`T`$ therefore requires an extensive temporary increase of the min-entropy deficit. The system must develop a largest eigenvalue at least inverse polynomial in $`L`$ during the protocol.

This conclusion allows controller memory. As proved in U1, joint operations on site $`1`$ and the controller leave $`Q\otimes I_C`$ unchanged, and the current expectation depends only on the reduced chain state $`\rho_t`$. Neither unitality nor a memoryless description of this reduced trajectory is assumed in R1.

### The spectral meaning of the bound

An extensive min-entropy change does not imply an extensive von Neumann entropy change. A useful explicit comparison, for any unit vector $`|v\rangle`$ in the chain Hilbert space, is

```math
\omega_L=L^{-2}|v\rangle\langle v|
+(1-L^{-2})\frac{I_{d_S}}{d_S}.
```

Its largest eigenvalue is $`L^{-2}+(1-L^{-2})/d_S`$, giving

```math
H_{\min}(\omega_L)=2\log L+o(1).
```

By concavity of von Neumann entropy,

```math
0\leq\log d_S-S(\omega_L)
\leq L^{-2}\log d_S
=\frac{\log3}{L}.
```

This example compares spectral quantities; it makes no reachability assertion. It shows why R1 alone supplies neither an extensive average-entropy reduction nor a heat, work, or Landauer cost. Its resource is concentration in the largest eigenvalue. The finite-controller statement below counts a different, explicitly specified physical resource model.

### Prefix-channel formulation

Suppose a controller and all supplied environmental states have a fixed initialization independent of the unknown chain input. The reduced evolution up to each time $`t`$ then defines a CPTP channel $`\Phi_t`$ on the chain, even when its time evolution is not divisible into memoryless reduced channels. Positivity gives

```math
\rho_t=\Phi_t(\rho_0)
\leq\frac{\Phi_t(I_{d_S})}{r}.
```

Combining this with R1 yields

```math
{
\boxed{
\sup_{0\leq t\leq T}\log\|\Phi_t(I_{d_S})\|_\infty
\geq(L-1)\log3-\log\frac{JT}{\delta}.
}
}
\tag{R1a}
```

The target replacement channel $`\mathcal R_{I_{d_S}/d_S}`$ is unital. Nevertheless, a fast implementation must contain prefixes whose action on the identity has the large norm in R1a. This formulation measures a property of the actual prefixes without assigning a budget to a chosen decomposition into elementary channels.

## R2. Accumulated channel budget

For a CPTP channel $`\mathcal E`$ with the same input and output dimension $`d`$, define

```math
b(\mathcal E)=\log\|\mathcal E(I_d)\|_\infty.
```

Since $`\mathcal E(I_d)`$ is positive with trace $`d`$, its norm lies between $`1`$ and $`d`$. Thus $`0\leq b(\mathcal E)\leq\log d`$, and $`b(\mathcal E)=0`$ exactly when $`\mathcal E`$ is unital.

**Result R2.** Consider a finite, memoryless sequence of endpoint CPTP maps $`\mathcal E_k`$, applied at times $`t_k`$, interspersed with the fixed bulk evolution and any additional unital endpoint evolution. Set

```math
B(t)=\sum_{k:t_k\leq t}b(\mathcal E_k).
```

Local randomization to error $`\varepsilon`$ requires

```math
{
\boxed{
B(T)\geq(L-1)\log3-\log\frac{JT}{\delta}.
}
}
\tag{R2}
```

The bound is necessary; it is not a sufficient criterion for fast erasure.

### Exact increase of the min-entropy deficit

Let $`A`$ be the channel input and let $`B`$ be any finite idle ancillary system. For every state $`\rho_{AB}`$, positivity implies

```math
(\mathcal E\otimes\mathrm{id}_B)(\rho_{AB})
\leq\|\rho_{AB}\|_\infty\,
\mathcal E(I_d)\otimes I_B.
```

Taking operator norms gives

```math
\|(\mathcal E\otimes\mathrm{id}_B)(\rho_{AB})\|_\infty
\leq e^{b(\mathcal E)}\|\rho_{AB}\|_\infty.
```

Input and output dimensions agree, so the corresponding increase of $`P_\infty`$ is at most $`b(\mathcal E)`$. Equality is attained on the maximally mixed state of $`A\otimes B`$. Hence

```math
b(\mathcal E)
=\sup_{B,\rho_{AB}}
\left\{
P_\infty\bigl[(\mathcal E\otimes\mathrm{id}_B)(\rho_{AB})\bigr]
-P_\infty(\rho_{AB})
\right\}.
```

Thus $`b`$ is exactly the complete increasing power of the min-entropy deficit. The ancillary system in this identity is idle during the channel application; it does not model an independently supplied reset resource.

### Proof of the accumulated bound

Starting from $`\rho_0\leq I_{d_S}/r`$, each endpoint map increases the upper bound on the largest eigenvalue by at most $`e^{b(\mathcal E_k)}`$. The other evolution is unital. Induction therefore gives

```math
\|\rho_t\|_\infty\leq
\min\left\{1,\frac{e^{B(t)}}{r}\right\}.
```

Since $`B(t)`$ is nondecreasing, U1 implies

```math
\begin{aligned}
p_\downarrow(L,T)
&\leq J\int_0^T
\min\left\{1,\frac{e^{B(t)}}{r}\right\}\,dt\\
&\leq\frac{J}{r}\int_0^T e^{B(t)}\,dt\\
&\leq\frac{JT}{r}e^{B(T)}.
\end{aligned}
```

Success requires $`p_\downarrow(L,T)\geq\delta`$, which rearranges to R2. For the physical qutrit endpoint, every $`b(\mathcal E_k)`$ uses $`d=3`$.

### Exact relation to channel max-relative entropy

Let $`\mathcal U_d`$ be the unital CPTP channels on dimension $`d`$. Use the complete-positivity order to define

```math
D_{\max}(\mathcal E\Vert\mathcal F)
=\log\inf\{\mu:\mu\mathcal F-\mathcal E
\text{ is completely positive}\}.
```

Define the generalized robustness relative to $`\mathcal U_d`$ by

```math
R_{\mathcal U_d}(\mathcal E)
=\inf\left\{
s\geq0:
\frac{\mathcal E+s\mathcal G}{1+s}\in\mathcal U_d,
\quad\mathcal G\text{ CPTP}
\right\}.
```

Then the same channel quantity has the exact expression

```math
b(\mathcal E)
=\min_{\mathcal F\in\mathcal U_d}
D_{\max}(\mathcal E\Vert\mathcal F)
=\log\bigl[1+R_{\mathcal U_d}(\mathcal E)\bigr].
```

To prove the first equality, put $`\lambda=\|\mathcal E(I_d)\|_\infty`$. If $`\mu\mathcal F-\mathcal E`$ is CP and $`\mathcal F`$ is unital, evaluating it on $`I_d`$ gives $`\mathcal E(I_d)\leq\mu I_d`$, hence $`\mu\geq\lambda`$.

For the converse, if $`\lambda>1`$, the operator

```math
\tau=
\frac{I_d-\mathcal E(I_d)/\lambda}
{d(1-1/\lambda)}
```

is positive and has trace one. Define

```math
\mathcal F=\frac{\mathcal E}{\lambda}
+\left(1-\frac1\lambda\right)\mathcal R_\tau,
\qquad
\mathcal R_\tau(X)=\tau\mathrm{Tr}X.
```

This convex combination is CPTP. Direct evaluation gives $`\mathcal F(I_d)=I_d`$, and

```math
\lambda\mathcal F-\mathcal E=(\lambda-1)\mathcal R_\tau
```

is CP. The optimal factor is therefore $`\lambda`$. If $`\lambda=1`$, the trace condition already forces $`\mathcal E(I_d)=I_d`$, so choosing $`\mathcal F=\mathcal E`$ covers that case.

Finally, a robustness decomposition with coefficient $`s`$ gives CP domination by $`(1+s)\mathcal F`$. Conversely, if $`\mu\mathcal F-\mathcal E`$ is CP with $`\mu>1`$, then

```math
\mathcal G=\frac{\mu\mathcal F-\mathcal E}{\mu-1}
```

is trace preserving as well as CP, and supplies a robustness decomposition with $`s=\mu-1`$. This proves the second equality.

The channel-resource framework, including complete increasing power, CP-order max-relative entropy, and generalized robustness, is established in [Liu and Winter, *Resource theories of quantum channels and the universal role of resource erasure*](https://arxiv.org/html/1904.04201v1), Example 2 and Sections V.2.1–V.2.3. The equalities above specialize that framework to the unital class. The chain-specific consequence is the necessary physical-time budget R2. See [related work](../references/related_work.md) for the broader attribution.

### Continuous endpoint generators

There is also a useful sufficient envelope for a time-dependent, memoryless endpoint Lindblad generator $`\mathcal L_{1,t}`$. Set

```math
\ell(t)=\lambda_{\max}\bigl[\mathcal L_{1,t}(I_3)\bigr],
\qquad
B(t)=\int_0^t\ell(s)\,ds,
```

and add any discrete pulse contributions. The generator's action on the identity is Hermitian and traceless, so $`\ell(t)\geq0`$.

For completeness, let $`\mathcal K_t`$ denote the full generator and put $`m(t)=e^{B(t)}/r`$. Between pulses, $`Y_t=m(t)I_{d_S}-\rho_t`$ obeys

```math
\dot Y_t=\mathcal K_t(Y_t)
+m(t)\left[\ell(t)I_{d_S}-\mathcal K_t(I_{d_S})\right].
```

The inhomogeneous term is positive because
$`\mathcal K_t(I_{d_S})=\mathcal L_{1,t}(I_3)\otimes I_{2,\ldots,L}`$; all Hamiltonian terms annihilate the identity. The propagator of $`\mathcal K_t`$ is positive, so $`Y_0\geq0`$ implies $`Y_t\geq0`$. At a pulse the preceding positive-map estimate preserves the bound with the corresponding increment of $`B`$. The same proof of R2 thus applies to this envelope.

For the fixed-total-rate bath of [the model](model.md), with $`0\leq p\leq2/3`$,

```math
\mathcal L_{1,p}(I_3)
=\gamma(2-3p)|0\rangle\langle0|
-\gamma\left(1-\frac{3p}{2}\right)
\bigl(|\uparrow\rangle\langle\uparrow|
+|\downarrow\rangle\langle\downarrow|\bigr).
```

Its envelope rate is $`\ell=\gamma(2-3p)`$, including $`2\gamma`$ for pure loss and zero for the unbiased bath. This envelope can accumulate over time even when a reservoir still has slow mixing. The actual filling obstruction is separately quantified by [the reservoir threshold](reservoir_threshold.md).

An accumulated budget refers to the chosen channel segmentation and can overestimate the nonuniformity generated by the composite evolution. R1a gives the complementary statement directly in terms of the actual prefix channels.

## R3. Finite controller resource

Let a controller $`C`$ of dimension $`K`$ start in a fixed state $`\sigma_C`$, independently of the chain input. Its joint initial state is

```math
\rho_{SC}(0)=\rho_0\otimes\sigma_C.
```

Allow arbitrary unital CPTP operations on site $`1`$ together with the controller, including joint unitary controls and time-dependent unital joint generators. All controller degrees of freedom are retained in this description until the final partial trace. The bulk Hamiltonian remains $`H\otimes I_C`$.

**Result R3.** Local randomization to error $`\varepsilon`$ requires

```math
{
\boxed{
T K\|\sigma_C\|_\infty
\geq\frac{3^{L-1}}{J}\left(\frac13-\varepsilon\right).
}
}
\tag{R3}
```

Equivalently, since
$`D_{\max}(\sigma_C\Vert I_C/K)=\log(K\|\sigma_C\|_\infty)`$,

```math
T\exp D_{\max}\!\left(\sigma_C\middle\Vert\frac{I_C}{K}\right)
\geq\frac{r\delta}{J}.
```

### Proof

Independence of the initial state and the known bound on $`\rho_0`$ give

```math
\rho_{SC}(0)
\leq\frac{\|\sigma_C\|_\infty}{r}I_{SC}.
```

All subsequent joint dynamics is unital, so positivity preserves this domination for every $`t`$. The positive and negative parts of $`C_Q\otimes I_C`$ each have trace $`JK`$. The current proof of U1, applied to the joint state, therefore yields

```math
\begin{aligned}
p_\downarrow(L,T)
&\leq\int_0^T
\left|\mathrm{Tr}\bigl[(C_Q\otimes I_C)\rho_{SC}(t)\bigr]\right|\,dt\\
&\leq\frac{JT}{r}K\|\sigma_C\|_\infty.
\end{aligned}
```

The required down probability is at least $`\delta`$. Rearranging proves R3. Tracing out the controller at the end has no effect on this last-site population.

### What the controller factor counts

For a maximally mixed controller, $`K\|\sigma_C\|_\infty=1`$, so the obstruction is exactly the unital lower bound regardless of the controller's dimension. For a pure controller, the factor is $`K`$, and polynomial-time local randomization requires

```math
\log K\geq(L-1)\log3-\log\frac{JT}{\delta}.
```

In particular, if the initially supplied resource consists of $`n`$ pure qutrit ancillas, all subsequent joint operations are unital, and used ancillas are retained as inactive controller degrees of freedom, then $`K=3^n`$ and

```math
n\geq L-1-\log_3\frac{JT}{\delta}.
```

Any extra initially maximally mixed ancillary factors cancel between the total dimension and the initial largest eigenvalue. Swapping the endpoint with a fresh pure ancilla fits this model when that ancilla was preallocated and its used output remains counted.

The resource being bounded is the initial nonuniformity of an independent, finite controller under unital joint operations. Extending this count to a continuously supplied bath, discarded measurement records, or initially correlated controller states would require an explicit model of those additional resources. R3 by itself gives no heat cost and no ancilla-use upper bound for the continuous reservoir protocol.

The constructive erasure dynamics is developed separately through [charge transport](charge_transport.md) and [the reservoir criterion](reservoir_threshold.md). Those results establish how specified baths achieve fast erasure; R1–R3 establish necessary conditions in the respective control models defined here.
