import math
import cmath 
complex_num = complex(input())

print(math.sqrt(math.pow(complex_num.real,2)+math.pow(complex_num.imag,2)))
print(cmath.phase(complex_num))