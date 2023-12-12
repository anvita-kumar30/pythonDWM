import numpy as np

def printMat(a):
    for i in range(len(a)):
        for j in range(len(a)):
            print(a[i][j], end=" ")
        print()
    print()

n = int(input("Enter no. of nodes: "))
adj_mat = []
for i in range(0, n):
    row = []
    for j in range(0, n):
        row.append(int(input("Enter the value at row {} and column {}: ".format(i + 1, j + 1))))
    adj_mat.append(row)

print()
print("Adjacency matrix: ")
printMat(adj_mat)

def solve_rank(n, adj_mat):
    trans_matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if adj_mat[j][i] == 1:
                sum = 0
                for k in range(n):
                    if adj_mat[j][k] == 1:
                        sum += 1
                row.append(round(1 / sum, 2))
            else:
                row.append(0)
        trans_matrix.append(row)
    print("Transition Probability Matrix A: ")
    return trans_matrix

matrix = solve_rank(n, adj_mat)
print(matrix)
print()
r = np.array([1 / n] * n)  # Create a NumPy array for the initial vector
# Perform matrix-vector multiplication for 3 iterations
for i in range(3):
    r = np.dot(matrix, r)
    print(r)
# highest will be rank and print out later
ans = dict()
for i in range(0, X.size):
    ans[f'Page {i + 1}'] = X[i][0]
ans = dict(sorted(ans.items(), key=lambda item: -item[1]))
ctn = 1
for i in ans:
    print(f"Rank {ctn}: {i}")
    ctn += 1

