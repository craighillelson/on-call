""" __doc__ """

import imports
import employees

D = imports.datetime.now()

MONDAYS = []
EMPLOYEE_ASSIGNMENTS = []

d1 = imports.datetime.strptime('2019-11-22', "%Y-%m-%d")
d2 = imports.datetime.strptime('2019-11-29', "%Y-%m-%d")
d3 = imports.datetime.strptime('2019-12-18', "%Y-%m-%d")
d4 = imports.datetime.strptime('2019-12-26', "%Y-%m-%d")

def print_employee_holiday_week(a, b, c, d):
    if a < date < b or c < date < d:
        print date.strftime('%Y-%m-%d'), employee_assigned, "- holiday week"
    else:
        print date.strftime('%Y-%m-%d'), employee_assigned

number_of_weeks = input("How many weeks in the future would you like to make \
the schedule for? ")
number_of_weeks = number_of_weeks + 1

for i in range(1, number_of_weeks, 1):
    MONDAYS.append(D + imports.relativedelta(weekday=imports.MO(+i)))
    d5 = D + imports.relativedelta(weekday=imports.MO(+i))

for n, employee in enumerate(imports.cycle(employees.EMPLOYEES)):
    EMPLOYEE_ASSIGNMENTS.append(employee)
    if n >= number_of_weeks:
        break

ASSIGNMENTS = dict(zip(MONDAYS, EMPLOYEE_ASSIGNMENTS))

for date, employee_assigned in sorted(ASSIGNMENTS.items()):
    print_employee_holiday_week(d1, d2, d3, d4)
