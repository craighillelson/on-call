""" __doc__ """

import imports
import employees
import thanksgiving
import xmas

D = imports.datetime.now()

MONDAYS = []
EMPLOYEE_ASSIGNMENTS = []

number_of_weeks = input("How many weeks in the future would you like to make \
the schedule for? ")
number_of_weeks = number_of_weeks + 1

for i in range(1, number_of_weeks, 1):
    MONDAYS.append(D + imports.relativedelta(weekday=imports.MO(+i)))

for n, employee in enumerate(imports.cycle(employees.EMPLOYEES)):
    EMPLOYEE_ASSIGNMENTS.append(employee)
    if n >= number_of_weeks:
        break

ASSIGNMENTS = dict(zip(MONDAYS, EMPLOYEE_ASSIGNMENTS))

for date, employee_assigned in sorted(ASSIGNMENTS.items()):
    print date.strftime('%Y-%m-%d'), employee_assigned
