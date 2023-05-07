# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int,input().split()))
n = int(input())
other_set = set()
for i in range(n):
    other_set.update(set(map(int,input().split())))
  
print(A.issuperset(other_set))  