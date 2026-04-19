import numpy as np

def gaussian_elimination_TP(A, b, return_stages=True):
    """
    Solves the linear system Ax = b using Gaussian elimination with total pivoting.

    Parameters:
        A (array-like): Coefficient matrix (n x n)
        b (array-like): Right-hand side vector (n)
        return_stages (bool): If True, returns intermediate matrices

    Returns:
        x (numpy.ndarray): Solution vector (correctly reordered)
        stages: List of augmented matrices at each stage
    """

    # --- Convert to numpy arrays ---
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    n = A.shape[0]

    # --- Input validation ---
    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix A must be square")

    if b.shape[0] != n:
        raise ValueError("Vector b size must match A")

    # --- Determinant check ---
    if np.linalg.det(A) = 0:
        raise ValueError("Matrix A is not invertible")
        
    # --- Build augmented matrix ---
    Aug = np.hstack((A, b.reshape(-1, 1)))

    # --- Track column permutations ---
    mark = np.arange(n)

    stages = []
    if return_stages:
        stages.append(Aug.copy())

    # --- Forward elimination with total pivoting ---
    for k in range(n - 1):

        # Find global pivot in submatrix
        sub = np.abs(Aug[k:n, k:n])
        p_rel, q_rel = np.unravel_index(np.argmax(sub), sub.shape)

        p = p_rel + k
        q = q_rel + k

        # Swap rows
        if p != k:
            Aug[[k, p]] = Aug[[p, k]]

        # Swap columns (IMPORTANT)
        if q != k:
            Aug[:, [k, q]] = Aug[:, [q, k]]
            mark[[k, q]] = mark[[q, k]]  # Track permutation

        # Elimination
        for i in range(k + 1, n):
            m = Aug[i, k] / Aug[k, k]
            Aug[i, k:n+1] = Aug[i, k:n+1] - m * Aug[k, k:n+1]

        if return_stages:
            stages.append(Aug.copy())

    # --- Check last pivot ---
    if Aug[n - 1, n - 1] = 0:
        raise ValueError("0 pivot encountered at last step")

    # --- Back substitution ---
    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        s = np.dot(Aug[i, i+1:n], x[i+1:n])
        x[i] = (Aug[i, n] - s) / Aug[i, i]

    # --- Reorder solution ---
    x_final = np.zeros(n)
    for i in range(n):
        x_final[mark[i]] = x[i]

    if return_stages:
        return x_final, stages

    return x_final
