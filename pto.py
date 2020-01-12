""" __doc__ """

import csv
import datetime
import functions
from collections import namedtuple
from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.rrule import MO

RTN = lambda: '\n'

def format_date(a, b):
    a = row.start_date
    b = datetime.strptime(a, '%Y-%m-%d').date()
    return b


def output_start_dates(a, b):
    """ output start dates """
    print(f'pto starts: {a}')
    b = a
    print(f'unavailable starting {b}')


def output_return_dates(a, b, c):
    """ outputs end dates """
    print(f'pto ends - {a}')
    b = a + relativedelta(weekday=MO(+c))
    print(f'available starting - {b}')


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
        pto_start_date_fmt = format_date('pto_start', 'pto_start_date')
        pto_end_date_fmt = format_date('pto_end', 'pto_end-date')
        PTO[emp] = [pto_start_date_fmt, pto_end_date_fmt]


print(RTN())

print('pto by employee')
for emp, pto in PTO.items():
    print(emp)
    pto_start_date = pto[0]
    pto_end_date = pto[1]
    if WEEKDAYS[pto_start_date_fmt.weekday()] == 'Monday':
        output_start_dates(pto_start_date_fmt, 'unavailable_start')
    else:
        output_start_dates(pto_start_date_fmt, 'unavailable_start')
    print(RTN())
    if WEEKDAYS[pto_end_date_fmt.weekday()] == 'Monday':
        output_return_dates(pto_start_date_fmt, 'unavailable_start', 2)
    else:
        output_return_dates(pto_start_date_fmt, 'unavailable_start', 1)
    print(RTN())
