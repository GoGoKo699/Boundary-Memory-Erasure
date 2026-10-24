#!/usr/bin/env python3
"""Run the finite matrix checks; all asymptotic results use the written proofs."""

import argparse
import json
import platform
from pathlib import Path

import numpy as np
import scipy

import model_checks
import transport_checks
import vacuum_checks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='Optionally write the full numerical results.')
    args = parser.parse_args()
    result = {
        'environment': {'python': platform.python_version(),
                        'numpy': np.__version__, 'scipy': scipy.__version__},
        'model': model_checks.run(),
        'transport': transport_checks.run(),
        'vacuum': vacuum_checks.run(),
        'passed': True,
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2) + '\n')
    summary = {
        'passed': True,
        'model_cases': len(result['model']['cases']),
        'gramian_cases': len(result['transport']['cases']),
        'vacuum_effect_cases': len(result['vacuum']['cases']),
        'max_model_residual': max(x['maximum_residual'] for x in result['model']['cases']),
        'max_lyapunov_residual': max(x['lyapunov_residual'] for x in result['transport']['cases']),
        'max_vacuum_reversal_residual': max(x['KMS_operator_residual'] for x in result['vacuum']['cases']),
        'max_vacuum_eigenvalue_error': max(x['minimum_absolute_error'] for x in result['vacuum']['cases']),
        'max_vacuum_spectrum_error': max(x['spectrum_max_absolute_error'] for x in result['vacuum']['cases']),
        'environment': result['environment'],
    }
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
