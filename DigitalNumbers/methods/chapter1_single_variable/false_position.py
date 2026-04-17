"""
False Position Method (Regula Falsi)
=====================================
Finds a root of f(x) = 0 on the interval [a, b] using a linear
interpolation between the endpoints to estimate the root, rather
than simply halving the interval as in bisection.

Requires: f(a) * f(b) < 0  (sign change must exist at the start)

Author: Juan Guillermo Isaza  ← replace with your name
Last updated: April 2026
"""

import numpy as np
import pandas as pd


def false_position(f, a: float, b: float, tol: float, n_max: int) -> dict:
    """
    False Position method to find a root of f(x) = 0 on [a, b].

    The new estimate is computed as:
        p = (f(b)*a - f(a)*b) / (f(b) - f(a))

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
        'root'      : float        — approximated root
        'iters'     : int          — number of iterations performed
        'error'     : float        — final absolute error
        'table'     : pd.DataFrame — iteration table
        'converged' : bool         — True if tolerance was reached
    """

    # --- Validate starting interval ---
    if f(a) * f(b) > 0:
        raise ValueError(
            f"f(a) and f(b) must have opposite signs. "
            f"Got f({a}) = {f(a):.6f}, f({b}) = {f(b):.6f}"
        )

    # --- Initialization ---
    f_a   = f(a)
    f_b   = f(b)
    p_mid = (f_b * a - f_a * b) / (f_b - f_a)   # linear interpolation
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
            "p":         round(p_mid, 10),
            "f(p)":      round(f_mid, 10),
            "error":     round(error, 10),
        })

        # Narrow the interval using the sign of f at the new point
        if f_a * f_mid < 0:
            b   = p_mid         # root is in the left sub-interval
            f_b = f_mid
        else:
            a   = p_mid         # root is in the right sub-interval
            f_a = f_mid

        p_prev = p_mid
        f_a    = f(a)
        f_b    = f(b)
        p_mid  = (f_b * a - f_a * b) / (f_b - f_a)
        f_mid  = f(p_mid)
        error  = abs(p_mid - p_prev)
        count += 1

    # Append final row
    rows.append({
        "Iteration": count,
        "a":         round(a, 10),
        "b":         round(b, 10),
        "p":         round(p_mid, 10),
        "f(p)":      round(f_mid, 10),
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
