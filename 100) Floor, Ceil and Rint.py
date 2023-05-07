import numpy as np
np.set_printoptions(legacy='1.13')
array = np.array(list(map(float,input().split())))

print(np.floor(array))
print(np.ceil(array))
print(np.rint(array))