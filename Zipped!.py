n ,x= map(int, input().split())
total = []
for i in range(x):
    marks = list(map(float, input().split()))
    total.append(marks)
totalmarks = (list(zip(*total)))
for student in totalmarks:
    marksofstudent = 0
    for i in student:
        marksofstudent +=i
    average = (marksofstudent/x)
    print(average) 
