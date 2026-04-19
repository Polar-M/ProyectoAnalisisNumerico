import math


def fixed_point_method(g, x0, tol=1e-7, max_iter=100):
    print("Iteration |     x_n        |     Error")
    print("---------------------------------------------")

    x_n = x0

    for i in range(1, max_iter + 1):

        x_next = g(x_n)

        error = abs(x_next - x_n)

        print(f"{i:^9} | {x_n:^14.10f} | {error:.10e}")

        if error < tol:
            print("\nConverged successfully.")
            return x_next, i

        x_n = x_next

    print("\nMaximum number of iterations reached.")
    return x_n, max_iter


# g(x) from your transformation
def g(x):
    return math.log(math.sin(x)**2 + 1) - 0.5


# Initial value
x0 = -0.5

# Run test
root, iterations = fixed_point_method(g, x0)

print("\nFinal Result:")
print(f"Root = {root}")
print(f"Iterations = {iterations}")
