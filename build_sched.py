""" __doc__ """

import create_shifts
import employees
import functions
import pto
from datetime import date
from itertools import cycle

# data stores
ASSIGNED_EMPS = []
CONFLICTS = []
ELIG_EMPS = []
EMPS_RES =[]
REMAINING_EMPS = []
REMAINING_SHIFTS = []
ASSIGNMENTS = {}
RESOLVED_ASSIGNMENTS = {}
SCHED = {}
UNFILTERED_ASSIGNMENTS = {}

today = date.today()

last_shift = create_shifts.SHIFTS[-1]

# populate EMPLOYEES_DCT with employees whose start date is twelve or more weeks
# in the past
for email, start_date in employees.EMPLOYEES_DCT.items():
    start_date_fmt = functions.fmt_date('start_date', start_date)
    first_elig_shift = functions.calc_dates('first_elig', start_date_fmt, 12)
    if first_elig_shift < last_shift:
        ELIG_EMPS.append(email)

# zip SHIFTS and ELIG_EMPS to create UNFILTERED_ASSIGNMENTS
for shift, email in zip(create_shifts.SHIFTS, cycle(ELIG_EMPS)):
    UNFILTERED_ASSIGNMENTS[shift] = email

# find pto conflicts
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

# output shifts and assignments
if remainder == 0:
    print('schedule - no conflicts')
    for i, (shift, email) in enumerate(ASSIGNMENTS.items(), 1):
        print(i, shift, email)
        SCHED[shift] = email
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

    # iterate through employees for the number of shifts not yet assigned
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

    # output assignments through resolved conflict
    print('assignments ending in resolution')
    for i, (shift, email) in enumerate(ASSIGNMENTS.items(), 1):
        print(i, shift, email)

    print(functions.RTN())

    for shift, email in zip(REMAINING_SHIFTS, REMAINING_EMPS):
        RESOLVED_ASSIGNMENTS[shift] = email

    # concatenate dictionaries
    SCHED = dict(ASSIGNMENTS)
    SCHED.update(RESOLVED_ASSIGNMENTS)

    # output resolved assignments
    print('resolved assignments')
    for i, (shift, email) in enumerate(SCHED.items(), 1):
        print(i, shift, email)

# write SCHED to csv
file_name = str(today) + '_assignments.csv'

functions.write_dct_to_csv(['shift','email'], file_name, 'shift, email', SCHED)

# update user
print(functions.RTN())

print(f'"{file_name}" exported successfully')

print(functions.RTN())
