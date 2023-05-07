from collections import namedtuple

N = int(input())
columns = input()
sheet = namedtuple('sheet',columns)
avg = 0
for i in range(N):
    row = input().split()
    sht = sheet(*row)
    avg += int(sht.MARKS)
    
print(avg/N)