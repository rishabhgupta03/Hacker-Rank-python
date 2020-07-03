nm = input().split()
n = int(nm[0])
m = int(nm[1])
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
k = int(input())
for i in sorted(arr, key = lambda i : int(i[k])):
    print(*i)
