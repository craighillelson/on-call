""" __doc__ """

# imports
import csv
import datetime
import functions
from collections import namedtuple

# lambda
RTN = lambda: '\n'

# data stores
PTO = {}
WEEKDAYS = (
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
    )

# need to make individual dictionaries for each employee
# populate the dictionary PTO with the contents of 'pto.csv'
with open('pto.csv', 'r') as csv_file:
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        emp = row.employee
        start_date = row.start_date
        end_date = row.end_date
        pto_start_date_fmt = functions.format_date('pto_start_date', start_date)
        pto_end_date_fmt = functions.format_date('pto_end-date', end_date)
        PTO[emp] = [pto_start_date_fmt, pto_end_date_fmt]


print(RTN())

# output pto by employee
print('pto by employee')
print(RTN())
for emp, pto in PTO.items():
    print(f'employee: {emp}')
    print(RTN())
    pto_start_date = pto[0]
    pto_end_date = pto[1]
    if WEEKDAYS[pto_start_date_fmt.weekday()] == 'Monday':
        functions.output_start_dates(pto_start_date_fmt, 'unavailable_start')
    else:
        functions.output_start_dates(pto_start_date_fmt, 'unavailable_start')
    if WEEKDAYS[pto_end_date_fmt.weekday()] == 'Monday':
        functions.output_rtn_dates(pto_start_date_fmt, 'unavailable_start', 2)
    else:
        functions.output_rtn_dates(pto_start_date_fmt, 'unavailable_start', 1)
    print(RTN())
