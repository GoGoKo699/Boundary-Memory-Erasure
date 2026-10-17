# Physical meaning and worked examples

[Overview](overview.md) · [Model](model.md) · [Reservoir theorem](reservoir_threshold.md)

The chain carries a memory because particles cannot pass and the bulk preserves their ordered spin word. A boundary reservoir can alter the first letter of that word. Reaching its last letter requires a sequence of removals that exposes it to the controlled endpoint. The results quantify how the boundary operation changes the time required for this process.

## One Hamiltonian, different allowed reservoirs

The [unital bound](control_obstruction.md) begins from a simple state that is nearly maximally mixed. Every unital endpoint map preserves a uniform upper bound on its eigenvalues. The current changing the relevant tail-spin projector has only two nonzero eigenvalues, $+J$ and $-J$. That current can carry only exponentially little probability per unit time from this state. The last-site down population therefore remains far from its uniform value for exponential time.

The pure-loss reservoir removes the condition responsible for that eigenvalue bound. The chain can approach the vacuum, a common state that has no spin word. Refilling it creates a new word with independent unbiased spin labels. The [reference-system proof](erasure_protocol.md) ensures that this construction forgets the original quantum input, including its correlations with another system.

The implemented resources are a fixed coherent bulk, one addressed endpoint, bounded gain/loss rates, and one predetermined change of the bath filling. The final target remains $I/3^L$. The operation that changes is the allowed intermediate boundary channel.

## Imperfect removal and the empty-chain weight

At filling $p$, the stationary probability of an empty chain is $(1-p)^L$. The [vacuum-effect calculation](vacuum_accessibility.md) proves the exact identity

$$
\lambda_{\min}\!\left(E_{p,t}^*(P_{\mathrm{vac}})\right)
=(1-p)^L\det\!\left[I-G_\gamma(t)^\dagger G_\gamma(t)\right].
$$

An interval of length $2T_L(\gamma)=\Theta(L^3)$ makes the determinant at least $1/2$. The [complete channel bound](channel_mixing.md) then turns this uniform accessibility into mixing after $O((1-p)^{-L}\log((L+1)/\varepsilon))$ such intervals. This is an unconditional statement about the reservoir evolution. Empty-chain events are not measured, selected, or used to determine the switch time.

The matching converse keeps track of the original last spin. Starting from a fully occupied all-up chain, a filling floor prevents the charge covariance from dropping below $p_LI$. The tail-empty probability is consequently at most $(1-p_L)^{L-1}$. The original last spin can be replaced only through that rare sector. This gives the inverse empty-weight lower bound for every allowed schedule.

