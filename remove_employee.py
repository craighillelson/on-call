""" __doc__ """

# remove employee
import csv
from collections import namedtuple
import employees
import functions

nums = []
EMP_DCT = {}
SCHED = {}

for i, email in enumerate(employees.EMPLOYEES, 1):
    nums.append(i)
    EMP_DCT[i] = email

print(functions.RTN())

# prompt user to select an employee to remove
print(f'Please select an employee to remove.')
for num, email in EMP_DCT.items():
    print(num, email)

while True:
    usr_choice = int(input())
    emp_to_del = functions.switch_case(usr_choice, EMP_DCT)
    if usr_choice not in nums:
        print('Not an option. Please select one of the options above. ')
    else:
        print(functions.RTN())
        break

print(f'You selected {emp_to_del}')

print(functions.RTN())
del employees.EMPLOYEES_DCT[emp_to_del]

print('updated list of employees')
for email, start_date in employees.EMPLOYEES_DCT.items():
    print(email, start_date)

print(functions.RTN())

functions.write_dct_to_csv(['email','start_date'], 'employees.csv', 'k, v',
                           employees.EMPLOYEES_DCT)

# update user
print('"employees.csv" exported successfully')

with open('2020-02-12_assignments.csv') as csv_file:
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        SCHED[row.shift] = row.email

for shift, email in SCHED.items():
    if emp_to_del in email:
        print(shift, email)

# find conflicts
print('it is suggested that you edit or rebuild the schedule')

print(functions.RTN())
