mealcost=float(input())
x=int(input())
y=int(input())
tip=mealcost*(x/100)
tax=mealcost*(y/100)
sum=mealcost+tip+tax
print (round(sum))
