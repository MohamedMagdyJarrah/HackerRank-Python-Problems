import numpy

N,M,P = map(int,input().split())

array1=[]
array2=[]
for i in range(N):
    row = list(map(int,input().split()))
    array1.append(row)

np_array1 = numpy.array(array1)   
for i in range(M):
    row = list(map(int,input().split()))
    array2.append(row)
np_array2 = numpy.array(array2) 

print(numpy.concatenate((np_array1,np_array2),axis = 0))