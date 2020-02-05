""" __doc__ """

# imports
import csv
from datetime import date
from datetime import datetime
from collections import namedtuple
from itertools import cycle
import employees
import functions
from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.rrule import MO
import prompt_user

# variables
# RTN = lambda: '\n'
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
functions.write_list_to_csv(['shifts'], 'shifts.csv', 'shift', SHIFTS)

print(functions.RTN())

# print shifts
print('shifts')
for i, shift in enumerate(SHIFTS, 1):
    print(i, shift)

print(functions.RTN())

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

print(functions.RTN())

# output assignments
print('assignments')
for shift, emp in zip(SHIFTS, ELIGIBLE_EMPLOYEES):
    print(shift, emp)
    ASSIGNMENTS[shift] = emp

on_call_sched_qtr_year = 'Q' + str(prompt_user.starting_qtr) + '-' + YEAR
file_name = on_call_sched_qtr_year + '_assignments.csv'

# write dictionary to csv
functions.write_dct_to_csv(['shift', 'employee'], file_name, 'shift, emp',
                           ASSIGNMENTS)

print(functions.RTN())

# update user
print(f'{file_name} exported successfully')

print(functions.RTN())
