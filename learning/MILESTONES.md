# Project milestones

[Repository](../README.md) · [Scientific overview](../science/overview.md) · [Rivas–Huelga bridge](RIVAS_HUELGA_BRIDGE.md)

These thirty milestones describe the project's complete conceptual route, from one local qutrit and its endpoint dynamics to a global classification of memory erasure. Their content and dependencies are intrinsic to the scientific results.

The sole educational anchor is Ángel Rivas and Susana F. Huelga, [*Open Quantum Systems: An Introduction*, arXiv:1104.5242v2](https://arxiv.org/pdf/1104.5242v2). All section and page pointers below refer to the printed pages of that 9 February 2012 preprint. The [Rivas–Huelga bridge](RIVAS_HUELGA_BRIDGE.md) is the single source bridge. It connects the book's evolution framework to the specialized arguments proved in the scientific pages.

## Structure

| Phase | Milestones | Progression |
|---|---|---|
| Background and preliminaries | [M01](#m01)–[M13](#m13) | Local states and operations, the reservoir model, global channel criteria, and the mathematical proof objects; M13 synthesizes the foundations |
| Narrative and innovation | [M14](#m14)–[M30](#m30) | Local obstruction, exact transport, complete erasure, sharp reservoir classification, and controller resources; M30 synthesizes the full account |

The 13/17 allocation reflects three connected sets of concepts: endpoint channels and operator order, charge transport and semigroups, and complete quantum mixing. The second phase treats stationary reversal, the vacuum spectrum, CP minorization, and coherence contraction as separate transitions because each changes the kind of statement available about the unknown input.

## Shared conventions

The model uses one fixed coherent Hamiltonian and a spin-independent gain/loss reservoir with total injection divided equally between the two spins:

```math
\alpha=\gamma p,\qquad
\beta=\gamma(1-p),\qquad
0\leq p\leq\frac23,\qquad
\pi=\frac{I}{3^L}.
```

The system's target is the identity-preserving replacement channel, and the complete error includes an idle reference:

```math
\mathcal R_\pi(X)=\pi\operatorname{Tr}X,\qquad
D(\rho,\sigma)=\frac12\|\rho-\sigma\|_1,\qquad
\frac12\|\Phi_T-\mathcal R_\pi\|_\diamond\leq\varepsilon.
```

At fixed error, $`\varepsilon`$ is independent of $`L`$. The unital local obstruction uses $`0<\varepsilon<1/3`$, and the filling converses use $`0<\varepsilon<1/2`$. Each canonical theorem retains its full hypotheses. Fixed finite-dimensional relaxation and a quantitative complete rate that tracks chain length are different levels of description.

## Phase I: background and preliminaries

<a id="m01"></a>

### M01. A local state and its observable probabilities

- **Central question:** What information can one qutrit site store and reveal?
- **Understanding target:** Identify the vacancy and the two spin states, construct their effects, and distinguish occupation from spin information. Extend local effects by identities when they are measured inside the chain.
- **Earlier dependencies:** None.
- **Story role:** This establishes the local physical objects from which both memory witnesses and reservoir jumps are built.
- **Conceptual connection:** A local measurement probability is an expectation of an operator on the entire chain, which will later make a local output sufficient to disprove global erasure.
- **Source pointers:** [Rivas–Huelga §4.1, pp. 24–25, Theorem 4.1](https://arxiv.org/pdf/1104.5242v2#page=24) supplies the pure-marginal and composite-state foundation. The qutrit states and local effects are specified in the model below.
- **Canonical science:** [Model: Chain and fixed Hamiltonian](../science/model.md#chain-and-fixed-hamiltonian); [Control obstruction: U1. Bottleneck inequality](../science/control_obstruction.md#u1-bottleneck-inequality) for the definitions of the local down-population effect only.

<a id="m02"></a>

### M02. Endpoint channels and the dual picture

- **Central question:** How does a trace-preserving boundary operation act on observables away from that boundary?
- **Understanding target:** Relate CPTP Schrödinger evolution to its unital adjoint, track tensor factors, and explain why an endpoint operation fixes observables with the identity on that endpoint.
- **Earlier dependencies:** [M01](#m01).
- **Story role:** This supplies the locality statement behind the bottleneck and keeps trace preservation distinct from unitality of a state channel.
- **Conceptual connection:** No direct change of a distant effect does not mean no eventual influence; the fixed Hamiltonian can transport the effect's probability current.
- **Source pointers:** [Rivas–Huelga §4.2, pp. 26–29, Eqs. (35)–(36), Theorem 4.3](https://arxiv.org/pdf/1104.5242v2#page=26) supplies universal CP maps and their spectator-system extension. The endpoint adjoint identity is derived in the canonical proof below.
- **Canonical science:** [Model: Boundary controls](../science/model.md#boundary-controls); [Control obstruction: Proof: the endpoint cannot change the tail projector directly](../science/control_obstruction.md#proof-the-endpoint-cannot-change-the-tail-projector-directly).

<a id="m03"></a>

### M03. Coherent motion without passing

- **Central question:** Which properties of a spin configuration survive coherent hopping in this chain?
- **Understanding target:** Reconstruct the allowed Hermitian hopping terms, particle-number sectors, and ordered spin word. Identify the one-dimensional vacuum sector and the physical restrictions responsible for order preservation.
- **Earlier dependencies:** [M01](#m01)–[M02](#m02).
- **Story role:** This extends the local description to the constrained many-body Hamiltonian without yet deriving a relaxation theorem.
- **Conceptual connection:** Coherent superpositions of particle positions coexist with an ordered label structure, allowing a memory mechanism and a simpler description of charge motion.
- **Source pointers:** The coherent no-passing Hamiltonian and ordered-word identification are supplied by the canonical scientific pages below.
- **Canonical science:** [Model: Chain and fixed Hamiltonian](../science/model.md#chain-and-fixed-hamiltonian); [Charge transport: Positions and the ordered spin word](../science/charge_transport.md#positions-and-the-ordered-spin-word).

<a id="m04"></a>

### M04. Injection and loss in physical time

- **Central question:** How do the endpoint jump coefficients determine the actual generator and rate scale?
- **Understanding target:** Write the Lindblad dissipator, distinguish total gain $`\alpha`$ from per-spin gain $`\alpha/2`$, and recover $`\beta=\gamma(1-p)`$ and $`\alpha=\gamma p`$. Keep the coherent term and elapsed physical time explicit.
- **Earlier dependencies:** [M02](#m02)–[M03](#m03).
- **Story role:** This fixes the reservoir convention used in every quantitative bound and avoids interpreting a pulse count as physical time.
- **Conceptual connection:** One controlled site induces an open evolution of a much larger coherent system; changing the filling changes the local generator while the bulk Hamiltonian and total rate can stay fixed.
- **Source pointers:** [Rivas–Huelga §5.2, pp. 37–41, Theorem 5.1, Eqs. (46), (51)](https://arxiv.org/pdf/1104.5242v2#page=37) supplies the GKSL form. The physical gain/loss coefficients and their total-rate convention are fixed by the model below.
- **Canonical science:** [Model: Reservoir convention](../science/model.md#reservoir-convention); [Ideal erasure: E1. Ideal erasure theorem](../science/erasure_protocol.md#e1-ideal-erasure-theorem) for the two-stage rates.

<a id="m05"></a>

### M05. Stationary states and the unital boundary

- **Central question:** Why is the unbiased reservoir unital while a dilute reservoir has a nonuniform stationary state?
- **Understanding target:** Derive the local balance relation and the product stationary state $`\Pi_p`$, check commutation with the hopping Hamiltonian, and identify $`p=0`$ and $`p=2/3`$. Distinguish the stationary-state calculation and qualitative finite-dimensional relaxation from a quantitative complete rate that tracks $`L`$.
- **Earlier dependencies:** [M03](#m03)–[M04](#m04).
- **Story role:** This connects the allowed reservoir filling to the stationary target and defines the unital comparison class.
- **Conceptual connection:** A common stationary identity constrains operator order, whereas an intermediate nonuniform stationary state can change what a control protocol achieves before returning to the same final target.
- **Source pointers:** [Rivas–Huelga §5.4, pp. 45–48, Definition 5.3, Eq. (63), Theorems 5.3–5.4](https://arxiv.org/pdf/1104.5242v2#page=45) supplies stationarity and finite-dimensional relaxation. The project supplies the product filling state and the quantitative dependence on chain length.
- **Canonical science:** [Model: Reservoir convention](../science/model.md#reservoir-convention); [Model: Boundary controls](../science/model.md#boundary-controls); [Interpretation: One Hamiltonian, different allowed reservoirs](../science/interpretation.md#one-hamiltonian-different-allowed-reservoirs).

<a id="m06"></a>

### M06. Erasure of a system and its reference correlations

- **Central question:** What does it mean to erase every unknown quantum input?
- **Understanding target:** Distinguish local trace-distance conditions, convergence of a selected input, and half-diamond distance from a replacement channel. Explain why the reference marginal must be preserved and decoupled from the system.
- **Earlier dependencies:** [M01](#m01)–[M02](#m02) and [M05](#m05).
- **Story role:** This sets the global operational objective before any upper-bound construction is accepted as sufficient.
- **Conceptual connection:** A simple local effect can certify failure, while success requires a statement about the whole channel and an arbitrary reference system.
- **Source pointers:** [Rivas–Huelga §2.1, pp. 4–5, Propositions 2.1–2.2](https://arxiv.org/pdf/1104.5242v2#page=4) supplies norm conventions; [Rivas–Huelga §4.2, pp. 26–29](https://arxiv.org/pdf/1104.5242v2#page=26) supplies universal CP maps with an idle reference. The half-diamond replacement criterion is defined in the model below.
- **Canonical science:** [Model: Information erasure and distances](../science/model.md#information-erasure-and-distances); [Ideal erasure: Draining also decouples the reference](../science/erasure_protocol.md#draining-also-decouples-the-reference) for the purpose of the reference comparison.

<a id="m07"></a>

### M07. Operator order and spectral concentration

- **Central question:** How can positivity turn a largest-eigenvalue bound into a constraint on dynamics?
- **Understanding target:** Use $`0\leq\rho\leq\|\rho\|_\infty I`$, preservation of order by positive maps, and unital preservation of an identity upper bound. Define min-entropy and explain why it measures a different concentration property from von Neumann entropy.
- **Earlier dependencies:** [M02](#m02), [M05](#m05)–[M06](#m06).
- **Story role:** This provides the order estimate needed by the local obstruction and the later resource statements.
- **Conceptual connection:** The maximum eigenvalue connects a many-body probability-current bound with a one-shot measure of system nonuniformity.
- **Source pointers:** [Rivas–Huelga §2.1, pp. 4–5](https://arxiv.org/pdf/1104.5242v2#page=4) supplies matrix-norm foundations. The operator-order estimate and the min-entropy distinctions are developed in the canonical scientific pages below.
- **Canonical science:** [Control obstruction: Proof: the Hamiltonian current has two nonzero eigenvalues](../science/control_obstruction.md#proof-the-hamiltonian-current-has-two-nonzero-eigenvalues); [Resources: R1. Temporary system nonuniformity](../science/resources.md#r1-temporary-system-nonuniformity); [Resources: The spectral meaning of the bound](../science/resources.md#the-spectral-meaning-of-the-bound).

<a id="m08"></a>

### M08. Charge coordinates and Gaussian information

- **Central question:** What information is retained by a charge description, and when is a covariance matrix sufficient?
- **Understanding target:** Identify positions with a fermionic charge Fock space, distinguish charge reduction from reconstruction of physical spin states, and define the covariance matrix with $`0\leq C\leq I`$. Explain the additional Gaussian assumption needed for higher correlations and empty-set determinants.
- **Earlier dependencies:** [M03](#m03)–[M04](#m04) and [M07](#m07).
- **Story role:** This prepares the two separate uses of charge dynamics: arbitrary-input observable bounds and exact evolution of a specified invariant family.
- **Conceptual connection:** A closed two-point equation can hold for every state even though two-point data reconstructs only Gaussian states; this distinction is essential to a universal quantum claim.
- **Source pointers:** The ordered-word charge representation, covariance equation, and Gaussian reconstruction conditions are supplied by T1 in the canonical scientific page below.
- **Canonical science:** [Charge transport: Positions and the ordered spin word](../science/charge_transport.md#positions-and-the-ordered-spin-word); [Charge transport: Reduction of arbitrary physical states](../science/charge_transport.md#reduction-of-arbitrary-physical-states); [Charge transport: Covariance evolution](../science/charge_transport.md#covariance-evolution).

<a id="m09"></a>

### M09. Number symmetry and quantum coherences

- **Central question:** How does number covariance organize the parts of a quantum channel without removing them physically?
- **Understanding target:** Define number twirling and fixed charge-difference Fourier components. Explain covariance of definite-charge jumps, the finite range $`-L,\ldots,L`$, and the distinction between a proof decomposition and an implemented dephasing operation.
- **Earlier dependencies:** [M02](#m02)–[M04](#m04), [M06](#m06), and [M08](#m08).
- **Story role:** This gives the organization needed to restore the coherences not visible in a charge marginal.
- **Conceptual connection:** The same symmetry that permits an exact reduction of number-diagonal observables also permits a separate complete bound on cross-number coherences.
- **Source pointers:** The exact number twirl, covariance statement, and finite charge-difference decomposition are supplied by T1 and M1 in the canonical scientific pages below.
- **Canonical science:** [Charge transport: Reduction of arbitrary physical states](../science/charge_transport.md#reduction-of-arbitrary-physical-states); [Complete mixing: Coherences with nonzero charge difference](../science/channel_mixing.md#coherences-with-nonzero-charge-difference); [Complete mixing: Sum over all charge differences](../science/channel_mixing.md#sum-over-all-charge-differences).

<a id="m10"></a>

### M10. Stable semigroups and integrated survival

- **Central question:** What additional control is needed to turn decay of a linear drift into a uniform time bound?
- **Understanding target:** Relate a dissipative drift $`A`$, its propagator $`G(t)`$, Hurwitz stability, and the Lyapunov integral $`X=\int_0^\infty G^\dagger G\,dt`$. Separate a spectral decay rate from a bound on the full transient and its trace survival.
- **Earlier dependencies:** [M04](#m04), [M07](#m07)–[M08](#m08).
- **Story role:** This supplies the analytic language for a polynomial transport estimate without relying on a gap alone.
- **Conceptual connection:** A one-particle matrix integral can bound the expected surviving population of a many-body input when the reduction and operator order are used correctly.
- **Source pointers:** [Rivas–Huelga §2.3, pp. 8–10, Definition 2.5, Theorems 2.2–2.3](https://arxiv.org/pdf/1104.5242v2#page=8) supplies the fixed-generator semigroup framework. The one-particle stability, Lyapunov integral, and transient estimate are supplied by T2 below.
- **Canonical science:** [Charge transport: T2. Exact Gramian and a uniform survival estimate](../science/charge_transport.md#t2-exact-gramian-and-a-uniform-survival-estimate); [Charge transport: Existence and the Lyapunov equation](../science/charge_transport.md#existence-and-the-lyapunov-equation); [Charge transport: From the integrated survival to a geometric bound](../science/charge_transport.md#from-the-integrated-survival-to-a-geometric-bound).

<a id="m11"></a>

### M11. Stationary-state weighted reversal

- **Central question:** How can a stationary state relate an evolved observable to a state-evolution calculation?
- **Understanding target:** Define the invertible stationary-state sandwich and distinguish ordinary adjoints, weighted reversal, and the sign of a coherent Hamiltonian term. Recognize that a proposed reversal identity must be checked against the actual jump coefficients.
- **Earlier dependencies:** [M02](#m02), [M04](#m04)–[M05](#m05), and [M09](#m09).
- **Story role:** This prepares the passage from one known vacuum evolution to an operator statement about every input.
- **Conceptual connection:** Stationary balance can translate a question about an effect's smallest eigenvalue into a more accessible state spectrum, without reversing the laboratory Hamiltonian.
- **Source pointers:** [Rivas–Huelga §5.4, pp. 45–48](https://arxiv.org/pdf/1104.5242v2#page=45) supplies the stationary-state framework. The weighted reversal and its Hamiltonian sign are established by direct generator algebra in the canonical scientific page below.
- **Canonical science:** [Vacuum accessibility: Stationary-state reversal](../science/vacuum_accessibility.md#stationary-state-reversal) for the definitions and the type of identity to be established in M20.

<a id="m12"></a>

### M12. Complete positivity and contraction

- **Central question:** What strengthens a probability estimate into a mixing estimate that survives an arbitrary reference system?
- **Understanding target:** Distinguish scalar effect domination from CP minorization, explain Kadison-Schwarz for a unital CP adjoint, and connect complete operator-norm bounds to diamond-norm bounds. Identify where rank-one support and symmetry enter such arguments.
- **Earlier dependencies:** [M02](#m02), [M06](#m06)–[M07](#m07), and [M09](#m09).
- **Story role:** This assembles the norm and positivity concepts used in the complete mixing proof.
- **Conceptual connection:** Complete positivity is both a physical constraint on a channel and the mathematical property that controls its extension to unseen reference correlations.
- **Source pointers:** [Rivas–Huelga §4.2, pp. 26–29](https://arxiv.org/pdf/1104.5242v2#page=26) supplies complete positivity, and [Rivas–Huelga §4.3, pp. 29–30, Theorem 4.4](https://arxiv.org/pdf/1104.5242v2#page=29) supplies trace-norm contraction. CP minorization, complete Kadison-Schwarz contraction, and diamond/cb duality are developed in M1 below.
- **Canonical science:** [Complete mixing: Theorem M1](../science/channel_mixing.md#theorem-m1); [Complete mixing: Number-diagonal component](../science/channel_mixing.md#number-diagonal-component); [Complete mixing: Coherences with nonzero charge difference](../science/channel_mixing.md#coherences-with-nonzero-charge-difference); [Complete mixing: Sum over all charge differences](../science/channel_mixing.md#sum-over-all-charge-differences).

<a id="m13"></a>

### M13. Background synthesis: the erasure problem and its proof objects

- **Central question:** Which objects must a complete control comparison track from a local reservoir to a global channel?
- **Understanding target:** Assemble the fixed Hamiltonian, three control domains, stationary family, local necessary witness, reference-preserving replacement objective, charge propagator, vacuum effect, and coherence decomposition into one coherent description. State where an arbitrary-input claim needs more than a Gaussian calculation.
- **Earlier dependencies:** [M01](#m01)–[M12](#m12).
- **Story role:** This closes the preliminary phase by connecting its local definitions to the global question before the project-specific theorems are developed.
- **Conceptual connection:** The obstruction and the construction share a physical system and target but require different mathematical objects because a counterexample input and a uniform channel guarantee have different logical demands.
- **Source pointers:** The [Rivas–Huelga bridge](RIVAS_HUELGA_BRIDGE.md) assembles the source framework, particularly [Rivas–Huelga §4.2, pp. 26–29](https://arxiv.org/pdf/1104.5242v2#page=26) and [Rivas–Huelga §5.2, pp. 37–41](https://arxiv.org/pdf/1104.5242v2#page=37). The model and overview supply the project-specific comparison.
- **Canonical science:** [Model](../science/model.md); [Overview: Principal conclusions](../science/overview.md#principal-conclusions); [Overview: How the proof fits together](../science/overview.md#how-the-proof-fits-together).

## Phase II: narrative and innovation

<a id="m14"></a>

### M14. The rank-two tail-memory current

- **Central question:** Where can the probability of the protected tail label actually change?
- **Understanding target:** Construct $`Q`$ for the specified product input, prove that endpoint operations fix it, identify its single hopping pair, and derive U1 using the local down-population inclusion and the correct current constant $`J`$.
- **Earlier dependencies:** [M02](#m02)–[M03](#m03), [M07](#m07), and [M13](#m13).
- **Story role:** This is the local mechanism behind the unital obstruction and the R1–R3 resource bounds. The filling converses use a separate full-chain rightmost-spin flux.
- **Conceptual connection:** A many-body memory bottleneck is carried by a two-dimensional current subspace, so its physical time bound depends on spectral concentration rather than a count of controller pulses.
- **Source pointers:** U1 and the two-site current calculation in the canonical scientific pages below supply this result. The channel foundation is [Rivas–Huelga §4.2, pp. 26–29](https://arxiv.org/pdf/1104.5242v2#page=26).
- **Canonical science:** [Control obstruction: U1. Bottleneck inequality](../science/control_obstruction.md#u1-bottleneck-inequality); [Interpretation: A two-site calculation](../science/interpretation.md#a-two-site-calculation) for the current example.

<a id="m15"></a>

### M15. Exponential memory against all unital endpoint operations

- **Central question:** Why does the same simple input resist every allowed unital endpoint protocol for exponential time?
- **Understanding target:** Preserve $`\rho_t\leq I/3^{L-1}`$ under the stated control class and derive U2 and its local-erasure time bound for fixed $`0<\varepsilon<1/3`$. Explain the physical-time quantifiers, including strong controls, and keep a retained nonuniform controller outside that unital reduced-map assumption.
- **Earlier dependencies:** [M05](#m05)–[M07](#m07) and [M14](#m14).
- **Story role:** This promotes the local current mechanism into the first global statement about an entire endpoint control class.
- **Conceptual connection:** The obstruction combines a low-rank current with a high-rank preparation; the exponent is already certified by one measured population at the far end.
- **Source pointers:** U2 in the canonical scientific page below supplies the quantified physical-time lower bound. Its positivity framework connects to [Rivas–Huelga §4.2, pp. 26–29](https://arxiv.org/pdf/1104.5242v2#page=26).
- **Canonical science:** [Control obstruction: U2. Exponential lower bound for unital endpoint control](../science/control_obstruction.md#u2-exponential-lower-bound-for-unital-endpoint-control); [Control obstruction: Control scope and physical meaning](../science/control_obstruction.md#control-scope-and-physical-meaning).

<a id="m16"></a>

### M16. Exact charge reduction and the mixed-word lift

- **Central question:** Which parts of the full spinful evolution can be computed through free charge dynamics exactly?
- **Understanding target:** Prove the reduction identity for arbitrary inputs and time-dependent spin-independent gain/loss rates, including the factor of two in spin injection. Separately prove invariance and trace-norm preservation of the mixed-word lift, and derive the covariance equation with its precise domain of reconstruction.
- **Earlier dependencies:** [M03](#m03)–[M04](#m04), [M08](#m08)–[M09](#m09), and [M13](#m13).
- **Story role:** This establishes the exact bridge from the physical chain to the tools used by both constructive erasure and the filling-floor converse.
- **Conceptual connection:** Erasing the word in a mathematical marginal is not the same operation as physically erasing it; the reduction and the lift answer distinct questions.
- **Source pointers:** T1 in the canonical scientific page below supplies the full physical-to-charge intertwining, mixed-word lift, and Gaussian-scope statements. These identities are derived for the specified endpoint generator.
- **Canonical science:** [Charge transport: T1. Exact charge reduction](../science/charge_transport.md#t1-exact-charge-reduction); [Charge transport: Reduction of arbitrary physical states](../science/charge_transport.md#reduction-of-arbitrary-physical-states); [Charge transport: The invariant family with mixed words](../science/charge_transport.md#the-invariant-family-with-mixed-words); [Charge transport: Covariance evolution](../science/charge_transport.md#covariance-evolution).

<a id="m17"></a>

### M17. The exact cubic survival estimate

- **Central question:** How does the one-particle drift produce an input-uniform polynomial survival bound?
- **Understanding target:** Establish Hurwitz stability for the actual endpoint drift, verify the explicit Gramian solution, obtain $`T_L=\Theta(L^3)`$, and turn its trace integral into $`f_\gamma(2mT_L)\leq2^{-m}`$ for $`m\geq1`$.
- **Earlier dependencies:** [M07](#m07), [M10](#m10), and [M16](#m16).
- **Story role:** This converts the exact reduction into a quantitative time scale without an uncontrolled transient prefactor.
- **Conceptual connection:** The same integrated survival estimate controls near-vacuum preparation under pure loss and uniform vacuum accessibility at positive filling, connecting two uses of the charge dynamics.
- **Source pointers:** [Rivas–Huelga §2.3, pp. 8–10](https://arxiv.org/pdf/1104.5242v2#page=8) supplies the semigroup framework. T2 and the two-site calculation below supply the exact Gramian, its cubic trace, and the uniform survival estimate.
- **Canonical science:** [Charge transport: T2. Exact Gramian and a uniform survival estimate](../science/charge_transport.md#t2-exact-gramian-and-a-uniform-survival-estimate); [Charge transport: Uniform loss bound for every input](../science/charge_transport.md#uniform-loss-bound-for-every-input); [Interpretation: A two-site calculation](../science/interpretation.md#a-two-site-calculation) for the Gramian example.

<a id="m18"></a>

### M18. Draining an unknown state also decouples its reference

- **Central question:** Why does high vacuum probability imply erasure of quantum correlations in the ideal drain?
- **Understanding target:** Combine the arbitrary-input number bound with rank-one vacuum projection, gentle projection, and the reference marginal's positive remainder. Derive the joint bound $`D\leq\sqrt u+u/2`$ and its uniform channel consequence.
- **Earlier dependencies:** [M06](#m06)–[M07](#m07), [M12](#m12), and [M16](#m16)–[M17](#m17).
- **Story role:** This is the first step that turns a particle-removal estimate into a complete information-erasure statement.
- **Conceptual connection:** A unique zero-particle system state cannot retain system-reference information, but controlling this claim requires a joint-state estimate rather than vacuum population alone.
- **Source pointers:** [Rivas–Huelga §4.1, pp. 24–25, Theorem 4.1](https://arxiv.org/pdf/1104.5242v2#page=24) supplies the exact pure-marginal product statement, and [Rivas–Huelga §4.3, pp. 29–30, Theorem 4.4](https://arxiv.org/pdf/1104.5242v2#page=29) supplies trace contraction. E1 below proves the quantitative approximate reference-decoupling estimate.
- **Canonical science:** [Ideal erasure: Draining also decouples the reference](../science/erasure_protocol.md#draining-also-decouples-the-reference); [Charge transport: Uniform loss bound for every input](../science/charge_transport.md#uniform-loss-bound-for-every-input).

<a id="m19"></a>

### M19. Refilling and universal ideal erasure

- **Central question:** How can a known drained state be refilled without restoring dependence on the unknown input?
- **Understanding target:** Use the mixed-word Gaussian evolution and Bernoulli coupling to bound refill error, combine that bound with [M18](#m18) under channel contraction, and recover the explicit one-switch schedule with $`O(L^3[1+\log(1/\varepsilon)])`$ time.
- **Earlier dependencies:** [M05](#m05)–[M06](#m06), [M08](#m08), [M15](#m15), and [M16](#m16)–[M18](#m18).
- **Story role:** This completes the universal ideal protocol and places it against the all-unital obstruction from [M15](#m15).
- **Conceptual connection:** A nonuniform intermediate state lets the finite-time channel approach the identity-preserving replacement channel $`\mathcal R_\pi`$, connecting an implementation's prefixes to its limiting target.
- **Source pointers:** [Rivas–Huelga §2.4, pp. 14–18, Eqs. (12)–(17)](https://arxiv.org/pdf/1104.5242v2#page=14) supplies changing-generator propagators and composition; [Rivas–Huelga §4.3, pp. 29–30, Theorem 4.4](https://arxiv.org/pdf/1104.5242v2#page=29) supplies contraction. E1 below supplies the refill estimate and the uniform schedule.
- **Canonical science:** [Ideal erasure: Refilling a known state](../science/erasure_protocol.md#refilling-a-known-state); [Ideal erasure: Composition and the explicit schedule](../science/erasure_protocol.md#composition-and-the-explicit-schedule); [Ideal erasure: E1. Ideal erasure theorem](../science/erasure_protocol.md#e1-ideal-erasure-theorem).

<a id="m20"></a>

### M20. Reversing the vacuum-effect calculation

- **Central question:** How can the full finite-filling vacuum effect be computed from one specified initial state?
- **Understanding target:** Derive the stationary-state sandwich identity for the physical qutrit generator, track both spin jump coefficients, and show why the auxiliary generator has Hamiltonian $`-H`$. Reduce the evolved vacuum effect to the reverse evolution of vacuum.
- **Earlier dependencies:** [M04](#m04)–[M05](#m05), [M11](#m11), and [M16](#m16).
- **Story role:** This opens the finite-filling argument by changing a universal-input effect problem into a known-input state problem.
- **Conceptual connection:** Mathematical reversal accesses information about the actual forward channel without adding a Hamiltonian reversal to the allowed controls.
- **Source pointers:** [Rivas–Huelga §5.4, pp. 45–48](https://arxiv.org/pdf/1104.5242v2#page=45) supplies the stationary-state framework. The precise weighted identity, physical spin factors, and auxiliary Hamiltonian reversal are derived in V1 below.
- **Canonical science:** [Vacuum accessibility: Stationary-state reversal](../science/vacuum_accessibility.md#stationary-state-reversal).

<a id="m21"></a>

### M21. The exact vacuum-accessibility spectrum

- **Central question:** Why is the worst-case vacuum probability the stationary empty-chain weight times a charge determinant?
- **Understanding target:** Diagonalize the reverse vacuum covariance, cancel the physical spin multiplicities in the sandwich, minimize over charge-mode occupations, and obtain V1. Use [M17](#m17) to establish $`E_{p,2T_L}^*(P_{\mathrm{vac}})\geq(1-p)^LI/2`$ on the full physical space.
- **Earlier dependencies:** [M05](#m05), [M08](#m08), [M16](#m16)–[M17](#m17), and [M20](#m20).
- **Story role:** This supplies the model-specific operator constant needed for a complete positive-filling mixing theorem.
- **Conceptual connection:** A Gaussian calculation for one known state yields an operator inequality valid for every non-Gaussian, coherent, or reference-entangled input.
- **Source pointers:** V1 in the canonical scientific page below supplies the complete vacuum-effect spectrum and its input-independent lower bound. The Gaussian reverse evolution is a specified-state calculation within T1.
- **Canonical science:** [Vacuum accessibility: Theorem V1](../science/vacuum_accessibility.md#theorem-v1); [Vacuum accessibility: Spectrum of the vacuum effect](../science/vacuum_accessibility.md#spectrum-of-the-vacuum-effect); [Vacuum accessibility: A uniform time interval](../science/vacuum_accessibility.md#a-uniform-time-interval).

<a id="m22"></a>

### M22. A CP replacement component for number-diagonal evolution

- **Central question:** How does uniform vacuum accessibility erase the number-diagonal part of the input?
- **Understanding target:** Construct $`F=E\mathcal D_N`$, prove $`F-q\mathcal R_{\mathrm{vac}}`$ completely positive using rank-one vacuum output, and iterate the resulting replacement decomposition. Show that the argument works with a reference because the relevant operator has zero system partial trace.
- **Earlier dependencies:** [M06](#m06), [M09](#m09), [M12](#m12), and [M21](#m21).
- **Story role:** This proves the first part of the mixing estimate while preserving the distinction between number-diagonal data and the full quantum input.
- **Conceptual connection:** A scalar vacuum probability becomes a genuine channel component only after the support and complete-positivity argument; this is the point at which a renewal intuition becomes a controlled channel bound.
- **Source pointers:** [Rivas–Huelga §4.2, pp. 26–29, Theorem 4.3](https://arxiv.org/pdf/1104.5242v2#page=26) supplies the CP-map foundation. M1 below proves the replacement minorization and its complete iteration; [related work](../references/related_work.md#complete-contraction-and-channel-resources) identifies the established contraction framework.
- **Canonical science:** [Complete mixing: Number-diagonal component](../science/channel_mixing.md#number-diagonal-component); [Complete mixing: Theorem M1](../science/channel_mixing.md#theorem-m1) for the rank-one and finite-charge hypotheses.

<a id="m23"></a>

### M23. Complete contraction of charge coherences

- **Central question:** How are the quantum coherences omitted by number twirling controlled in the actual unmeasured evolution?
- **Understanding target:** Use the sign of a nonzero charge difference to exclude vacuum from the appropriate support, apply complete Kadison-Schwarz, and sum the at most $`2L`$ Fourier components. Combine with [M22](#m22) to derive the half-diamond bound M1.
- **Earlier dependencies:** [M06](#m06), [M09](#m09), [M12](#m12), and [M21](#m21)–[M22](#m22).
- **Story role:** This closes the quantum and reference-system part of the finite-filling proof.
- **Conceptual connection:** Covariance makes a proof decomposition reversible at the level of bounds: the population component and all coherence components together certify the original channel without applying dephasing.
- **Source pointers:** [Rivas–Huelga §4.2, pp. 26–29](https://arxiv.org/pdf/1104.5242v2#page=26) supplies the spectator-system foundation. M1 below proves complete coherence-sector contraction, the Fourier sum, and the diamond/cb norm step.
- **Canonical science:** [Complete mixing: Coherences with nonzero charge difference](../science/channel_mixing.md#coherences-with-nonzero-charge-difference); [Complete mixing: Sum over all charge differences](../science/channel_mixing.md#sum-over-all-charge-differences); [Complete mixing: Application to the coherent chain](../science/channel_mixing.md#application-to-the-coherent-chain).

<a id="m24"></a>

### M24. The matching fixed-filling exponent

- **Central question:** Why does the inverse stationary vacuum weight determine the exact leading mixing exponent?
- **Understanding target:** Convert [M21](#m21)–[M23](#m23) into the channel upper bound, derive the all-up input's rightmost-spin flux lower bound through the Gaussian tail-empty determinant, and squeeze the exponential rate to $`-\log(1-p)`$. Distinguish this input and observable from [M14](#m14)–[M15](#m15). The exponential limit uses fixed $`J,\gamma>0`$, fixed $`0<p\leq2/3`$, and fixed $`0<\varepsilon<1/2`$.
- **Earlier dependencies:** [M05](#m05)–[M06](#m06), [M15](#m15)–[M17](#m17), and [M21](#m21)–[M23](#m23).
- **Story role:** This gives the first matching quantitative law for the full coherent channel.
- **Conceptual connection:** The same empty-chain weight appears in a universal accessibility upper bound and an input-specific memory lower bound, while polynomial transport factors do not affect the leading exponent.
- **Source pointers:** [Rivas–Huelga §5.4, pp. 45–48](https://arxiv.org/pdf/1104.5242v2#page=45) supplies the qualitative relaxation framework. F1 below gives the matching quantitative, size-dependent, complete-channel law.
- **Canonical science:** [Reservoir threshold: Theorem F1](../science/reservoir_threshold.md#theorem-f1); [Reservoir threshold: Complete channel upper bound](../science/reservoir_threshold.md#complete-channel-upper-bound); [Reservoir threshold: Rightmost-spin obstruction](../science/reservoir_threshold.md#rightmost-spin-obstruction).

<a id="m25"></a>

### M25. A filling-floor obstruction for every allowed schedule

- **Central question:** Why can arbitrary predetermined changes of gain and loss not evade a positive filling floor?
- **Understanding target:** Derive the positive-source equation for $`C-p_LI`$ in integral form for bounded measurable rates, preserve its positivity, and integrate the rightmost-spin flux. Obtain the lower bound with $`\alpha(t)+\beta(t)\leq\Gamma`$ for erasure into the fixed target $`\pi`$ at $`0<\varepsilon<1/2`$.
- **Earlier dependencies:** [M04](#m04), [M07](#m07), [M16](#m16), and [M24](#m24).
- **Story role:** This strengthens a constant-reservoir obstruction to a converse for the full stated family of open-loop schedules.
- **Conceptual connection:** The reservoir filling is not assumed to equal the instantaneous system density; the covariance lower bound is a dynamical consequence of the chosen input and the permitted control floor.
- **Source pointers:** [Rivas–Huelga §2.4, pp. 14–18](https://arxiv.org/pdf/1104.5242v2#page=14) supplies the two-parameter propagator framework, and [Rivas–Huelga §5.2, pp. 37–41, Theorem 5.1](https://arxiv.org/pdf/1104.5242v2#page=37) supplies time-dependent GKSL evolution. F2 below provides the positive-source covariance comparison and its reservoir-floor converse.
- **Canonical science:** [Reservoir threshold: Theorem F2](../science/reservoir_threshold.md#theorem-f2); [Reservoir threshold: Converse for every allowed schedule](../science/reservoir_threshold.md#converse-for-every-allowed-schedule).

<a id="m26"></a>

### M26. The sharp one-switch filling criterion

- **Central question:** Exactly which filling floors still permit polynomial-time erasure of every quantum input?
- **Understanding target:** Prepare $`\Pi_{p_L}`$ uniformly through [M23](#m23), apply the known-state refill estimate, and combine with [M25](#m25) to prove the equivalence of polynomial time and $`Lp_L=O(\log L)`$. Interpret dilute, logarithmic-over-length, superpolynomial, and fixed-filling regimes at fixed error. The classification concerns $`0\leq p_L\leq2/3`$ within the stated bounded-rate, open-loop, spin-independent gain/loss class.
- **Earlier dependencies:** [M17](#m17), [M19](#m19), [M23](#m23)–[M25](#m25).
- **Story role:** This completes the central reservoir classification and explains why the intermediate target need not be close to vacuum.
- **Conceptual connection:** Rare vacuum accessibility, rather than approximate vacuum preparation, permits imperfect draining; a size-dependent control constraint becomes a sharp global time classification.
- **Source pointers:** [Rivas–Huelga §2.4, pp. 14–18](https://arxiv.org/pdf/1104.5242v2#page=14) and [Rivas–Huelga §4.3, pp. 29–30, Theorem 4.4](https://arxiv.org/pdf/1104.5242v2#page=29) support composition and propagation of error. F2 below supplies the sharp filling criterion and the worked regimes.
- **Canonical science:** [Reservoir threshold: Uniform construction with one reservoir change](../science/reservoir_threshold.md#uniform-construction-with-one-reservoir-change); [Reservoir threshold: The resulting time regimes](../science/reservoir_threshold.md#the-resulting-time-regimes); [Interpretation: Filling regimes](../science/interpretation.md#filling-regimes).

<a id="m27"></a>

### M27. Necessary temporary nonuniformity of the system

- **Central question:** What property must every fast endpoint protocol create somewhere along its trajectory?
- **Understanding target:** Derive R1 from local success at $`0<\varepsilon<1/3`$, obtain the extensive min-entropy-deficit excursion at polynomial time, and express the condition through actual prefix channels when initialization is independent. Keep the statement valid with retained memory without inferring an average-entropy or heat cost.
- **Earlier dependencies:** [M06](#m06)–[M07](#m07), [M14](#m14)–[M15](#m15), [M19](#m19), and [M26](#m26).
- **Story role:** This interprets the control separation as a necessary spectral property of any fast implementation, beyond the particular reservoir construction.
- **Conceptual connection:** The target replacement channel preserves the identity, while a fast implementation that approaches it must contain prefixes with substantial nonuniformity. Implementation properties therefore depend on more than the final target channel.
- **Source pointers:** [Rivas–Huelga §4.2, pp. 26–29](https://arxiv.org/pdf/1104.5242v2#page=26) supplies the state-independent reduced-channel framework. R1 and R1a below supply the trajectory and prefix nonuniformity statements, with their stated initialization assumptions.
- **Canonical science:** [Resources: R1. Temporary system nonuniformity](../science/resources.md#r1-temporary-system-nonuniformity); [Resources: The spectral meaning of the bound](../science/resources.md#the-spectral-meaning-of-the-bound); [Resources: Prefix-channel formulation](../science/resources.md#prefix-channel-formulation).

<a id="m28"></a>

### M28. Endpoint-channel budget and its continuous envelope

- **Central question:** How can the required nonuniformity be related to the operations supplied by a specified memoryless controller?
- **Understanding target:** Establish the exact complete increasing power $`b(\mathcal E)=\log\|\mathcal E(I)\|_\infty`$, its CP-order max-relative-entropy and robustness forms, and the necessary accumulated budget R2. Derive the positive-source continuous envelope and distinguish it from the actual prefix-channel quantity.
- **Earlier dependencies:** [M02](#m02), [M07](#m07), [M12](#m12), and [M27](#m27).
- **Story role:** This quantifies one explicit operational realization of the general spectral necessity without turning that budget into a sufficient mixing condition.
- **Conceptual connection:** Operator order links resource generation, distance from unital channels, and a physical-time obstruction, but a chosen decomposition can overcount what the composite evolution actually generates.
- **Source pointers:** [Rivas–Huelga §4.2, pp. 26–29](https://arxiv.org/pdf/1104.5242v2#page=26) and [Rivas–Huelga §5.2, pp. 37–41](https://arxiv.org/pdf/1104.5242v2#page=37) supply channel and continuous-generator foundations. R2 below derives the complete increasing power, CP-order resource identities, accumulated budget, and continuous envelope.
- **Canonical science:** [Resources: R2. Accumulated channel budget](../science/resources.md#r2-accumulated-channel-budget); [Resources: Exact increase of the min-entropy deficit](../science/resources.md#exact-increase-of-the-min-entropy-deficit); [Resources: Exact relation to channel max-relative entropy](../science/resources.md#exact-relation-to-channel-max-relative-entropy); [Resources: Continuous endpoint generators](../science/resources.md#continuous-endpoint-generators).

<a id="m29"></a>

### M29. The finite-controller resource model

- **Central question:** Which initial controller resource can weaken the unital memory obstruction?
- **Understanding target:** Derive R3 from joint unital domination and the joint current trace, interpret $`K\|\sigma_C\|_\infty`$, and recover the maximally mixed and preallocated pure-ancilla cases. State the independence, retained-output, and joint-unital assumptions that make this a finite-controller claim.
- **Earlier dependencies:** [M02](#m02), [M06](#m06)–[M07](#m07), [M14](#m14)–[M15](#m15), and [M27](#m27)–[M28](#m28).
- **Story role:** This places coherent controller memory inside a precise enlarged model instead of incorrectly applying the reduced unital theorem to it.
- **Conceptual connection:** Controller dimension is useful only together with initial nonuniformity; an arbitrarily large maximally mixed controller does not remove this bottleneck.
- **Source pointers:** [Rivas–Huelga §4.2, pp. 26–29](https://arxiv.org/pdf/1104.5242v2#page=26) supplies the joint-channel framework. R3 below provides the initial-controller resource count and its retained-ancilla scope.
- **Canonical science:** [Resources: R3. Finite controller resource](../science/resources.md#r3-finite-controller-resource); [Resources: What the controller factor counts](../science/resources.md#what-the-controller-factor-counts); [Model: Boundary controls](../science/model.md#boundary-controls).

<a id="m30"></a>

### M30. Full synthesis: boundary memory, erasure, and resources

- **Central question:** What complete statement about controllable boundary memory follows from the project, and which assumptions make each part true?
- **Understanding target:** Reconstruct the same-Hamiltonian unital obstruction and universal erasure comparison, the matching fixed-filling exponent, the necessary-and-sufficient filling scale, and the three resource interpretations. Assign every conclusion its control class, input quantifier, error convention, and proof mechanism. Distinguish sharp laws from nonoptimal polynomial factors, analytic proofs from finite algebra checks, and the complete contribution from established ingredients in the inspected sources.
- **Earlier dependencies:** [M13](#m13)–[M29](#m29).
- **Story role:** This closes the narrative phase by assembling all results and their exact relationship rather than introducing a new theorem.
- **Conceptual connection:** Ordered-spin memory, local dissipation, a free-charge estimate, rare-state renewal, complete quantum contraction, and one-shot nonuniformity jointly explain one global operational classification.
- **Source pointers:** The [Rivas–Huelga bridge](RIVAS_HUELGA_BRIDGE.md) connects the verified evolution framework, including [Rivas–Huelga §4.2, pp. 26–29](https://arxiv.org/pdf/1104.5242v2#page=26) and [Rivas–Huelga §5.4, pp. 45–48](https://arxiv.org/pdf/1104.5242v2#page=45), to the project. The canonical scientific pages, related-work comparison, and verification account below establish the claims and their evidence boundaries.
- **Canonical science:** [Overview](../science/overview.md); [Interpretation](../science/interpretation.md); [Model: Boundary controls](../science/model.md#boundary-controls); [Reservoir threshold](../science/reservoir_threshold.md); [Resources](../science/resources.md); [Related work: The complete relationship](../references/related_work.md#the-complete-relationship); [Verification: What each check establishes](../verification/README.md#what-each-check-establishes).

The [Rivas–Huelga bridge](RIVAS_HUELGA_BRIDGE.md) supplies the source-to-project connection throughout both phases. The [canonical scientific account](../science/overview.md) remains the authority for the exact model, derivations, and quantified conclusions.
