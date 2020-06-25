import numpy
m = input().split()
for i in range(len(m)):
    m[i] = int(m[i])

print (numpy.zeros((m), dtype = numpy.int))
print (numpy.ones((m), dtype = numpy.int))

