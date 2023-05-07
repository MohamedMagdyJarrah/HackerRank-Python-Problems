import numpy as np

N,M = map(int,input().split())

matrix = []
for i in range(N):
    row = list(map(int,input().split()))
    matrix.append(row)

np_matrix = np.array(matrix)
np.around(np_matrix,decimals=12)
print(np.mean(np_matrix,axis =1 ))
print(np.var(np_matrix,axis = 0 ))
print(round(np.std(np_matrix),11))

