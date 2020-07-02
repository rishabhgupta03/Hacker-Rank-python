import itertools
k,m  = map(int, input().split())
l=[]
results=[]
for i in range(k):
    ni = input().split()
    l.append(ni[1:])
for j in l:
    for k in range(len(j)):
        j[k] = int(j[k])
ms = (list(itertools.product(*l)))
for ele in ms:
    result = (sum(int(i)**2 for i in ele)%m)
    results.append(result)
print(max(results))
