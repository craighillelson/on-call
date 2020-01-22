""" __doc__ """

# imports
import csv
import employees

# prompt user
domain = input('What is your domain name?\n')

while True:
    print('Enter the employee\'s name ' + str(len(employees.EMPLOYEES_DCT) + 1) +
        ' (Or enter nothing to stop.):')
    email_prefix = input()
    email = email_prefix + '@' + domain
    if email_prefix == '':
        break
    print('start date')
    start_date = input()
    employees.EMPLOYEES_DCT[email] = start_date

# write to csv
HEADERS = 'email', 'start_date'

with open('employees.csv', 'w') as out_file:
    out_csv = csv.writer(out_file)
    out_csv.writerow(HEADERS)
    for email, start_date in employees.EMPLOYEES_DCT.items():
        keys_values = email, start_date
        out_csv.writerow(keys_values)

# update user
print('email, start date')
for email, start_date in employees.EMPLOYEES_DCT.items():
    print(email, start_date)
