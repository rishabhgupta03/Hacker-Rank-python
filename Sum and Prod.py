import numpy
n,m = input().split()
array = numpy.array([input().split() for i in range(int(n))], int)
s = (numpy.sum(array, axis=0))
print(numpy.prod(s, axis = None))
