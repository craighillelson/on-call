""" __doc__ """

import csv
import employees
import functions
from collections import namedtuple

def switch_case(a, b):
    """ switch case statement """
    a
    return a.get(b, 'nothing')


AVAILABLE_EMPS_DCT = {}
DCT = {}
SHIFTS_UPDATE = {}
EMPS = employees.EMPLOYEES
AVAILABLE_EMPS = []
AVAILABLE_EMPS_OPTIONS = []

# populate DCT with the contents of 'assignments.csv'
with open('assignments_2020-02-24-2020-05-18.csv') as csv_file:
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    i = 1
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        DCT[i] = [row.shift, row.email]
        i += 1

ASSIGN_OPTIONS = list(DCT.keys())

# prompt user to select a shift to edit
# output available employees
while True:
    print(functions.RTN())
    print('please select a shift to edit')
    for k, v in DCT.items():
        print(f'{k} {v[0]} {v[1]}')
    usr_choice = int(input())
    if usr_choice not in ASSIGN_OPTIONS:
        print('not an option')
    else:
        break

print(functions.RTN())
usr_choice_lst = switch_case(DCT, usr_choice)
print('you selected')
print(f'{usr_choice_lst[0]} {usr_choice_lst[1]}')
print(functions.RTN())

print(usr_choice)
print(functions.RTN())

if usr_choice - 1 < 0:
    usr_choice == DCT[-1]
else:
    prec_shift = usr_choice - 1
    prec_shift_lst = DCT[prec_shift]
    prec_shift_assign = prec_shift_lst[1]
    print(f'preceding shift {prec_shift} {prec_shift_assign}')

if usr_choice + 1 > len(DCT):
    usr_choice == DCT[+1]
else:
    succ_shift = usr_choice + 1
    succ_shift_lst = DCT[succ_shift]
    succ_shift_assign = succ_shift_lst[1]
    print(f'succeeding shift {succ_shift} {succ_shift_assign}')

print(functions.RTN())

for emp in EMPS:
    if usr_choice_lst[1] != emp and emp != prec_shift_assign and \
    emp != succ_shift_assign:
        AVAILABLE_EMPS.append(emp)

if AVAILABLE_EMPS:
    if len(AVAILABLE_EMPS) > 1:
        while True:
            print(f'please select an employee to substitute for shift '
                  f'{usr_choice_lst[0]}')
            for i, emp in enumerate(AVAILABLE_EMPS, 1):
                AVAILABLE_EMPS_DCT[i] = emp
                print(i, emp)
            emp_choice = int(input())
            subs_emp = switch_case(AVAILABLE_EMPS_DCT, emp_choice)
            print(f'you selected {subs_emp}')
            break
    else:
        print('available employee')
        print(AVAILABLE_EMPS[0])
else:
    print('there are no available employees')

DCT[usr_choice] = [usr_choice_lst[0], subs_emp]

print(functions.RTN())

for k, v in DCT.items():
    print(k, v[0], v[1])

HEADERS = 'shift','email'

with open('updates.csv', 'w') as out_file:
    out_csv = csv.writer(out_file)
    out_csv.writerow(HEADERS)
    for k, v in DCT.items():
        keys_values = (v[0], v[1])
        out_csv.writerow(keys_values)

print(functions.RTN())

print('"updates.csv" exported successfully')

print(functions.RTN())