The recurrence through empty configurations has a classical counterpart, including the first-passage analysis of [Jansen, Nedea, and Lukkien](../references/related_work.md#classical-single-file-renewal). The full quantum conclusion additionally requires control of charge coherences, arbitrary spin–charge correlations, and external references. Those are supplied by the operator-effect and complete-contraction arguments.

## Filling regimes

Fix the error independently of $L$ and keep $J$ and the allowed rate scale fixed. The following consequences are evaluations of the analytical bounds in [F2](reservoir_threshold.md#theorem-f2).

| Minimum filling $p_L$ | Inverse vacuum weight $(1-p_L)^{-L}$ | Consequence in the stated bath class |
|---|---|---|
| $0$ | $1$ | Ideal one-switch erasure has an $O(L^3)$ upper bound |
| $a/L$, fixed $a>0$ | $e^{a+o(1)}$ | Polynomial erasure is possible |
| $c\log L/L$, fixed $c>0$ | $L^{c+o(1)}$ | Polynomial erasure is possible; the lower and upper powers need not match |
| $L^{-a}$, fixed $0<a<1$ | $\exp[(1+o(1))L^{1-a}]$ | Every allowed schedule takes superpolynomial time |
| Fixed $p\in(0,2/3]$ | $\exp[-L\log(1-p)]$ | Exponential time, with this exact leading exponent |

For $p_L=c\log L/L$, the lower bound has scale $L^{c+o(1)}$ and the construction has scale $L^{3+c+o(1)}$ up to logarithmic factors. The theorem identifies the polynomial-time threshold without determining the optimal polynomial exponent. For an oscillatory sequence of floors, failure of the $O(\log L)$ condition excludes a uniform polynomial bound; growth faster than every polynomial along the entire sequence follows from the stronger limit $Lp_L/\log L\to\infty$.

## A two-site calculation

The smallest chain already displays the distinction between the current and the charge-transport estimate. For $L=2$,

$$
Q=I_3\otimes|\uparrow\rangle\langle\uparrow|,
\qquad
\rho_0=(I_3/3)\otimes|\uparrow\rangle\langle\uparrow|.
$$

The only hopping pair that changes $Q$ is $|\uparrow0\rangle\leftrightarrow|0\uparrow\rangle$. Its current has eigenvalues $\pm J$, while $\|\rho_0\|_\infty=1/3$. Hence

$$
D(\rho_2(T),I_3/3)\geq\frac13-\frac{JT}{3}
$$

under unital endpoint control. At error $\varepsilon=0.1$ and $J=1$, this lower bound is $T\geq0.7$. This finite-size value is not the asymptotic separation; the exponential factor emerges as the rank of the preparation grows with $L$.

The charge drift and its exact Gramian are

$$
A_\gamma=
\begin{pmatrix}-\gamma/2&-iJ\\-iJ&0\end{pmatrix},
\qquad
X_\gamma=
\begin{pmatrix}
2/\gamma&i/(2J)\\
-i/(2J)&2/\gamma+\gamma/(4J^2)
\end{pmatrix}.
$$

Direct multiplication gives $A_\gamma^\dagger X_\gamma+X_\gamma A_\gamma=-I$, and

$$
T_2(\gamma)=\operatorname{Tr}X_\gamma
=\frac4\gamma+\frac\gamma{4J^2}.
$$

With $J=\gamma=1$, the survival-block length is $2T_2=8.5$. For $\varepsilon=0.1$, the ideal protocol uses

$$
\left\lceil\log_2(9/\varepsilon^2)\right\rceil=10
\quad\text{drain blocks},
\qquad
\left\lceil\log_2(4/(3\varepsilon))\right\rceil=4
\quad\text{refill blocks}.
$$

The sufficient total time is therefore $119$. These are deliberately uniform proof bounds, with different purposes from an optimal finite-size control calculation. Their gap at $L=2$ does not contradict the asymptotic exponential-versus-polynomial comparison.

For illustration of the filling constant, take $p=1/4$ in the same two-site chain. The stationary vacuum weight is $9/16$, and V1 guarantees vacuum probability at least $9/32$ from every input after one interval of length $8.5$. The intermediate stationary state is $\operatorname{diag}(3/4,1/8,1/8)^{\otimes2}$. The protocol may first erase into that state and then refill to the uniform target; it need not prepare a nearly empty chain.

## What is sharp, and what the resources mean

The leading exponential rate at fixed filling and the necessary-and-sufficient polynomial filling scale are sharp statements. The cubic constructive transport factor is an upper bound in the stated model. The results apply to the exactly constrained hopping chain and the specified controls; they do not assume that the same charge reduction survives added interactions, disorder, passing, or spin exchange.

The [resource inequalities](resources.md) refer to the largest eigenvalue of the system state and to the initial nonuniformity of a specified independent finite controller. A state can have min-entropy of order $\log L$ while its von Neumann entropy remains nearly maximal. Consequently these inequalities do not assign a heat or work cost to the continuous reservoir.

The contribution combines a local-memory obstruction for the entire unital endpoint class with a universal erasure construction and a sharp filling law for the gain/loss class. These claims require no quantum advantage over a classical computational model. Their relationship to prior boundary memory, local relaxation, renewal, and channel-contraction results is set out in [related work](../references/related_work.md).
