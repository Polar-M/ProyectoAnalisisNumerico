import math


def newton_method(f, df, x0, tol=1e-7, max_iter=100):
    """
    Newton-Raphson Method for solving f(x) = 0

    Conditions:
    - The function must be differentiable near the root
    - The derivative must not be zero
    - A good initial guess is required for convergence

    Parameters:
    f        : function
    df       : derivative of f
    x0       : initial guess
    tol      : tolerance (default 1e-8)
    max_iter : maximum iterations (default 100)

    Returns:
    root approximation, number of iterations
    """

    print("Iteration |     x_n        |    f(x_n)      |     Error")
    print("-----------------------------------------------------------")

    x_n = x0

    for i in range(1, max_iter + 1):
        f_xn = f(x_n)
        df_xn = df(x_n)

        # CONDITION 1: derivative must not be zero
        if df_xn == 0:
            print("Error: derivative is zero. Method fails.")
            return None, i

        # Newton formula
        x_next = x_n - f_xn / df_xn

        # Absolute error
        error = abs(x_next - x_n)

        print(f"{i:^9} | {x_n:^14.10f} | {f_xn:^14.10f} | {error:.10e}")

        # CONDITION 2: stopping criterion
        if error < tol:
            print("\nConverged successfully.")
            return x_next, i

        x_n = x_next

    # CONDITION 3: maximum number of iterations reached
    print("\nMaximum number of iterations reached.")
    return x_n, max_iter


# Test function
def f(x):
    return math.log(math.sin(x)**2 + 1) - 0.5


# Derivative of the function
def df(x):
    return (2 * math.sin(x) * math.cos(x)) / (math.sin(x)**2 + 1)


# Initial value
x0 = 0.5

# Run test
root, iterations = newton_method(f, df, x0)

print("\nFinal Result:")
print(f"Root = {root}")
print(f"Iterations = {iterations}")
