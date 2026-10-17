"""Finite qutrit/charge operator checks in the fixed-total-rate convention."""
import itertools

import numpy as np


def physical_data(n, hopping=1.0):
    states = list(itertools.product(range(3), repeat=n))
    index = {s: k for k, s in enumerate(states)}
    dim = len(states)
    h = np.zeros((dim, dim), dtype=complex)
    for k, s in enumerate(states):
        for j in range(n - 1):
            if (s[j] == 0) != (s[j + 1] == 0):
                u = list(s)
                u[j], u[j + 1] = u[j + 1], u[j]
                h[index[tuple(u)], k] += hopping
    losses = []
    for color in (1, 2):
        a = np.zeros_like(h)
        for k, s in enumerate(states):
            if s[0] == color:
                a[index[(0,) + s[1:]], k] = 1
        losses.append(a)
    return states, index, h, losses


def charge_data(n, hopping=1.0):
    states = list(itertools.product(range(2), repeat=n))
    index = {s: k for k, s in enumerate(states)}
    dim = len(states)
    h = np.zeros((dim, dim), dtype=complex)
    a = np.zeros_like(h)
    for k, s in enumerate(states):
        if s[0]:
            a[index[(0,) + s[1:]], k] = 1
        for j in range(n - 1):
            if s[j] != s[j + 1]:
                u = list(s)
                u[j], u[j + 1] = u[j + 1], u[j]
                h[index[tuple(u)], k] += hopping
    return states, index, h, a


def dissipator(a, rho):
    aa = a.conj().T @ a
    return a @ rho @ a.conj().T - (aa @ rho + rho @ aa) / 2


def generator(h, jumps, rho):
    out = -1j * (h @ rho - rho @ h)
    for a in jumps:
        out += dissipator(a, rho)
    return out


def charge_trace(rho, physical_states, charge_index):
    out = np.zeros((len(charge_index), len(charge_index)), dtype=complex)
    words = [tuple(x for x in s if x) for s in physical_states]
    occupancies = [charge_index[tuple(int(x != 0) for x in s)]
                   for s in physical_states]
    for j, wj in enumerate(words):
        for k, wk in enumerate(words):
            if wj == wk:
                out[occupancies[j], occupancies[k]] += rho[j, k]
    return out


def isotropic_lift(sigma, physical_states, charge_index):
    dim = len(physical_states)
    out = np.zeros((dim, dim), dtype=complex)
    words = [tuple(x for x in s if x) for s in physical_states]
    occupancies = [charge_index[tuple(int(x != 0) for x in s)]
                   for s in physical_states]
    for j, wj in enumerate(words):
        for k, wk in enumerate(words):
            if wj == wk:
                out[j, k] = sigma[occupancies[j], occupancies[k]] / 2 ** len(wj)
    return out


def adjoint_generator(h, jumps, observable):
    out = 1j * (h @ observable - observable @ h)
    for a in jumps:
        rate = a.conj().T @ a
        out += a.conj().T @ observable @ a - (
            rate @ observable + observable @ rate
        ) / 2
    return out


