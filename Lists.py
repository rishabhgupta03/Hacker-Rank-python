list =[]
n = int(input())
for i in range(n):
    s = input().split()
    cmd = s[0]
    e = s[1:]
    if cmd == 'insert':
        cmd = cmd + "(" + ",".join(e) + ")"
        eval("list."+cmd)
    elif cmd == 'remove':
        cmd = cmd + "(" + ",".join(e) + ")"
        eval("list."+cmd)
    elif cmd == 'append':
        cmd = cmd + "(" + ",".join(e) + ")"
        eval("list." + cmd)
    elif cmd == 'sort':
        list.sort()
    elif cmd == 'pop':
        list.pop()
    elif cmd == 'reverse':
        list.reverse()
    elif cmd == 'print':
        print(list)
    else:
        break

