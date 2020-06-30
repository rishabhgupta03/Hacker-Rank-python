import numpy
myarray = list(map(int, input().split()))
carray = numpy.array(myarray)
carray.shape = (3,3)
print(carray)
