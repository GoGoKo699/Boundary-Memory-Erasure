# Exact charge transport and boundary survival

The particle positions admit an exact free-fermion description even when the physical spin state is correlated with those positions. This reduction supplies two different tools: a bound on the number of particles remaining from any input, and a reconstruction of the entire physical state for a specified family with maximally mixed spin words. Keeping these uses separate is essential to the complete erasure guarantee.

The Hamiltonian, physical reservoir, and distance conventions are defined in [Model and conventions](model.md). The results below use the hopping-only chain with $J>0$ and endpoint loss and injection rates

$$
\beta=\gamma(1-p),
\qquad
\alpha=\gamma p.
$$

The physical injection rate is $\alpha/2$ for each of the two spin labels. The corresponding charge injection rate is $\alpha$.

Ordered-spin conservation and its boundary-memory consequences are established features of constrained one-dimensional spinful systems; see [Rakovszky et al., Statistical localization](https://arxiv.org/html/1910.06341v2), Section II. Quasi-free covariance methods are also established, including their application to dissipative preparation; see [Zhan et al., Rapid quantum ground state preparation via dissipative dynamics](https://arxiv.org/html/2503.15827v3), Sections V.1 and VI.1 and Appendix C. The account below derives the precise reduction and integrated survival estimate used here. The broader comparisons are in [Related work](../references/related_work.md).

## T1. Exact charge reduction

### Positions and the ordered spin word

A physical basis configuration with $m$ particles is uniquely specified by occupied positions

$$
1\leq x_1<\cdots<x_m\leq L
$$

and an ordered word $(s_1,\ldots,s_m)$ with $s_a\in\{\uparrow,\downarrow\}$. Identify this basis vector with

$$
|x_1\wedge\cdots\wedge x_m\rangle
\otimes|s_1\cdots s_m\rangle.
$$

This gives a unitary identification

$$
\mathcal H_{\mathrm{phys}}
\cong
\bigoplus_{m=0}^{L}
\left(\wedge^m\mathbb C^L\right)\otimes\mathcal W_m,
\qquad
\mathcal W_m=(\mathbb C^2)^{\otimes m},
\tag{T1.1}
$$

with $\mathcal W_0=\mathbb C$. Write $\mathcal F=\bigoplus_m\wedge^m\mathbb C^L$ for the spinless charge Fock space, and let $c_j$ be its canonical fermionic annihilation operators. The one-particle hopping matrix and its second quantization are

$$
h=J\sum_{j=1}^{L-1}
\left(|j\rangle\langle j+1|+|j+1\rangle\langle j|\right),
\qquad
H_{\mathrm{ch}}=\sum_{j,k=1}^{L}h_{jk}c_j^\dagger c_k.
\tag{T1.2}
$$

An allowed nearest-neighbor hop moves a particle into a vacancy without changing the order of the particles. The associated fermionic matrix element has positive sign because there is no occupied site between the source and destination. Consequently,

$$
H
\cong
\bigoplus_{m=0}^{L}
\left(H_{\mathrm{ch}}\big|_{\wedge^m\mathbb C^L}\right)
\otimes I_{\mathcal W_m}.
\tag{T1.3}
$$

The word is conserved by the bulk, while charge positions evolve under free hopping.

### Reduction of arbitrary physical states

Let $P_m$ project onto total particle number $m$. Define the reduction

$$
\mathcal C(\rho)
=
\bigoplus_{m=0}^{L}
\operatorname{Tr}_{\mathcal W_m}(P_m\rho P_m).
\tag{T1.4}
$$

The unitary identification in (T1.1) is understood in this formula. The map first discards cross-number blocks and then traces the word in each remaining block. It is completely positive and trace preserving, with number-diagonal output on $\mathcal F$. It allows arbitrary correlations between positions and spin words and arbitrary coherence between words of the same length.

For nonnegative, possibly time-dependent rates $\alpha(t)$ and $\beta(t)$, define the physical and charge generators

$$
\begin{aligned}
\mathcal L_t
&=-i[H,\cdot]
+\beta(t)\sum_s\mathcal D[a_s]
+\frac{\alpha(t)}2\sum_s\mathcal D[a_s^\dagger],
\\
\mathcal K_t
&=-i[H_{\mathrm{ch}},\cdot]
+\beta(t)\mathcal D[c_1]
+\alpha(t)\mathcal D[c_1^\dagger],
\end{aligned}
\tag{T1.5}
$$

where $a_s=|0\rangle\langle s|_1$ and $\mathcal D[b]\, (X)=bXb^\dagger-\{b^\dagger b,X\}/2$.

**T1, reduction statement.** The generators intertwine:

$$
\mathcal C\mathcal L_t=\mathcal K_t\mathcal C.
\tag{T1.6}
$$

Thus $\sigma(t)=\mathcal C(\rho(t))$ obeys the exact charge master equation for every physical input. The statement holds for both injection and loss and for any bounded measurable choice of their rates.

To verify the jump terms, a particle at site $1$ is always the first particle in the ordered word. Its removal acts as $c_1$ on positions and deletes that first letter. Summing over the removed spin and tracing the remaining word gives

$$
\mathcal C\left(\sum_s a_s\rho a_s^\dagger\right)
=c_1\mathcal C(\rho)c_1^\dagger.
\tag{T1.7}
$$

Injection at an empty site $1$ acts as $c_1^\dagger$ on positions and prepends the selected letter. Each of the two injected letters has the same charge trace, so

$$
\mathcal C\left(\sum_s a_s^\dagger\rho a_s\right)
=2c_1^\dagger\mathcal C(\rho)c_1.
\tag{T1.8}
$$

There is no endpoint fermionic string in either identity. The anticommutator terms follow from

$$
\sum_s a_s^\dagger a_s=n_1,
\qquad
\sum_s a_sa_s^\dagger=2(I-n_1),
\tag{T1.9}
$$

where $n_1$ becomes $c_1^\dagger c_1$ on charge space. Equations (T1.7)–(T1.9) produce loss rate $\beta$ and total injection rate $\alpha$ in (T1.5).

For a number-diagonal input these identities follow directly block by block. To include cross-number coherences, observe that $[H,N]=0$ and the jump operators have definite number change. The physical dynamics is therefore covariant under $e^{i\theta N}$, and it commutes with the number twirl

$$
\mathcal D_N(\rho)
=\frac1{2\pi}\int_0^{2\pi}
e^{i\theta N}\rho e^{-i\theta N}\,d\theta
=\sum_mP_m\rho P_m.
\tag{T1.10}
$$

Every number-diagonal charge observable has the same expectation before and after this twirl. In particular, total number, vacuum probability, and the probability that a specified set of sites is empty are exactly determined by $\mathcal C(\rho(t))$. The twirl is a mathematical reduction; the physical evolution retains its number coherences.

### The invariant family with mixed words

For a number-diagonal charge operator $\sigma=\bigoplus_m\sigma_m$, define

$$
\mathcal V(\sigma)
=\bigoplus_{m=0}^{L}
\sigma_m\otimes\frac{I_{\mathcal W_m}}{2^m}.
\tag{T1.11}
$$

This lift inserts a maximally mixed word, independently of the charge state within each number block. It satisfies

$$
\mathcal C\mathcal V=\operatorname{id},
\qquad
\mathcal L_t\mathcal V=\mathcal V\mathcal K_t,
\qquad
\|\mathcal V(X)\|_1=\|X\|_1
\tag{T1.12}
$$

for number-diagonal $X$.

For loss, tracing the first letter of $I_{\mathcal W_m}/2^m$ leaves $I_{\mathcal W_{m-1}}/2^{m-1}$. For injection, the sum over the two equally weighted letters produces $I_2/2$ tensor the previous mixed word. The Hamiltonian acts trivially on the word. These facts prove invariance. Trace-norm preservation follows from the direct sum and the identity

$$
\left\|X_m\otimes\frac{I_{\mathcal W_m}}{2^m}\right\|_1
=\|X_m\|_1.
$$

The vacuum and every product reservoir state $\Pi_p$ belong to this family. More explicitly, the charge state

$$
\sigma_p
=\bigoplus_{m=0}^{L}
p^m(1-p)^{L-m}I_{\wedge^m\mathbb C^L}
\tag{T1.13}
$$

lifts to

$$
\mathcal V(\sigma_p)
=
\bigotimes_{j=1}^{L}
\operatorname{diag}(1-p,p/2,p/2)
=\Pi_p.
\tag{T1.14}
$$

An arbitrary physical state generally cannot be recovered by lifting its charge reduction. Equation (T1.12) reconstructs the full physical evolution only when its initial state is in the displayed invariant family.

### Covariance evolution

Define the one-particle correlation matrix by

$$
C_{jk}(t)=\operatorname{Tr}\!\left(\sigma(t)c_k^\dagger c_j\right).
\tag{T1.15}
$$

The canonical anticommutation relations imply $0\leq C(t)\leq I$ for every charge density operator. Applying $\mathcal K_t^*$ to the bilinears gives the closed equation

$$
\dot C=A_tC+CA_t^\dagger+\alpha(t)P_1,
\qquad
A_t=-ih-\frac{\alpha(t)+\beta(t)}2P_1,
\qquad
P_1=|1\rangle\langle1|.
\tag{T1.16}
$$

No Gaussian assumption is needed for this equation. The Hamiltonian contributes $-i[h,C]$, the two dissipators contribute $-(\alpha+\beta)\{P_1,C\}/2$, and injection contributes $\alpha P_1$.

If $G(t,s)$ solves $\partial_tG(t,s)=A_tG(t,s)$ with $G(s,s)=I$, the solution is

$$
C(t)=G(t,0)C(0)G(t,0)^\dagger
+\int_0^t
\alpha(s)G(t,s)P_1G(t,s)^\dagger\,ds.
\tag{T1.17}
$$

At fixed total rate $\gamma=\alpha+\beta$ and filling $p=\alpha/\gamma$, put

$$
A_\gamma=-ih-\frac\gamma2P_1,
\qquad
G_\gamma(t)=e^{A_\gamma t}.
\tag{T1.18}
$$

Since $A_\gamma+A_\gamma^\dagger=-\gamma P_1$, (T1.17) reduces to

$$
C(t)=pI+G_\gamma(t)[C(0)-pI]G_\gamma(t)^\dagger.
\tag{T1.19}
$$

The drift depends on the total rate $\gamma$, not separately on the filling $p$. In particular, the same $G_\gamma$ describes the drain and refill stages when $\gamma$ is held fixed.

A gauge-invariant Gaussian charge state is characterized by a matrix $C$ whose eigenvalues $\nu_j\in[0,1]$ are independent Bernoulli occupation probabilities in the diagonalizing mode basis. Quadratic hopping with the linear jumps $c_1,c_1^\dagger$ preserves this family. One way to verify preservation is to insert Wick determinants into the closed hierarchy of number-balanced correlations: their derivatives agree with (T1.16), and uniqueness of the finite-dimensional master equation fixes the evolution.

Gaussianity is needed to reconstruct higher correlations from $C$, but it is unnecessary for the number bound below. For a Gaussian charge state and a set of sites $B$,

$$
\Pr(\text{all sites in }B\text{ empty})
=\det(I_B-C_B),
\tag{T1.20}
$$

where $C_B$ is the principal submatrix. The fully occupied all-up physical input reduces to the filled Slater state with $C(0)=I$. Its charge state remains Gaussian even though its physical spin word is not maximally mixed. This is the specific use of (T1.20) in the [reservoir-floor converse](reservoir_threshold.md).

### Uniform loss bound for every input

For pure loss, $p=0$ and $\beta=\gamma$, so (T1.19) and $C(0)\leq I$ imply

$$
C(t)=G_\gamma(t)C(0)G_\gamma(t)^\dagger,
\qquad
\langle N(t)\rangle
=\operatorname{Tr}C(t)
\leq f_\gamma(t),
\tag{T1.21}
$$

where

$$
f_\gamma(t)
=\operatorname{Tr}\!\left(G_\gamma(t)^\dagger G_\gamma(t)\right).
\tag{T1.22}
$$

Because $I-P_{\mathrm{vac}}\leq N$,

$$
1-\operatorname{Tr}\!\left(P_{\mathrm{vac}}E_{0,t}(\rho)\right)
\leq f_\gamma(t)
\tag{T1.23}
$$

for every physical input $\rho$. This includes non-Gaussian states, spin-charge correlations, and number coherences. Applied to the system marginal of any joint system-reference input, it gives the same bound with an arbitrary idle reference.

## T2. Exact Gramian and a uniform survival estimate

Define

$$
X_\gamma
=\int_0^\infty
G_\gamma(t)^\dagger G_\gamma(t)\,dt.
\tag{T2.1}
$$

The integral exists and is positive definite. Its exact entries and trace yield a time estimate without a spectral-eigenvector conditioning factor.

**T2, Gramian and survival statement.** For $1\leq j\leq k\leq L$,

$$
(X_\gamma)_{jk}
=
\begin{cases}
(L+1-k)\left[
\dfrac j\gamma+\dfrac{\gamma(j-1)}{4J^2}
\right],
&j,k\text{ have the same parity},\\[6pt]
\dfrac{i(L+1-k)}{2J},
&j<k\text{ have opposite parity}.
\end{cases}
\tag{T2.2}
$$

The lower triangle is the Hermitian conjugate. In particular,

$$
T_L(\gamma):=\operatorname{Tr}X_\gamma
=
\frac{L(L+1)(L+2)}{6\gamma}
+\frac{\gamma L(L^2-1)}{24J^2}.
\tag{T2.3}
$$

For every integer $m\geq1$,

$$
f_\gamma\!\left(2mT_L(\gamma)\right)\leq2^{-m}.
\tag{T2.4}
$$

At fixed $J,\gamma>0$, the time $T_L(\gamma)$ is $\Theta(L^3)$.

### Existence and the Lyapunov equation

If $A_\gamma v=\lambda v$, dissipativity gives

$$
2\operatorname{Re}\lambda\,\|v\|^2
=v^\dagger(A_\gamma+A_\gamma^\dagger)v
=-\gamma|v_1|^2.
\tag{T2.5}
$$

Every eigenvalue has nonpositive real part. If one had zero real part, then $v_1=0$. The first row of the eigenvector equation gives $v_2=0$, and the nearest-neighbor recurrence forces all remaining components to vanish. Hence $A_\gamma$ is Hurwitz: every eigenvalue has strictly negative real part.

It follows that $G_\gamma(t)\to0$ exponentially in finite dimension and that the integral (T2.1) converges. Integration of its derivative gives

$$
A_\gamma^\dagger X_\gamma+X_\gamma A_\gamma=-I.
\tag{T2.6}
$$

This Lyapunov equation has a unique solution. Indeed, if $A_\gamma^\dagger Y+YA_\gamma=0$, then $G_\gamma(t)^\dagger YG_\gamma(t)=Y$ for all $t$, whose limit implies $Y=0$. Positivity of the integral is strict because $G_\gamma(0)=I$.

### Verification of every matrix entry

With all out-of-range entries set to zero, (T2.6) reads

$$
iJ\left(
X_{j-1,k}+X_{j+1,k}-X_{j,k-1}-X_{j,k+1}
\right)
-\frac\gamma2(\delta_{j1}+\delta_{k1})X_{jk}
=-\delta_{jk}.
\tag{T2.7}
$$

To verify (T2.2), write

$$
y_k=L+1-k,
\qquad
a_j=\frac j\gamma+\frac{\gamma(j-1)}{4J^2}.
$$

On the upper triangle the proposed same-parity entries are $a_jy_k$, and the opposite-parity entries are $iy_k/(2J)$.

For diagonal entries with $j>1$, the difference $y_j-y_{j+1}=1$ makes the hopping term in (T2.7) equal to $-1$; this also holds at $j=L$ with $y_{L+1}=0$. At $j=1$, the hopping term is $L-1$ and the boundary term is $-\gamma X_{11}=-L$, again giving $-1$.

For $j<k$ of the same parity with $j>1$, the hopping term vanishes because $2y_k-y_{k-1}-y_{k+1}=0$. At the boundary $j=1$, that term is $y_k/2$, canceled by $-\gamma X_{1k}/2=-y_k/2$.

For $j<k$ of opposite parity with $j>1$, both $a_j$ and $y_k$ are affine, so

$$
(a_{j-1}+a_{j+1})y_k
-a_j(y_{k-1}+y_{k+1})=0.
$$

At $j=1$, the missing out-of-range term leaves $(a_2-2a_1)y_k=\gamma y_k/(4J^2)$. Its contribution $i\gamma y_k/(4J)$ is canceled by the boundary term $-\gamma X_{1k}/2$. Hermitian conjugation covers the lower triangle. Thus (T2.2) solves (T2.7), and uniqueness identifies it with (T2.1).

Taking the diagonal sum uses

$$
\sum_{j=1}^{L}j(L+1-j)
=\frac{L(L+1)(L+2)}6,
\qquad
\sum_{j=1}^{L}(j-1)(L+1-j)
=\frac{L(L^2-1)}6,
$$

which proves (T2.3).

### From the integrated survival to a geometric bound

The one-particle propagator is contractive because $A_\gamma+A_\gamma^\dagger=-\gamma P_1\leq0$. Its squared Frobenius norm obeys

$$
f_\gamma'(t)
=-\gamma\|\langle1|G_\gamma(t)\|_2^2\leq0,
\qquad
\int_0^\infty f_\gamma(t)\,dt=T_L(\gamma).
\tag{T2.8}
$$

Set $\tau=2T_L(\gamma)$. Monotonicity gives

$$
\tau f_\gamma(\tau)
\leq\int_0^\tau f_\gamma(t)\,dt
\leq T_L(\gamma),
\qquad
f_\gamma(\tau)\leq\frac12.
\tag{T2.9}
$$

Semigroup composition and the Frobenius-norm product inequality imply

$$
\begin{aligned}
f_\gamma(s+t)
&=\|G_\gamma(s)G_\gamma(t)\|_{\mathrm F}^2\\
&\leq
\|G_\gamma(s)\|_{\mathrm F}^2
\|G_\gamma(t)\|_{\mathrm F}^2
=f_\gamma(s)f_\gamma(t).
\end{aligned}
\tag{T2.10}
$$

Iteration at the time $\tau$ proves (T2.4). The restriction $m\geq1$ matters: $f_\gamma(0)=L$. For the positive block times used in the erasure schedules, the estimate already controls the total expected surviving population, with no additional factor of $L$.

## How these tools enter the erasure result

The arbitrary-input loss estimate (T1.23), combined with (T2.4), supplies the drain stage of [Ideal erasure](erasure_protocol.md). The mixed-word lift and Gaussian covariance determine the subsequent refill state exactly. The same propagator and Gramian also enter the [vacuum-accessibility identity](vacuum_accessibility.md); that identity and [complete channel mixing](channel_mixing.md) handle reservoirs with positive filling. Their combination yields the [sharp reservoir threshold](reservoir_threshold.md).

The comparator uses the same coherent Hamiltonian and endpoint location, as established in [The unital control obstruction](control_obstruction.md). The full logical relationship is collected in the [scientific overview](overview.md).
