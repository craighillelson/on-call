""" __doc__ """

import create_shifts
import csv
import datetime
import employees
import eligible_emps
import functions
import pto
from datetime import date
from itertools import cycle

# data stores
AVAILS = {}
ASSIGNMENTS = {}
CONFLICTS = {}
EDIT_MERGED_ASSIGNMENTS = {}
PTO = dict(pto.PTO)
REM_EMPS_DCT = {}
SCHED_GROUPED_BY_EMP = {}
UNFILT_ASSIGNS = {}
UPDATED_ASSIGNMENTS = {}
ALL_EMPS = list(eligible_emps.ELIG_EMPS)
REM_EMPS = []
SHIFTS = list(create_shifts.SHIFTS)

today = date.today()

# build unfiltered assignments
for shift, email in zip(create_shifts.SHIFTS,
                        cycle(eligible_emps.ELIG_EMPS)):
    UNFILT_ASSIGNS[shift] = email

# find pto conflicts
if UNFILT_ASSIGNS:
    if len(UNFILT_ASSIGNS) > 1:
        print('assignments - break on conflict')
        for i, ((k, v), (k2, v2)) in enumerate(zip(UNFILT_ASSIGNS.items(),
                                                   PTO.items()), 1):
            if v != v2:
                ASSIGNMENTS[k] = v
                print(i, k, v)
            else:
                break
    else:
        print('assignment - break on conflict')
        for (k, v), (k2, v2) in zip(UNFILT_ASSIGNS.items(), PTO.items()):
            if v != v2:
                ASSIGNMENTS[k] = v
                print(k, v)
            else:
                break
else:
    pass

print(functions.RTN())

range_start = len(ASSIGNMENTS)
range_stop = len(SHIFTS)
REMAINING_SHIFTS = SHIFTS[range_start:range_stop]

if REMAINING_SHIFTS:
    print('shifts to fill')
    for i, shift in enumerate(REMAINING_SHIFTS, 1):
        print(i, shift)

    print(functions.RTN())

    print('remaining shifts')
    for i, (shift, email) in enumerate(zip(REMAINING_SHIFTS,
                                       cycle(ALL_EMPS)), 1):
        UPDATED_ASSIGNMENTS[shift] = email
        print(i, shift, email)

    print(functions.RTN())

MERGED_ASSIGNMENTS = {}
MERGED_ASSIGNMENTS.update(ASSIGNMENTS)
MERGED_ASSIGNMENTS.update(UPDATED_ASSIGNMENTS)

# find conflicts
for (k, v), (k2, v2) in zip(UNFILT_ASSIGNS.items(), pto.PTO.items()):
    if v != v2:
        AVAILS[k] = v
    else:
        CONFLICTS[k] = v

# resolve pto conflicts
if CONFLICTS:
    AVAILABLE_EMPS = eligible_emps.ELIG_EMPS
    if len(CONFLICTS) > 1:
        print('multiple conflicts')
        for i, (shift, email) in enumerate(CONFLICTS.items(), 1):
            print(f'{i} {shift} {email}')
            conflict_index = AVAILABLE_EMPS.index(v)
        del AVAILABLE_EMPS[conflict_index]
        print(functions.RTN())
        if AVAILABLE_EMPS:
            if len(AVAILABLE_EMPS) > 1:
                print('options')
                for i, emp in enumerate(AVAILABLE_EMPS, 1):
                    print(i, emp)
                print(functions.RTN())
            else:
                print('option')
                functions.output_emps(emp, AVAILABLE_EMPS)
        else:
            print(f'there are no employees available to cover the shift '
                  f'starting on {k}')
    else:
        print('one conflict')
        for shift, email in CONFLICTS.items():
            print(shift, email)
            next_week = k + datetime.timedelta(days=-today.weekday(), weeks=1)
            conflict_index = AVAILABLE_EMPS.index(v)
        del AVAILABLE_EMPS[conflict_index]
        print(functions.RTN())
        if AVAILABLE_EMPS:
            if len(AVAILABLE_EMPS) > 1:
                prev_shift_assign = k + datetime.timedelta(days=-k.weekday(),
                                                           weeks=-1)
                emp = MERGED_ASSIGNMENTS[prev_shift_assign]
                print('previous shift assignment')
                print(f'{prev_shift_assign} {emp}')
                print(functions.RTN())
                next_shift_assign = k + datetime.timedelta(days=-k.weekday(),
                                                           weeks=1)
                emp = MERGED_ASSIGNMENTS[next_shift_assign]
                print('next shift assignment')
                print(f'{next_shift_assign} {emp}')
                conflict_index = AVAILABLE_EMPS.index(emp)
                del AVAILABLE_EMPS[conflict_index]
                print(functions.RTN())
                if AVAILABLE_EMPS:
                    if len(AVAILABLE_EMPS) > 1:
                        print('best options')
                        functions.output_emps(emp, AVAILABLE_EMPS)
                    else:
                        print('available option')
                        functions.output_emps(emp, AVAILABLE_EMPS)
                else:
                    print(f'there are no employees available to cover the '
                          f'shift starting on {k}')
            else:
                print('option')
                for emp in AVAILABLE_EMPS:
                    print(emp)
                print(functions.RTN())
        else:
            print(f'there are no employees available to cover the shift '
                  f'starting on {k}')
else:
    pass

print('proposed assignments')
for i, (shift, email) in enumerate(MERGED_ASSIGNMENTS.items(), 1):
    print(i, shift, email)

print(functions.RTN())

selections = [
    'y',
    'n',
]

# prompt user to accept schedule as is or make edits
print('enter "y" to accept this schedule or "n" to make edits')
usr_choice = input()
if usr_choice not in selections:
    print('enter "y" to accept this schedule or "n" to make edits')
    usr_choice = input()

if usr_choice == 'y':
    HEADERS = 'shift','email'
    first_shift = str(create_shifts.SHIFTS[0])
    last_shift = str(create_shifts.SHIFTS[-1])
    file_name = 'assignments' + '_' + first_shift + '-' + last_shift + '.csv'
    with open(file_name, 'w') as out_file:
        out_csv = csv.writer(out_file)
        out_csv.writerow(HEADERS)
        for shift, email in MERGED_ASSIGNMENTS.items():
            keys_values = (shift, email)
            out_csv.writerow(keys_values)
    print(functions.RTN())
    print(f'"{file_name}" exported successfully')
else:
    exec(open('edit_sched.py').read())

for shift, email in sorted(MERGED_ASSIGNMENTS.items()):
    SCHED_GROUPED_BY_EMP.setdefault(email, []).append(shift)

print(functions.RTN())

# output on-call shifts by employee
print('summary')
print(functions.RTN())
print('shifts grouped by employee')

for email, shifts in SCHED_GROUPED_BY_EMP.items():
    print(f'{email} is scheduled for {len(shifts)} shifts')
    for i, shift in enumerate(shifts, 1):
        print(i, shift)
    print(functions.RTN())

# write assignments to csv
HEADERS = 'shift','email'

with open('assignments.csv', 'w') as out_file:
    out_csv = csv.writer(out_file)
    out_csv.writerow(HEADERS)
    for shift, email in MERGED_ASSIGNMENTS.items():
        keys_values = (shift, email)
        out_csv.writerow(keys_values)

# update user
print('"updated_assignments.csv" exported successfully')

print(functions.RTN())

# text each employee a list of shifts assigned to them
