# Reservoir filling and erasure time

The stationary vacuum weight determines the leading exponential time needed to erase the ordered spin memory. This page proves both the fixed-filling mixing law and the threshold for time-dependent reservoirs with a prescribed filling floor. The upper bounds control the entire quantum channel, including entangled inputs; the lower bounds use one fully occupied all-up input.

Throughout, the [model](model.md) has the fixed hopping-only Hamiltonian $`H`$ with $`J>0`$, and the reservoir rates are

```math
\alpha=\gamma p,
\qquad\beta=\gamma(1-p),
\qquad0\leq p\leq\frac23.
```

The total injection $`\alpha`$ is divided equally between the two spins. An occupied spin is lost at rate $`\beta`$. For constant parameters, let $`E_{p,t}=e^{t\mathcal L_{H,p}}`$ and

```math
\Pi_p=\bigotimes_{j=1}^L\operatorname{diag}(1-p,p/2,p/2),
\qquad\pi=\Pi_{2/3}=I/3^L.
```

All logarithms are natural except $`\log_2`$ in explicit schedules. Fix an error $`0<\varepsilon<1/2`$ independent of $`L`$ when discussing asymptotic time classes.

## Theorem F1

Define the half-diamond mixing time of the constant reservoir by

```math
t_{\mathrm{mix}}^{\diamond}(\varepsilon;p,L)
=\inf\left\{t\geq0:
\frac12\|E_{p,t}-\mathcal R_{\Pi_p}\|_\diamond\leq\varepsilon\right\}.
```

For every $`0<p\leq2/3`$,

```math
\frac{[1+(1-p)^L]/2-\varepsilon}{\gamma(1-p)^L}
\leq t_{\mathrm{mix}}^{\diamond}(\varepsilon;p,L)
\leq
2T_L(\gamma)
\left\lceil
4(1-p)^{-L}\log\frac{L+1}{\varepsilon}
\right\rceil,
```

where

```math
T_L(\gamma)
=\frac{L(L+1)(L+2)}{6\gamma}
+\frac{\gamma L(L^2-1)}{24J^2}.
```

Consequently, for fixed $`p\in(0,2/3]`$ and fixed $`J,\gamma>0`$,

```math
\boxed{
\lim_{L\to\infty}\frac1L
\log\!\left(\gamma t_{\mathrm{mix}}^{\diamond}(\varepsilon;p,L)\right)
=-\log(1-p).
}
\tag{F1}
```

At the unbiased filling $`p=2/3`$, the leading exponent is $`\log3`$. The theorem determines the exponential rate; its upper and lower polynomial prefactors differ.

### Complete channel upper bound

[Vacuum accessibility](vacuum_accessibility.md) and [complete channel mixing](channel_mixing.md) give, with $`\tau=2T_L(\gamma)`$,

```math
\frac12\|E_{p,n\tau}-\mathcal R_{\Pi_p}\|_\diamond
\leq(L+1)
\exp\!\left[-\frac{n(1-p)^L}{4}\right].
```

Choosing $`n=\left\lceil4(1-p)^{-L}\log[(L+1)/\varepsilon]\right\rceil`$ proves the stated upper bound. In particular,

```math
t_{\mathrm{mix}}^{\diamond}(\varepsilon;p,L)
=O\!\left(L^3(1-p)^{-L}\log\frac{L+1}{\varepsilon}\right)
```

at fixed $`J`$ and $`\gamma`$. The estimate follows from the exact semigroup and is uniform over all physical inputs and reference systems.

### Rightmost-spin obstruction

Prepare

```math
\rho_{\uparrow}=|\uparrow\rangle\langle\uparrow|^{\otimes L}.
```

Let $`P_\uparrow`$ project onto configurations whose rightmost occupied spin in the full chain is up; the vacuum is excluded. Ordered-spin conservation implies $`[H,P_\uparrow]=0`$. Injection changes this projector only when an up spin enters vacuum; loss changes it only when the sole particle is an up spin at site 1. Therefore

```math
\mathcal L_{H,p}^*(P_\uparrow)
=\frac\alpha2P_{\mathrm{vac}}
-\beta|\uparrow0\cdots0\rangle\langle\uparrow0\cdots0|.
```

The reduced charge dynamics of this input is exactly a free-fermion gain/loss evolution. This statement uses the arbitrary-input reduction from [charge transport](charge_transport.md), not the mixed-word lift: injection inserts a first spin letter and summing its two choices gives total gain rate $`\alpha`$, while loss traces the first letter. Tracing the remaining ordered word in every number block yields the charge generator $`-i[H_{\mathrm{ch}},\cdot]+\beta\mathcal D[c_1]+\alpha\mathcal D[c_1^\dagger]`$, with $`H_{\mathrm{ch}}=\sum_{jk}h_{jk}c_j^\dagger c_k`$, even when the physical spin word is polarized or correlated with charge.

The fully occupied charge input is Gaussian with $`C(0)=I`$, so at constant filling

