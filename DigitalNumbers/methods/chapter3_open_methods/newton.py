def newton_method(f, df, x0, tol=1e-8, max_iter=100):
    """
    Newton-Raphson Method for solving f(x) = 0

    Parameters:
    f        : function
               Function whose root we want to find
    df       : function
               Derivative of f
    x0       : float
               Initial guess
    tol      : float
               Tolerance for stopping criterion (default = 1e-8)
    max_iter : int
               Maximum number of iterations (default = 100)

    Returns:
    root approximation, number of iterations
    """

    print("Iteration |     x_n        |    f(x_n)      |     Error")
    print("-----------------------------------------------------------")

    x_n = x0

    for i in range(1, max_iter + 1):
        f_xn = f(x_n)
        df_xn = df(x_n)

        # CONDITION 1:
        # Derivative must not be zero (avoids division by zero)
        if df_xn == 0:
            print("Error: derivative is zero. Method fails.")
            return None, i

        # Newton-Raphson formula
        x_next = x_n - f_xn / df_xn

        # Compute absolute error
        error = abs(x_next - x_n)

        print(f"{i:^9} | {x_n:^14.10f} | {f_xn:^14.10f} | {error:.10e}")

        # CONDITION 2:
        # Stop if error is less than tolerance
        if error < tol:
            print("\nConverged successfully.")
            return x_next, i

        x_n = x_next

    # CONDITION 3:
    # Stop if maximum number of iterations is reached
    print("\nMaximum number of iterations reached. Method did not converge.")
    return x_n, max_iter


# =========================
# Example usage
# =========================
if __name__ == "__main__":

    # Example function: f(x) = x^2 - 2
    def f(x):
        return x**2 - 2

    # Derivative: f'(x) = 2x
    def df(x):
        return 2 * x

    # Initial guess
    x0 = 1.0

    root, iterations = newton_method(f, df, x0)

    print("\nFinal Result:")
    print(f"Approximate root = {root}")
    print(f"Iterations       = {iterations}")
