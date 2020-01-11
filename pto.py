""" __doc__ """

import csv
import datetime
from collections import namedtuple
from datetime import datetime

RTN = lambda: '\n'

def format_date(a, b):
    """ format date """
    a = datetime.strptime(b, '%Y-%m-%d')
    return a.strftime('%Y-%m-%d')


def date_day(a, b, c, d):
    """ determine the days of the week that employee's pto starts and ends """
    a = datetime.strptime(pto[b], '%Y-%m-%d')
    c = a.date()
    d = WEEKDAYS[c.weekday()]
    return d


PTO = {}
PTO_START = {}
PTO_END = {}
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
        pto_start = format_date('end_date_strptime', row.start_date)
        pto_end = format_date('end_date_strptime', row.end_date)
        PTO[emp] = [pto_start, pto_end]
        PTO_START[pto_start] = emp
        PTO_END[pto_end] = emp

print(RTN())

print('pto by employee')
for emp, pto in PTO.items():
    start_pto = date_day('pto_start', 0, 'pto_start_date', 'pto_start_day')
    end_pto = date_day('pto_end', 1, 'pto_end_date', 'pto_end_day')
    print(f'{emp}')
    print(f'start: {start_pto} {pto[0]}')
    print(f'end: {end_pto} {pto[1]}')
    print(RTN())
