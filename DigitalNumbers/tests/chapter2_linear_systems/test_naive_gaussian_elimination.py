"""
Test — Naive Gaussian Elimination
================================
Runs test cases and prints the elimination stages and final solution.

To run:
    python tests/chapter2_linear_systems/test_naive_gaussian_elimination.py
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import numpy as np
from methods.chapter2_linear_systems.naive_gaussian_elimination import naive_gaussian_elimination


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

# ──────────────────────────────────────────────
# Test 1 
# A = 
#   [2, -1, 0, 3]
#   [1, 0.5, 3, 8]
#   [0, 13, -2, 11]
#   [14, 5, -2, 3]
# 
# b = [1, 1, 1, 1] 
# Expected results:
# x = [0.038495, -0.180227, -0.309711, 0.247594]
# ──────────────────────────────────────────────
