import re
t = int(input())
for i in range(t):
    s = input()
    ans = True
    try:
        regex = re.compile(s)
    except:
        ans = False
    print(ans)
