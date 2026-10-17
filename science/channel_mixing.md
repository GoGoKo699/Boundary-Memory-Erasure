# Complete mixing from vacuum accessibility

A lower bound on vacuum probability does not by itself identify how quantum coherences decay. This page gives the additional channel argument needed for the reservoir in [the model](model.md). It controls arbitrary reference systems and separates the number-diagonal component from coherences between different particle numbers.

Write $\mathcal R_\sigma(X)=\sigma\operatorname{Tr}X$ for the replacement channel. The channel error is always the half-diamond distance $\tfrac12\|\Phi-\mathcal R_\sigma\|_\diamond$.

## Theorem M1

Let $\mathcal H=\bigoplus_{m=0}^L\mathcal H_m$ be a finite-dimensional Hilbert space with number operator $N=\sum_{m=0}^LmP_m$. Assume:

1. The charge spectrum is contained in the nonnegative integers $0,\ldots,L$, and $\mathcal H_0$ is one-dimensional, with projector $P_{\mathrm{vac}}$.
2. $E$ is a CPTP channel covariant under $U_\theta=e^{i\theta N}$: $E(U_\theta XU_\theta^\dagger)=U_\theta E(X)U_\theta^\dagger$.
3. $E$ has a stationary state $\Pi$ satisfying $[N,\Pi]=0$.
4. For some $0<q\leq1$, its vacuum effect satisfies $E^*(P_{\mathrm{vac}})\geq qI$.

Then for every integer $n\geq1$,

$$
\boxed{
\frac12\|E^n-\mathcal R_\Pi\|_\diamond
\leq(1-q)^n+L(1-q)^{n/2}
\leq(L+1)e^{-qn/2}.
}
\tag{M1}
$$

The rank-one vacuum and the finite nonnegative charge spectrum are explicit hypotheses. They supply, respectively, a replacement-channel component and a bound on the number of coherence sectors. A larger zero-charge subspace does not automatically give this conclusion.

If $q=1$, every output has support on the one-dimensional vacuum space, so $E=\mathcal R_{P_{\mathrm{vac}}}$ and $\Pi=P_{\mathrm{vac}}$. The proof below addresses $0<q<1$.

## Number-diagonal component

Define the total-number twirl

$$
\mathcal D_N(X)
=\frac1{2\pi}\int_0^{2\pi}U_\theta XU_\theta^\dagger\,d\theta
=\sum_{m=0}^LP_mXP_m,
\qquad F=E\mathcal D_N.
$$

Covariance implies $E\mathcal D_N=\mathcal D_NE$. Therefore $F$ has number-diagonal output, $F(\Pi)=\Pi$, and

$$
F^n=E^n\mathcal D_N\qquad(n\geq1).
$$

Let $B=E^*(P_{\mathrm{vac}})$. Since the vacuum projector is number invariant, covariance also gives $\mathcal D_N(B)=B$. The vacuum-output part of $F$ is

$$
P_{\mathrm{vac}}F(X)P_{\mathrm{vac}}
=P_{\mathrm{vac}}\operatorname{Tr}(BX).
$$

There are no vacuum-to-nonvacuum output blocks. With $Q=I-P_{\mathrm{vac}}$, this gives the exact decomposition

$$
F(X)-q\mathcal R_{P_{\mathrm{vac}}}(X)
=P_{\mathrm{vac}}\operatorname{Tr}\!\left[(B-qI)X\right]
+QF(X)Q.
$$

Both terms on the right are completely positive: $B-qI\geq0$ defines a positive scalar functional, and compression of a CP map is CP. Their sum has trace $(1-q)\operatorname{Tr}X$. Thus

$$
F=q\mathcal R_{P_{\mathrm{vac}}}+(1-q)S
$$

for a CPTP channel $S$. This is a CP minorization, rather than only a lower bound on scalar transition probabilities.

Because $F(\Pi)=\Pi$,

$$
F^n-\mathcal R_\Pi
=F^n(\mathrm{id}-\mathcal R_\Pi)
=(1-q)^nS^n(\mathrm{id}-\mathcal R_\Pi).
$$

For the last equality, $\mathrm{id}-\mathcal R_\Pi$ produces trace-zero operators, every trace-preserving map preserves that property, and a replacement channel annihilates them. After tensoring with an arbitrary reference $R$, the same reasoning uses zero partial trace over the system:

$$
\operatorname{Tr}_S
\!\left[((\mathrm{id}-\mathcal R_\Pi)\otimes\mathrm{id}_R)(X_{SR})\right]
=0.
$$

Consequently the argument remains valid at every reference dimension. Since a CPTP channel has diamond norm one and $\|\mathrm{id}-\mathcal R_\Pi\|_\diamond\leq2$,

