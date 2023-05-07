import numpy as np

coeff = list(map(float,input().split())) 
x = int(input())

print(np.polyval(coeff,x))