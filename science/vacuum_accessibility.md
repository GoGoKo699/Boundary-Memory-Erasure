# Vacuum accessibility at finite reservoir filling

The finite-filling reservoir can erase spin information even when its stationary state has very little vacuum weight. The relevant input-independent quantity is the smallest eigenvalue of the evolved vacuum effect. This page computes that eigenvalue on the full physical qutrit Hilbert space.

The [model and conventions](model.md) fix the coherent Hamiltonian $`H`$, the endpoint operators $`a_s=|0\rangle\langle s|_1`$, and

```math
\mathcal L_{H,p}
=-i[H,\cdot]
+\gamma(1-p)\sum_{s=\uparrow,\downarrow}\mathcal D[a_s]
+\frac{\gamma p}{2}\sum_{s=\uparrow,\downarrow}\mathcal D[a_s^\dagger].
```

Here $`J,\gamma>0`$, $`0<p\leq 2/3`$, the total injection rate is $`\alpha=\gamma p`$, and the loss rate of an occupied spin is $`\beta=\gamma(1-p)`$. Write $`E_{p,t}=e^{t\mathcal L_{H,p}}`$, $`N`$ for the particle-number operator, and $`P_{\mathrm{vac}}=|\mathrm{vac}\rangle\langle\mathrm{vac}|`$.

The charge propagator and its survival integral, derived in [charge transport](charge_transport.md), are

```math
A_\gamma=-ih-\frac\gamma2 P_1,
\qquad h=J\sum_{j=1}^{L-1}
\left(|j\rangle\langle j+1|+|j+1\rangle\langle j|\right),
\qquad P_1=|1\rangle\langle1|,
\qquad G_\gamma(t)=e^{tA_\gamma},
```

```math
T_L(\gamma)
=\int_0^\infty\mathrm{Tr}\!\left(G_\gamma(t)^\dagger G_\gamma(t)\right)dt
=\frac{L(L+1)(L+2)}{6\gamma}
+\frac{\gamma L(L^2-1)}{24J^2}.
```

## Theorem V1

For every $`t\geq0`$, the exact minimum eigenvalue of the physical vacuum effect is

```math
{
\boxed{
\lambda_{\min}\!\left(E_{p,t}^*(P_{\mathrm{vac}})\right)
=(1-p)^L\det\!\left[I-G_\gamma(t)^\dagger G_\gamma(t)\right].
}
}
\tag{V1}
```

In particular, with

```math
\tau=2T_L(\gamma),
\qquad q_p=\frac12(1-p)^L,
```

one has the full operator inequality

```math
E_{p,\tau}^*(P_{\mathrm{vac}})\geq q_p I.
```

Thus every physical input has vacuum probability at least $`q_p`$ after the same time $`\tau`$. The inequality allows arbitrary spin-charge correlations, coherences between different particle numbers, and entanglement with an external reference. It makes no Gaussian assumption about that input.

## Stationary-state reversal

The stationary state is

```math
\Pi_p=\bigotimes_{j=1}^L\mathrm{diag}(1-p,p/2,p/2)
=(1-p)^L\zeta^N,
\qquad \zeta=\frac{p}{2(1-p)}.
```

Since $`p>0`$ and $`p<1`$, this state is invertible. Set $`S_p=\Pi_p^{1/2}`$ and define the invertible sandwich map

```math
\Gamma_p(X)=S_pXS_p.
```

The number-preserving Hamiltonian commutes with $`S_p`$. Since $`a_s`$ removes one particle,

```math
S_p^{-1}a_sS_p=\sqrt\zeta\,a_s,
\qquad
S_p^{-1}a_s^\dagger S_p=\zeta^{-1/2}a_s^\dagger.
```

Conjugating the Schrödinger generator with Hamiltonian $`-H`$ therefore gives

```math
\mathcal L_{H,p}^*
=\Gamma_p^{-1}\mathcal L_{-H,p}\Gamma_p.
```

To check the jump coefficients explicitly, the loss jump becomes

```math
\beta S_p^{-1}a_sS_p\,X\,S_pa_s^\dagger S_p^{-1}
=\beta\zeta\,a_sXa_s^\dagger
=\frac\alpha2 a_sXa_s^\dagger,
```

and the gain jump becomes $`\beta a_s^\dagger Xa_s`$. The anticommutator projectors commute with $`S_p`$, so their coefficients remain unchanged. The reverse Hamiltonian supplies $`+i[H,X]`$, exactly the Heisenberg commutator. Both the factor of two in spin injection and the sign of $`H`$ are necessary for this identity.

Exponentiation yields

```math
E_{p,t}^*(O)
=\Pi_p^{-1/2}
e^{t\mathcal L_{-H,p}}
\!\left(\Pi_p^{1/2}O\Pi_p^{1/2}\right)
\Pi_p^{-1/2}.
```

