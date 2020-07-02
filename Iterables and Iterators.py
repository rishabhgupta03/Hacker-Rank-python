import itertools
n =  int(input())
st = input().split()
r = int(input())
count=0
comb = list(itertools.combinations(st,r))
for i in comb:
    if 'a' in i:
        count+=1
    else:
        pass
print(count/len(comb))
