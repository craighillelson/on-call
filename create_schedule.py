""" __doc__ """

import csv
import employees
import shifts
from datetime import date
from itertools import cycle

RTN = lambda: '\n'
ELIGIBLE_EMPLOYEES = []
ASSIGNMENTS = {}

print('shift start dates')
for monday in shifts.SHIFTS:
    print(monday)

print(RTN())

print('eligible employees')
for employee, date_first_eligible in employees.EMPLOYEES_FIRST_ELIGIBLE.items():
    print(employee)
    ELIGIBLE_EMPLOYEES.append(employee)

# loop through shifts, if employee is not on pto, assign a shift
# if employee is on pto, skip to next employee

print(RTN())

for shift, emp in zip((shifts.SHIFTS), cycle(ELIGIBLE_EMPLOYEES)):
    ASSIGNMENTS[shift] = emp

print(RTN())

print('output schedule')
for shift, employee in ASSIGNMENTS.items():
    print(shift, employee)

# write to csv

print(RTN())

# i = 1
# TODAY = date.today()
# ELIGIBLE_EMPLOYEES = []
# ASSIGNMENTS = {}

# for emp in employees.EMPLOYEES_LST:
#     if i >= shifts.num_weeks:
#         break
#     name = emp[0]
#     first_eligible = emp[1]
#     if first_eligible < TODAY:
#         ELIGIBLE_EMPLOYEES.append(emp[0])
#     else:
#         pass
#     i += 1

# i = 1

# print('shift, employee')
# for shift, emp in ASSIGNMENTS.items():
#     print(f'{i} - {shift} - {emp}')
#     i += 1

# print(RTN())

# with open('shifts.csv', 'w') as out_file:
#     HEADERS = 'shift', 'employee'
#     out_csv = csv.writer(out_file)
#     out_csv.writerow(HEADERS)
#     for shift, emp in ASSIGNMENTS.items():
#         keys_values = (shift, emp)
#         out_csv.writerow(keys_values)

# print('"shifts.csv" exported successfully')

# print(RTN())
