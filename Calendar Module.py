import calendar
calendar.TextCalendar(firstweekday=6).formatyear(2015)
date = list(map(int, input().split()))
day = date[1]
month = date[0]
year = date[2]
week = (calendar.weekday(year,month,day))
print(calendar.day_name[week].upper())
