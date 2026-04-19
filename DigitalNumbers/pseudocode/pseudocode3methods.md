# Pseudocode — Chapter 1: Single Variable Equations
**DigitalNumbers Project · EAFIT University**
Author: Juan Guillermo Isaza · April 2026

---

## Method 1 — Incremental Search

**Purpose:** Find an interval [a, b] where the function changes sign, which guarantees
that a root exists somewhere inside it.

**Inputs:**
- f — a continuous function
- x0 — the starting point of the search
- h — the size of each step forward
- N — maximum number of steps allowed

**Output:**
- The interval [a, b] where the sign change was found

---

**BEGIN**

Set the current point to x0 and evaluate f there.  
Move one step forward to get the next point, and evaluate f there too.

Repeat up to N times:

> Check whether the function values at the two consecutive points have opposite signs.  
> If they do, a root must lie between them — stop and report that interval.
>
> If they do not, discard the left point and move one step forward again,  
> keeping only the most recent point and evaluating the function at the new one.

If no sign change was found after N steps, report that no interval was found.

**END**

---

## Method 2 — Bisection

**Purpose:** Given an interval [a, b] where a sign change is known to exist,
repeatedly cut the interval in half and keep only the half that still contains
the sign change, until the interval is small enough.

**Inputs:**
- f — a continuous function
- a, b — the endpoints of the starting interval (f(a) and f(b) must have opposite signs)
- tol — the acceptable error (how small the interval must get before stopping)
- N — maximum number of iterations allowed

**Output:**
- The midpoint of the final interval, which approximates the root

---

**BEGIN**

Verify that f(a) and f(b) have opposite signs. If not, stop — the method cannot proceed.

Compute the midpoint of [a, b] and evaluate f there.  
Set the initial error to a large number so the loop starts.

Repeat until the error is smaller than the tolerance or N iterations are reached:

> Remember the current midpoint before updating it.
>
> Check the sign of f at the midpoint:
> - If f(a) and f(midpoint) have opposite signs, the root is in the left half —  
>   replace b with the current midpoint.
> - Otherwise, the root is in the right half —  
>   replace a with the current midpoint.
>
> Compute the new midpoint of the updated interval.  
> Evaluate f at the new midpoint.  
> Calculate the error as the absolute difference between the new and old midpoints.  
> Increase the iteration counter by one.

Report the final midpoint as the approximation of the root.

**END**

---

## Method 3 — False Position (Regula Falsi)

**Purpose:** Similar to bisection, but instead of cutting the interval exactly in half,
it draws a straight line between the two endpoints and uses the point where that
line crosses zero as the next estimate. This tends to converge faster than bisection
when the function behaves smoothly.

**Inputs:**
- f — a continuous function
- a, b — the endpoints of the starting interval (f(a) and f(b) must have opposite signs)
- tol — the acceptable error
- N — maximum number of iterations allowed

**Output:**
- The estimated root where the line crossed zero

---

**BEGIN**

Verify that f(a) and f(b) have opposite signs. If not, stop — the method cannot proceed.

Evaluate f at both endpoints.  
Compute the first estimate by drawing a straight line between (a, f(a)) and (b, f(b))  
and finding where it crosses the x-axis. This is done with the formula:

> p = ( f(b)·a − f(a)·b ) / ( f(b) − f(a) )

Evaluate f at this new point p.  
Set the initial error to a large number so the loop starts.

Repeat until the error is smaller than the tolerance or N iterations are reached:

> Remember the current estimate p before updating it.
>
> Check the sign of f at p:
> - If f(a) and f(p) have opposite signs, the root is between a and p —  
>   replace b with p and update f(b).
> - Otherwise, the root is between p and b —  
>   replace a with p and update f(a).
>
> Re-evaluate f at the updated endpoints a and b.  
> Compute the new estimate p using the same straight-line formula as before.  
> Evaluate f at the new p.  
> Calculate the error as the absolute difference between the new and old estimates.  
> Increase the iteration counter by one.

Report the final estimate p as the approximation of the root.

**END**

# Pseudocode — Chapter 2: Linear Systems
**DigitalNumbers Project · EAFIT University**
Author: Jerónimo Mesa Alzate · April 2026

---

## Method 1 — Naive Gaussian Elimination

**Purpose:** To solve de Equation Ax = b by reducing the coeficient matrix into it's upper triangular form using simple row equations in the augmented matrix, then, back substitution is used to solve the variables starting from the last row to find the values of the x components

**Inputs:**
- Matrix A (nxn)
- Vector b (nx1)
  
**Output:**
- Solution vector x
- Intermediate matrices of the process

**BEGIN**  

Check input dimensions: If A is not square (nxn) → Stop, and if b is not compatible with b (nx1) → Stop  
Check if the det(A) = 0 if it is → Stop.  
Chack if the number in the position A(1,1) = 0, if it is → Stop.  


> Form the augmented martix Aug = [A|b], then start the process of elimination:  
> For k = 1 to n-1:  
>   If Aug[k,k] = 0:  
>     Stop: zero pivot encountered  
>   For i = k+1 to n:  
>     m_i = Aug[i,k] / Aug[k,k]  
>     For j = k to n+1:  
>       Aug[i,j] = Aug[i,j] - m_i * Aug[k,j]  
      
