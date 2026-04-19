def fixed_point_method(g, x0, tol=1e-8, max_iter=100):
    """
    Fixed Point Iteration Method for solving x = g(x)

    Parameters:
    g        : function
               Function in the form x = g(x)
    x0       : float
               Initial guess
    tol      : float
               Tolerance for stopping criterion (default = 1e-8)
    max_iter : int
               Maximum number of iterations (default = 100)

    Returns:
    root approximation, number of iterations
    """

    print("Iteration |     x_n        |     Error")
    print("---------------------------------------------")

    x_n = x0

    for i in range(1, max_iter + 1):

        # Fixed point iteration formula
        x_next = g(x_n)

        # Absolute error
        error = abs(x_next - x_n)

        print(f"{i:^9} | {x_n:^14.10f} | {error:.10e}")

        # CONDITION 1:
        # Stop if the error is less than tolerance
        if error < tol:
            print("\nConverged successfully.")
            return x_next, i

        x_n = x_next

    # CONDITION 2:
    # Stop if maximum number of iterations is reached
    print("\nMaximum number of iterations reached. Method did not converge.")
    return x_n, max_iter


# Example usage
if __name__ == "__main__":

    # Example: solving x^2 - 2 = 0
    # Rewrite as x = g(x)
    # One possible choice:
    # g(x) = (x + 2/x) / 2

    def g(x):
        return (x + 2/x) / 2

    x0 = 1.0

    root, iterations = fixed_point_method(g, x0)

    print("\nFinal Result:")
    print(f"Approximate root = {root}")
    print(f"Iterations       = {iterations}")
