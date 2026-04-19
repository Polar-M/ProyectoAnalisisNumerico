"""
Test — Gaussian Elimination with Total Pivoting
===============================================
Runs test case and prints the elimination stages and final solution.

To run:
    python tests/chapter2_linear_systems/test_gaussian_elimination_TP.py
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import numpy as np
from methods.chapter2_linear_systems.gaussian_elimination_TP import gaussian_elimination_TP


# ──────────────────────────────────────────────
# Helper to print matrices nicely
# ──────────────────────────────────────────────
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{val:10.6f}" for val in row))
    print()


# ──────────────────────────────────────────────
# Helper to print results consistently
# ──────────────────────────────────────────────
def print_results(label: str, x, stages):
    print(f"\n{'='*55}")
    print(f"  {label}")
    print(f"{'='*55}\n")

    for i, stage in enumerate(stages):
        print(f"Stage {i}")
        print_matrix(stage)

    print("After back substitution:\n")
    print("x:")
    for xi in x:
        print(f"{xi:.6f}")

    print()