```math
C(t)=pI+(1-p)G_\gamma(t)G_\gamma(t)^\dagger\geq pI.
```

For a gauge-invariant fermionic Gaussian state, the probability that a set of sites is empty is the determinant of the corresponding principal submatrix of $`I-C`$. Thus, writing $`C_{\mathrm{tail}}`$ for sites $`2,\ldots,L`$,

```math
\Pr(\text{sites }2,\ldots,L\text{ empty})
=\det(I_{L-1}-C_{\mathrm{tail}}(t))
\leq(1-p)^{L-1}.
```

Since the sole-up-at-site-1 projector is bounded by the empty-tail projector,

```math
\frac{d}{dt}\operatorname{Tr}(P_\uparrow\rho_t)
\geq-\beta(1-p)^{L-1}
=-\gamma(1-p)^L.
```

The initial expectation is one. Spin symmetry of $`\Pi_p`$ gives

```math
\operatorname{Tr}(P_\uparrow\Pi_p)
=\frac{1-(1-p)^L}{2}.
```

Using the variational characterization of trace distance,

```math
D(\rho_t,\Pi_p)
\geq\operatorname{Tr}\!\left[P_\uparrow(\rho_t-\Pi_p)\right]
\geq\frac{1+(1-p)^L}{2}-\gamma t(1-p)^L.
```

A channel within half-diamond distance $`\varepsilon`$ must in particular bring $`\rho_\uparrow`$ within trace distance $`\varepsilon`$. This proves the lower bound. At fixed $`p`$, the logarithm of the polynomial and logarithmic upper-bound factors is $`o(L)`$, whereas the lower prefactor remains positive because $`\varepsilon<1/2`$. The two bounds therefore give F1.

## Theorem F2

For each chain length, prescribe a filling floor $`p_L\in[0,2/3]`$. Allow arbitrary predetermined, spin-independent gain/loss schedules

```math
0\leq\gamma(t)=\alpha(t)+\beta(t)\leq\Gamma,
\qquad
p(t)=\frac{\alpha(t)}{\alpha(t)+\beta(t)}\in[p_L,2/3]
```

whenever $`\gamma(t)>0`$. At a time with zero total rate, the filling condition is irrelevant. The positive constants $`J`$ and $`\Gamma`$ are independent of $`L`$. The Hamiltonian stays fixed, and the time-dependent generator consists solely of that Hamiltonian and these gain/loss terms. Let $`\Phi_T`$ be its channel at time $`T`$.

A family of such schedules achieves

```math
\frac12\|\Phi_T-\mathcal R_\pi\|_\diamond\leq\varepsilon
```

in time polynomial in $`L`$ if and only if

```math
\boxed{
L\log\frac1{1-p_L}=O(\log L)
\quad\Longleftrightarrow\quad
Lp_L=O(\log L).
}
\tag{F2}
```

The constructive schedule uses a constant reservoir at filling $`p_L`$ followed by a predetermined change to filling $`2/3`$, with a fixed total rate throughout. It erases every input, including correlations with a reference. No knowledge of the input is used to choose the switch time.

### Converse for every allowed schedule

Use the same all-up, fully occupied input and rightmost-spin projector as above. The charge reduction remains exact for time-dependent rates, and Gaussianity is preserved for this specified charge input. Its covariance satisfies

```math
\dot C=A_tC+CA_t^\dagger+\alpha(t)P_1,
\qquad
A_t=-ih-\frac{\gamma(t)}2P_1.
```

Let $`Y=C-p_LI`$. Its equation is

```math
\dot Y=A_tY+YA_t^\dagger
+[\alpha(t)-p_L\gamma(t)]P_1,
\qquad Y(0)=(1-p_L)I.
```

The source is positive because $`\alpha(t)\geq p_L\gamma(t)`$. More explicitly, if $`K(t,s)`$ is the propagator generated by $`A_t`$, then

```math
Y(t)=K(t,0)Y(0)K(t,0)^\dagger
+\int_0^tK(t,s)[\alpha(s)-p_L\gamma(s)]P_1K(t,s)^\dagger\,ds
\geq0.
```

Therefore $`C(t)\geq p_LI`$, and the same determinant bound gives a tail-empty probability at most $`(1-p_L)^{L-1}`$ at every time. Integrating the rightmost-spin flux now yields

```math
D(\rho_T,\pi)
\geq\frac{1+3^{-L}}2
-\left(\int_0^T\beta(t)\,dt\right)(1-p_L)^{L-1}.
```

The target here is the uniform state $`\pi`$, whose vacuum probability is $`3^{-L}`$; it is not the instantaneous stationary state of the scheduled reservoir. Since

```math
\beta(t)=\gamma(t)[1-p(t)]\leq\Gamma(1-p_L),
```

every successful schedule must obey

```math
T\geq
\frac{(1+3^{-L})/2-\varepsilon}{\Gamma}
(1-p_L)^{-L}.
```

