import numpy
n = int(input())
l=[]
for i in range(n):
    c = list(map(float, input().split()))
    l.append(c)
print(round(numpy.linalg.det(l),2))
