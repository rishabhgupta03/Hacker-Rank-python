import numpy
array = (numpy.array(input().split(), float))
numpy.set_printoptions(legacy='1.13')
print(numpy.floor(array))
print(numpy.ceil(array))
print(numpy.rint(array))
