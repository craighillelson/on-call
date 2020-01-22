""" __doc__ """

# imports
import csv
from datetime import date
from datetime import datetime
from collections import namedtuple
from itertools import cycle
import employees
import functions
# import pto
from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.rrule import MO
import prompt_user

# variables
RTN = lambda: '\n'
YEAR = str(prompt_user.YEAR)
# i = 0

# data stores
ASSIGNMENTS = {}
# INDEXES = []
QTR_START_END_DATES = []
SHIFTS = []
ELIGIBLE_EMPLOYEES = []

user_selected_qtr = prompt_user.starting_qtr
QTR_START_END = functions.start_end_date_str(user_selected_qtr)

# append list QTR_START_END_DATES
for qtr_date in QTR_START_END:
    date_str = functions.cat_date(YEAR, qtr_date)
    date_fmt = datetime.strptime(date_str, '%Y-%m-%d')
    date = date_fmt.date()
    QTR_START_END_DATES.append(date)

# find first and last Mondays of the quarter
QTR_START_DATE = QTR_START_END_DATES[0]
QTR_END_DATE = QTR_START_END_DATES[1]

# determine number of weeks between the start and end of the quarter
DATE_DELTA = QTR_END_DATE - QTR_START_DATE
WEEKS_BETWEEN = round(DATE_DELTA.days / 7) + 1

# append SHIFTS with the date of each Monday in the selected quarter
for i in range(1, WEEKS_BETWEEN, 1):
    SHIFTS.append(QTR_START_DATE + relativedelta(weekday=MO(+i)))

# write shifts to csv
functions.write_to_csv(['shifts'], 'shifts.csv', 'shift', SHIFTS)

print(RTN())

# print shifts
print('shifts')
for i, shift in enumerate(SHIFTS, 1):
    print(i, shift)

print(RTN())

# determine eligbility
# print('shift, start date, employee, eligibility')
for shift, emp, start in zip(SHIFTS, cycle(employees.EMPLOYEES),
                             cycle(employees.EMP_START_DATES)):
    start_strptime = datetime.strptime(start, '%Y-%m-%d')
    start_fmt = start_strptime.date()
    emp_start = emp, start_fmt
    if shift > start_fmt + relativedelta(weekday=MO(+12)):
        ELIGIBLE_EMPLOYEES.append(emp)
    else:
        pass

print('eligible employees')
for i, emp in enumerate(ELIGIBLE_EMPLOYEES, 1):
    print(i, emp)

print(RTN())

print('assignments')
for shift, emp in zip(SHIFTS, ELIGIBLE_EMPLOYEES):
    print(shift, emp)
    ASSIGNMENTS[shift] = emp

on_call_sched_qtr_year = 'Q' + str(prompt_user.starting_qtr) + '-' + YEAR
file_name = on_call_sched_qtr_year + '_assignments.csv'

HEADERS = 'shift', 'employee'

with open(file_name, 'w') as out_file:
    out_csv = csv.writer(out_file)
    out_csv.writerow(HEADERS)
    for shift, emp in ASSIGNMENTS.items():
        keys_values = (shift, emp)
        out_csv.writerow(keys_values)

print(RTN())

# update user
print(f'{file_name} exported successfully')

# print('assignments')
# for assignment in ASSIGNMENTS:
#     print(assignment[1], assignment[0])
    # process row
# for i, assignment in enumerate(ASSIGNMENTS, 1):
#     print(i, assignment[1], assignment[0])

# HEADERS = 'shift', 'employee'

# with open('assignments.csv', 'w') as out_file:
#     out_csv = csv.writer(out_file)
#     out_csv.writerow(HEADERS)
#     for shift_emp in ASSIGNMENTS:
#         shift = shift_emp[1]
#         emp = shift_emp[0]
#         shift_emp = shift, emp
#         out_csv.writerow(shift_emp)

# based on employee start dates, populate a list of employees eligible to work
# on call shifts
# for shift, start_date in zip(SHIFTS, cycle(employees.EMP_START_DATES)):
#     start_date_fmt = datetime.strptime(start_date, '%Y-%m-%d').date()
#     first_eligible = start_date_fmt + relativedelta(weekday=MO(+12))
#     if shift > first_eligible:
#         if i >= len(employees.EMP_START_DATES):
#             i = 0
#             functions.append_list(INDEXES, i)
#         else:
#             functions.append_list(INDEXES, i)
#     else:
#         i = 0
#         functions.append_list(INDEXES, i)
#     i += 1

# populate the assignments list
# for ind, emp in zip(INDEXES, cycle(employees.EMPLOYEES)):
#     ASSIGNMENTS.append(employees.EMPLOYEES[ind])

# print(RTN())

# output assignments
# print('assignments')
# for shift, assignment in zip(SHIFTS, ASSIGNMENTS):
    # print(shift, assignment)

# print(RTN())

# write assignments to csv
# on_call_sched_qtr_year = 'Q' + str(prompt_user.starting_qtr) + '-' + YEAR
# file_name = on_call_sched_qtr_year + '_assignments.csv'

# with open(file_name, 'w') as out_file:
    # out_csv = csv.writer(out_file)
    # out_csv.writerow(['shift','employee'])
    # for shift, employee in zip(SHIFTS, ASSIGNMENTS):
        # assignments = (shift, employee)
        # out_csv.writerow(assignments)

# alert user
# print(f'"{file_name}" was exported successfully')

print(RTN())
