import csv
from collections import namedtuple
from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.rrule import MO, SU

RTN = lambda: "\n"

def output_date(a):
    return start_eligible_dates[a].strftime('%Y-%m-%d')


employees_dct = {}
employees_lst = []

with open('employees.csv') as csv_file:
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        date_strptime = datetime.strptime(row.start_date, '%Y-%m-%d')
        first_eligible_shift = date_strptime + relativedelta(weekday=MO(+12))
        employees_dct[row.employee] = [date_strptime, first_eligible_shift]

# print(RTN())

# print('employee, start_eligible_dates')
# for emp, start_eligible_dates in employees_dct.items():
    # print(emp)
    # print(f"start date: {output_date(0)}")
    # print(f"first eligible shift: {output_date(1)}")
    # print(RTN())
