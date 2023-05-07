from collections import defaultdict
n,m = map(int,input().split())

A = defaultdict(list)
B = []

for i in range(n):
    A[input()].append(i+1)
    
for i in range(m):
    B.append(input())

A = dict(A)

for i in range(m):
  if B[i] in A:
    print(*A[B[i]])
  else:
    print(-1)