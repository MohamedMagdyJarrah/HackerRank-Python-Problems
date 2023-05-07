# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for i in range(T):
    nums_A = int(input())
    A = set(map(int,input().split()))
    nums_B = int(input())
    B = set(map(int,input().split()))
    
    print(A.issubset(B))
    