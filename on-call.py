""" __doc__ """

import employees
import functions
import vars
from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.rrule import MO, SU
from itertools import cycle

RTN = lambda: "\n"

TODAY = datetime.now()
MONDAYS = []
EMPLOYEE_ASSIGNMENTS = []

NUMBER_OF_WEEKS = input('How many weeks in the future would you like to make \
the schedule for? ')
NUMBER_OF_WEEKS = int(NUMBER_OF_WEEKS) + 1

# populate a list of mondays
for i in range(1, NUMBER_OF_WEEKS, 1):
    mon_incremented = TODAY + relativedelta(weekday=MO(+i))
    MONDAYS.append(mon_incremented)
    i = i + 1

for n, employee in enumerate(cycle(employees.EMPLOYEES)):
    EMPLOYEE_ASSIGNMENTS.append(employee)
    if n >= NUMBER_OF_WEEKS:
        break

ASSIGNMENTS = dict(zip(MONDAYS, EMPLOYEE_ASSIGNMENTS))

print('shift -', 'employee -', 'holiday week')

for shift, employee in ASSIGNMENTS.items():
    month = shift.month
    day = shift.day
    shift_month_day = (month, day)
    if vars.TGIVING_WK_START < shift_month_day <= vars.TGIVING_WK_END or \
    vars.XMAS_WK_START < shift_month_day < vars.XMAS_WK_END:
        print(f"{shift.strftime('%Y-%m-%d')} - {employee} - yes")
    else:
        print(f"{shift.strftime('%Y-%m-%d')} - {employee} - no")

print(RTN())

output = str(TODAY.strftime("%Y-%m-%d_%H:%M")) + '_on_call.csv'
functions.write_to_csv(output, ASSIGNMENTS)
print(f'{output} has been exported successfully')

print(RTN())
