n=int(input())
phone_dict={}
for i in range(n):
    record = input().split()
    phone_dict[record[0]] = record[1]
while True:
    try:
        name = input()
        if name in phone_dict:
            print(f'{name}={phone_dict[name]}')
        else:
            print("Not found")
    except:
        break
