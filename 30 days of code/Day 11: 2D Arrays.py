arr=[]
for _ in range(6):
    arr.append(list(map(int, input().split())))
total = None
for i in range(4):
    for j in range(4):
        count = sum(arr[i][j:j+3]) + (arr[i+1][j+1]) + sum(arr[i+2][j:j+3])
        if total is None or count > total:
            total = count
        else:
            continue
print(total)
