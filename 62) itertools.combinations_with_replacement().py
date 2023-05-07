from itertools import combinations_with_replacement
S,K = input().split()
S = sorted(S)
K= int(K)

comb = list(combinations_with_replacement(S,K))
for i in range(len(comb)):
  string = ''.join(str(letter) for letter in list(comb[i]))
  print(string)