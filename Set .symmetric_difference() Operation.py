n=input()
english = input().split()
m=input()
french = input().split()
s1= set(english)
s2 = set(french)
ad = s1 ^ s2
print(len(ad))
