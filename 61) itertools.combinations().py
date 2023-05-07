from itertools import combinations
S,K = input().split()
S = sorted(S)
K= int(K)
for i in range(1,K+1):
  comb = list(combinations(S,i))
  for item in comb:
    string = ''.join(str(letter) for letter in list(item))
    print(string)