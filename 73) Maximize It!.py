from itertools import product
K,M = map(int,input().split())

def Sq(n):
    return int(n)**2
lists = []
for i in range(K):
    lists.append(list(map(Sq,input().split()[1:])))


lists = list(product(*lists))

maxm = -1
for i in range(len(lists)):
  check = sum(lists[i])%M
  if check > maxm:
    maxm = check

print(maxm)
