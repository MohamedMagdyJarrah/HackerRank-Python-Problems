from collections import OrderedDict

N = int(input())
items = OrderedDict()
for i in range(N):
    order = input().split()
    if len(order) == 3:
        name = order[0] + ' ' + order[1]
        price = int(order[2])
    elif len(order) == 2:
        name = order[0] 
        price = int(order[1])
    
    if name in items:
        items[name] = items[name] + price
    else:
        items[name] = price

items = dict(items)

for i , p in items.items():
  print(i + ' ' + str(p))