For fixed error, a polynomial upper bound on $`T`$ thus requires $`L\log[1/(1-p_L)]=O(\log L)`$. The converse depends only on one allowed input, so it also obstructs the stronger full-channel objective.

### Uniform construction with one reservoir change

First suppose $`p_L>0`$. Choose any fixed $`0<\gamma\leq\Gamma`$ independent of $`L`$ and hold $`p=p_L`$ for

```math
t_d=2T_L(\gamma)
\left\lceil
4(1-p_L)^{-L}\log\frac{2(L+1)}{\varepsilon}
\right\rceil.
```

The complete mixing theorem guarantees

```math
\frac12\|E_{p_L,t_d}-\mathcal R_{\Pi_{p_L}}\|_\diamond
\leq\frac\varepsilon2.
```

Change the filling to $`2/3`$ while retaining the same total rate $`\gamma`$. The known state $`\Pi_{p_L}`$ belongs to the mixed-word Gaussian family. Its charge covariance during this second stage is

```math
C_f(t)=\frac23I+\left(p_L-\frac23\right)
G_\gamma(t)G_\gamma(t)^\dagger.
```

The target charge covariance $`(2/3)I`$ is invariant under any charge-mode basis change. Diagonalizing $`G_\gamma G_\gamma^\dagger`$ therefore makes both charge states products of Bernoulli mode occupations. Coupling each pair of occupations and using the trace-norm-preserving mixed-word lift gives

```math
D(E_{2/3,t}(\Pi_{p_L}),\pi)
\leq\left(\frac23-p_L\right)f_\gamma(t)
\leq\frac23f_\gamma(t).
```

The [charge survival estimate](charge_transport.md), $`f_\gamma(2mT_L)\leq2^{-m}`$, shows that

```math
t_f=2T_L(\gamma)
\left\lceil\log_2\frac{4}{3\varepsilon}\right\rceil
```

adds at most $`\varepsilon/2`$ trace-distance error. Channel contraction and the triangle inequality give

```math
\begin{aligned}
\frac12\|E_{2/3,t_f}E_{p_L,t_d}-\mathcal R_\pi\|_\diamond
&\leq\frac12\|E_{p_L,t_d}-\mathcal R_{\Pi_{p_L}}\|_\diamond
+D(E_{2/3,t_f}(\Pi_{p_L}),\pi)\\
&\leq\varepsilon.
\end{aligned}
```

The equality between a replacement-channel difference's half-diamond norm and the corresponding state trace distance justifies the second term. The first term already accounts for arbitrary reference entanglement.

For $`p_L=0`$, the [ideal drain/refill protocol](erasure_protocol.md) supplies the stronger bound $`O(L^3[1+\log(1/\varepsilon)])`$. For $`p_L=2/3`$, the two reservoir fillings coincide, and a single constant bath suffices.

For general $`0<p_L\leq2/3`$, the construction takes

```math
O\!\left(L^3(1-p_L)^{-L}\log\frac{L+1}{\varepsilon}
+L^3\left[1+\log\frac1\varepsilon\right]\right)
```

time. Thus the necessary condition is also sufficient. Finally, for $`0\leq p\leq2/3`$,

```math
p\leq-\log(1-p)\leq\frac{p}{1-p}\leq3p,
```

which proves the equivalence of the two criteria in F2.

## The resulting time regimes

At a floor $`p_L=c\log L/L`$ with fixed $`c>0`$, the converse is $`L^{c+o(1)}`$ and the constructive upper bound is $`L^{3+c+o(1)}`$ times logarithmic factors. If $`Lp_L/\log L\to\infty`$, every allowed schedule takes superpolynomial time. A fixed positive floor gives exponential time. If the ratio is unbounded but oscillatory, the theorem still excludes a uniform polynomial bound on the family, without asserting monotone asymptotic growth.

The sharp conclusion concerns polynomial versus superpolynomial time and, at fixed filling, the leading exponential rate. It does not identify the optimal polynomial prefactor. The control class in F2 consists of open-loop spin-independent gain/loss schedules in the specified coherent model; arbitrary coherent endpoint controls or measurement-based feedback are different control classes.

The separate [unital control obstruction](control_obstruction.md) applies to every sequence of unital endpoint operations and uses a nearly maximally mixed product input with a local far-end population witness. F1 and F2 use a fully occupied all-up input and the full-chain rightmost-spin projector. The two converses address different comparators, as summarized in the [overview](overview.md).

The implemented upper-bound schedule has a fixed coherent bulk, one controlled endpoint, bounded rates, and at most one reservoir change. Neither the stationary-state reversal in [vacuum accessibility](vacuum_accessibility.md) nor the number twirl in [complete mixing](channel_mixing.md) is implemented. The intermediate target can have exponentially small vacuum weight; no empty-chain event is observed or postselected. The relationship to established boundary-memory, local-control, and classical renewal results is detailed in [related work](../references/related_work.md).
