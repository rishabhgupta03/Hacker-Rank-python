k = int(input())
roomlist = list(map(int, input().split()))
roomset = set(roomlist)
sum1 = sum(roomlist)
sum2 = sum(roomset)
group = sum2*k-sum1
captainroom = group//(k-1)
print(captainroom)    
