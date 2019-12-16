""" __doc__ """

import csv
import employees
from datetime import datetime

RTN = lambda: '\n'

domain = input('What is your fully qualified domain name?\n')

email_prefix = input('Enter the email prefix of the employee to be added \n')
email = email_prefix + '@' + domain

add_start_date = input('Enter the employee\'s start date (YYYY-MM-DD)\n')
# validate that user entered date in YYYY-MM-DD format
date_strptime = datetime.strptime(add_start_date, '%Y-%m-%d')
date_formatted = date_strptime.date()

employees.EMPLOYEES_DCT[email] = date_formatted

print(RTN())

HEADERS = 'employee', 'start_date'

print('employee added')
print(f'key: {email}')
print(f'value: {date_formatted}')

print(RTN())

print('employees')
for email, start_date in employees.EMPLOYEES_DCT.items():
    print(email, start_date)

with open('employees.csv', 'w') as out_file:
    out_csv = csv.writer(out_file)
    out_csv.writerow(HEADERS)
    for email, start_date in employees.EMPLOYEES_DCT.items():
        keys_values = (email, start_date)
        out_csv.writerow(keys_values)

print(RTN())
