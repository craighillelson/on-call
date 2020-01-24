""" __doc__ """

# imports
import csv
import functions
import employees

# prompt user
domain = input('What is your domain name?\n')

while True:
    print('Enter the employee\'s name ' + str(len(employees.EMPLOYEES_DCT) + 1)
          + ' (Or enter nothing to stop.):')
    email_prefix = input()
    email = email_prefix + '@' + domain
    if email_prefix == '':
        break
    print('start date')
    start_date = input()
    employees.EMPLOYEES_DCT[email] = start_date

# write dictionary to csv
functions.write_dct_to_csv(['email', 'start_date'], 'employees.csv',
                           'email, start_date', employees.EMPLOYEES_DCT)

# update user
print('email, start date')
for email, start_date in employees.EMPLOYEES_DCT.items():
    print(email, start_date)
