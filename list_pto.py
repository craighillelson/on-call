""" __doc__ """

import csv
from collections import namedtuple
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from dateutil.rrule import MO

def output_date(a):
    """ format date """
    return a.strftime('%Y-%m-%d')

RTN = lambda: "\n"

pto = {}

print(RTN())

with open('pto.csv') as csv_file:
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        start_date_strptime = datetime.strptime(row.start_date, '%Y-%m-%d')
        pto_start = start_date_strptime + relativedelta(weekday=MO(-1))
        end_date_strptime = datetime.strptime(row.end_date, '%Y-%m-%d')
        pto_end = end_date_strptime + relativedelta(weekday=MO(+2))
        pto[row.employee] = [pto_start, pto_end]

for emp, pto in pto.items():
    print(f'employee: {emp}')
    print(f'on pto starting: {output_date(start_date_strptime)}')
    print(f'pto ending: {output_date(end_date_strptime)}')
    print(f"on pto for shift starting: {output_date(pto[0])}")
    print(f"available again: {output_date(pto[1])}")
    print(RTN())

print(RTN())
