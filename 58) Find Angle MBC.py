import math

AB = int(input())
BC = int(input())

H = math.sqrt(AB**2 + BC**2)/2.0
BM = BC/2.0

angle = int(round(math.degrees(math.acos(BM/H))))

print(str(angle)+chr(176))
