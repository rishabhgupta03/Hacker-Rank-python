from collections import OrderedDict
n = int(input())
od = OrderedDict()
for i in range(n):
    entry = input().split()
    price = int(entry[-1])
    item = " ".join(entry[:-1])
    if item in od:
        od[item]=od.get(item)+price
    else:
        od[item] = price
for key,value in od.items():
    print(key,value)
