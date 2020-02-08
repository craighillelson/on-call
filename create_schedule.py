""" __doc__ """

import employees
import functions
from datetime import date

EMP_FIRST_ELIG = {}
SHIFTS_INELIG_EMP = {}
ASSIGNMENTS = {}
PTO = {}
PTO_SCHED = {}
SHIFTS = []
ELIG_EMP = []
INELIG_EMP = []

i = 0
today = date.today()
this_monday = functions.calc_dates('this_monday', today, 1)

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
    print(functions.RTN())
    print(f'start date: {this_monday}')
    print(functions.RTN())
    functions.append_shifts(this_monday, SHIFTS)
else:
    print('please specify a start date for the schedule (YYYY-MM-DD)')
    usr_start_date = input()
    print(functions.RTN())
    usr_start_date_fmt = functions.fmt_date('usr_start_date', usr_start_date)
    functions.append_shifts(usr_start_date_fmt, SHIFTS)

for email, start_date in employees.EMPLOYEES_DCT.items():
    start_date_fmt = functions.fmt_date('start_date_fmt', start_date)
    first_eligible = functions.calc_dates('first_eligible', start_date_fmt, 12)
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

functions.open_csv(PTO_SCHED)

for (shift1, email_lst1), (shift2, email_lst2) in zip(SHIFTS_INELIG_EMP.items(),
                                                      PTO_SCHED.items()):
    combined = email_lst1 + email_lst2
    for email in employees.EMPLOYEES:
        if email not in combined:
            ELIG_EMP.append(email)
    ASSIGNMENTS[shift1] = ELIG_EMP[i]
    i += 1
    if i > len(ELIG_EMP):
        i = 0

print('assignments')
for shift, email in ASSIGNMENTS.items():
    print(shift, email)

# write to csv
HEADERS = 'shift','email'
file_name = str(today) + '_assignments.csv'
functions.write_dct_to_csv(HEADERS, file_name, 'shift, email', ASSIGNMENTS)

print(functions.RTN())

# update user
print(f'"{file_name}" exported successfully')

print(functions.RTN())
