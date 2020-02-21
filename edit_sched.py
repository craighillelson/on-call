""" __doc__ """

import csv
import elig_emps
import emps
import functions
from collections import namedtuple

print(functions.RTN())

ALL_EMPS = list(elig_emps.ELIG_EMPS)
ASSIGNS = {}
AVAIL_EMPS = {}
MERGED_ASSIGNMENTS_ENUM = {}

with open('assignments.csv') as csv_file:
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        ASSIGNS[row.shift] = row.email

for i, (k, v) in enumerate(ASSIGNS.items(), 1):
    MERGED_ASSIGNMENTS_ENUM[i] = k, v

print(functions.RTN())

print('please select a shift')
for num, shift_email in MERGED_ASSIGNMENTS_ENUM.items():
    shift = shift_email[0]
    email = shift_email[1]
    print(num, shift, email)
usr_sel_shift = int(input())
usr_sel_shift_lst = functions.switch_case(MERGED_ASSIGNMENTS_ENUM,
                                          usr_sel_shift)
sel_shift = usr_sel_shift_lst[0]
sel_assign = usr_sel_shift_lst[1]
functions.update_user(f'you selected\n{sel_shift} {sel_assign}')
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

functions.update_user('please select an employee')

i = 1
for emp in ALL_EMPS:
    if emp != sel_assign and emp != prev_shift_assign \
    and emp != subs_shift_assign:
        AVAIL_EMPS[i] = emp
        i += 1

for num, email in AVAIL_EMPS.items():
    print(num, email)

usr_sel_emp = int(input())
sel_emp = functions.switch_case(AVAIL_EMPS, usr_sel_emp)

print(f'you selected {sel_emp}')
print(functions.RTN())

print('shift to update')
print(f'{usr_sel_shift} {sel_shift} {sel_emp}')
print(functions.RTN())

MERGED_ASSIGNMENTS_ENUM[usr_sel_shift] = [sel_shift, sel_emp]

print('upadted assignments')
for num, shift_email in MERGED_ASSIGNMENTS_ENUM.items():
    print(num, shift_email[0], shift_email[1])
    
functions.csv_write(['num','shift','email'], 'updated_assignments.csv',
                    'num, shift_email', MERGED_ASSIGNMENTS_ENUM)
functions.update_user('updated_assignments.csv')
