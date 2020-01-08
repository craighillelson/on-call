""" __doc__ """

import csv
from collections import namedtuple
from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.rrule import MO

EMPLOYEES_LST = []
EMPLOYEES_DCT = {}
EMPLOYEES_FIRST_ELIGIBLE = {}

with open('employees.csv') as csv_file:
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        date_strptime = datetime.strptime(row.start_date, '%Y-%m-%d')
        first_eligible_shift = date_strptime + relativedelta(weekday=MO(+12))
        first_eligible_shift_fmt = first_eligible_shift.date()
        emp_first_eligible = row.employee, first_eligible_shift_fmt
        EMPLOYEES_LST.append(emp_first_eligible)
        EMPLOYEES_DCT[row.employee] = row.start_date
        EMPLOYEES_FIRST_ELIGIBLE[row.employee] = first_eligible_shift_fmt
