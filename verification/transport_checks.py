"""Direct Lyapunov and survival checks; no scaling fits."""

import numpy as np
from scipy.linalg import expm, solve_continuous_lyapunov


def explicit_gramian(length, hopping, loss):
    q = np.zeros((length, length), dtype=complex)
    for j in range(1, length + 1):
        for k in range(j, length + 1):
            if (j - k) % 2 == 0:
                entry = (length + 1 - k) * (
                    j / loss + loss * (j - 1) / (4 * hopping**2)
                )
            else:
                entry = 1j * (length + 1 - k) / (2 * hopping)
            q[j - 1, k - 1] = entry
            q[k - 1, j - 1] = np.conj(entry)
    return q


def trace_formula(length, hopping, loss):
    return (
        length * (length + 1) * (length + 2) / (6 * loss)
        + loss * length * (length**2 - 1) / (24 * hopping**2)
    )


def run():
    results = []
    tolerance = 1e-9
    for length in (1, 2, 3, 4, 7, 12):
        for hopping, gamma in ((0.7, 1.3), (1.0, 0.5), (1.0, 3.0)):
            h = hopping * (np.eye(length, k=1) + np.eye(length, k=-1))
            a = -1j * h
            a[0, 0] -= gamma / 2
            x = explicit_gramian(length, hopping, gamma)
            numerical = solve_continuous_lyapunov(a.conj().T, -np.eye(length))
            residual = np.linalg.norm(a.conj().T @ x + x @ a + np.eye(length))
            relative_error = np.linalg.norm(x - numerical) / np.linalg.norm(x)
            minimum = np.linalg.eigvalsh(x).min()
            trace = trace_formula(length, hopping, gamma)
            trace_error = abs(np.trace(x).real - trace)
            survival = []
            for blocks in (1, 2, 3):
                g = expm(2 * blocks * trace * a)
                f = float(np.linalg.norm(g, 'fro')**2)
                if f > 2.0**(-blocks) + tolerance:
                    raise AssertionError('Survival exceeds the proved block bound.')
                survival.append(f)
            if max(residual, relative_error, trace_error) >= tolerance or minimum <= 0:
                raise AssertionError((length, hopping, gamma, residual, relative_error))
            results.append({
                'L': length, 'J': hopping, 'gamma': gamma,
                'lyapunov_residual': float(residual),
                'relative_solution_error': float(relative_error),
                'minimum_gramian_eigenvalue': float(minimum),
                'trace': float(trace), 'trace_error': float(trace_error),
                'survival_at_one_two_three_blocks': survival,
            })
    return {'tolerance': tolerance, 'cases': results}

