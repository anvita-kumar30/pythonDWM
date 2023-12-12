n = 4
adj_mat =  [[0, 1, 1, 1],
            [0, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 1, 0]]
for row in adj_mat:
    print(row)
print()


out_degree = []
for i in range(n):
    out_count = 0
    for j in range(n):
        if adj_mat[i][j] == 1:
            out_count += 1
    out_degree.append(out_count)
for i in range(n):
    print(f"Node {i+1}: Out degree {out_degree[i]}")
print(out_degree)
print()


A = []
for i in range(n):
    A_row = []
    for j in range(n):
        if adj_mat[j][i] == 1:
            A_row.append(1/out_degree[j])
        else:
            A_row.append(0)
    A.append(A_row)
for row in A:
    print(row)
print()


import numpy as np
X = np.ones((n, 1))
A = np.array(A)
prev = np.array([])
for _ in range(0, 3):
    X = A @ X
    prev = X
print(X)


ans = dict()
for _ in range(0, X.size):
    ans[f'Page {_+1}'] = X[_][0]
ans = dict(sorted(ans.items(), key=lambda item: -item[1]))
print()
print(ans)
print()
ctn = 1
for i in ans:
    print(f"Rank {ctn}: {i}")
    ctn += 1
