"""
Test — Incremental Search Method
==================================
Runs two test cases and prints the iteration table for each.

To run:
    python tests/chapter1_single_variable/test_incremental_search.py
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import numpy as np
from methods.chapter1_single_variable.incremental_search import incremental_search

# ──────────────────────────────────────────────
# Helper to print results consistently
# ──────────────────────────────────────────────
def print_results(label: str, result: dict):
    print(f"\n{'='*55}")
    print(f"  {label}")
    print(f"{'='*55}")
    print(result["table"].to_string(index=False))
    print(f"\n  Iterations : {result['iters']}")
    if result["found"]:
        print(f"  Interval   : [{result['a']:.8f},  {result['b']:.8f}]")
        print(f"  Status     : Sign change found ✓")
    else:
        print(f"  Status     : No sign change found — try a smaller step or different x0")
    print()


# ──────────────────────────────────────────────
# Test 1 — f(x) = cos(x) - x
# Expected: root near x ≈ 0.7391
# ──────────────────────────────────────────────
f1 = lambda x: np.cos(x) - x
result1 = incremental_search(f=f1, x0=0.0, h=0.5, n_max=100)
print_results("Test 1: f(x) = cos(x) - x  |  x0=0.0, h=0.5", result1)


# ──────────────────────────────────────────────
# Test 2 — f(x) = x^3 - x - 2
# Expected: root near x ≈ 1.5214
# ──────────────────────────────────────────────
f2 = lambda x: x**3 - x - 2
result2 = incremental_search(f=f2, x0=0.0, h=0.5, n_max=100)
print_results("Test 2: f(x) = x³ - x - 2  |  x0=0.0, h=0.5", result2)
