"""
Bisection Method
================
Finds a root of f(x) = 0 on the interval [a, b] by repeatedly
halving the interval and keeping the half where a sign change occurs.

Requires: f(a) * f(b) < 0  (sign change must exist at the start)

Author: Juan Guillermo Isaza  ← replace with your name
Last updated: April 2026
"""

import numpy as np
import pandas as pd


def bisection(f, a: float, b: float, tol: float, n_max: int) -> dict:
    """
    Bisection method to find a root of f(x) = 0 on [a, b].

    Parameters
    ----------
    f     : callable — continuous function f(x)
    a     : float    — left endpoint of the initial interval
    b     : float    — right endpoint of the initial interval
    tol   : float    — error tolerance (stopping criterion)
    n_max : int      — maximum number of iterations

    Returns
    -------
    dict with keys:
        'root'   : float        — approximated root
        'iters'  : int          — number of iterations performed
        'error'  : float        — final absolute error
        'table'  : pd.DataFrame — iteration table
        'converged' : bool      — True if tolerance was reached
    """

    # --- Validate starting interval ---
    if f(a) * f(b) > 0:
        raise ValueError(
            f"f(a) and f(b) must have opposite signs. "
            f"Got f({a}) = {f(a):.6f}, f({b}) = {f(b):.6f}"
        )

    # --- Initialization ---
    f_a  = f(a)
    p_mid = (a + b) / 2.0
    f_mid = f(p_mid)
    error = 1000.0
    count = 1

    rows = []

    # --- Iteration loop ---
    while error > tol and count < n_max:
        rows.append({
            "Iteration": count,
            "a":         round(a, 10),
            "b":         round(b, 10),
            "midpoint":  round(p_mid, 10),
            "f(mid)":    round(f_mid, 10),
            "error":     round(error, 10),
        })

        # Narrow the interval
        if f_a * f_mid < 0:
            b = p_mid           # root is in the left half
        else:
            a     = p_mid       # root is in the right half
            f_a   = f_mid

        p_prev = p_mid
        p_mid  = (a + b) / 2.0
        f_mid  = f(p_mid)
        error  = abs(p_mid - p_prev)
        count += 1

    # Append final row
    rows.append({
        "Iteration": count,
        "a":         round(a, 10),
        "b":         round(b, 10),
        "midpoint":  round(p_mid, 10),
        "f(mid)":    round(f_mid, 10),
        "error":     round(error, 10),
    })

    table = pd.DataFrame(rows)
    return {
        "root":      p_mid,
        "iters":     count,
        "error":     error,
        "table":     table,
        "converged": error <= tol,
    }
