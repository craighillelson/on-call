""" __doc__ """

import csv
import employees
from datetime import datetime

RTN = lambda: '\n'

add_emp = input('Enter the email address of the employee to be added  \n')
# validate that user entered an email address
add_start_date = input('Enter the employee\'s start date (YYYY-MM-DD) \n')
# validate that user entered date in YYYY-MM-DD format
date_strptime = datetime.strptime(add_start_date, '%Y-%m-%d')
date_formatted = date_strptime.date()

employees.EMPLOYEES_DCT[add_emp] = date_formatted

print(RTN())

HEADERS = 'employee', 'start_date'

print('employee added')
print(f'key: {add_emp}')
print(f'value: {date_formatted}')

print(RTN())

print('employees')
for emp, start_date in employees.EMPLOYEES_DCT.items():
    print(emp, start_date)

with open('employees.csv', 'w') as out_file:
    out_csv = csv.writer(out_file)
    out_csv.writerow(HEADERS)
    for emp, start_date in employees.EMPLOYEES_DCT.items():
        keys_values = (emp, start_date)
        out_csv.writerow(keys_values)

print(RTN())