Then we apply back substitution:  

> x[n] = Aug[n,n+1] / Aug[n,n]  
> For i = n-1 down to 1:  
>   x[i] = (Aug[i,n+1] - Σ Aug[i,j]*x[j]) / Aug[i,i]  

And finally the outputs are printed  


## Method 2 — Gaussian Elimination with Partial Pivoting (PP)  
**Purpose:** Similar to naive gaussian elimination, this method utilises row changes to face the problem that the firts number could be too small compared to the other numbers leading to a not exact answer, also solves the problem of a number in the position [1,1] being a 0  

**Input:**   
- Matrix A (n × n)
- vector b (n × 1)
  
**Output:**  
- Solution vector x  

Check input dimensions:   
  If A is not square → Stop  
  If b size is not compatible → Stop  
  If det(A) = 0 → Stop.   
  
Form augmented matrix Aug = [A | b]

> For k = 1 to n-1:  
>  Find pivot row:  
>  p = index of row i (from k to n) that maximizes |Aug[i,k]|  
> If the number on the new pivot is 0 then:  
>   Stop  
> If p ≠ k:  
>   Swap rows k and p  
> For i = k+1 to n:  
>   m = Aug[i,k] / Aug[k,k]  
> For j = k to n+1:  
>   Aug[i,j] = Aug[i,j] - m * Aug[k,j]  
  
> If the last pivot is 0 then  
>   Stop

Then we apply back substitution:  

> x[n] = Aug[n,n+1] / Aug[n,n]  
> For i = n-1 down to 1:  
>   x[i] = (Aug[i,n+1] - Σ Aug[i,j]*x[j]) / Aug[i,i]  

And finally the outputs are printed  

## Method 3 — Gaussian Elimination with Total Pivoting (TP)  
**Purpose:** find the largest absolute value number in the matrix A and with row and column swapping, you swap it for the current pivot, reducing the risk of dividing by very small numbers and minimizing the propagation of round-off errors, although it increases computational cost and requires tracking column permutations.  

**Input:**   
- Matrix A (n × n)
- vector b (n × 1)
  
**Output:**  
- Solution vector x  

Check input dimensions:   
  If A is not square → Stop  
  If b size is not compatible → Stop  
  If det(A) = 0 → Stop.   
  
Form augmented matrix Aug = [A | b]

Then, initialize a index vector that keeps track of the column swaps
> mark = [1, 2, ..., n]  
  
Find maximum element in submatrix:  
> Find (p, q) such that:  
> |Aug[p,q]| = max |Aug[i,j]| for i,j = k,...,n  

Then do row and column swapping:  
> If p ≠ k:  
> Swap rows p and k  
  
> If q ≠ k:  
> Swap columns q and k  
> Swap mark[q] and mark[k]

> For i = k+1 to n:  
>   m = Aug[i,k] / Aug[k,k]  
> For j = k to n+1:  
>   Aug[i,j] = Aug[i,j] - m * Aug[k,j]  
  
> If the last pivot is 0 then  
>   Stop

Then we apply back substitution:  

> x[n] = Aug[n,n+1] / Aug[n,n]  
> For i = n-1 down to 1:  
>   x[i] = (Aug[i,n+1] - Σ Aug[i,j]*x[j]) / Aug[i,i]
  
Lastly reorder the vector x to match the swaps of columns during the process:  
Create vector x_final such that:  
> x_final[mark[i]] = x[i]

return x_final
---

## Method 4 — Newton-Raphson

**Purpose:** Starting from an initial guess, this method uses the tangent line of the function to generate better approximations of the root at each step. It usually converges very fast when the initial guess is close to the actual root.

**Inputs:**
- f — a function
- df — derivative of the function
- x0 — initial approximation
- tol — acceptable error
- N — maximum number of iterations

**Output:**
- Approximation of the root

---

**BEGIN**

Set the current approximation to x0 and evaluate f and df at that point.  
Set the initial error to a large number so the loop starts.

Repeat until the error is smaller than the tolerance or N iterations are reached:

> Check if the derivative at the current point is zero.  
> If it is, stop — the method cannot proceed due to division by zero.
>
> Compute the next approximation using the tangent line formula:  
> x_next = x_current − f(x_current) / df(x_current)
>
> Calculate the error as the absolute difference between the new and old approximation.  
>
> Update the current approximation with the new value.  
> Evaluate f and df at the new point.  
> Increase the iteration counter by one.

Report the final approximation as the root.

**END**

---

## Method 5 — Fixed Point Iteration

**Purpose:** Transform the equation into the form x = g(x) and generate a sequence of approximations by repeatedly evaluating the function. The success of the method depends strongly on the choice of g(x).

**Inputs:**
- g — function written as x = g(x)
- x0 — initial approximation
- tol — acceptable error
- N — maximum number of iterations

**Output:**
- Approximation of the root

---

**BEGIN**

Set the current approximation to x0.  
Set the initial error to a large number so the loop starts.

Repeat until the error is smaller than the tolerance or N iterations are reached:

> Compute the next approximation by evaluating the function:  
> x_next = g(x_current)
>
> Calculate the error as the absolute difference between the new and old approximation.  
>
> Update the current approximation with the new value.  
> Increase the iteration counter by one.

Report the final approximation as the root.

**END**
