"""
Based on start date, determine the earliest date that each employee would
be eligible to be scheduled for an on-call shift.
"""

import csv
from emps import EMPLOYEES_DCT
from functions import (calc_dates,
                       fmt_date)
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

for email, start_date in EMPLOYEES_DCT.items():
    start_date_fmt = fmt_date('start_date', start_date)
    first_elig_shift = calc_dates(start_date_fmt, 12)
    if first_elig_shift < last_shift:
        ELIG_EMPS.append(email)
