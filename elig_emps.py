""" __doc__ """

import csv
import emps
import functions
from collections import namedtuple
from datetime import datetime

ELIG_EMPS = []
SHIFTS = []

with open('shifts.csv') as csv_file:
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        shift = datetime.strptime(row.shift, '%Y-%m-%d')
        SHIFTS.append(shift.date())

last_shift = SHIFTS[-1]

for email, start_date in emps.EMPLOYEES_DCT.items():
    start_date_fmt = functions.fmt_date('start_date', start_date)
    first_elig_shift = functions.calc_dates('first_elig', start_date_fmt, 12)
    if first_elig_shift < last_shift:
        ELIG_EMPS.append(email)
