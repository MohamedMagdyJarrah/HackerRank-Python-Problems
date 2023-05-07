happiness = 0
n,m = map(int,input().split())
integers = list(map(int,input().split()))
A = set(map(int,input().split()))
B = set(map(int,input().split()))

for i in integers:
    if i in A:
        happiness +=1
    if i in B:
        happiness -=1
    
print(happiness)
