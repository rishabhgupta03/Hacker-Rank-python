ls=[]
m=[]
n=int(input())
for i in range(n):
    name=input()
    marks=float(input())
    ls.append([name,marks])
    m.append(marks)
ls.sort(key = lambda x : x[1])
b = sorted(m)[1]
for a,c in ls:
    if b==c:
        print(a)




