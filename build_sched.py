""" __doc__ """

import create_shifts
import csv
import datetime
import employees
import functions
import pto
from datetime import date
from itertools import cycle

def calc_date(a, b):
    """ calculate first eligible shift """
    a = b + datetime.timedelta(days=-b.weekday(), weeks=12)
    return a


ASSIGNED_EMPS = []
CONFLICTS = []
ELIG_EMPS = []
EMPS_RES =[]
INDEXES = []
REMAINING_EMPS = []
REMAINING_SHIFTS = []
ASSIGNMENTS = {}
EMPS_FIRST_ELIG_SHIFTS = {}
RESOLVED_ASSIGNMENTS = {}
SCHED = {}
UNFILTERED_ASSIGNMENTS = {}

today = date.today()

last_shift = create_shifts.SHIFTS[-1]

for email, start_date in employees.EMPLOYEES_DCT.items():
    start_date_fmt = functions.fmt_date('start_date', start_date)
    first_elig_shift = calc_date('first_elig', start_date_fmt)
    if first_elig_shift < last_shift:
        ELIG_EMPS.append(email)

for shift, email in zip(create_shifts.SHIFTS, cycle(ELIG_EMPS)):
    UNFILTERED_ASSIGNMENTS[shift] = email

for i, ((k, v), (k2, v2)) in enumerate(zip(UNFILTERED_ASSIGNMENTS.items(),
                                           pto.PTO.items()), 1):
    pto_shift = functions.fmt_date('pto_shift', k2)
    if k == pto_shift and v != v2:
        ASSIGNMENTS[k] = v
        ASSIGNED_EMPS.append(v)
    else:
        res = ELIG_EMPS.index(v) + 1
        print(f'{i} {k} {v} - CONFLICT - resolution: {ELIG_EMPS[res]}')
        ASSIGNMENTS[k] = ELIG_EMPS[res]
        break

remainder = 13 - i

if remainder == 0:
    print('schedule - no conflicts')
    for i, (shift, email) in enumerate(ASSIGNMENTS.items(), 1):
        print(i, shift, email)
    print(functions.RTN())
else:
    print(f'index of resolution: {res}')

    print(functions.RTN())

    next_emp = res + 1

    for i in range(0, remainder, 1):
        EMPS_RES.append(ELIG_EMPS[next_emp])
        next_emp += 1
        if next_emp == len(ELIG_EMPS):
            next_emp = 0
        else:
            pass

    print('pick up from resolution')
    for i, email in enumerate(EMPS_RES, 1):
        print(i, email)
        REMAINING_EMPS.append(email)

    print(functions.RTN())

    print('remaining shifts')
    len_emps_res = len(EMPS_RES) * -1

    for i in range(len_emps_res, 0, 1):
        REMAINING_SHIFTS.append(create_shifts.SHIFTS[i])

    for i, shift in enumerate(REMAINING_SHIFTS, 1):
        print(i, shift)

    print(functions.RTN())

    print('assignments ending in resolution')
    for i, (shift, email) in enumerate(ASSIGNMENTS.items(), 1):
        print(i, shift, email)

    print(functions.RTN())

    for shift, email in zip(REMAINING_SHIFTS, REMAINING_EMPS):
        RESOLVED_ASSIGNMENTS[shift] = email

    # concat dictionaries
    SCHED = dict(ASSIGNMENTS)
    SCHED.update(RESOLVED_ASSIGNMENTS)

    print('resolved assignments')
    for i, (shift, email) in enumerate(SCHED.items(), 1):
        print(i, shift, email)

file_name = str(today) + '_assignments.csv'

HEADERS = 'shift','email'

with open(file_name, 'w') as out_file:
    out_csv = csv.writer(out_file)
    out_csv.writerow(HEADERS)
    for shift, email in SCHED.items():
        keys_values = (shift, email)
        out_csv.writerow(keys_values)

# update user
print(functions.RTN())

print(f'"{file_name}" exported successfully')

print(functions.RTN())
