# Endpoint control obstruction

The fixed hopping Hamiltonian and distance conventions are specified in [the model](model.md). This section proves that a local spin population retains memory for exponentially long physical time under every allowed unital endpoint protocol. The proof uses one product preparation and a current supported on a two-dimensional subspace. The [overview](overview.md) places this obstruction alongside the erasure protocols.

Throughout, $`L\geq 2`$, $`J>0`$, and the only engineered operations act on site $`1`$. The total elapsed time is $`T`$. Write $`\rho_t`$ for the state of the chain, $`\rho_L(t)`$ for its last-site marginal, and

```math
\rho_0=\left(\frac{I_3}{3}\right)^{\otimes(L-1)}
\otimes|\uparrow\rangle\langle\uparrow|_L,
\qquad r=3^{L-1}.
```

The last site is prepared up; every other site is independently maximally mixed. This same preparation will be used for every endpoint protocol.

## U1. Bottleneck inequality

Let $`Q`$ be the projector onto basis configurations whose rightmost occupied spin among sites $`2,\ldots,L`$ is up. The empty tail is excluded, and $`Q`$ acts as the identity on site $`1`$. Also define the local down-population effect

```math
R_\downarrow=I_{1,\ldots,L-1}\otimes
|\downarrow\rangle\langle\downarrow|_L,
\qquad
p_\downarrow(L,t)=\operatorname{Tr}(R_\downarrow\rho_t).
```

**Result U1.** For arbitrary trace-preserving endpoint channels, including nonunital channels, interspersed with the fixed bulk evolution,

```math
\boxed{
p_\downarrow(L,T)
\leq J\int_0^T\|\rho_t\|_\infty\,dt.
}
\tag{U1}
```

The same inequality holds with simultaneous local Hamiltonian or local Lindblad control. It also holds for the reduced chain trajectory when a retained controller interacts only with site $`1`$. In that case all controller operations are included in the joint, unconditional trace-preserving evolution.

### Proof: the endpoint cannot change the tail projector directly

For any CPTP map $`\mathcal E`$ on site $`1`$, trace preservation gives $`\mathcal E^*(I_3)=I_3`$. Since $`Q=I_3\otimes Q_{2,\ldots,L}`$,

```math
(\mathcal E^*\otimes\operatorname{id})(Q)=Q.
```

An instantaneous endpoint pulse therefore leaves $`\operatorname{Tr}(Q\rho)`$ unchanged, regardless of whether the pulse is unital. A local Hamiltonian commutes with $`Q`$, while the adjoint of a trace-preserving local generator annihilates $`Q`$. Neither contributes directly to its continuous-time derivative.

Initially, every configuration in the support of $`\rho_0`$ has an up spin at site $`L`$. Hence

```math
Q\rho_0=\rho_0,
\qquad \operatorname{Tr}(Q\rho_0)=1.
```

The rank of $`Q`$ is $`(3^L-3)/2`$: half the nonempty tail configurations have an up rightmost spin, and the first site has three independent states. The proof below uses its current rather than this rank.

### Proof: the Hamiltonian current has two nonzero eigenvalues

Hopping within the tail preserves the ordered spin word and thus preserves its rightmost spin. A hop between sites $`1`$ and $`2`$ can change $`Q`$ only when every other tail site is vacant and the transferred spin is up. Consequently the only transition contributing to the commutator is

```math
|a\rangle=|\uparrow,0,\ldots,0\rangle
\quad\longleftrightarrow\quad
|b\rangle=|0,\uparrow,0,\ldots,0\rangle.
```

In this subspace $`Q|a\rangle=0`$ and $`Q|b\rangle=|b\rangle`$. Its Hamiltonian current is therefore

```math
C_Q:=i[H,Q]
=iJ\bigl(|a\rangle\langle b|-|b\rangle\langle a|\bigr).
```

The nonzero eigenvalues are $`+J`$ and $`-J`$. Writing $`C_Q=C_+-C_-`$ for its positive and negative parts gives

```math
\operatorname{Tr}C_+=\operatorname{Tr}C_-=J.
```

For any density matrix $`\rho`$, positivity and $`\rho\leq\|\rho\|_\infty I`$ imply

```math
0\leq\operatorname{Tr}(C_\pm\rho)
\leq J\|\rho\|_\infty.
```

Both numbers lie in the same interval of length $`J\|\rho\|_\infty`$, so their difference satisfies

```math
|\operatorname{Tr}(C_Q\rho)|
\leq J\|\rho\|_\infty.
```

In particular, a factor of two from the full trace norm of $`C_Q`$ is unnecessary.

At every time of continuous evolution,

```math
\frac{d}{dt}\operatorname{Tr}(Q\rho_t)
=\operatorname{Tr}(C_Q\rho_t).
```

The endpoint terms vanish by the first part of the proof. Endpoint pulses produce no jumps in this expectation, so integrating uses the actual elapsed time under the fixed $`H`$.

### Proof: a single-site measurement detects the obstruction

If site $`L`$ is down, then the tail's rightmost occupied spin is down. Thus

```math
R_\downarrow\leq I-Q.
```

Using the initial expectation of $`Q`$ and integrating its current,

