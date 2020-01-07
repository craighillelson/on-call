""" __doc__ """

import csv
import employees
from datetime import date
from datetime import datetime

today = date.today()

RTN = lambda: '\n'

domain = input('What is your domain name?\n')
# determine domain name from existing employees and
# prompt user re: whether or not to use that domain when adding next employee
# prompt user re: how many employees they'd like to add
# num_emp_to_add = int(input('How many employees would you like to add?\n'))

email_prefix = input('Enter the email prefix of the employee to be added\n')
email = email_prefix + '@' + domain

while True:
    try:
        add_start_date = str(input('Enter the employee\'s start date '
                                   '(MMMM-DD-YY) '))
        date_strptime = datetime.strptime(add_start_date, '%Y-%m-%d')
        date_formatted = date_strptime.date()
        if date_formatted < today:
            print('Please choose today\'s date or later as a start date')
        else:
            print(f'You selected {date_formatted} as a start date.')
            break
    except ValueError:
        print('Please enter a date in YYYY-MM-DD format.')

employees.EMPLOYEES_DCT[email] = date_formatted

print(RTN())

HEADERS = 'employee', 'start_date'

print(RTN())

with open('employees.csv', 'w') as out_file:
    out_csv = csv.writer(out_file)
    out_csv.writerow(HEADERS)
    for email, start_date in employees.EMPLOYEES_DCT.items():
        keys_values = (email, start_date)
        out_csv.writerow(keys_values)

print(RTN())

print('employees')
for email, start_date in employees.EMPLOYEES_DCT.items():
    print(email, start_date)

print(RTN())

print('employee added')
print(f'key: {email}')
print(f'value: {date_formatted}')

print(RTN())
