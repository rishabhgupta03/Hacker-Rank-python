from collections import OrderedDict
od = OrderedDict()
n = int(input())
for i in range(n):
    word = input()
    if word not in od:
        od[word] = 1
    else:
        od[word] +=1

print(len(od))
print(*od.values())
