""" __doc__ """

import csv
from collections import namedtuple

RTN = lambda: "\n"

SCHED = {}

# output shifts
with open('shifts.csv') as csv_file:
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        print(row.shifts)
