"""Build schedule."""

import create_shifts
import csv
import datetime
import emps
import elig_emps
from functions import (csv_write,
                       prev_subs_shift_lst,
                       switch_case,
                       update_user)
import pto
import pyinputplus as pyip
from datetime import date
from itertools import cycle

# data stores
ASSIGNMENTS = {}
AVAILS = {}
AVAIL_EMPS = {}
CONFLICTS = {}
MERGED_ASSIGNS = {}
PTO = dict(pto.PTO)
UNFILT_ASSIGNS = {}
UPDATED_ASSIGNMENTS = {}
ALL_EMPS = list(elig_emps.ELIG_EMPS)
SHIFTS = list(create_shifts.SHIFTS)

today = date.today()

# build unfiltered assignments
for shift, email in zip(create_shifts.SHIFTS, cycle(elig_emps.ELIG_EMPS)):
    UNFILT_ASSIGNS[shift] = email

# find range of remaining shifts
range_start = len(ASSIGNMENTS)
range_stop = len(SHIFTS)
REMAINING_SHIFTS = SHIFTS[range_start:range_stop]

# if a conflict is found, zip remaining shifts with employees
if REMAINING_SHIFTS:
    print('\nshifts to fill')
    for i, shift in enumerate(REMAINING_SHIFTS, 1):
        print(i, shift)
    print('\nremaining shifts')
    for i, (shift, email) in enumerate(zip(REMAINING_SHIFTS,
                                       cycle(ALL_EMPS)), 1):
        UPDATED_ASSIGNMENTS[shift] = email
        print(i, shift, email)
    # print(functions.RTN())
else:
    print('no conflicts found')

# merge existing assignments with assignments wherein conflicts have been
# resolved
MERGED_ASSIGNMENTS = {}
MERGED_ASSIGNMENTS_ENUM = {}
MERGED_ASSIGNMENTS.update(ASSIGNMENTS)
MERGED_ASSIGNMENTS.update(UPDATED_ASSIGNMENTS)


# find conflicts
for (shift1, email1), (shift2, email2) in zip(UNFILT_ASSIGNS.items(),
                                              pto.PTO.items()):
    if email1 != email2:
        AVAILS[shift1] = email1
    else:
        CONFLICTS[shift1] = email1

if CONFLICTS:
    if len(CONFLICTS) > 1:
        print('conflicts')
        for i, (shift, email) in enumerate(CONFLICTS.items(), 1):
            print(f'{i} {shift} {email} - PTO')
    else:
        print('conflict')
        for shift, email in CONFLICTS.items():
            print(f'{shift} {email} - PTO')
else:
    pass

print('\nproposed assignments')
for i, (shift, email) in enumerate(MERGED_ASSIGNMENTS.items(), 1):
    print(i, shift, email)
    MERGED_ASSIGNMENTS_ENUM[i] = [shift, email]

usr_choice = pyip.inputYesNo('\nenter \'yes\' to accept this schedule or '
                             '\'no\' to make edits\n> ')

if usr_choice == 'yes':
    file_name = 'assignments.csv'
    csv_write(['shift','email'], file_name, 'shift, email',
                        MERGED_ASSIGNMENTS)
    update_user(f'{file_name} exported successfully')
else:
    print('please select a shift')
    for num, shift_email in MERGED_ASSIGNMENTS_ENUM.items():
        shift = shift_email[0]
        email = shift_email[1]
        print(num, shift, email)
    usr_sel_shift = int(input())
    usr_sel_shift_lst = switch_case(MERGED_ASSIGNMENTS_ENUM,
                                              usr_sel_shift)
    sel_shift = usr_sel_shift_lst[0]
    sel_assign = usr_sel_shift_lst[1]
    update_user(f'you selected\n{sel_shift} {sel_assign}')
    prev_shift_lst = functions.prev_subs_shift_lst('prev_shift_lst',
                                                   MERGED_ASSIGNMENTS_ENUM,
                                                   usr_sel_shift, -1)
    prev_shift = prev_shift_lst[0]
    prev_shift_assign = prev_shift_lst[1]
    subs_shift_lst = functions.prev_subs_shift_lst('subs_shift_lst',
                                                   MERGED_ASSIGNMENTS_ENUM,
                                                   usr_sel_shift, 1)
    subs_shift = subs_shift_lst[0]
    subs_shift_assign = subs_shift_lst[1]
    print(f'previous shift {prev_shift} {prev_shift_assign}')
    print(f'subsequent shift {subs_shift} {subs_shift_assign}')

    update_user('please select an employee')

    i = 1
    for emp in ALL_EMPS:
        if emp != sel_assign and emp != prev_shift_assign \
        and emp != subs_shift_assign:
            AVAIL_EMPS[i] = emp
            i += 1

    for num, email in AVAIL_EMPS.items():
        print(num, email)

    usr_sel_emp = int(input())
    sel_emp = switch_case(AVAIL_EMPS, usr_sel_emp)

    print(f'you selected {sel_emp}\n')
    # print(functions.RTN())

    print('shift to update')
    print(f'{usr_sel_shift} {sel_shift} {sel_emp}\n')
    # print(functions.RTN())

    MERGED_ASSIGNMENTS_ENUM[usr_sel_shift] = [sel_shift, sel_emp]

    print('upadted assignments')
    for num, shift_email in MERGED_ASSIGNMENTS_ENUM.items():
        print(num, shift_email[0], shift_email[1])
        MERGED_ASSIGNS[shift_email[0]] = shift_email[1]

    csv_write(['shift','email'], 'updated_assignments.csv',
                        'shift_email', MERGED_ASSIGNS)
    update_user('updated_assignments.csv')
