import numpy as np

def pagerank(M, num_iterations=100, d=0.85):
    N = M.shape[1]
    r = np.ones(N) / N
    for i in range(num_iterations):
        new_r = np.ones(N) * (1 - d) / N + d * M.dot(r)
        if np.allclose(new_r, r, atol=1e-6):
            break
        r = new_r
    return r

# Example usage:
# Create an adjacency matrix for a simple directed graph
# Each row represents a page, and each column represents links to other pages
# Here, A[i][j] is 1 if there is a link from page i to page j, otherwise 0.
A = np.array([[0, 1, 1, 1],
              [0, 0, 0, 1],
              [1, 0, 0, 1],
              [1, 0, 1, 0]])

# Normalize the matrix by dividing each column by its sum to ensure stochasticity
M = A / A.sum(axis=0)

# Calculate PageRank
page_rank = pagerank(M)
print("PageRank:", page_rank)
