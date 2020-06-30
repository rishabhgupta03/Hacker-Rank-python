from collections import deque
n = int(input())
d=deque()
for i in range(n):
    operation = input().split()
    command = operation[0]
    element = operation[-1]
    if command == 'append':
        d.append(element)
    elif command == 'appendleft':
        d.appendleft(element)
    elif command == 'clear':
        d.clear()
    elif command == 'extend':
        d.extend(element)
    elif command == 'extendleft':
        d.extendleft(element)
    elif command == 'pop':
        d.pop()
    elif command == 'popleft':
        d.popleft()
    elif command == 'reverse':
        d.reverse()
    elif command == 'rotate':
        d.rotate(element)
    elif command == 'count':
        d.count(element)
print(*d)
