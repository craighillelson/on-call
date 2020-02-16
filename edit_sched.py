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
ASSIGN_OPTIONS = []
AVAILABLE_EMPS_OPTIONS = []

# populate DCT with the contents of 'assignments.csv'
with open('assignments.csv') as csv_file:
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    i = 1
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        DCT[i] = [row.shift, row.email]
        ASSIGN_OPTIONS.append(i)
        i += 1

# prompt user to select a shift to edit
for k, v in DCT.items():
    print(f'{k} {v[0]} {v[1]}')

# output available employees
while True:
    print('please select a shift to edit')
    usr_choice = int(input())
    if usr_choice not in ASSIGN_OPTIONS:
        print('not an option')
    else:
        break

print(functions.RTN())
usr_choice_lst = switch_case(DCT, usr_choice)
print(f'you selected\n{usr_choice_lst[0]} {usr_choice_lst[1]}')
print(functions.RTN())
for emp in EMPS:
    if usr_choice_lst[1] != emp:
        AVAILABLE_EMPS.append(emp)

if AVAILABLE_EMPS:
    print('available employees')
    if len(AVAILABLE_EMPS) > 1:
        for i, emp in enumerate(AVAILABLE_EMPS, 1):
            AVAILABLE_EMPS_DCT[i] = emp
            AVAILABLE_EMPS_OPTIONS.append(i)
        while True:
            print(f'please select an employee to substitute for shift '
                  f'{usr_choice_lst[0]}')
            print(functions.RTN())
            for k, v in AVAILABLE_EMPS_DCT.items():
                print(k, v)
            usr_choice = int(input())
            if usr_choice not in AVAILABLE_EMPS_DCT:
                print('not an option')
            else:
                break
        print(functions.RTN())
        emp_update = switch_case(AVAILABLE_EMPS_DCT, usr_choice)
        print(f'you selected {emp_update}')
        SHIFTS_UPDATE[usr_choice_lst[0]] = emp_update
    else:
        print('available employee')
        print(AVAILABLE_EMPS[0])
else:
    print('there are no available employees')

print(functions.RTN())

print('shift to update')
for k, v in SHIFTS_UPDATE.items():
    print(k, v)

# finalize shifts
# write to csv
# update user

print(functions.RTN())
