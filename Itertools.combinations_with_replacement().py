from itertools import combinations_with_replacement
s,k = input().split()
cwr = list(combinations_with_replacement(sorted(s),int(k)))
for j in cwr:
    print("".join(j))
