from collections import namedtuple
n = int(input())
colum = namedtuple('colum', input().split())
print(sum(float(colum(*input().split()).MARKS) for _ in range(n))/n)
