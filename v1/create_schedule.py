""" __doc__ """

import calendar
import csv
from collections import namedtuple
import datetime
import employees
from datetime import date
from itertools import cycle

EMP_FIRST_ELIG = {}
SHIFTS_INELIG_EMP = {}
ASSIGNMENTS = {}
PTO = {}
SHIFTS = []
ELIG_EMP = []
INELIG_EMP = []

RTN = lambda: '\n'

def find_day(a):
    usr_start_day = datetime.datetime.strptime(a, '%Y-%m-%d').weekday()
    return (calendar.day_name[usr_start_day])

today = date.today()
this_monday = today + datetime.timedelta(days=-today.weekday(), weeks=1)

print(f'Would you like the on-call schedule to start on {this_monday} (y/n)? ')

answers = [
    'y',
    'n'
]

while True:
    user_choice = input()
    if user_choice not in answers:
        print(f'Would you like the on-call schedule to start on {this_monday} '
              f'(y/n)? ')
    else:
        break

if user_choice == 'y':
    print(RTN())
    print(f'start date: {this_monday}')
    for i in range(0, 14, 1):
        monday = this_monday + datetime.timedelta(days=-this_monday.weekday(), weeks=i)
        SHIFTS.append(monday)
else:
    print('please specify a start date for the schedule (YYYY-MM-DD)')
    usr_start_date = input()
    print(find_day(usr_start_date))
    usr_start_date_fmt = datetime.datetime.strptime(usr_start_date, '%Y-%m-%d').date()
    for i in range(0, 14, 1):
        monday = usr_start_date_fmt + datetime.timedelta(days=-usr_start_date_fmt.weekday(), weeks=i)
        SHIFTS.append(monday)

for email, start_date in employees.EMPLOYEES_DCT.items():
    start_date_fmt = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
    first_eligible = start_date_fmt + datetime.timedelta(days=-today.weekday(),
                                                         weeks=12)
    EMP_FIRST_ELIG[email] = first_eligible

for shift in SHIFTS:
    PTO[shift] = ''
    shift_ineligibles = str(shift) + '_ineligibles'
    shift_ineligibles = []
    for email, first_eligible in EMP_FIRST_ELIG.items():
        if shift > first_eligible:
            pass
        else:
            shift_ineligibles.append(email)
            SHIFTS_INELIG_EMP[shift] = shift_ineligibles

PTO_SCHED = {}

with open('pto.csv') as csv_file:
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        PTO_SCHED[row.shift] = [row.email]

print(RTN())

i = 0

for (shift1, email_lst1), (shift2, email_lst2) in zip(SHIFTS_INELIG_EMP.items(),
                              PTO_SCHED.items()):
    # print(shift1)
    # print(f'all employees: {employees.EMPLOYEES}')
    # print(f'ineligible employee(s): {email_lst1}')
    # print(f'pto scheduled: {email_lst2}')
    combined = email_lst1 + email_lst2
    # print(f'combined {combined}')
    for email in employees.EMPLOYEES:
        if email not in combined:
            ELIG_EMP.append(email)
    # print(f'eligible employees: {set(ELIGIBLE_EMPLOYEES)}')
    ASSIGNMENTS[shift1] = ELIG_EMP[i]
    i += 1
    if i > len(ELIG_EMP):
        i = 0

print('assignments')
for shift, email in ASSIGNMENTS.items():
    print(shift, email)

import csv

HEADERS = 'shift','email'

file_name = str(today) + '_assignments.csv'

with open(file_name, 'w') as out_file:
    out_csv = csv.writer(out_file)
    out_csv.writerow(HEADERS)
    for shift, email in ASSIGNMENTS.items():
        keys_values = (shift, email)
        out_csv.writerow(keys_values)

print(RTN())

# update user
print(f'"{file_name}" exported successfully')

print(RTN())
