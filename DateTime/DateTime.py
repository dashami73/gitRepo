import datetime
import time
import calendar
yy = 2017
mm = 11

print(calendar.month(yy, mm))

print(f'MONDAY		{calendar.MONDAY}')
print(f'TUESDAY		{calendar.TUESDAY}'	)
print(f'WEDNESDAY	{calendar.WEDNESDAY}')
print(f'THURSDAY	{calendar.THURSDAY}')
print(f'FRIDAY		{calendar.FRIDAY}')
print(f'SATURDAY	{calendar.SATURDAY}')
print(f'SUNDAY		{calendar.SUNDAY}'	)
''' 
class timeDate:
    def __init__(self):
        pass

    @classmethod
    def fromtimestamp(cls, t):
        y, m, d, hh, mm, ss, wday, jday, dst = _time.localtime(t)
        return(y, m, d)
    

def datTime():
    x = datetime.datetime.now()

    print(x)
    print(x.year, x.month, x.day, x.hour, x.minute, x.second, x.microsecond)
    print(x.strftime("%a"))
    print(x.strftime("%A"))
    print(x.strftime("%w"))
    print(x.strftime("%d"))
    print(x.strftime("%b"))
    print(x.strftime("%B"))
    print(x.strftime("%m"))
    print(x.strftime("%y"))
    print(x.strftime("%Y"))
    print(x.strftime("%H"))
    print(x.strftime("%I"))
    print(x.strftime("%M"))
    print(x.strftime("%S"))
    print(x.strftime("%f"))
    print(x.strftime("%z"))
    print(x.strftime("%Z"))
    print(x.strftime("%j"))
    print(x.strftime("%U"))
    print(x.strftime("%W"))
    print(x.strftime("%c"))
    print(x.strftime("%C"))
    print(x.strftime("%x"))
    print(x.strftime("%X"))
    print(x.strftime("%%"))
    print(x.strftime("%G"))
    print(x.strftime("%u"))
    print(x.strftime("%V"))
'''
