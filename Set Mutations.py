a = input()
A = set(map(int, input().split()))
n = int(input())
for i in range(n):
    operation = input().split()
    se = set(map(int, input().split()))
    if operation[0] == 'update':
        A.update(se)
    elif operation[0] == 'intersection_update':
        A.intersection_update(se)
    elif operation[0] == 'difference_update':
        A.difference_update(se)
    elif operation[0] == 'symmetric_difference_update':
        A.symmetric_difference_update(se)
print(sum(A))
