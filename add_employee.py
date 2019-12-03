""" __doc__ """

import csv
import employees
from datetime import datetime

RTN = lambda: '\n'

add_emp = input('Enter the name of the employee to be added \n')
add_start_date = input('Enter the employee\'s start date (YYYY-MM-DD) \n')
date_strptime = datetime.strptime(add_start_date, '%Y-%m-%d')
date_formatted = date_strptime.date()

employees.EMPLOYEES_DCT[add_emp] = date_formatted

print(RTN())

HEADERS = 'employee', 'start_date'

with open('employees.csv', 'w') as out_file:
    out_csv = csv.writer(out_file)
    out_csv.writerow(HEADERS)
    for emp, start_date in employees.EMPLOYEES_DCT.items():
        keys_values = (emp, date_formatted)
        out_csv.writerow(keys_values)

print('employee added')
print(f'key: {add_emp}')
print(f'value: {date_formatted}')

print(RTN())
