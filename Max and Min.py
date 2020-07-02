import numpy
n,m= map(int, input().split())
array = numpy.array([input().split() for _ in range(n)], int)
mini = numpy.min(array, axis=1)
print(max(mini))
