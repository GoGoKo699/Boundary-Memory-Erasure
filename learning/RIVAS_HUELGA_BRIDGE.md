# From open quantum systems to boundary memory erasure

[Repository](../README.md) · [Thirty milestones](MILESTONES.md) · [Scientific overview](../science/overview.md) · [Model](../science/model.md)

One controlled endpoint can erase the whole chain, but the available reservoir determines the time required. The learning problem is to connect a local master equation to a statement about every unknown quantum input, including its correlations with a reference. This bridge develops that connection in the notation of the project. The complete proofs remain in their linked scientific pages.

The sole educational anchor is **Ángel Rivas and Susana F. Huelga, _Open Quantum Systems: An Introduction_**, first edition, copyright 2012, [DOI 10.1007/978-3-642-23354-8](https://doi.org/10.1007/978-3-642-23354-8). Source pointers below use the corrected author preprint [arXiv:1104.5242v2, 9 February 2012](https://arxiv.org/abs/1104.5242v2). All page numbers are its **printed pages**, not the publisher's pagination.

The [milestone map](MILESTONES.md) has 13 background milestones and 17 narrative milestones. Its order follows the project's dependencies. The source provides targeted foundations; reading the entire book is not a prerequisite.

## Targeted source route

| Passage in the selected preprint | Foundation to bring into the project | Milestones |
|---|---|---|
| [2.1, pp. 4–5](https://arxiv.org/pdf/1104.5242v2#page=4) | Norms and operator estimates | M01, M07, M10 |
| [2.3, pp. 8–10](https://arxiv.org/pdf/1104.5242v2#page=8); [2.4, pp. 14–18](https://arxiv.org/pdf/1104.5242v2#page=14) | Semigroups and changing generators | M04, M10, M17, M25 |
| [4.1, pp. 24–25, Theorem 4.1](https://arxiv.org/pdf/1104.5242v2#page=24) | A pure marginal and product structure | M06, M18 |
| [4.2, pp. 26–29, Eqs. (35)–(36), Theorem 4.3](https://arxiv.org/pdf/1104.5242v2#page=26) | Kraus maps, complete positivity, and references | M02, M06, M12 |
| [4.3, pp. 29–30, Theorem 4.4](https://arxiv.org/pdf/1104.5242v2#page=29) | Trace-norm contraction | M12, M18–M19 |
| [4.5, p. 35, Definition 4.1](https://arxiv.org/pdf/1104.5242v2#page=35); [5.2, pp. 37–41, Eqs. (46), (51)](https://arxiv.org/pdf/1104.5242v2#page=37) | Divisible dynamics and GKSL generators | M04–M05 |
| [5.4, pp. 45–48](https://arxiv.org/pdf/1104.5242v2#page=45) | Stationarity and relaxation | M05, M10, M13 |

The specialized charge reduction, Gramian, vacuum-effect spectrum, complete mixing bound, and resource identities are developed in this repository. Each milestone points to the corresponding derivation. The [related-work account](../references/related_work.md) retains primary research attribution; those sources serve a different purpose from the single educational anchor.

## Notation and physical assumptions

Keep the space on which an object acts visible. A small matrix controlling charge motion and a channel acting on the chain answer different questions.

| Project notation | Meaning and convention |
|---|---|
| $`L`$, $`d=3^L`$, $`N`$ | Number of sites, system dimension, and particle-number operator, respectively |
| $`H`$, $`h`$ | Full constrained hopping Hamiltonian and its one-particle hopping matrix |
| $`\mathcal L`$, $`\mathcal L^*`$ | State generator and observable adjoint, defined by trace pairing |
| $`A_\gamma=-ih-\gamma P_1/2`$ | One-particle drift; $`P_1=\lvert1\rangle\langle1\rvert`$ acts on the position space |
| $`\alpha,\beta,\gamma`$ | Total charge injection, occupied-spin loss, and $`\gamma=\alpha+\beta`$ |
| $`p=\alpha/\gamma`$ | Controlled reservoir filling when $`\gamma>0`$ |
| $`D(\rho,\sigma)=\lVert\rho-\sigma\rVert_1/2`$ | Half trace distance; channel errors likewise use half diamond distance |
| $`\Pi_p`$, $`\pi`$ | Stationary state at filling $`p`$, and final target $`\pi=I/3^L`$ |

The book's symbols for dimension, microscopic coupling, inverse temperature, and spectral density need not have these meanings. In particular, the project's $`\alpha`$ and $`\beta`$ are rates, and $`J`$ is the hopping amplitude.

The [model](../science/model.md) stipulates an engineered finite-dimensional GKSL reservoir. The mathematical results apply to that generator. A microscopic bath derivation is a separate physical question; relevant context is in [6.2, pp. 56–73](https://arxiv.org/pdf/1104.5242v2#page=56) and [6.4.1, pp. 77–80](https://arxiv.org/pdf/1104.5242v2#page=77). The product state $`\Pi_p`$ is not assigned a bath temperature, and particle removal is not identified with ground-state cooling or a heat cost.

## From a physical channel to universal erasure

**Milestones M01–M02 and M06.** A prescribed protocol defines one linear CPTP map $`\Phi_T`$. Its environment is initially independent of the entire system–reference input. This allows arbitrary entanglement inside $`\rho_{SR}`$ while keeping the same physical map for every input.

The source's universal dynamical map terminology concerns this input-independent physical validity. The project's universal erasure condition adds the requirement

```math
\frac12\|\Phi_T-\mathcal R_\pi\|_\diamond\leq\varepsilon,
\qquad
\mathcal R_\pi(X)=\pi\,\mathrm{Tr}X.
```

For every joint input, the desired output is $`\pi\otimes\rho_R`$. The reference marginal is preserved; all dependence of the system on the unknown input is removed to the stated error. A reference of dimension $`d`$ suffices in the diamond-norm supremum.

The two directions of a proof have different demands. One input and one output measurement can disprove erasure. To establish erasure, an upper bound must hold for all joint inputs. This is why the [local obstruction](../science/control_obstruction.md) can use one last-site population, while the [erasure protocol](../science/erasure_protocol.md) needs an explicit reference-decoupling argument.

## From the generator to the stationary family

**Milestones M03–M05.** Each site has states $`0,\uparrow,\downarrow`$. Hopping exchanges an occupied site with an adjacent vacancy. Since particles cannot pass or exchange spin labels, their ordered spin word is preserved by $`H`$.

Let $`a_s=|0\rangle\langle s|_1`$ and define

```math
\mathcal D[A](\rho)=A\rho A^\dagger-\frac12\{A^\dagger A,\rho\}.
```

In the project's rate convention,

```math
\mathcal L_{H,p}(\rho)
=-i[H,\rho]
+\beta\sum_s\mathcal D[a_s](\rho)
+\frac{\alpha}{2}\sum_s\mathcal D[a_s^\dagger](\rho),
\qquad
\alpha=\gamma p,\quad \beta=\gamma(1-p).
```

For a fixed reservoir, $`0\leq p\leq2/3`$ and $`\gamma>0`$. The hopping amplitude and constructive rate scale are positive constants independent of chain length.

The factor $`1/2`$ in the injection coefficient divides total gain between two spins. It is separate from the anticommutator's $`1/2`$. Absorbing the rates into jump operators gives $`\sqrt\beta\,a_s`$ and $`\sqrt{\alpha/2}\,a_s^\dagger`$.

The balance equation

```math
\beta\frac p2=\frac\alpha2(1-p)
```

gives the local stationary weights. Configurations connected by hopping have the same product weight, so

```math
\Pi_p=\bigotimes_{j=1}^L\mathrm{diag}(1-p,p/2,p/2),
\qquad
\mathcal L_{H,p}(\Pi_p)=0.
```

At $`p=0`$, the stationary state is vacuum. At $`p=2/3`$, it is the identity divided by dimension and the generator is unital. These calculations identify stationary states; the later transport and channel estimates provide the quantitative convergence needed here.

A fixed reservoir gives $`E_{p,t}=e^{t\mathcal L_{H,p}}`$. A changing reservoir gives a two-parameter propagator with

```math
\Phi_{t,s}=\Phi_{t,r}\Phi_{r,s},
\qquad
\partial_t\Phi_{t,s}=\mathcal L_t\Phi_{t,s}.
```

A one-switch schedule is an exact composition of two semigroups. Bounded measurable schedules satisfy the corresponding integral equation, with derivatives almost everywhere. No derivative at a switching time is needed.

**Source time-argument note.** In [Theorem 2.6, printed p. 15](https://arxiv.org/pdf/1104.5242v2#page=15), the lower-end derivative needs $`\mathcal L_s`$: $`\partial_s\Phi_{t,s}=-\Phi_{t,s}\mathcal L_s`$. This follows by expanding $`\Phi_{s+h,s}=I+h\mathcal L_s+o(h)`$ in the composition law. The forward equation above has the time argument used throughout this project.

## From locality to an exponential memory obstruction

**Milestones M07 and M14–M15.** Consider the input

```math
\rho_0=(I/3)^{\otimes(L-1)}
\otimes|\uparrow\rangle\langle\uparrow|,
\qquad r=3^{L-1}.
```

The useful witness $`Q`$ has the identity on site 1 and projects onto configurations whose rightmost occupied site in the tail $`2,\ldots,L`$ has spin up. The empty tail contributes zero. Every trace-preserving endpoint operation fixes $`Q`$ in the adjoint picture, because its endpoint factor is the identity.

Only one hopping pair changes this tail property: a lone up spin moves between sites 1 and 2 while the remaining tail is empty. Consequently $`i[H,Q]`$ has two nonzero eigenvalues, $`+J`$ and $`-J`$. Combining this current with the inclusion of the last-site down event gives

```math
D(\rho_L(T),I/3)
\geq\frac13-J\int_0^T\|\rho_t\|_\infty\,dt.
```

This is [U1](../science/control_obstruction.md#u1-bottleneck-inequality), valid for the stated endpoint control setting. It shows why a largest eigenvalue enters the memory question: probability must pass through a current of fixed rank.

For unital endpoint system evolution, positivity preserves $`\rho_t\leq I/r`$. Thus [U2](../science/control_obstruction.md#u2-exponential-lower-bound-for-unital-endpoint-control) yields

```math
D(\rho_L(T),I/3)\geq\frac13-\frac{JT}{r}.
```

Strong endpoint operations cannot change the current's bulk scale $`J`$. The resulting lower bound counts physical time and applies to the whole stated unital system-control class. A retained controller has its own model and resource bound in M29.

## From the spinful chain to exact charge motion

**Milestones M08–M09 and M16.** Within a fixed particle-number sector, a configuration is specified by its ordered positions and spin word. This gives

```math
\mathcal H
\cong\bigoplus_{m=0}^L
\left(\bigwedge^m\mathbb C^L\right)
\otimes(\mathbb C^2)^{\otimes m}.
```

The [charge reduction T1](../science/charge_transport.md#t1-exact-charge-reduction) first takes the number-diagonal part and then traces out the word. The resulting CPTP map intertwines the physical generator with a free-fermion charge generator having gain $`\alpha`$ and loss $`\beta`$. This identity holds for arbitrary physical inputs, including spin–charge correlations and number coherences; the number pinch is a mathematical part of the reduction.

A different statement concerns reconstruction. The lift

```math
\mathcal V(\sigma)
=\bigoplus_{m=0}^L\sigma_m\otimes
\frac{I_{2^m}}{2^m}
```

is invariant under the dynamics and preserves trace distance on its number-diagonal charge inputs. It describes states whose spin words are maximally mixed within each sector. It does not reconstruct an arbitrary physical state from its charge marginal.

For the charge covariance $`C_{jk}=\mathrm{Tr}(\sigma c_k^\dagger c_j)`$,

```math
\dot C=A_tC+CA_t^\dagger+\alpha(t)P_1,
\qquad
A_t=-ih-\frac{\gamma(t)}2P_1,
\qquad 0\leq C\leq I.
```

This closed equation holds without a Gaussian assumption. Gaussian charge states additionally permit higher correlations to be recovered from $`C`$, including an empty-region probability $`\det(I-C_{\mathrm{region}})`$. The proofs invoke that determinant for known Gaussian inputs, while arbitrary-input survival uses only $`C\leq I`$.

## From relaxation to a uniform survival time

**Milestones M10 and M17.** With fixed $`\gamma>0`$, write $`G(t)=e^{tA_\gamma}`$. The full Liouvillian acts on the chain; $`A_\gamma`$ acts on its one-particle position space. The latter is Hurwitz, so the Gramian

```math
X=\int_0^\infty G(t)^\dagger G(t)\,dt,
\qquad
A_\gamma^\dagger X+XA_\gamma=-I
```

exists. [T2](../science/charge_transport.md#t2-exact-gramian-and-a-uniform-survival-estimate) solves this equation entry by entry and obtains

```math
T_L=\mathrm{Tr}X
=\frac{L(L+1)(L+2)}{6\gamma}
+\frac{\gamma L(L^2-1)}{24J^2}.
```

At fixed positive $`J,\gamma`$, this is a cubic time scale. Let $`f_\gamma(t)=\mathrm{Tr}(G^\dagger G)`$. Its monotonicity, integral $`T_L`$, and semigroup contraction imply

```math
f_\gamma(2mT_L)\leq2^{-m},
\qquad m=1,2,\ldots.
```

This estimate includes a controlled transient and explicit dependence on $`L`$. Qualitative relaxation or the sign of spectral real parts would not supply those constants. The [two-site calculation](../science/interpretation.md#a-two-site-calculation) gives $`T_2=4/\gamma+\gamma/(4J^2)`$, making the construction directly checkable.

## From vacuum preparation to erasure with a reference

**Milestones M18–M19.** During pure loss, the expected number of particles in any input is at most $`f_\gamma(t)`$. Since any nonvacuum state contains at least one particle, its nonvacuum probability $`u`$ is no larger.

For a joint output $`\omega_{SR}`$, projection onto vacuum has the form

```math
(P_{\mathrm{vac}}\otimes I)\omega_{SR}
(P_{\mathrm{vac}}\otimes I)
=P_{\mathrm{vac}}\otimes\tau_R,
\qquad
\mathrm{Tr}\tau_R=1-u.
```

The zero-particle system space is one dimensional. Gentle projection controls the change in the joint state, and $`\rho_R-\tau_R\geq0`$ has trace $`u`$. Together these give the [reference estimate](../science/erasure_protocol.md#draining-also-decouples-the-reference)

```math
D(\omega_{SR},P_{\mathrm{vac}}\otimes\rho_R)
\leq\sqrt u+\frac u2
\leq\frac32\sqrt u.
```

This argument turns an arbitrary-input particle bound into a uniform channel bound.

Refilling starts from known vacuum, which belongs to the invariant mixed-word Gaussian family. At filling $`2/3`$, the charge covariance approaches $`(2/3)I`$. Coupling its independent mode occupations to their stationary values gives

```math
D(E_{2/3,t}(P_{\mathrm{vac}}),\pi)
\leq\frac23 f_\gamma(t).
```

Contractivity propagates the drain error through refill. The total error is therefore at most

```math
\frac32\sqrt{f_\gamma(t_d)}
+\frac23 f_\gamma(t_f).
```

[E1](../science/erasure_protocol.md#composition-and-the-explicit-schedule) allocates these errors explicitly and obtains $`O(L^3[1+\log(1/\varepsilon)])`$ time with one predetermined reservoir change. The final replacement target preserves the identity, while the protocol passes through a nonuniform intermediate state.

## From a known state to the full vacuum effect

**Milestones M11 and M20–M21.** With positive filling, the chain need not become close to vacuum. The useful question becomes: does every input have a controlled chance of being found there after a fixed interval?

For $`p>0`$, the full-rank stationary state defines $`\Gamma_p(O)=\Pi_p^{1/2}O\Pi_p^{1/2}`$. Checking the physical gain and loss coefficients gives

```math
\mathcal L_{H,p}^*
=\Gamma_p^{-1}\mathcal L_{-H,p}\Gamma_p.
```

This [weighted reversal](../science/vacuum_accessibility.md#stationary-state-reversal) relates the evolved vacuum effect to the reverse evolution of known vacuum. The auxiliary sign $`-H`$ belongs to the proof; the implemented protocol keeps $`H`$.

The reverse vacuum state has Gaussian charge covariance $`p(I-G^\dagger G)`$. If $`\eta_j`$ are the eigenvalues of $`G^\dagger G`$, the corresponding physical vacuum-effect eigenvalues are

```math
\prod_{j\notin M}(1-p+p\eta_j)
\prod_{j\in M}(1-p)(1-\eta_j).
```

The [spectrum calculation](../science/vacuum_accessibility.md#spectrum-of-the-vacuum-effect) includes the spin multiplicities. Occupying a charge mode gives the smaller factor, so the minimum occurs when every mode is occupied:

```math
\lambda_{\min}\!\left(E_{p,t}^*(P_{\mathrm{vac}})\right)
=(1-p)^L\det(I-G^\dagger G).
```

At $`t=2T_L`$, the survival trace is at most $`1/2`$. Hence the determinant is at least $`1/2`$ and

```math
E_{p,2T_L}^*(P_{\mathrm{vac}})\geq qI,
\qquad q=\frac{(1-p)^L}{2}.
```

A Gaussian calculation for one known state has now produced an operator inequality on the entire physical Hilbert space. This is the bridge to arbitrary coherent inputs.

## From vacuum accessibility to complete mixing

**Milestones M09, M12, and M22–M23.** The [mixing theorem M1](../science/channel_mixing.md#theorem-m1) uses number covariance, a one-dimensional vacuum sector, and the effect bound above. Write $`E=E_{p,2T_L}`$ and let $`\mathcal D_N`$ be number twirling.

For the number-diagonal component, $`F=E\mathcal D_N`$ has block-diagonal output. Its vacuum block is a rank-one output map. The effect inequality then yields a genuine CP decomposition

```math
F=q\mathcal R_{\mathrm{vac}}+(1-q)S
```

with $`S`$ CPTP. This is stronger than knowing a scalar probability for each input. On differences with zero system partial trace, the replacement term vanishes even in the presence of a reference, giving contraction by $`1-q`$ per interval.

The actual input can also contain coherences between distinct particle numbers. Decompose these into charge differences $`k=-L,\ldots,L`$. For a nonzero difference, either $`X^\dagger X`$ or $`XX^\dagger`$ has no vacuum support. The unital CP adjoint and Kadison–Schwarz then give a complete operator-norm contraction factor $`\sqrt{1-q}`$. The proof applies after adjoining every reference dimension.

Combining the number-diagonal component and the $`2L`$ nonzero Fourier components gives

```math
\frac12\|E^n-\mathcal R_{\Pi_p}\|_\diamond
\leq(1-q)^n+L(1-q)^{n/2}
\leq(L+1)e^{-qn/2},
\qquad n\geq1.
```

The twirl organizes the proof. No number measurement, physical dephasing, postselection, or feedback is inserted into the bath schedule. The [separate complete-contraction argument](../science/channel_mixing.md#coherences-with-nonzero-charge-difference) is what makes the population calculation sufficient for the full quantum task.

## From the vacuum weight to the filling threshold

**Milestones M24–M26.** The complete upper bound contains the inverse stationary vacuum weight $`(1-p)^{-L}`$. To test whether that exponential factor is necessary, [F1](../science/reservoir_threshold.md#theorem-f1) uses a fully occupied all-up input. Its initial charge covariance is $`I`$ and stays Gaussian with $`C(t)\geq pI`$. The probability that the tail is empty is at most $`(1-p)^{L-1}`$.

Here the memory observable is the **full-chain** rightmost-spin-up projector. It differs from the tail projector $`Q`$ in U1, and the input differs from the nearly mixed input in U2. The boundary can change this full-chain label only through a state with an empty tail. Integrating that limited flux gives a lower bound with the same exponential weight as the upper bound:

```math
\lim_{L\to\infty}\frac1L
\log\!\left(\gamma t_{\mathrm{mix}}^\diamond(\varepsilon;p,L)\right)
=-\log(1-p)
```

for fixed $`0<p\leq2/3`$, fixed positive $`J,\gamma`$, and fixed $`0<\varepsilon<1/2`$. This concerns convergence to the bath's own $`\Pi_p`$.

The final-target question fixes the same $`H`$ and $`J>0`$, and allows time-dependent rates with $`0\leq\gamma(t)\leq\Gamma`$, where $`\Gamma>0`$ is independent of $`L`$. Whenever $`\gamma(t)>0`$, the filling obeys $`0\leq p_L\leq p(t)\leq2/3`$; intervals with both rates zero need no filling assignment. For the same all-up input, set $`Y=C-p_LI`$. Its equation is

```math
\dot Y=A_tY+YA_t^\dagger+
[\alpha(t)-p_L\gamma(t)]P_1.
```

Both its initial value and source are positive, so $`C(t)\geq p_LI`$. The [floor converse](../science/reservoir_threshold.md#converse-for-every-allowed-schedule) integrates the resulting rightmost-spin flux and gives

```math
T\geq
\frac{(1+3^{-L})/2-\varepsilon}{\Gamma}
(1-p_L)^{-L}.
```

This bound covers every allowed predetermined schedule. The filling floor constrains the generator; the covariance floor is a conclusion about this particular input's dynamics.

For the converse construction, hold the reservoir at $`p_L>0`$ until M1 erases every input into $`\Pi_{p_L}`$, then change once to $`p=2/3`$ and refill. When $`p_L=0`$, use E1. Since $`p\leq-\log(1-p)\leq3p`$ on the permitted interval, [F2](../science/reservoir_threshold.md#theorem-f2) gives

```math
\text{Polynomial-time erasure exists}
\quad\Longleftrightarrow\quad
L\log\frac1{1-p_L}=O(\log L)
\quad\Longleftrightarrow\quad
Lp_L=O(\log L).
```

For $`p_L=c\log L/L`$, the converse is of order $`L^c`$ and the construction is at most of order $`L^{3+c}`$ times logarithmic factors. The threshold is sharp; the optimal polynomial prefactor is not determined. If $`Lp_L/\log L`$ tends to infinity, the lower bound is eventually superpolynomial. An unbounded oscillatory ratio instead excludes a single polynomial bound uniform in $`L`$. The [filling-regime examples](../science/interpretation.md#filling-regimes) make these quantifiers explicit.

## From fast control to a counted nonuniformity resource

**Milestones M27–M29.** Return to U1 and put $`\delta=1/3-\varepsilon>0`$. Any protocol that achieves the local target must satisfy

```math
\sup_{0\leq t\leq T}\|\rho_t\|_\infty
\geq\frac{\delta}{JT},
\qquad
\inf_{0\leq t\leq T}H_{\min}(\rho_t)
\leq\log\frac{JT}{\delta}.
```

At polynomial time, this requires an extensive decrease from the initial min-entropy $`\log r`$, equivalently an extensive increase over the initial deficit $`\log3`$. It constrains the largest eigenvalue. A spectrum can have this concentration while its von Neumann entropy remains near maximal; [R1's example](../science/resources.md#the-spectral-meaning-of-the-bound) establishes that distinction without claiming the example is reachable.

If the environment or retained memory starts independently, each actual prefix is a CPTP system map $`\Phi_t`$. Applying it to $`\rho_0\leq I/r`$ gives

```math
\sup_{t\leq T}\log\|\Phi_t(I)\|_\infty
\geq\log r-\log\frac{JT}{\delta}.
```

For a specified **memoryless** sequence of endpoint channels, [R2](../science/resources.md#r2-accumulated-channel-budget) counts

```math
b(\mathcal E)=\log\|\mathcal E(I)\|_\infty,
\qquad
\sum_k b(\mathcal E_k)
\geq\log r-\log\frac{JT}{\delta}.
```

The [resource identity](../science/resources.md#exact-relation-to-channel-max-relative-entropy) equates this quantity with the channel's complete increasing power for min-entropy deficit and its minimum CP-order max-relative-entropy distance to unital channels. The accumulated sum is a necessary budget for that implementation, and can exceed the actual nonuniformity produced by its prefixes. The [continuous envelope](../science/resources.md#continuous-endpoint-generators) uses $`\lambda_{\max}(\mathcal L_{1,t}(I))`$; for the stated bath this is $`\gamma(t)[2-3p(t)]`$.

A retained controller changes the accounting. Under the independently initialized finite-controller model, with dimension $`K`$, initial state $`\sigma_C`$, and unital joint endpoint–controller operations, [R3](../science/resources.md#r3-finite-controller-resource) gives

```math
TK\|\sigma_C\|_\infty
\geq\frac{r\delta}{J}.
```

A maximally mixed controller has $`K\|\sigma_C\|_\infty=1`$, so increasing its dimension alone does not weaken this bound. A pure controller has factor $`K`$ and supplies a counted initial nonuniformity. These are spectral and operational resource statements within their stated control models.

## Reassemble the complete argument

**Milestones M13 and M30.** The [scientific overview](../science/overview.md) assembles the theorem dependencies. The [interpretation](../science/interpretation.md) connects them to the physical mechanism and worked examples. The same fixed Hamiltonian supports exponentially persistent memory under unital endpoint system control and polynomial universal erasure when the reservoir can become sufficiently dilute.

The construction requires both transport and information estimates. Exact charge motion supplies a cubic survival scale. Weighted reversal turns known Gaussian evolution into a universal vacuum-effect bound. Complete positivity and number covariance then control every quantum coherence and reference extension. The matching flux obstruction identifies precisely when a reservoir filling floor defeats polynomial erasure.

The [related-work account](../references/related_work.md#the-complete-relationship) identifies established ingredients and the particular relationship proved here. The [verification guide](../verification/README.md) states the finite domains checked by the scripts. Those checks support the algebraic bookkeeping; the linked scientific proofs establish the arbitrary-input, arbitrary-reference, and asymptotic claims.

Continue through the [thirty-milestone map](MILESTONES.md), or go directly to the [exact model and control domains](../science/model.md#boundary-controls).
