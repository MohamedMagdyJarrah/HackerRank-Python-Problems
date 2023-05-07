import numpy as np

N,M = map(int,input().split())

matrix = []
for i in range(N):
    row = list(map(int,input().split()))
    matrix.append(row)

np_matrix = np.array(matrix)

print(np.prod(np.sum(np_matrix,axis = 0)))
