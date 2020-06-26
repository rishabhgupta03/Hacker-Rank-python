from itertools import permutations
s,k = input().split()
r = "".join(sorted(s))
res = (list(permutations(r,int(k))))
for i in res:
    print("".join(i))
