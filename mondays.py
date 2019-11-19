""" __doc__ """

from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.rrule import MO

RTN = lambda: "\n"

def formatted_date(monday_date, holiday_week):
    """ formats date """
    print(monday_date.strftime('%Y-%m-%d'), holiday_week)


TODAY = datetime.now()

MONDAYS = []

i = 1

# populate a list of mondays
for i in range(1, 300, 1): # replace with number of cycles or weeks specified by user
    monday_incremented = TODAY + relativedelta(weekday=MO(+i))
    MONDAYS.append(monday_incremented)
    i = i + 1

for monday in MONDAYS:
    month = monday.month
    day = monday.day
    monday_month_day = (month, day)
    TGIVING_WK_START = (11, 19)
    TGIVING_WK_END = (11, 25)
    XMAS_WK_START = (12, 18)
    XMAS_WK_END = (12, 26)
    if TGIVING_WK_START < monday_month_day <= TGIVING_WK_END or \
    XMAS_WK_START < monday_month_day < XMAS_WK_END:
        formatted_date(monday, '- holiday week')
    else:
        formatted_date(monday, '')
