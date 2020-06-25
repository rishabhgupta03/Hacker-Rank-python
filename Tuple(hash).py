n = int(input())
m = input().split()
for i in range(n):
    m[i] = int(m[i])
tup = tuple(m)
print(hash(tup))
