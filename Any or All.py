n = int(input())
line = input().split()
print(all(int(j)>0 for j in line) and any(i == i[::-1] for i in line))
