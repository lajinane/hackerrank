'''
https://docs.python.org/3/library/calendar.html
https://docs.python.org/3/library/datetime.html
'''

import calendar
from datetime import datetime

# using datetime

dt = datetime.strptime(input(), '%m %d %Y').date()
print(dt.strftime('%A').upper())

# using datetime and calendar

dt = datetime.strptime(input(), '%m %d %Y').date()
print(calendar.day_name[dt.weekday()].upper())

#  using calendar

m, d, y = map(int, input().split())
print(calendar.day_name[calendar.weekday(y, m, d)].upper())
