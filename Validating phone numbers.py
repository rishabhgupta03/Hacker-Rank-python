import re
n=int(input())
for i in range(n):
    match = re.search(r"^[(9|8|7)]\d{9}$", input())
    if match:
        print("YES")
    else:
        print("NO")