$$
\frac12\|F^n-\mathcal R_\Pi\|_\diamond\leq(1-q)^n.
$$

The twirl analyzes one component of $E^n$. It is not applied during the physical reservoir evolution.

## Coherences with nonzero charge difference

Consider an observable $X$ with definite charge difference $d\neq0$:

$$
[N,X]=dX.
$$

If $d>0$, the range of $X$ lies in positive-charge sectors because the spectrum of $N$ is nonnegative. In particular,

$$
XX^\dagger\leq\|X\|_\infty^2(I-P_{\mathrm{vac}}).
$$

The adjoint $E^*$ is unital and completely positive. Kadison-Schwarz and the vacuum-effect bound imply

$$
E^*(X)E^*(X)^\dagger
\leq E^*(XX^\dagger)
\leq\|X\|_\infty^2\left[I-E^*(P_{\mathrm{vac}})\right]
\leq(1-q)\|X\|_\infty^2 I.
$$

Hence $\|E^*(X)\|_\infty\leq\sqrt{1-q}\,\|X\|_\infty$. If $d<0$, the same proof uses $X^\dagger X$, whose support excludes the vacuum.

This contraction is complete. For an observable on the system and any reference, replace $N$ by $N\otimes I_R$ and $P_{\mathrm{vac}}$ by $P_{\mathrm{vac}}\otimes I_R$. The support argument, operator domination, and Kadison-Schwarz inequality all hold for $E^*\otimes\mathrm{id}_R$. Thus the same constant applies at every matrix amplification.

Covariance preserves the charge difference under $E^*$. Iterating within that sector gives

$$
\|(E^*)^n(X)\|_\infty
\leq(1-q)^{n/2}\|X\|_\infty,
$$

also with an arbitrary reference.

## Sum over all charge differences

For $-L\leq d\leq L$, define the Fourier projection

$$
\mathcal P_d(X)
=\frac1{2\pi}\int_0^{2\pi}
e^{-id\theta}U_\theta XU_\theta^\dagger\,d\theta.
$$

Each $\mathcal P_d$ is completely contractive in operator norm: it is an average of unitary conjugations multiplied by a scalar of modulus one. Moreover,

$$
\sum_{d=-L}^L\mathcal P_d=\mathrm{id},
\qquad\mathcal P_0=\mathcal D_N.
$$

The adjoint replacement map is $\mathcal R_\Pi^*(X)=I\operatorname{Tr}(\Pi X)$. Since $[N,\Pi]=0$, it vanishes on every nonzero charge-difference component. Covariance then yields

$$
(E^n-\mathcal R_\Pi)^*
=(F^n-\mathcal R_\Pi)^*
+\sum_{\substack{d=-L\\d\neq0}}^L(E^*)^n\mathcal P_d.
$$

The first term has completely bounded operator norm at most $2(1-q)^n$, by the number-diagonal result and norm duality. Each remaining term has completely bounded operator norm at most $(1-q)^{n/2}$. There are at most $2L$ such terms. Using $\|\Delta\|_\diamond=\|\Delta^*\|_{\mathrm{cb},\infty\to\infty}$ gives

$$
\frac12\|E^n-\mathcal R_\Pi\|_\diamond
\leq(1-q)^n+L(1-q)^{n/2}.
$$

Finally, $1-q\leq e^{-q}$ proves M1's exponential form. All factors of two use the half-diamond convention specified above.

## Application to the coherent chain

For the reservoir channel $E=E_{p,\tau}$, [Theorem V1](vacuum_accessibility.md) provides

$$
\tau=2T_L(\gamma),
\qquad q=\frac12(1-p)^L,
\qquad\Pi=\Pi_p.
$$

The physical generator is number covariant: the Hamiltonian preserves number and every jump changes it by a definite amount. The zero-particle sector is one-dimensional. The product state $\Pi_p$ is stationary and number diagonal. All hypotheses therefore hold on the entire qutrit space, without restricting an unknown input to a Gaussian or number-diagonal family.

The result applies to the actual continuous-time bath because $E_{p,\tau}^n=E_{p,n\tau}$. The equal time intervals in the estimate introduce no measurements, resets, feedback, or additional controls. It supplies the full channel upper bound used in [the reservoir threshold](reservoir_threshold.md) and complements the direct vacuum estimate in [ideal erasure](erasure_protocol.md).

Replacement-channel minorization and quantum contraction are established tools; [related work](../references/related_work.md) records that attribution. The exact vacuum effect and the finite charge decomposition make their constants explicit for the [control comparison](overview.md).
