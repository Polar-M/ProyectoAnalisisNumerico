# DigitalNumbers — Numerical Analysis Project
**EAFIT University · Department of Computer Science and Systems**  
Course: Numerical Analysis · Instructor: Edwar Samir Posada  
Team: Juan Felipe Florez · Jerónimo Mesa · Juan Guillermo Isaza · Luciana Pineda

---

## Table of Contents
1. [Project Overview](#1-project-overview)
2. [Project Structure](#2-project-structure)
3. [How to Run](#3-how-to-run)
4. [Methods Implemented](#4-methods-implemented)
5. [Pattern: How to Add Your Methods](#5-pattern-how-to-add-your-methods)
6. [Output Format (Required by the Professor)](#6-output-format-required-by-the-professor)
7. [Coding Standards](#7-coding-standards)

---

## 1. Project Overview

DigitalNumbers is a web application that implements numerical methods studied in class.
The Python code is organized by chapter and method, so each team member can work
independently and later integrate their part without conflicts.

**Chapters covered:**
| Chapter | Topic                          | Owner              |
|---------|--------------------------------|--------------------|
| 1       | Single Variable Equations      | Juan Guillermo     |
| 2       | Systems of Linear Equations    | *(assign)*         |
| 3       | Interpolation                  | *(assign)*         |

---

## 2. Project Structure

```
DigitalNumbers/
│
├── methods/                          ← All numerical method implementations
│   ├── __init__.py
│   │
│   ├── chapter1_single_variable/     ← Chapter 1 (Juan Guillermo)
│   │   ├── __init__.py
│   │   ├── incremental_search.py
│   │   ├── bisection.py
│   │   └── false_position.py
│   │
│   ├── chapter2_linear_systems/      ← Chapter 2 (add yours here)
│   │   ├── __init__.py
│   │   ├── gaussian_elimination.py   ← example
│   │   └── ...
│   │
│   └── chapter3_interpolation/       ← Chapter 3 (add yours here)
│       ├── __init__.py
│       └── ...
│
├── tests/                            ← One test file per method
│   ├── __init__.py
│   │
│   ├── chapter1_single_variable/
│   │   ├── __init__.py
│   │   ├── test_incremental_search.py
│   │   ├── test_bisection.py
│   │   └── test_false_position.py
│   │
│   ├── chapter2_linear_systems/      ← add your tests here
│   │   └── __init__.py
│   │
│   └── chapter3_interpolation/       ← add your tests here
│       └── __init__.py
│
├── requirements.txt
└── README.md
```

---

## 3. How to Run

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run a specific test (from the project root)
```bash
python tests/chapter1_single_variable/test_bisection.py
python tests/chapter1_single_variable/test_false_position.py
python tests/chapter1_single_variable/test_incremental_search.py
```

> **Important:** always run from the project root (`DigitalNumbers/`), not from inside a subfolder.
> This ensures Python can find the `methods/` package correctly.

---

## 4. Methods Implemented

### Chapter 1 — Single Variable Equations

| Method             | File                    | Inputs                        | Outputs                              |
|--------------------|-------------------------|-------------------------------|--------------------------------------|
| Incremental Search | `incremental_search.py` | `f, x0, h, n_max`             | `a, b, iters, table, found`          |
| Bisection          | `bisection.py`          | `f, a, b, tol, n_max`         | `root, iters, error, table, converged` |
| False Position     | `false_position.py`     | `f, a, b, tol, n_max`         | `root, iters, error, table, converged` |

All methods return a **dict** and a **pandas DataFrame table** with the iteration history.

---

## 5. Pattern: How to Add Your Methods

Follow these steps exactly so everything integrates cleanly.

### Step 1 — Create your method file

Create `methods/chapterX_your_topic/your_method.py` using this template:

```python
"""
Method Name
===========
One-paragraph explanation of what the method does and when to use it.

Author: Your Name
Last updated: April 2026
"""

import numpy as np
import pandas as pd


def your_method(param1, param2, tol: float, n_max: int) -> dict:
    """
    Short description.

    Parameters
    ----------
    param1 : type — description
    param2 : type — description
    tol    : float — error tolerance
    n_max  : int   — maximum iterations

    Returns
    -------
    dict with keys:
        'root'      : float        — approximated solution
        'iters'     : int          — iterations performed
        'error'     : float        — final error
        'table'     : pd.DataFrame — iteration table
        'converged' : bool         — True if tolerance was met
    """

    rows = []

    # --- Initialization ---
    # ... your setup here ...

    # --- Iteration loop ---
    for i in range(1, n_max + 1):

        # Append current state to table
        rows.append({
            "Iteration": i,
            "x":         round(x, 10),   # adjust columns to your method
            "f(x)":      round(fx, 10),
            "error":     round(error, 10),
        })

        # --- Stopping criterion ---
        if error < tol:
            break

        # ... update step ...

    table = pd.DataFrame(rows)
    return {
        "root":      x,
        "iters":     i,
        "error":     error,
        "table":     table,
        "converged": error <= tol,
    }
```

### Step 2 — Register it in `__init__.py`

Open (or create) `methods/chapterX_your_topic/__init__.py` and add:

```python
from .your_method import your_method
```

Then open `methods/__init__.py` and add:

```python
from .chapterX_your_topic import your_method
```

### Step 3 — Create your test file

Create `tests/chapterX_your_topic/test_your_method.py` using this template:

```python
"""
Test — Method Name
===================
To run:
    python tests/chapterX_your_topic/test_your_method.py
"""

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import numpy as np
from methods.chapterX_your_topic.your_method import your_method


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


# Test 1 — describe the function and expected root
f1 = lambda x: ...   # your function here
result1 = your_method(f=f1, ...)
print_results("Test 1: f(x) = ...  |  params", result1)

# Test 2 — a different function
f2 = lambda x: ...
result2 = your_method(f=f2, ...)
print_results("Test 2: f(x) = ...  |  params", result2)
```

### Step 4 — Check the output format

The professor requires that every method prints a table. Make sure your table has:
- An `"Iteration"` column as the first column
- An `"error"` column as the last column
- At least the key variables at each step in between

---

## 6. Output Format (Required by the Professor)

Every test must print output like this:

```
=======================================================
  Test 1: f(x) = cos(x) - x  |  [0, 1]  tol=1e-7
=======================================================
 Iteration         a         b      midpoint        f(mid)         error
          1   0.0000    1.0000        0.5000        0.3776   1000.0000000
          2   0.5000    1.0000        0.7500       -0.0183    250.0000000
         ...
         24   0.7391    0.7391        0.7391        0.0000      0.0000001

  Iterations : 24
  Root       : 0.7390851332
  Error      : 8.94e-08
  Status     : Converged ✓
```

Use `result["table"].to_string(index=False)` to print the table — do not use `print(df)` alone
because it truncates rows.

---

## 7. Coding Standards

- **Language:** English only — comments, docstrings, variable names, print messages.
- **Functions:** one function per file, same name as the file (`bisection.py` → `def bisection(...)`).
- **Return type:** always a `dict` (see pattern above). Never return plain floats.
- **Table:** always build the table with a list of `rows` dicts → `pd.DataFrame(rows)`.
- **Rounding in table:** use `round(value, 10)` when appending to rows.
- **No global variables** — everything goes inside the function.
- **No `print()` inside method files** — printing happens only in test files.
- **Error handling:** raise `ValueError` with a clear message for invalid inputs
  (e.g., no sign change when required).
