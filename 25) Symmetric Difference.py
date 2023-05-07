# Enter your code here. Read input from STDIN. Print output to STDOUT
size_M = int(input())
M = set(map(int,input().split()))
size_N =  int(input())
N = set(map(int,input().split()))

new_set = M.difference(N)
new_set1 = N.difference(M)
result = new_set.update(new_set1)
new_set = sorted(new_set)

for num in new_set:
  print(num)