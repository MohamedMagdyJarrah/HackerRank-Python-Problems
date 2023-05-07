from collections import Counter

shoes = int(input())
sizes = list(map(int,input().split()))
customers = int(input())

sizes = dict(Counter(sizes))

earned_money = 0
for i in range(customers):
    size,cost = map(int,input().split())
    if size in sizes:
        if sizes[size] != 0:
            earned_money += cost
            sizes[size] -= 1
            
print(earned_money)