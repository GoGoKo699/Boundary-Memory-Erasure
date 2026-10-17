# Boundary memory and its erasure

[Model](model.md) · [Repository](../README.md)

A no-passing chain preserves the order of its spin labels. Changing the last label through the opposite boundary requires removing the labels ahead of it. This makes long memory natural, but does not determine how long the memory survives under different boundary controls. The results here identify that dependence for a fixed coherent hopping Hamiltonian.

## Principal conclusions

Fix the model and distance convention in [model.md](model.md). Let $`J`$ and the available boundary rate scale be positive constants independent of $`L`$.

| Conclusion | Exact domain | Authoritative proof |
|---|---|---|
| Exponential local-memory obstruction | Every sequence of unital operations on site 1; one fixed product input; a far-end population witness | [Control obstruction](control_obstruction.md) |
| Universal erasure in $`O(L^3[1+\log(1/\varepsilon)])`$ | Pure particle loss followed once by the unbiased reservoir; arbitrary unknown input and reference | [Erasure protocol](erasure_protocol.md) |
| Mixing exponent $`-\log(1-p)`$ | Constant filling $`0<p\leq2/3`$, fixed $`0<\varepsilon<1/2`$, full coherent channel | [Reservoir threshold](reservoir_threshold.md) |
| Polynomial erasure iff $`Lp_L=O(\log L)`$ | Open-loop spin-independent gain/loss schedules with filling floor $`p_L\in[0,2/3]`$ and bounded rates | [Reservoir threshold](reservoir_threshold.md) |
| Necessary temporary min-entropy reduction and finite-controller cost | The explicitly specified endpoint-map and controller models | [Resources](resources.md) |

The local unital theorem is already witnessed by

```math
\rho_0=(I/3)^{\otimes(L-1)}\otimes
|\uparrow\rangle\langle\uparrow|.
```

For this same input against every unital endpoint protocol, the last-site marginal obeys

```math
D(\rho_L(T),I/3)\geq\frac13-\frac{JT}{3^{L-1}}.
```

At fixed $`0<\varepsilon<1/3`$, local randomization therefore requires time at least $`3^{L-1}(1/3-\varepsilon)/J`$. A one-switch particle-removal protocol reaches the stronger full-channel target in polynomial time. The Hamiltonian, chain, controlled endpoint, and final state are the same in this comparison.

## The filling criterion

For a reservoir with a nonzero fixed filling $`p`$, the exact exponential rate is

```math
\lim_{L\to\infty}\frac1L
\log\!\left(\gamma t_{\mathrm{mix}}^\diamond(\varepsilon;p,L)\right)
=-\log(1-p).
```

The equilibrium empty-chain weight is $`(1-p)^L`$. The mixing time is its inverse up to polynomial and logarithmic factors. The lower and upper estimates establish this statement for the full coherent quantum channel.

If the available reservoir cannot have filling below $`p_L`$, a polynomial-time erasure schedule exists precisely when

```math
L\log\frac1{1-p_L}=O(\log L),
\qquad\text{equivalently}\qquad
Lp_L=O(\log L).
```

The necessary bound covers every allowed time-dependent schedule. The sufficient schedule holds the reservoir at $`p_L`$ long enough to erase input dependence into $`\Pi_{p_L}`$, then switches to $`p=2/3`$. It does not observe an empty-chain event or condition on one. In particular, perfect draining is unnecessary, although a size-independent positive filling floor still gives exponential memory.

## How the proof fits together

The two lower bounds use different preparations and observables. The unital theorem uses the nearly maximally mixed product state above and a local down-population. The filling-floor converse uses the fully occupied all-up state and a projector onto the rightmost occupied spin of the whole chain. [The interpretation](interpretation.md) explains why these domains should be kept distinct.

The upper proof has three physical and mathematical ingredients:

1. The ordered-word representation reduces charge motion to free fermions, and an exact one-particle Lyapunov Gramian bounds survival uniformly in the input. See [charge transport](charge_transport.md).
2. Stationary-state reversal yields the entire vacuum-accessibility effect, including its minimum eigenvalue. This supplies an operator lower bound that holds for every input. See [vacuum accessibility](vacuum_accessibility.md).
3. A covariant-channel argument turns that accessibility into full mixing. A replacement-channel minorization controls the number-diagonal part, while a complete contraction bound controls all nonzero charge differences and arbitrary references. See [channel mixing](channel_mixing.md).

The rank-one vacuum is the common route through which all ordered spin words can be forgotten. The proof uses a number twirl and a reversed Hamiltonian as mathematical devices; the implemented schedule uses neither operation.

## Reading routes

For the connected account, read [model](model.md), [control obstruction](control_obstruction.md), [charge transport](charge_transport.md), [ideal erasure](erasure_protocol.md), [vacuum accessibility](vacuum_accessibility.md), [channel mixing](channel_mixing.md), and [reservoir threshold](reservoir_threshold.md), followed by the [interpretation and worked example](interpretation.md).

The [resource bounds](resources.md) develop the largest-eigenvalue bottleneck into a separate operational consequence. [Related work](../references/related_work.md) identifies established mechanisms and mathematical ingredients. [Verification](../verification/README.md) gives runnable finite checks and their relation to the analytical claims.

For a structured study route, use the [thirty-milestone map](../learning/MILESTONES.md) and the [Rivas–Huelga source bridge](../learning/RIVAS_HUELGA_BRIDGE.md). They connect the open-system foundations to these proofs, with the exact source edition, targeted passages, and notation translations.
