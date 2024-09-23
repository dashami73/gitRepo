import calendar
import datetime
from datetime import date, time


print(calendar.calendar(2020)) #getfirstweekday())
print(calendar.firstweekday())
print(calendar.weekday(2020, 1, 10))

print(calendar.month(2020, 5))

monthCal = calendar.monthcalendar(2020, 5)

print(monthCal)

for x in monthCal:
    print(x[0][0])

for moth in range(1, 13):
    monthCal = calendar.monthcalendar(2020, moth)
    for day in monthCal:
        '''
        print(day[0][0])
        print(day[0][1])
        print(day[0][2])
        print(day[0][3])
        print(day[0][4])
        '''
        print(day)
        