""" __doc__ """

import csv
from collections import namedtuple

RTN = lambda: "\n"

dct = {}

with open('shifts.csv') as csv_file:
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        dct[row.shift] = row.employee

print(RTN())

# do holiday week calculations here

print('shift, employee')
for shift, emp in dct.items():
    print(shift, emp)

print(RTN())
