N, M = str(input()).split()
p='.|.'
for i in range(int(N)//2):
    pattern = (p*(i*2+1)).center(int(M), '-')
    print (pattern)
print("WELCOME".center(int(M), '-'))
for j in range(int(N)//2,0,-1):
    print((p*(j*2-1)).center(int(M), '-'))

