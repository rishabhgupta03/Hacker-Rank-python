t = int(input())
for i in range(t):
    n = int(input())
    sl = list(map(int, input().split()))
    smallest = sl.index(min(sl))
    left = sl[:smallest]
    right = sl[smallest+1:]
    if left == sorted(left, reverse=True) and right == sorted(right):
        print("Yes")
    else:
        print("No")
