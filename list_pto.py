""" __doc__ """

# imports
import csv
from collections import namedtuple
from datetime import datetime
# from datetime import timedelta
# from dateutil.relativedelta import relativedelta
# from dateutil.rrule import MO

# function and lambda
def format_date(a, b):
    """ format date """
    a = datetime.strptime(b, '%Y-%m-%d')
    return a.strftime('%Y-%m-%d')


RTN = lambda: '\n'

# data store
PTO = {}

# populate the dictionary PTO with the contents of 'pto.csv'
with open('pto.csv', 'r') as csv_file:
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        employee = row.employee
        pto_start = format_date('end_date_strptime', row.start_date)
        pto_end = format_date('end_date_strptime', row.end_date)
        PTO[employee] = [pto_start, pto_end]

print(RTN())

# output employees and pto start and end dates
# print('employees and pto')

# print(RTN())

# for emp, pto_date_range in PTO.items():
#     print(f'employee: {emp}')
#     print(f'pto start date: {pto_date_range[0]}')
#     print(f'pto end date: {pto_date_range[1]}')
#     print(RTN())
