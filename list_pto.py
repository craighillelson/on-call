""" __doc__ """

import csv
from collections import namedtuple
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from dateutil.rrule import MO

def format_date(a, b):
    a = datetime.strptime(b, '%Y-%m-%d')
    return a.strftime('%Y-%m-%d')


RTN = lambda: "\n"

PTO = {}

with open('pto.csv') as csv_file:
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        pto_start = format_date('end_date_strptime', row.end_date)
        pto_end = format_date('end_date_strptime', row.end_date)
        PTO[row.employee] = [pto_start, pto_end]
        # start_date_strptime = format_date('start_date_strptime', row.start_date)
        # pto_start = output_date(start_date_strptime)
        # end_date_strptime = format_date('end_date_strptime', row.end_date)
        # pto_end = output_date(end_date_strptime)
        # start_date_strptime = datetime.strptime(row.start_date, '%Y-%m-%d')
        # end_date_strptime = datetime.strptime(row.end_date, '%Y-%m-%d')
        # start_date_strptime = datetime.strptime(row.start_date, '%Y-%m-%d')
        # end_date_strptime = datetime.strptime(row.end_date, '%Y-%m-%d')
        # pto_start = start_date_strptime + relativedelta(weekday=MO(-1))
        # pto_end = end_date_strptime + relativedelta(weekday=MO(+2))
        # print(row.employee)
        # print(f'{pto_start} - {pto_end}')
        # print(RTN())

# for emp, pto in pto.items():
    # print(f'employee: {emp}')
    # print(f'pto starting: {output_date(start_date_strptime)}')
    # print(f'pto ending: {output_date(end_date_strptime)}')
    # print(RTN())
    # print(f"on pto for shift starting: {output_date(pto[0])}")
    # print(f"available again: {output_date(pto[1])}")
    # print(RTN())
    # print('-' * 40)
    # print(RTN())

# for k, v in PTO.items(): # rename dct, keys, and values to make them meaningful
    # print(k, v[0], v[1]) # process row
