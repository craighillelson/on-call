""" __doc__ """

import functions
import imports
import employees

D = imports.datetime.now()
year = D.year

tgiving_wk_start = '11-22'
tgiving_wk_end = '11-29'
xmas_wk_start = '12-18'
xmas_wk_end = '12-26'

tgiving_wk_start = functions.format_dates(tgiving_wk_start)
tgiving_wk_end = functions.format_dates(tgiving_wk_end)
xmas_wk_start = functions.format_dates(xmas_wk_start)
xmas_wk_end = functions.format_dates(xmas_wk_end)

MONDAYS = []
EMPLOYEE_ASSIGNMENTS = []

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
    functions.print_employee_holiday_week(tgiving_wk_start, tgiving_wk_end, \
    xmas_wk_start, xmas_wk_end)
