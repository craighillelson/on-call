""" __doc__ """

import csv
from collections import namedtuple

RTN = lambda: "\n"

dct = {}
employees = []
res = []

with open('shifts.csv') as csv_file:
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        dct[row.shift] = row.employee

print(RTN())

SCHED_GROUPED_BY_EMP = {}

for shift, emp in sorted(dct.items()):
    SCHED_GROUPED_BY_EMP.setdefault(emp, []).append(shift)

print('shifts grouped by employee')
print(RTN())

for emp, shifts in SCHED_GROUPED_BY_EMP.items():
    print(emp)
    for i, shift in enumerate(shifts):
        i += 1
        print(i, shift)
    print(RTN())
