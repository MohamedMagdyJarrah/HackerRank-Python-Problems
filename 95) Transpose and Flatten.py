import numpy

N,M = map(int,input().split())
matrix = []
for i in range(N):
    row = list(map(int,input().split()))
    matrix.append(row)
np_matrix = numpy.array(matrix)
print(numpy.transpose(np_matrix))
print(np_matrix.flatten())
