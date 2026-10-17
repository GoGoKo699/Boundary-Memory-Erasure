# Universal erasure by draining and refilling

One predetermined change of the endpoint reservoir prepares the maximally mixed chain from every quantum input. The first stage removes particles and makes the system approximately vacuum, which also removes its correlations with an external reference. The second stage fills that known state with an unbiased reservoir.

The precise [model and rate convention](model.md) are

$$
\mathcal L_{H,p}
=-i[H,\cdot]
+\gamma(1-p)\sum_s\mathcal D[a_s]
+\frac{\gamma p}{2}\sum_s\mathcal D[a_s^\dagger],
\qquad
E_{p,t}=e^{t\mathcal L_{H,p}}.
\tag{E1.1}
$$

The Hamiltonian $H$, addressed site, and total rate $\gamma>0$ remain fixed. Write $P_{\mathrm{vac}}=|\mathrm{vac}\rangle\langle\mathrm{vac}|$ and $\pi=I/3^L=\Pi_{2/3}$. The replacement channel is $\mathcal R_\pi(X)=\pi\operatorname{Tr}X$, and the error is one half of the diamond norm.

Local relaxation as a route to controlling a larger system is established by [Burgarth and Giovannetti](https://arxiv.org/pdf/0710.0302). Continuous endpoint loss and the inverse-cubic single-excitation relaxation scale have a close precedent in [Beer and Burgarth](https://arxiv.org/html/2609.23960v1). The proof here uses the exact charge reduction and Gramian to give an explicit uniform bound for this reservoir protocol. Its place in the control comparison is described in [Related work](../references/related_work.md) and the [scientific overview](overview.md).

## E1. Ideal erasure theorem

For $L\geq2$, fixed $J,\gamma>0$, and $0<\varepsilon<1$, define

$$
T_L(\gamma)
=\frac{L(L+1)(L+2)}{6\gamma}
+\frac{\gamma L(L^2-1)}{24J^2},
\tag{E1.2}
$$

and choose the predetermined times

$$
\begin{aligned}
t_{\mathrm d}
&=2T_L(\gamma)
\left\lceil\log_2\frac9{\varepsilon^2}\right\rceil,\\
t_{\mathrm f}
&=2T_L(\gamma)
\left\lceil\log_2\frac4{3\varepsilon}\right\rceil.
\end{aligned}
\tag{E1.3}
$$

Run the pure-loss bath $p=0$ for $t_{\mathrm d}$, then the unbiased bath $p=2/3$ for $t_{\mathrm f}$. The resulting channel

$$
\Phi=E_{2/3,t_{\mathrm f}}E_{0,t_{\mathrm d}}
\tag{E1.4}
$$

satisfies

$$
\frac12\|\Phi-\mathcal R_\pi\|_\diamond\leq\varepsilon.
\tag{E1.5}
$$

The total time is

$$
t_{\mathrm d}+t_{\mathrm f}
=O\!\left(L^3[1+\log(1/\varepsilon)]\right),
\tag{E1.6}
$$

where the implicit constant depends only on the fixed $J$ and $\gamma$. At fixed accuracy this is $O(L^3)$. The guarantee holds for every initial system state and every entanglement with an idle reference.

The loss rate of an occupied spin is $\gamma$ during the drain. During refill it is $\gamma/3$, and the injection rate of each spin is $\gamma/3$. Thus the total charge injection rate during refill is $2\gamma/3$, while loss plus total injection remains $\gamma$ in both stages.

## Draining also decouples the reference

Let $\rho_{SR}$ be any input, with no assumption on the dimension or state of the reference $R$, and let

$$
\omega_{SR}
=(E_{0,t}\otimes\operatorname{id}_R)(\rho_{SR}),
\qquad
P=P_{\mathrm{vac}}\otimes I_R.
$$

The reference marginal is unchanged: $\omega_R=\rho_R$. By T1 in [Exact charge transport](charge_transport.md), the failure probability

$$
u=1-\operatorname{Tr}(P\omega_{SR})
\leq\langle N(t)\rangle
\leq f_\gamma(t),
\qquad
f_\gamma(t)=\operatorname{Tr}\!\left(G_\gamma(t)^\dagger G_\gamma(t)\right),
\tag{E1.7}
$$

is uniform over $\rho_{SR}$. This bound uses only the system marginal and the operator inequality $I-P_{\mathrm{vac}}\leq N$.

Because the system vacuum has rank one, there is a positive, subnormalized operator $\tau_R$ such that

$$
P\omega_{SR}P=P_{\mathrm{vac}}\otimes\tau_R,
\qquad
\operatorname{Tr}\tau_R=1-u.
\tag{E1.8}
$$

Gentle projection gives

$$
\|\omega_{SR}-P\omega_{SR}P\|_1\leq2\sqrt u.
\tag{E1.9}
$$

For completeness, this estimate follows by purifying $\omega_{SR}$, projecting that purification with $P$, and using trace-norm contraction under the purifying partial trace. For a pure vector with projection failure $u$, the norm of the difference between the original rank-one operator and its subnormalized projection is $\sqrt{u(4-3u)}\leq2\sqrt u$.

The cross terms between vacuum and nonvacuum vanish under the system partial trace. Hence

$$
\omega_R-\tau_R
=\operatorname{Tr}_S\!\left[(I-P)\omega_{SR}(I-P)\right]
\geq0,
\qquad
\|\omega_R-\tau_R\|_1=u.
\tag{E1.10}
$$

Combining (E1.8)–(E1.10) gives

$$
\begin{aligned}
D\!\left(\omega_{SR},P_{\mathrm{vac}}\otimes\rho_R\right)
&\leq\frac12\|\omega_{SR}-P\omega_{SR}P\|_1
+\frac12\|\tau_R-\omega_R\|_1\\
&\leq\sqrt u+\frac u2
\leq\frac32\sqrt u
\leq\frac32\sqrt{f_\gamma(t)}.
\end{aligned}
\tag{E1.11}
$$

This is a statement about the joint state, so it controls coherences and reference correlations as well as the vacuum population. The projections above appear only in the proof; the physical drain is the unconditional semigroup $E_{0,t}$.

## Refilling a known state

Let $q=2/3$. The vacuum is in the invariant mixed-word family of T1, and its charge covariance is $C(0)=0$. Under the refill bath,

$$
C(t)=q\left[I-G_\gamma(t)G_\gamma(t)^\dagger\right].
\tag{E1.12}
$$

Write $\eta_1,\ldots,\eta_L\in[0,1]$ for the eigenvalues of $G_\gamma(t)G_\gamma(t)^\dagger$. Contractivity of $G_\gamma$ ensures this interval. The charge state remains gauge-invariant Gaussian, with independent occupation probabilities

$$
\nu_j=q(1-\eta_j)
\tag{E1.13}
$$

in the diagonalizing mode basis.

The target charge state is

$$
\sigma_q
=\bigoplus_{m=0}^{L}
q^m(1-q)^{L-m}I_{\wedge^m\mathbb C^L}.
\tag{E1.14}
$$

It is invariant under every change of the single-particle mode basis. The actual and target charge states are therefore simultaneously diagonal, with product Bernoulli distributions of parameters $\nu_j$ and $q$.

Couple each pair of occupations using the same uniform random variable on $[0,1]$. The probability of a mismatch in mode $j$ is $q-\nu_j=q\eta_j$. The union bound and the coupling inequality for total variation give

$$
D(\sigma(t),\sigma_q)
\leq\sum_{j=1}^{L}q\eta_j
=q f_\gamma(t).
\tag{E1.15}
$$

The mixed-word lift preserves trace norm and maps $\sigma_q$ to $\Pi_q=\pi$. Consequently,

$$
D\!\left(E_{2/3,t}(P_{\mathrm{vac}}),\pi\right)
\leq\frac23 f_\gamma(t).
\tag{E1.16}
$$

This use of Gaussianity concerns the specified vacuum input after the comparison in (E1.11). It imposes no Gaussian restriction on the unknown input to the complete protocol.

The same argument supplies the refill estimate used for a reservoir with a positive initial filling. For $0\leq p\leq2/3$, the known physical state $\Pi_p$ has Gaussian charge covariance $pI$, and

$$
\begin{aligned}
C(t)
&=\frac23I+
\left(p-\frac23\right)G_\gamma(t)G_\gamma(t)^\dagger,\\
D\!\left(E_{2/3,t}(\Pi_p),\pi\right)
&\leq\left(\frac23-p\right)f_\gamma(t).
\end{aligned}
\tag{E1.17}
$$

The construction that first prepares $\Pi_p$ uniformly from every input is given in [The reservoir threshold](reservoir_threshold.md).

## Composition and the explicit schedule

Apply the refill channel to the two states compared in (E1.11). Trace distance contracts under this channel. The second comparison, between refilled vacuum and $\pi$, tensor the same reference state, has the distance in (E1.16). Therefore, for every joint input,

$$
D\!\left(
(\Phi\otimes\operatorname{id}_R)(\rho_{SR}),
\pi\otimes\rho_R
\right)
\leq
\frac32\sqrt{f_\gamma(t_{\mathrm d})}
+\frac23 f_\gamma(t_{\mathrm f}).
\tag{E1.18}
$$

For a difference of quantum channels, the diamond norm is attained on a density operator with a reference of dimension at most the input dimension. Since (E1.18) holds for every reference, it proves

$$
\frac12\left\|
E_{2/3,t_{\mathrm f}}E_{0,t_{\mathrm d}}-\mathcal R_\pi
\right\|_\diamond
\leq
\frac32\sqrt{f_\gamma(t_{\mathrm d})}
+\frac23 f_\gamma(t_{\mathrm f}).
\tag{E1.19}
$$

T2 in [Exact charge transport](charge_transport.md) gives $f_\gamma(2mT_L)\leq2^{-m}$ for every integer $m\geq1$. The times in (E1.3) thus ensure

$$
f_\gamma(t_{\mathrm d})\leq\frac{\varepsilon^2}{9},
\qquad
f_\gamma(t_{\mathrm f})\leq\frac{3\varepsilon}{4}.
\tag{E1.20}
$$

The two contributions in (E1.19) are at most $\varepsilon/2$ each. This proves E1.

The logarithms in (E1.3) are base $2$ because they count the geometric-survival blocks. The asymptotic expression in (E1.6) is independent of the logarithm base. The additive $1$ keeps the bound valid uniformly over $0<\varepsilon<1$.

## Physical consequence

The complete protocol uses one endpoint and one preassigned reservoir switch at bounded rates. It requires no knowledge of the input. The drain changes the stationary filling and permits the chain to approach a unique zero-particle state; the subsequent unbiased bath creates the desired uniform state.

For the same fixed coherent Hamiltonian, [The unital control obstruction](control_obstruction.md) proves exponentially long persistence of a distant local memory under every unital endpoint protocol. The temporary particle removal therefore changes the achievable erasure time from exponential to polynomial in the stated comparison.

Perfect removal is the endpoint $p=0$ of a quantitative classification. [Vacuum accessibility](vacuum_accessibility.md) and [complete channel mixing](channel_mixing.md) extend the analysis to positive filling, and [The sharp reservoir threshold](reservoir_threshold.md) identifies which filling floors still allow polynomial-time erasure. The vacuum throughout this proof means zero particles; no ground-state, heat, or work interpretation is required.