```math
\begin{aligned}
p_\downarrow(L,T)
&\leq 1-\operatorname{Tr}(Q\rho_T)\\
&=-\int_0^T\operatorname{Tr}(C_Q\rho_t)\,dt\\
&\leq J\int_0^T\|\rho_t\|_\infty\,dt.
\end{aligned}
```

This proves U1.

For a retained controller $`C`$, replace $`Q`$ by $`Q\otimes I_C`$. Every joint operation on site $`1`$ and $`C`$ fixes this observable in the Heisenberg picture. The current expectation is

```math
\operatorname{Tr}\bigl[(C_Q\otimes I_C)\rho_{SC}(t)\bigr]
=\operatorname{Tr}\bigl[C_Q\rho_t\bigr],
```

so exactly the same proof yields U1 for the reduced state $`\rho_t=\operatorname{Tr}_C\rho_{SC}(t)`$. No assumption of unital reduced maps is needed for this statement.

## U2. Exponential lower bound for unital endpoint control

**Result U2.** Suppose the chain evolves through a sequence of CPTP endpoint maps satisfying $`\mathcal E_k(I_3)=I_3`$, with the fixed bulk Hamiltonian between them. Simultaneous time-dependent endpoint Hamiltonians and unital endpoint Lindblad generators are also allowed. Then

```math
\boxed{
D\!\left(\rho_L(T),\frac{I_3}{3}\right)
\geq \frac13-\frac{JT}{3^{L-1}}.
}
\tag{U2}
```

In particular, for $`0\leq\varepsilon<1/3`$, reaching local error at most $`\varepsilon`$ requires

```math
\boxed{
T\geq\frac{3^{L-1}}{J}
\left(\frac13-\varepsilon\right).
}
\tag{U2a}
```

This is a uniform statement over the specified control class. The protocol may depend on $`L`$, $`T`$, and the known preparation $`\rho_0`$. Its endpoint strengths and pulse count need not obey a size-independent bound.

### Proof

The initial state obeys

```math
0\leq\rho_0\leq\frac{I_{3^L}}{r}.
```

Every bulk unitary and every unital endpoint channel is positive and preserves $`I_{3^L}`$. Their compositions consequently preserve this operator domination. For continuous controls the global generator annihilates $`I_{3^L}`$, so its propagator has the same property. Hence

```math
0\leq\rho_t\leq\frac{I_{3^L}}{r},
\qquad\|\rho_t\|_\infty\leq\frac1r
```

at all times. Result U1 now gives $`p_\downarrow(L,T)\leq JT/r`$.

The binary measurement consisting of the down-spin projector and its complement has down probability $`1/3`$ on $`I_3/3`$. The variational characterization of half trace distance therefore implies

```math
\begin{aligned}
D\!\left(\rho_L(T),\frac{I_3}{3}\right)
&\geq\left|p_\downarrow(L,T)-\frac13\right|\\
&\geq\frac13-p_\downarrow(L,T)\\
&\geq\frac13-\frac{JT}{r}.
\end{aligned}
```

This proves U2 and, by rearrangement, U2a. When the displayed right-hand side becomes negative, the distance bound is simply vacuous.

If $`\Phi_T`$ is the complete chain channel and $`\pi=I_{3^L}/3^L`$, then a full erasure guarantee

```math
\frac12\|\Phi_T-\mathcal R_\pi\|_\diamond\leq\varepsilon
```

implies the local error condition on this particular input by evaluating the channel on $`\rho_0`$ and taking the last-site marginal. Thus U2a also lower-bounds every such uniform erasure protocol. No external reference is needed to exhibit its failure.

### Control scope and physical meaning

The fixed Hamiltonian is the only term that moves population across the two-dimensional current subspace. Increasing the endpoint strength or applying pulses more frequently leaves the current estimate unchanged. The argument is in the physical frame, so changes of frame do not replace $`J`$ by an engineered larger coupling in this inequality.

U2 concerns unital maps of the chain. A sequence of unitaries on the endpoint and a retained pure controller can induce nonunital reduced chain dynamics. Its resources are instead counted by [Result R3](resources.md#r3-finite-controller-resource). Result U1 continues to hold for that reduced trajectory and leads to [the temporary min-entropy requirement](resources.md#r1-temporary-system-nonuniformity).

The underlying connection between ordered spins and edge memory belongs to the established statistical-localization setting of [Rakovszky, Sala, Verresen, Knap, and Pollmann](https://arxiv.org/abs/1910.06341). The control bound is a concrete application of quantum bottleneck reasoning. [Rakovszky, Placke, Breuckmann, and Khemani](https://arxiv.org/html/2412.09598v1), particularly their Theorem 1 and discussion around Eq. (4), already treat bottlenecks and sequences of channels with a common stationary state. Here the fixed physical Hamiltonian, its rank-two current, and the simple local preparation and witness give the explicit constant in U2a. The source relationships are developed in [related work](../references/related_work.md).

The complementary upper bounds use [exact charge transport](charge_transport.md). Their dependence on the permitted filling of the endpoint reservoir is established in [the reservoir threshold](reservoir_threshold.md). That classification uses its own bath-specific input and observable; the preparation and local witness in U1 and U2 remain fixed as defined here.
