""" __doc__ """

import csv
from collections import namedtuple

RTN = lambda: "\n"

SCHED = {}

# open 'assignments.csv' and populate the dictionary SCHED with its contents
with open('assignments.csv') as csv_file:
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        SCHED[row.shift] = row.employee

print(RTN())

SCHED_GROUPED_BY_EMP = {}

for shift, emp in sorted(SCHED.items()):
    SCHED_GROUPED_BY_EMP.setdefault(emp, []).append(shift)

print(RTN())

# output on-call shifts by employee
print('shifts grouped by employee')
for emp, shifts in SCHED_GROUPED_BY_EMP.items():
    print(emp)
    for i, shift in enumerate(shifts, 1):
        print(i, shift)
    print(RTN())

# write shifts per employee to individual csvs