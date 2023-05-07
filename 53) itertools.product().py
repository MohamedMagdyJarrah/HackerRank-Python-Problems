from itertools import product

A = list(map(int,input().split()))
B = list(map(int,input().split()))

for point in list(product(A,B)): 
    print(point,end=" ")