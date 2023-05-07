import numpy as np

A = []
B = []
N = int(input())
for i in range(N):
    row = list(map(int,input().split()))
    A.append(row)
    
for i in range(N):
    row = list(map(int,input().split()))
    B.append(row)    
    
print(np.dot(A,B))