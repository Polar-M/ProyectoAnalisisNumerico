"""
Test — False Position Method (Regula Falsi)
============================================
Runs two test cases and prints the iteration table for each.

To run:
    python tests/chapter1_single_variable/test_false_position.py
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import numpy as np
from methods.chapter1_single_variable.false_position import false_position

# ──────────────────────────────────────────────
# Helper to print results consistently
# ──────────────────────────────────────────────
def print_results(label: str, result: dict):
    print(f"\n{'='*55}")
    print(f"  {label}")
    print(f"{'='*55}")
    print(result["table"].to_string(index=False))
    print(f"\n  Iterations : {result['iters']}")
    print(f"  Root       : {result['root']:.10f}")
    print(f"  Error      : {result['error']:.2e}")
    print(f"  Status     : {'Converged ✓' if result['converged'] else 'Max iterations reached'}")
    print()


# ──────────────────────────────────────────────
# Test 1 — f(x) = cos(x) - x
# Interval [0, 1] | Expected root ≈ 0.7390851332
# ──────────────────────────────────────────────
f1 = lambda x: np.cos(x) - x
result1 = false_position(f=f1, a=0.0, b=1.0, tol=1e-7, n_max=100)
print_results("Test 1: f(x) = cos(x) - x  |  [0, 1]  tol=1e-7", result1)


# ──────────────────────────────────────────────
# Test 2 — f(x) = x^3 - x - 2
# Interval [1, 2] | Expected root ≈ 1.5213797068
# ──────────────────────────────────────────────
f2 = lambda x: x**3 - x - 2
result2 = false_position(f=f2, a=1.0, b=2.0, tol=1e-7, n_max=100)
print_results("Test 2: f(x) = x³ - x - 2  |  [1, 2]  tol=1e-7", result2)
