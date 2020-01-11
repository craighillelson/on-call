""" __doc__ """

# imports
from datetime import date
from datetime import datetime
from collections import namedtuple
from itertools import cycle
import employees
import functions
import pto
from dateutil.relativedelta import relativedelta
from dateutil.rrule import MO
import prompt_user

# variables
RTN = lambda: '\n'
YEAR = str(prompt_user.YEAR)
i = 0

# lists
INDEXES = []
ASSIGNMENTS = []
QTR_START_END_DATES = []
SHIFTS = []
QTR_START_END = functions.start_end_date_str(prompt_user.starting_qtr)

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

# based on employee start dates, populate a list of employees eligible to work
# on call shifts
for shift, start_date in zip(SHIFTS, cycle(employees.EMP_START_DATES)):
    start_date_fmt = datetime.strptime(start_date, '%Y-%m-%d').date()
    first_eligible = start_date_fmt + relativedelta(weekday=MO(+12))
    if shift > first_eligible:
        if i >= len(employees.EMP_START_DATES):
            i = 0
            functions.append_list(INDEXES, i)
        else:
            functions.append_list(INDEXES, i)
    else:
        i = 0
        functions.append_list(INDEXES, i)
    i += 1

# populate the assignments list
for ind, emp in zip(INDEXES, cycle(employees.EMPLOYEES)):
    ASSIGNMENTS.append(employees.EMPLOYEES[ind])

print(RTN())

# output assignments
print('assignments')
for shift, assignment in zip(SHIFTS, ASSIGNMENTS):
    print(shift, assignment)

print(RTN())

# print('pto')
# print(RTN())
# for emp, pto_start_end in pto.PTO.items():
#     pto_start = datetime.strptime(pto_start_end[0], '%Y-%m-%d')
#     pto_end = datetime.strptime(pto_start_end[1], '%Y-%m-%d')
#     pto_start_fmt = pto_start + relativedelta(weekday=MO(-1))
#     pto_end_fmt = pto_end + relativedelta(weekday=MO(+1))
#     print(f'unavailable starting: {pto_start_fmt.date()} {emp}')
#     print(f'first shift after returning: {pto_end_fmt.date()} {emp}')
#     print(RTN())

# write assignments to csv
HEADERS = 'shift', 'employee'

on_call_sched_qtr_year = 'Q' + str(prompt_user.starting_qtr) + '-' + YEAR
file_name = on_call_sched_qtr_year + '_assignments.csv'
functions.write_to_csv("'shift', 'employee'", file_name, 'shift, assignment',
                       'zip(SHIFTS, ASSIGNMENTS)')

# alert user
print(f'"{file_name}" was exported successfully')

print(RTN())
