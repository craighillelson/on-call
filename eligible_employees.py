""" __doc__ """

import csv
from datetime import datetime
from collections import namedtuple
from itertools import cycle
from dateutil.relativedelta import relativedelta
from dateutil.rrule import MO

RTN = lambda: '\n'
emp_start_dates = []
eligible_employees = []
employees = []
indexes = []
assignments = []

with open('shifts.txt', 'r') as shifts:
    shifts = [shift.rstrip() for shift in shifts.readlines()]

with open('employees.csv', 'r') as csv_file:
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        emp = row.employee
        start = row.start_date
        employees.append(emp)
        emp_start_dates.append(start)

# print(RTN())

# print('shifts')
# for shift in enumerate(shifts, 1):
    # print(shift[0], shift[1])

# print(RTN())

# print('employee, start date, first eligible shift')
# for emp, start_date in zip(employees, emp_start_dates):
#     date = datetime.strptime(start_date, '%Y-%m-%d')
#     first_eligible = date + relativedelta(weekday=MO(+12))
#     print(emp)
#     print(f'start date: {start_date}')
#     print(f'first eligible shift: {first_eligible.date()}')
#     print(RTN())

i = 0

# print('shifts, start_date')
for shift, start_date in zip(shifts, cycle(emp_start_dates)):
    shift_fmt = datetime.strptime(shift, '%Y-%m-%d')
    start_date_fmt = datetime.strptime(start_date, '%Y-%m-%d')
    first_eligible = start_date_fmt + relativedelta(weekday=MO(+12))
    if shift_fmt > first_eligible:
        if i >= len(emp_start_dates):
            i = 0
            # print(f'{i} {shift_fmt.date()} {first_eligible.date()} '
                  # '- good to go')
            indexes.append(i)
        else:
            # print(f'{i} {shift_fmt.date()} {first_eligible.date()} '
                  # '- good to go')
            indexes.append(i)
    else:
        i = 0
        # print(f'{i} {shift_fmt.date()} {first_eligible.date()} '
              # '- not this shift')
        indexes.append(i)
    i += 1

print(RTN())

# print('indexes')
# for i in enumerate(indexes, 1):
#     print(i[0], i[1])

# print(RTN())

for ind, emp in zip(indexes, cycle(employees)):
    assignments.append(employees[ind])

print('assignments')
for assignment in enumerate(assignments, 1):
    print(assignment[0], assignment[1])

print(RTN())
