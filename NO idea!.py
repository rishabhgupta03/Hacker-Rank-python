n, m = input().split()
arr = input().split()
like = set(input().split())
dislike = set(input().split())
happiness = 0
for i in arr:
    if i in like:
        happiness+=1
    if i in dislike:
        happiness -= 1
print(happiness)