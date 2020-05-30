class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        self.scores = scores
        Person.__init__(self, firstName, lastName, idNum)

    def calculate(self):
        average = sum(scores)/numScores
        if 90<=average<=100:
            grade = 'O'
        elif 80<=average<90:
            grade = "E" 
        elif 70<=average<80:
            grade = "A"
        elif 55<=average<70:
            grade = "P"
        elif 40<=average<55:
            grade = "D"
        elif average<40:
            grade = "T"
        return grade

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
