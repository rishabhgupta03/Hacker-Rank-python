from itertools import combinations
s,k = input().split()
for i in range(1,int(k)+1):
    s = sorted(s)
    comb = list(combinations(s,i))
    for j in comb:
        print("".join(j))
