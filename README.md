# Boundary Memory Erasure

**When can one boundary erase a quantum memory that survives for exponentially long times?** This project answers that question for a coherent chain whose particles carry two spin labels and cannot pass one another. The bulk Hamiltonian is fixed; only the left endpoint is controlled.

The final erasure target is the completely mixed chain, $`\pi=I/3^L`$. The upper bounds replace every unknown input by this state and remove correlations with an external reference. The allowed boundary operations determine whether this can happen in polynomial time.

| Result | Boundary operation | Time statement at fixed accuracy |
|---|---|---|
| Local memory obstruction | Every sequence of unital endpoint system operations | Exponential lower bound, already from one simple product input and one local population |
| Universal erasure | Pure particle loss followed once by an unbiased reservoir | $`O(L^3)`$ constructive upper bound |
| Sharp filling threshold | Bounded, open-loop, spin-independent injection/loss with minimum filling $`p_L`$ | Polynomial erasure is possible exactly when $`Lp_L=O(\log L)`$ |

The last statement permits imperfect particle removal. More precisely, for the reservoir class and fixed-rate conventions in [the model](science/model.md),

```math
\boxed{
\text{Polynomial-time erasure exists}
\quad\Longleftrightarrow\quad
L\log\frac1{1-p_L}=O(\log L)
\quad\Longleftrightarrow\quad
Lp_L=O(\log L).
}
```

A fixed positive filling floor forces exponential time. A filling floor of order $`\log L/L`$ still allows a predetermined one-switch protocol. The proof controls the full quantum channel, including number coherences, spin–charge correlations, and entangled inputs.

## Read the science

Start with the [scientific overview](science/overview.md) and [precise model](science/model.md). The [physical interpretation](science/interpretation.md) explains the memory mechanism, the filling regimes, and a complete two-site example.

| To inspect | Read |
|---|---|
| Why even strong unital endpoint control leaves distant memory | [Endpoint control obstruction](science/control_obstruction.md) |
| The exact charge reduction and cubic survival estimate | [Charge transport and Gramian](science/charge_transport.md) |
| The universal drain/refill protocol and reference decoupling | [Erasure protocol](science/erasure_protocol.md) |
| The exact input-independent vacuum effect | [Vacuum accessibility](science/vacuum_accessibility.md) |
| How vacuum accessibility controls every quantum coherence | [Complete channel mixing](science/channel_mixing.md) |
| Matching filling bounds and the necessary-and-sufficient threshold | [Reservoir filling and erasure time](science/reservoir_threshold.md) |
| Temporary min-entropy change and finite-controller requirements | [Nonuniformity resources](science/resources.md) |
| Established ingredients and the contribution's relationship to them | [Related work](references/related_work.md) and [bibliography](references/references.bib) |
| Finite matrix identities and reproduction commands | [Verification](verification/README.md) |

The [LLM reading guide](llms.txt) maps questions to the authoritative files and gives direct proof routes.

## Learn the argument

The [thirty-milestone map](learning/MILESTONES.md) follows the project's logical dependencies: **13 background and preliminary milestones**, then **17 narrative and innovation milestones**, with a synthesis at the end of each phase. It connects the local qutrit model to the universal erasure guarantee, the sharp filling criterion, and the resource bounds.

The single educational anchor is Rivas and Huelga's *Open Quantum Systems: An Introduction* (2012 edition; [author preprint v2](https://arxiv.org/abs/1104.5242v2)). The [Rivas–Huelga bridge](learning/RIVAS_HUELGA_BRIDGE.md) gives targeted section and page pointers, translates the source's conventions, and develops the additional connections required by this project. Each milestone links to its authoritative scientific derivation.

## Two quantitative statements

For the product input $`(I/3)^{\otimes(L-1)}\otimes|\uparrow\rangle\langle\uparrow|`$, every unital endpoint system protocol obeys

```math
D(\rho_L(T),I/3)\geq\frac13-\frac{JT}{3^{L-1}},
```

where $`\rho_L(T)`$ is the last-site marginal and $`D`$ is half trace distance. Even local randomization to fixed error below $`1/3`$ therefore takes exponential physical time. The pure-loss/refill construction reaches the stronger uniform replacement-channel target in

```math
O\!\left(L^3[1+\log(1/\varepsilon)]\right).
```

For a constant reservoir with fixed filling $`0<p\leq2/3`$, convergence to its own product stationary state $`\Pi_p`$ has the exact leading exponent

```math
\lim_{L\to\infty}\frac1L
\log\!\left(\gamma t_{\mathrm{mix}}^\diamond(\varepsilon;p,L)\right)
=-\log(1-p).
```

Thus the inverse stationary vacuum weight $`(1-p)^{-L}`$ fixes the exponential factor. The upper proof obtains full-channel convergence from an exact vacuum-effect identity and a covariant-channel contraction argument. It does not monitor or postselect empty-chain events.

## Reproduce the finite checks

With Python, NumPy, and SciPy installed, run from the repository root:

```bash
python verification/run_all.py
```

The suite checks the physical-to-charge generator identities, spin-injection factors, memory observables, explicit Gramian, and vacuum-effect formula. [Verification instructions and recorded outputs](verification/README.md) specify the environment, tolerances, and finite domains. The general control bounds and asymptotic laws are established by the written proofs.

## Scope

The upper bounds use the exactly constrained, hopping-only qutrit chain with fixed $`J>0`$ and boundary rate scales independent of $`L`$. The filling threshold classifies predetermined spin-independent gain/loss schedules. The unital obstruction and the finite-controller inequalities have their separately stated control domains.

The fixed-filling exponential rate and polynomial filling threshold are sharp; the optimal polynomial prefactor is not determined. Particle removal means dilution of the chain. The largest-eigenvalue resource bounds do not assign a heat or work cost.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
