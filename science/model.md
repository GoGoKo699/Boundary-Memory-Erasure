# Model and operational question

[Scientific overview](overview.md) · [Repository](../README.md)

How quickly can control at one end of a quantum chain erase information stored throughout it? The bulk considered here transports particles coherently while preserving their order. A reservoir at the left endpoint can remove the first particle or insert a new first particle. The allowed boundary operation determines whether the distant spin memory survives for exponential time or can be erased in polynomial time.

## Chain and fixed Hamiltonian

There are $`L\geq2`$ sites. Each site has a vacancy $`|0\rangle`$ and two occupied states $`|\uparrow\rangle,|\downarrow\rangle`$. Set $`\hbar=1`$ and fix $`J>0`$. The Hamiltonian is

```math
H=J\sum_{j=1}^{L-1}\sum_{s\in\{\uparrow,\downarrow\}}
\left(|s0\rangle\langle0s|+|0s\rangle\langle s0|\right)_{j,j+1}.
```

An occupied site can exchange with a neighboring vacancy. There is no double occupancy, passing of particles, spin exchange, density interaction, or disorder in this model. If the occupied positions are written in increasing order, the associated spin string is unchanged by $`H`$. This conserved ordered spin word is the memory carrier.

Write

```math
N=\sum_{j=1}^L n_j,
\qquad n_j=|\uparrow\rangle\langle\uparrow|_j+
|\downarrow\rangle\langle\downarrow|_j,
\qquad P_{\mathrm{vac}}=|0\cdots0\rangle\langle0\cdots0|.
```

The Hamiltonian commutes with $`N`$. The zero-particle subspace is one dimensional. No particle-number superselection restriction is placed on the unknown input: number coherences and entanglement with an external reference are allowed.

## Boundary controls

All engineered operations act on site 1. Three control domains appear in the results.

| Domain | Allowed boundary action | Result |
|---|---|---|
| Unital endpoint control | Arbitrary sequences of unital qutrit channels, boundary Hamiltonian pulses, and time-dependent unital boundary generators, with fixed bulk $`H`$ | Exponential lower bound even for one local output population |
| Spin-independent reservoirs | Open-loop particle injection and loss with equal injection probabilities for the two spins | Matching reservoir-filling law and erasure threshold |
| Explicit finite controller | Unital joint operations on site 1 and an independently initialized finite-dimensional controller | A time–controller-nonuniformity bound |

The first domain concerns maps on the system endpoint. Retaining a controller is an additional resource, accounted for in the third domain. The reservoir converse concerns the second domain and does not classify every possible nonunital control.

### Reservoir convention

Let $`a_s=|0\rangle\langle s|_1`$ and

```math
\mathcal D[A](\rho)=A\rho A^\dagger-
\frac12\{A^\dagger A,\rho\}.
```

The reservoir generator is

```math
\mathcal L_{H,p}(\rho)=-i[H,\rho]
+\gamma(1-p)\sum_s\mathcal D[a_s](\rho)
+\frac{\gamma p}{2}\sum_s\mathcal D[a_s^\dagger](\rho),
\qquad 0\leq p\leq\frac23.
```

The loss rate of an occupied spin is $`\beta=\gamma(1-p)`$. The total injection rate into a vacancy is $`\alpha=\gamma p`$, split equally between the spins. Thus $`\gamma=\alpha+\beta`$ is the gain-plus-loss rate scale. The physical injection coefficient of each spin is $`\alpha/2`$.

For each constant $`p`$, the stationary state is

```math
\Pi_p=\bigotimes_{j=1}^{L}\mathrm{diag}(1-p,p/2,p/2).
```

Local balance gives $`\beta(p/2)=(\alpha/2)(1-p)`$, and configurations linked by $`H`$ have the same stationary weight. Therefore $`\mathcal L_{H,p}(\Pi_p)=0`$. Uniqueness and quantitative convergence follow from the channel bounds proved below; they are not extra mixing assumptions.

At $`p=0`$, the bath only removes particles. At $`p=2/3`$, all three local states have equal stationary weight and the generator is unital. The erasure target is

```math
\pi=\Pi_{2/3}=\frac{I}{3^L}.
```

The constructive protocols keep a fixed $`\gamma>0`$ while switching $`p`$ once. Both $`J`$ and $`\gamma`$ are independent of $`L`$. The filling-floor converse permits time-dependent $`\alpha(t),\beta(t)\geq0`$ subject to $`\gamma(t)=\alpha(t)+\beta(t)\leq\Gamma`$, with fixed $`\Gamma>0`$ independent of $`L`$. When $`\gamma(t)>0`$, the allowed filling satisfies $`p(t)=\alpha(t)/\gamma(t)\geq p_L`$. Intervals with both rates zero do not require a filling assignment. These schedules are predetermined, with no measurement or feedback.

The reservoir filling is a control parameter, not an assumption that the evolving chain remains at that filling. The positive covariance bound in [the filling-floor converse](reservoir_threshold.md) is derived from the selected initial state and the dynamics.

## Information erasure and distances

For states, use half trace distance,

```math
D(\rho,\sigma)=\frac12\|\rho-\sigma\|_1.
```

Let $`\mathcal R_\sigma(X)=\sigma\mathrm{Tr}X`$ denote replacement by $`\sigma`$. A protocol $`\Phi_T`$ erases with error at most $`\varepsilon`$ if

```math
\frac12\|\Phi_T-\mathcal R_\pi\|_\diamond\leq\varepsilon.
```

Equivalently, for every system–reference input $`\rho_{SR}`$, the output is within $`\varepsilon`$ of $`\pi\otimes\rho_R`$ in half trace distance. The reference can be taken to have dimension $`3^L`$. This is stronger than convergence of a chosen observable or of number-diagonal initial states.

For the constant-$`p`$ semigroup $`E_{p,t}=\exp(t\mathcal L_{H,p})`$, define

```math
t_{\mathrm{mix}}^\diamond(\varepsilon;p,L)
=\inf\left\{t\geq0:
\frac12\|E_{p,t}-\mathcal R_{\Pi_p}\|_\diamond\leq\varepsilon
\right\}.
```

The full-channel lower bounds follow from particular system inputs and observables. The upper bounds must control every input and reference. All logarithms are natural unless a base is displayed. Fixed-accuracy comparisons take $`\varepsilon`$ independent of $`L`$; the local unital bound requires $`0<\varepsilon<1/3`$, while the filling converse holds for $`0<\varepsilon<1/2`$.

## Physical interpretation

The target is a completely mixed chain with no retained information about the input. Particle removal prepares a useful intermediate state, after which the unbiased reservoir supplies fresh spin labels. The vacuum is a zero-particle state, not generally an energy ground state of $`H`$. The results quantify information erasure, filling, physical time, and the explicitly defined nonuniformity resources. They do not identify an energy, heat, or work cost.

Continue with the [control obstruction](control_obstruction.md), the [charge transport estimate](charge_transport.md), or the [complete result map](overview.md).
