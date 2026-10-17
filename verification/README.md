# Reproduce the finite checks

The scientific results are proved in [the topic-based account](../science/overview.md). This directory checks the finite matrix identities and conventions that those proofs use. It contains no fitted mixing exponent or extrapolation from a many-body simulation.

## Run

From the repository root, use Python 3.10 or later with NumPy and SciPy:

```bash
python -m pip install -r verification/requirements.txt
python verification/run_all.py
```

The committed reference output was produced with Python 3.12.14, NumPy 2.3.5, and SciPy 1.17.0. To save another run without replacing that record:

```bash
python verification/run_all.py --output verification/output/results.json
```

The default command prints a summary and makes no output file. Every check raises an error on failure, and the command exits nonzero. Floating-point residuals can vary across numerical libraries; the acceptance tolerances are encoded in the checks and retained in [results.json](results.json).

## What each check establishes

| Module | Finite checks | Related result |
|---|---|---|
| [model_checks.py](model_checks.py) | Physical qutrit generator versus spinless charge reduction, mixed-word lift, product stationarity, tail-current rank and spectrum, local-witness ordering, full-chain rightmost-spin flux | T1, U1–U2, F1–F2 |
| [transport_checks.py](transport_checks.py) | Explicit Gramian versus its Lyapunov equation and an independent numerical solver, positivity, trace formula, and survival at positive block times | T2 and E1 |
| [vacuum_checks.py](vacuum_checks.py) | Independently constructed sparse physical Liouvillian, reversed-vacuum operator sandwich, and minimum eigenvalue versus the determinant formula | V1 |

The model module uses $`L=2,3,4`$ and fillings $`0`$, $`0.13`$, and $`2/3`$, with $`J=0.8`$ and $`\gamma=1.2`$. It evaluates the reduction on deterministic random pure states with spin and number coherences. At $`L=2`$ it additionally checks the charge intertwining on all 81 physical matrix units at each filling, so that part is a complete finite-dimensional linear-map check. The endpoint commutators, rightmost-spin generator identity, current eigenvalues, and projector ordering are checked directly as matrices.

The transport module covers 18 choices: $`L\in\{1,2,3,4,7,12\}`$ and three positive pairs of $`J,\gamma`$. The physical chain theorem is stated for $`L\geq2`$; the one-site case checks the endpoint convention. The vacuum module covers five choices with $`L=1,2,3`$, several rates and times, and fillings $`0.13`$, $`0.37`$, and $`2/3`$. Its tensor-product construction is separate from the ordered-configuration construction in the model module.

## Reference output

The committed run passes all 9 model cases, 18 Gramian cases, and 5 vacuum-effect cases. Its largest residuals are:

| Quantity | Largest recorded residual | Acceptance threshold |
|---|---:|---:|
| Model identities | $`2.23\times10^{-16}`$ | $`10^{-10}`$ |
| Lyapunov equation | $`4.01\times10^{-14}`$ | $`10^{-9}`$ |
| Vacuum-effect reversal | $`8.92\times10^{-16}`$ | $`10^{-10}`$ |
| Minimum vacuum-effect eigenvalue | $`3.34\times10^{-16}`$ | $`10^{-10}`$ |

The rounded entries are upper roundings of the values in [results.json](results.json). Gramian relative-solution and trace errors, minimum Gramian eigenvalues, and individual cases are also retained there.

Finite checks test signs, spin degeneracies, rate factors, matrix identities, and implementation consistency. Arbitrary length, arbitrary input and reference, the complete covariant-channel lemma, and the asymptotic threshold follow from the written analytical proofs. The suite does not certify those universal statements by enumeration.
