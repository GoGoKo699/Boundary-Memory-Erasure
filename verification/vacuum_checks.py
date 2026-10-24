"""Independent finite-dimensional audit of the leaky-bath vacuum effect.

Checks the physical qutrit Lindbladian, its KMS reversal, and the claimed
vacuum-effect spectrum.  The analytic argument in science/vacuum_accessibility.md is primary.
"""

import itertools

import numpy as np
from scipy.linalg import expm
from scipy.sparse import csr_matrix, eye, kron
from scipy.sparse.linalg import expm_multiply


def tensor(ops):
    out = csr_matrix([[1.0]])
    for op in ops:
        out = kron(out, csr_matrix(op), format="csr")
    return out


def local(op, site, length):
    return tensor([op if j == site else np.eye(3) for j in range(length)])


def dissipator(jump):
    dim = jump.shape[0]
    ident = eye(dim, format="csr")
    rate = jump.conj().T @ jump
    return kron(jump.conjugate(), jump, format="csr") - 0.5 * (
        kron(ident, rate, format="csr")
        + kron(rate.T, ident, format="csr")
    )


def audit(length, hopping, gamma, filling, duration):
    dim = 3 ** length
    ident = eye(dim, format="csr")
    lowering = []
    for spin in (1, 2):
        op = np.zeros((3, 3))
        op[0, spin] = 1
        lowering.append(op)
    ham = csr_matrix((dim, dim), dtype=complex)
    for site in range(length - 1):
        for low in lowering:
            term = local(low.conj().T, site, length) @ local(low, site + 1, length)
            ham += hopping * (term + term.conj().T)
    loss = gamma * (1 - filling)
    total_gain = gamma * filling
    dis = csr_matrix((dim * dim, dim * dim), dtype=complex)
    for low in lowering:
        boundary = local(low, 0, length)
        dis += loss * dissipator(boundary)
        dis += total_gain / 2 * dissipator(boundary.conj().T)
    ham_super = -1j * (kron(ident, ham) - kron(ham.T, ident))
    generator = ham_super + dis
    reverse_generator = -ham_super + dis
    vac = np.zeros((dim, dim), dtype=complex)
    vac[0, 0] = 1
    vecvac = vac.ravel(order="F")
    effect = expm_multiply(duration * generator.conj().T, vecvac).reshape(
        (dim, dim), order="F"
    )
    reverse_output = expm_multiply(duration * reverse_generator, vecvac).reshape(
        (dim, dim), order="F"
    )
    weights = np.array([1.0])
    for _ in range(length):
        weights = np.kron(weights, [1 - filling, filling / 2, filling / 2])
    kms_effect = (1 - filling) ** length * reverse_output / np.sqrt(
        weights[:, None] * weights[None, :]
    )
    h = hopping * (np.eye(length, k=1) + np.eye(length, k=-1))
    drift = -1j * h.astype(complex)
    drift[0, 0] -= gamma / 2
    contraction = expm(duration * drift)
    eta = np.linalg.eigvalsh(contraction.conj().T @ contraction)
    minimum_formula = (1 - filling) ** length * np.prod(1 - eta)
    effect_eigenvalues = np.linalg.eigvalsh((effect + effect.conj().T) / 2)
    minimum_direct = effect_eigenvalues.min()
    # Each occupied charge mode contributes spin-word multiplicity two.
    # Comparing the complete spectrum checks these degeneracies as well as
    # the single extremal eigenvalue used by the accessibility bound.
    spectrum_formula = []
    for occupations in itertools.product((0, 1), repeat=length):
        eigenvalue = np.prod([
            (1 - filling) * (1 - value) if occupied
            else 1 - filling + filling * value
            for value, occupied in zip(eta, occupations)
        ])
        spectrum_formula.extend([eigenvalue] * 2**sum(occupations))
    spectrum_error = np.max(np.abs(effect_eigenvalues - np.sort(spectrum_formula)))
    return {
        "L": length,
        "J": hopping,
        "gamma": gamma,
        "p": filling,
        "t": duration,
        "KMS_operator_residual": float(np.linalg.norm(effect - kms_effect, 2)),
        "vacuum_effect_hermiticity": float(np.linalg.norm(effect - effect.conj().T, 2)),
        "minimum_direct": float(minimum_direct),
        "minimum_formula": float(minimum_formula),
        "minimum_absolute_error": float(abs(minimum_direct - minimum_formula)),
        "spectrum_max_absolute_error": float(spectrum_error),
    }


def run():
    cases = [
        audit(1, 0.8, 1.2, 0.13, 1.7),
        audit(2, 0.8, 1.2, 0.13, 2.3),
        audit(3, 0.8, 1.2, 0.13, 7.1),
        audit(3, 1.1, 0.7, 0.37, 8.0),
        audit(3, 0.6, 1.5, 2 / 3, 6.2),
    ]
    tolerance = 1e-10
    for row in cases:
        if max(row['KMS_operator_residual'], row['vacuum_effect_hermiticity'],
               row['minimum_absolute_error'], row['spectrum_max_absolute_error']) >= tolerance:
            raise AssertionError(row)
    return {'tolerance': tolerance, 'cases': cases}

