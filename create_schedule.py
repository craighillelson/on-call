""" __doc__ """

# imports
from datetime import date
from datetime import datetime
from collections import namedtuple
from itertools import cycle
import csv
from dateutil.relativedelta import relativedelta
from dateutil.rrule import MO
import prompt_user

# variables
RTN = lambda: '\n'
EMP_START_DATES = []
ELIGIBLE_EMPLOYEES = []
EMPLOYEES = []
INDEXES = []
ASSIGNMENTS = []
QTR_START_END_DATES = []
SHIFTS = []
YEAR = str(prompt_user.YEAR)

def start_end_date_str(argument):
    """ switch case statement """
    switcher = {
        1: ['01-01', '03-31'],
        2: ['04-01', '06-30'],
        3: ['07-01', '09-30'],
        4: ['10-01', '12-31'],
        }
    return switcher.get(argument, 'nothing')


def cat_date(a_a):
    """ concatenates year with start and end dates for each quarter """
    date_ymd = YEAR + '-' + a_a
    return date_ymd


def append_list():
    """ appends var to list """
    INDEXES.append(i)

QTR_START_END = start_end_date_str(prompt_user.starting_qtr)

# append list QTR_START_END_DATES
for qtr_date in QTR_START_END:
    date_str = cat_date(qtr_date)
    date_fmt = datetime.strptime(date_str, '%Y-%m-%d')
    date = date_fmt.date()
    QTR_START_END_DATES.append(date)

# find first and last Mondays of the quarter
QTR_START_DATE = QTR_START_END_DATES[0]
QTR_END_DATE = QTR_START_END_DATES[1]

# determine number of weeks between the start and end of the quarter
DATE_DELTA = QTR_END_DATE - QTR_START_DATE
WEEKS_BETWEEN = round(DATE_DELTA.days / 7)

# append SHIFTS with the date of each Monday in the selected quarter
for i in range(1, WEEKS_BETWEEN + 1, 1):
    SHIFTS.append(QTR_START_DATE + relativedelta(weekday=MO(+i)))

# write shifts to a text file
with open('shifts.txt', 'w') as out_file:
    OUT_CSV = csv.writer(out_file)
    for shift in SHIFTS:
        shift_str = str(shift)
        OUT_CSV.writerow([shift_str])

# import 'employees.csv' and populate two lists: EMPLOYEES and EMP_START_DATES
with open('employees.csv', 'r') as csv_file:
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        emp = row.employee
        start = row.start_date
        EMPLOYEES.append(emp)
        EMP_START_DATES.append(start)

i = 0

# based on employee start dates, populate a list of employees eligible to work
# on call shifts
for shift, start_date in zip(SHIFTS, cycle(EMP_START_DATES)):
    start_date_fmt = datetime.strptime(start_date, '%Y-%m-%d').date()
    first_eligible = start_date_fmt + relativedelta(weekday=MO(+12))
    if shift > first_eligible:
        if i >= len(EMP_START_DATES):
            i = 0
            append_list()
        else:
            append_list()
    else:
        i = 0
        append_list()
    i += 1

for ind, emp in zip(INDEXES, cycle(EMPLOYEES)):
    ASSIGNMENTS.append(EMPLOYEES[ind])

print(RTN())

# output assignments
print('assignments')
for shift, assignment in zip(SHIFTS, ASSIGNMENTS):
    print(shift, assignment)

print(RTN())

# write assignments to csv
HEADERS = 'shift', 'employee'

with open('assignments.csv', 'w') as out_file:
    OUT_CSV = csv.writer(out_file)
    OUT_CSV.writerow(HEADERS)
    for shift, assignment in zip(SHIFTS, ASSIGNMENTS):
        OUT_CSV.writerow([shift, assignment])

# alert user
print('"assignments.csv" was exported successfully')

print(RTN())
