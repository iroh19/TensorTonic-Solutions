import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    N = len(A)
    M = len(A[0])

    A_t = np.zeros((M,N))

    for i in range (N):
        for j in range (M):
            A_t[j,i] = A[i][j]

    return A_t
    
    pass
