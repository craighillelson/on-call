""" __doc__ """

from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *
D = datetime.now()
from itertools import cycle

MONDAYS = []
EMPLOYEE_ASSIGNMENTS = []

# replace with email addresses of your employees
EMPLOYEES = [
    'Ronnie',
    'Bobby',
    'Ricky',
    'Mike',
]

number_of_weeks = input("How many weeks in the future would you like to make \
the schedule for? ")
number_of_weeks = number_of_weeks + 1

for i in range(1, number_of_weeks, 1):
    MONDAYS.append(D + relativedelta(weekday=MO(+i)))

for n, employee in enumerate(cycle(EMPLOYEES)):
    EMPLOYEE_ASSIGNMENTS.append(employee)
    if n >= number_of_weeks:
        break

ASSIGNMENTS = dict(zip(MONDAYS, EMPLOYEE_ASSIGNMENTS))

for date, employee_assigned in sorted(ASSIGNMENTS.items()):
    print date.strftime('%Y-%m-%d'), employee_assigned
