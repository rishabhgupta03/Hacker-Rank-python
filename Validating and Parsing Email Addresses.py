import re
import email.utils
n=int(input())
for i in range(n):
    i = input().split()
    match = re.search(r"<[a-zA-Z][a-zA-Z0-9\-_\.]+@[A-Za-z]+\.[a-zA-Z]{1,3}>", i[1])
    if match:
        print (i[0], i[1])
    else:
        continue