Because $`\Gamma_p(P_{\mathrm{vac}})=(1-p)^LP_{\mathrm{vac}}`$,

```math
E_{p,t}^*(P_{\mathrm{vac}})
=(1-p)^L\Pi_p^{-1/2}
e^{t\mathcal L_{-H,p}}(P_{\mathrm{vac}})
\Pi_p^{-1/2}.
```

The Hamiltonian reversal is used only to evaluate this effect. The implemented reservoir evolution always has the fixed Hamiltonian $`H`$.

## Spectrum of the vacuum effect

Use the ordered-spin decomposition

```math
\mathcal H
=\bigoplus_{m=0}^L
\left(\wedge^m\mathbb C^L\right)\otimes(\mathbb C^2)^{\otimes m}
```

and the invariant mixed-word lift

```math
\mathcal V(\sigma)
=\bigoplus_{m=0}^L\sigma_m\otimes\frac{I_{2^m}}{2^m}.
```

Their generator identities are established in [charge transport](charge_transport.md). The reverse evolution from vacuum belongs to this family. Its charge state is a gauge-invariant fermionic Gaussian state with covariance

```math
C_{-H}(t)=p\left[I-G_\gamma(t)^\dagger G_\gamma(t)\right],
```

because the reverse charge drift is $`A_\gamma^\dagger`$. The charge propagator is a contraction: $`A_\gamma+A_\gamma^\dagger=-\gamma P_1\leq0`$. Consequently, the eigenvalues $`\eta_1,\ldots,\eta_L`$ of $`G_\gamma(t)^\dagger G_\gamma(t)`$ lie in $`[0,1]`$. In its natural mode basis, the reverse charge state has independent occupations

```math
c_j=p(1-\eta_j).
```

For an occupied mode set $`M`$ of size $`m`$, the charge-state eigenvalue is

```math
\prod_{j\notin M}(1-c_j)\prod_{j\in M}c_j.
```

The corresponding physical eigenvalue has an additional factor $`2^{-m}`$ from the mixed-word lift. Meanwhile, $`\Pi_p`$ is scalar on every number sector, so it is unchanged by the charge-mode basis transformation. Its eigenvalue in that sector is $`(1-p)^{L-m}(p/2)^m`$. The sandwich and the prefactor $`(1-p)^L`$ therefore multiply the charge-state eigenvalue by

```math
\frac{(1-p)^L\,2^{-m}}{(1-p)^{L-m}(p/2)^m}
=\left(\frac{1-p}{p}\right)^m.
```

It follows that the vacuum-effect eigenvalue associated with $`M`$ is

```math
\prod_{j\notin M}(1-p+p\eta_j)
\prod_{j\in M}(1-p)(1-\eta_j),
```

with spin-word multiplicity $`2^m`$. For each mode, the empty factor minus the occupied factor equals $`\eta_j\geq0`$. The minimum occupies all modes, giving

```math
(1-p)^L\prod_{j=1}^L(1-\eta_j)
=(1-p)^L\det(I-G_\gamma^\dagger G_\gamma).
```

This proves V1. The fully occupied charge sector attains the minimum, independently of its spin state. Gaussianity was used to compute a known reverse vacuum evolution; the resulting effect is an operator on the entire physical Hilbert space.

## A uniform time interval

Let

```math
f_\gamma(t)=\mathrm{Tr}\!\left(G_\gamma(t)^\dagger G_\gamma(t)\right).
```

Dissipativity makes $`f_\gamma`$ nonincreasing. Its exact integral implies

```math
2T_L(\gamma)\,f_\gamma(2T_L(\gamma))
\leq\int_0^{2T_L(\gamma)}f_\gamma(t)\,dt
\leq T_L(\gamma),
```

so $`\sum_j\eta_j=f_\gamma(\tau)\leq1/2`$. For numbers $`\eta_j\in[0,1]`$,

```math
\prod_j(1-\eta_j)\geq1-\sum_j\eta_j\geq\frac12.
```

The claimed inequality $`E_{p,\tau}^*(P_{\mathrm{vac}})\geq q_pI`$ follows. Tensoring it with an arbitrary identity preserves the inequality, and hence the same probability bound holds for every state of the chain and a reference.

At fixed $`J`$ and $`\gamma`$, $`\tau=\Theta(L^3)`$, whereas $`q_p`$ is half the stationary vacuum weight. The [complete channel mixing bound](channel_mixing.md) converts these quantities into a uniform erasure time. No vacuum observation or postselection is part of that construction. The zero-filling case is treated directly by the [ideal erasure protocol](erasure_protocol.md), which does not require an invertible stationary state.

The connection to the full control comparison is summarized in the [overview](overview.md); the roles of stationary-state reversal and classical renewal are distinguished in [related work](../references/related_work.md).
