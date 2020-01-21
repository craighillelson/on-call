""" __doc__ """

# imports
import csv
import employees
from datetime import date
from datetime import datetime

# lambda
RTN = lambda: '\n'

# variable
today = date.today()

# prompt user
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
        start_date = date_strptime.date()
        if start_date < today:
            print('Please choose today\'s date or later as a start date')
        else:
            print(f'You selected {start_date} as a start date.')
            break
    except ValueError:
        print('Please enter a date in YYYY-MM-DD format.')

# update dictionary
employees.EMPLOYEES_DCT[email] = start_date

# write to csv
HEADERS = 'employee', 'start_date'

with open('employees.csv', 'w') as out_file:
    out_csv = csv.writer(out_file)
    out_csv.writerow(HEADERS)
    for email, start_date in employees.EMPLOYEES_DCT.items():
        keys_values = email, start_date
        out_csv.writerow(keys_values)

# update user
print(RTN())

print('employee added')
print(f'key: {email}')
print(f'value: {start_date}')

print(RTN())

# output current list of employees
print('employees')
for email, start_date in employees.EMPLOYEES_DCT.items():
    print(email, start_date)

print(RTN())
