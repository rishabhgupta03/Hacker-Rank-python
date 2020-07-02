s = input()
lower = []
upper = []
odd = []
even = []
for i in range(len(s)):
    if s[i].islower():
        lower.append(s[i])
        lower = sorted(lower)
    elif s[i].isupper():
        upper.append(s[i])
        upper = sorted(upper)
    elif int(s[i])%2 == 0:
        even.append(int(s[i]))
        even = sorted(even)
    elif int(s[i])%2 != 0:
        odd.append(int(s[i]))
        odd = sorted(odd)
final = lower+upper+odd+even
print(*final,sep="")
