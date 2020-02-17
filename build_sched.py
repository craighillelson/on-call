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
REM_EMPS_DCT = {}
UNFILT_ASSIGNS = {}
UPDATED_ASSIGNMENTS = {}
ALL_EMPS = list(eligible_emps.ELIG_EMPS)
REM_EMPS = []
SCHED_GROUPED_BY_EMP = {}

# functions
def switch_case(a, b):
    """ switch case statement """
    a
    return a.get(b, 'nothing')

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
                                                   pto.PTO.items()), 1):
            if v != v2:
                ASSIGNMENTS[k] = v
                print(i, k, v)
            else:
                break
    else:
        print('assignment - break on conflict')
        for (k, v), (k2, v2) in zip(UNFILT_ASSIGNS.items(), pto.PTO.items()):
            if v != v2:
                ASSIGNMENTS[k] = v
                print(k, v)
            else:
                break
else:
    pass

print(functions.RTN())

range_start = len(ASSIGNMENTS)
range_stop = len(create_shifts.SHIFTS)
REMAINING_SHIFTS = create_shifts.SHIFTS[range_start:range_stop]

if REMAINING_SHIFTS:
    print('shifts to fill')
    for i, shift in enumerate(REMAINING_SHIFTS, 1):
        print(i, shift)

    print(functions.RTN())

    print('remaining shifts')
    for i, (shift, email) in enumerate(zip(REMAINING_SHIFTS,
                                       cycle(eligible_emps.ELIG_EMPS)), 1):
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
        for i, (k, v) in enumerate(CONFLICTS.items(), 1):
            print(f'{i} {k} {v}')
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
                for emp in AVAILABLE_EMPS:
                    print(emp)
                print(functions.RTN())
        else:
            print(f'there are no employees available to cover the shift '
                  f'starting on {k}')
    else:
        print('one conflict')
        for k, v in CONFLICTS.items():
            print(k, v)
            next_week = k + datetime.timedelta(days=-today.weekday(), weeks=1)
            conflict_index = AVAILABLE_EMPS.index(v)
        del AVAILABLE_EMPS[conflict_index]
        print(functions.RTN())
        if AVAILABLE_EMPS:
            if len(AVAILABLE_EMPS) > 1:
                # print('all options')
                # for i, emp in enumerate(AVAILABLE_EMPS, 1):
                #     print(i, emp)
                # print(functions.RTN())
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
                        for emp in AVAILABLE_EMPS:
                            print(emp)
                        print(functions.RTN())
                    else:
                        print('best option')
                        for emp in AVAILABLE_EMPS:
                            print(emp)
                        print(functions.RTN())
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
for i, (k, v) in enumerate(MERGED_ASSIGNMENTS.items(), 1):
    print(i, k, v)

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
    # name file in the following way: assignments_2020-02-17-2020-05-11.csv
    # MERGED_ASSIGNMENTS - keys [0] and [-1]
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
    # maybe move this to edit_sched.py
    print(functions.RTN())
    print('please select a shift to edit')
    for i, (k, v) in enumerate(MERGED_ASSIGNMENTS.items(), 1):
        EDIT_MERGED_ASSIGNMENTS[i] = [k, v]
    for k, v in EDIT_MERGED_ASSIGNMENTS.items():
        print(k, v[0], v[1])
    usr_choice = int(input())
    print(functions.RTN())
    usr_choice_lst = switch_case(EDIT_MERGED_ASSIGNMENTS, usr_choice)
    print(f'you selected')
    print(f'{usr_choice_lst[0]} {usr_choice_lst[1]}')
    print(functions.RTN())
    prec_lst = EDIT_MERGED_ASSIGNMENTS[usr_choice - 1]
    prec_emp = prec_lst[1]
    # subs_lst = EDIT_MERGED_ASSIGNMENTS[usr_choice + 1]
    # subs_emp = subs_lst[1]
    if usr_choice - 1 <= 0:
        print('succeeding shift')
        print(next_lst[0], next_lst[1])
        subs_lst = EDIT_MERGED_ASSIGNMENTS[usr_choice + 1]
        for i, emp in enumerate(ALL_EMPS, 1):
            if emp != usr_choice_lst[1] and emp != subs_emp:
                REM_EMPS.append(emp)
    elif (usr_choice + 1) >= (len(EDIT_MERGED_ASSIGNMENTS) + 1):
        print('preceding shift')
        print(prec_lst[0], prec_lst[1])
        print(functions.RTN())
        for i, emp in enumerate(ALL_EMPS, 1):
            if emp != usr_choice_lst[1] and emp != prec_emp:
                REM_EMPS.append(emp)
    else:
        subs_lst = EDIT_MERGED_ASSIGNMENTS[usr_choice + 1]
        subs_emp = subs_lst[1]
        print('preceding shift')
        print(prec_lst[0], prec_lst[1])
        print(functions.RTN())
        print('subsequent shift')
        print(subs_lst[0], subs_lst[1])
        print(functions.RTN())
        for i, emp in enumerate(ALL_EMPS, 1):
            if emp != usr_choice_lst[1] and emp != prec_emp and emp != subs_emp:
                REM_EMPS.append(emp)
    print('remaining options')
    for i, emp in enumerate(REM_EMPS, 1):
        REM_EMPS_DCT[i] = emp
        print(i, emp)
    print(functions.RTN())
    print('please select an employee')
    usr_sel_emp = int(input())
    usr_sel = switch_case(REM_EMPS_DCT, usr_sel_emp)
    print(functions.RTN())
    print(f'you selected {usr_sel}')

EDIT_MERGED_ASSIGNMENTS[usr_choice] = [usr_choice_lst[0], usr_sel]
for k, v in EDIT_MERGED_ASSIGNMENTS.items():
    print(k, v[0], v[1])

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

HEADERS = 'shift','email'

with open('updated_assignments.csv', 'w') as out_file:
    out_csv = csv.writer(out_file)
    out_csv.writerow(HEADERS) # define HEADERS before running function
    for k, v in EDIT_MERGED_ASSIGNMENTS.items(): # rename keys and values to make to make them meaningful
        keys_values = (v[0], v[1])
        out_csv.writerow(keys_values)

# update user
print('"updated_assignments.csv" exported successfully')

# text each employee a list of shifts assigned to them
