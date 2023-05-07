from itertools import combinations

N = int(input())
letters = input().lower().split()
K = int(input()) 

count = 0
possibilities = list(combinations(letters,K))
# print(possibilities)

for i in range(len(possibilities)):
  if "a" in possibilities[i]:
    count +=1

print(round(count/len(possibilities),4))
