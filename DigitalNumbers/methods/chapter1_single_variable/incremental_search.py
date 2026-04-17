"""
Incremental Search Method
=========================
Finds an interval [a, b] where f(x) changes sign,
which means a root of f(x) = 0 exists in that interval
(by the Intermediate Value Theorem).

Author: Juan Guillermo Isaza  ← replace with your name
Last updated: April 2026
"""

import numpy as np
import pandas as pd


def incremental_search(f, x0: float, h: float, n_max: int) -> dict:
    """
    Searches for an interval [a, b] where f(x) changes sign.

    Parameters
    ----------
    f     : callable  — continuous function f(x)
    x0    : float     — starting point
    h     : float     — step size (increment)
    n_max : int       — maximum number of iterations

    Returns
    -------
    dict with keys:
        'a'      : float — left endpoint of the interval
        'b'      : float — right endpoint of the interval
        'iters'  : int   — number of iterations performed
        'table'  : pd.DataFrame — iteration table
        'found'  : bool  — True if a sign change was found
    """

    # --- Initialization ---
    x_prev = x0
    f_prev = f(x_prev)
    x_curr = x_prev + h
    f_curr = f(x_curr)

    rows = []

    # --- Iteration loop ---
    for i in range(1, n_max + 1):
        rows.append({
            "Iteration": i,
            "x_prev":    round(x_prev, 10),
            "f(x_prev)": round(f_prev, 10),
            "x_curr":    round(x_curr, 10),
            "f(x_curr)": round(f_curr, 10),
        })

        # Sign change found → root is bracketed
        if f_prev * f_curr < 0:
            table = pd.DataFrame(rows)
            return {
                "a":     x_prev,
                "b":     x_curr,
                "iters": i,
                "table": table,
                "found": True,
            }

        # Advance one step
        x_prev = x_curr
        f_prev = f_curr
        x_curr = x_prev + h
        f_curr = f(x_curr)

    # Maximum iterations reached without finding a sign change
    table = pd.DataFrame(rows)
    return {
        "a":     x_prev,
        "b":     x_curr,
        "iters": n_max,
        "table": table,
        "found": False,
    }
