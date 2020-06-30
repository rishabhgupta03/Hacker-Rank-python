from itertools import groupby
s = input()
for c,k in groupby(s):
    print('({}, {})'.format(len(list(k)), int(c)), end=" ") 