def run():
    results = []
    tolerance = 1e-10
    hopping, gamma = 0.8, 1.2
    for length in (2, 3, 4):
        ps, pi, h, losses = physical_data(length, hopping)
        cs, ci, hc, a = charge_data(length, hopping)
        dim = len(ps)
        rng = np.random.default_rng(20261017 + length)
        z = rng.normal(size=dim) + 1j * rng.normal(size=dim)
        z /= np.linalg.norm(z)
        rho = np.outer(z, z.conj())
        sigma = charge_trace(rho, ps, ci)

        tail_up, last_down, rightmost_up = [], [], []
        for state in ps:
            tail = [s for s in state[1:] if s]
            word = [s for s in state if s]
            tail_up.append(bool(tail) and tail[-1] == 1)
            last_down.append(state[-1] == 2)
            rightmost_up.append(bool(word) and word[-1] == 1)
        q = np.diag(np.array(tail_up, dtype=float))
        p = np.diag(np.array(rightmost_up, dtype=float))
        current = 1j * (h @ q - q @ h)
        spectrum = np.linalg.eigvalsh(current)
        nonzero = spectrum[np.abs(spectrum) > tolerance]
        if len(nonzero) != 2 or not np.allclose(nonzero, [-hopping, hopping]):
            raise AssertionError('The bottleneck current is not the claimed rank-two block.')
        if int(np.trace(q)) != (3**length - 3) // 2:
            raise AssertionError('Incorrect tail-projector rank.')
        if np.any(np.array(last_down, int) + np.array(tail_up, int) > 1):
            raise AssertionError('The local down-population witness is not below I-Q.')

        endpoint_residual = 0.0
        for row in range(3):
            for col in range(3):
                unit = np.zeros((3, 3))
                unit[row, col] = 1
                op = np.kron(unit, np.eye(3**(length - 1)))
                endpoint_residual = max(endpoint_residual, np.linalg.norm(op @ q - q @ op))
        vacuum = np.zeros((dim, dim), complex)
        vacuum[pi[(0,) * length], pi[(0,) * length]] = 1
        one_up = np.zeros_like(vacuum)
        location = pi[(1,) + (0,) * (length - 1)]
        one_up[location, location] = 1

        for filling in (0.0, 0.13, 2 / 3):
            alpha, beta = gamma * filling, gamma * (1 - filling)
            jumps = [np.sqrt(beta) * x for x in losses]
            jumps += [np.sqrt(alpha / 2) * x.conj().T for x in losses]
            charge_jumps = [np.sqrt(beta) * a, np.sqrt(alpha) * a.conj().T]
            charge_error = np.linalg.norm(
                charge_trace(generator(h, jumps, rho), ps, ci)
                - generator(hc, charge_jumps, sigma)
            )
            lift_error = np.linalg.norm(
                generator(h, jumps, isotropic_lift(sigma, ps, ci))
                - isotropic_lift(generator(hc, charge_jumps, sigma), ps, ci)
            )
            charge_stationary = np.diag([
                filling**sum(state) * (1 - filling)**(length - sum(state))
                for state in cs
            ])
            physical_weights = np.array([1.0])
            for _ in range(length):
                physical_weights = np.kron(
                    physical_weights, [1 - filling, filling / 2, filling / 2]
                )
            target = np.diag(physical_weights)
            target_error = np.linalg.norm(isotropic_lift(charge_stationary, ps, ci) - target)
            stationary_error = np.linalg.norm(generator(h, jumps, target))
            rightmost_error = np.linalg.norm(
                adjoint_generator(h, jumps, p) - (alpha * vacuum / 2 - beta * one_up)
            )

            # At L=2, verify charge intertwining on every physical matrix unit.
            full_basis_error = 0.0
            if length == 2:
                for row in range(dim):
                    for col in range(dim):
                        unit = np.zeros((dim, dim), complex)
                        unit[row, col] = 1
                        full_basis_error = max(full_basis_error, np.linalg.norm(
                            charge_trace(generator(h, jumps, unit), ps, ci)
                            - generator(hc, charge_jumps, charge_trace(unit, ps, ci))
                        ))
            maximum = max(charge_error, lift_error, target_error, stationary_error,
                          rightmost_error, endpoint_residual, full_basis_error)
            if maximum >= tolerance:
                raise AssertionError((length, filling, maximum))
            results.append({
                'L': length, 'J': hopping, 'gamma': gamma, 'p': filling,
                'charge_intertwining_residual': float(charge_error),
                'mixed_word_lift_residual': float(lift_error),
                'stationary_lift_residual': float(target_error),
                'stationarity_residual': float(stationary_error),
                'rightmost_spin_generator_residual': float(rightmost_error),
                'all_endpoint_matrix_unit_commutator': float(endpoint_residual),
                'full_charge_intertwining_basis_size': dim**2 if length == 2 else 0,
                'full_basis_max_residual': float(full_basis_error),
                'current_nonzero_eigenvalues': nonzero.tolist(),
                'tail_projector_rank': int(np.trace(q)),
                'maximum_residual': float(maximum),
            })
    return {'tolerance': tolerance, 'cases': results}

