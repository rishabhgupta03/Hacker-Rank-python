A = set(input().split())
n = int(input())
for i in range(n):
    s = set(input().split())
    if not A.issuperset(s):
        verify = 'False'
        break
    else:
        verify = 'True'
print(verify)
