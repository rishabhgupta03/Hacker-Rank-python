no_of_students = int(input())
record = {}
for i in range(no_of_students):
    name, maths, physics, chemistry = str(input()).split()
    average = (float(physics)+float(chemistry)+float(maths))/3
    record.setdefault(name , '')
    record[name] = average
student_name = input()
print("{:.2f}".format(record[student_name]))