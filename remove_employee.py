""" __doc__ """

# imports
import csv
from collections import namedtuple
import pandas as pd

# lambda
RTN = lambda: '\n'

# data store
ASSIGNMENTS = {}

employees = pd.read_csv('employees.csv', index_col='email')

print(RTN())
print(employees)
print(RTN())

employee_rm = input('Please enter a employee\'s name to be deleted. \n')

employees.drop([employee_rm], inplace=True)

print(RTN())
print(employees)
print(RTN())

employees_updated = pd.DataFrame(employees)
employees_updated.to_csv('employees.csv')

print(f'{employee_rm} deleted successfully')

ASSIGNMENTS = {}

# get file name
with open('Q2-2020_assignments.csv') as csv_file:
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        ASSIGNMENTS[row.shift] = row.employee

print(RTN())

for shift, employee in ASSIGNMENTS.items():
    if employee_rm == employee:
        ASSIGNMENTS[shift] = 'empty'
    else:
        pass

print('updated assignments')
print('shift,employee')
for shift, employee in ASSIGNMENTS.items():
    print(shift, employee)

import csv

HEADERS = 'shift', 'employee'

with open('Q2-2020_assignments.csv', 'w') as out_file:
    out_csv = csv.writer(out_file)
    out_csv.writerow(HEADERS)
    for shift, employee in ASSIGNMENTS.items():
        keys_values = (shift, employee)
        out_csv.writerow(keys_values)

print(RTN())
