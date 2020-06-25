t= int(input())
for i in range(t):
    an = int(input())
    a = set(input().split())
    bn = int(input())
    b = set(input().split())
    if a.issubset(b):
        print('True')
    else:
        print('False')
