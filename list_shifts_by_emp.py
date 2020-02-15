""" __doc__ """

# imports
import csv
from collections import namedtuple

RTN = lambda: '\n'

# data stores
SCHED = {}
SCHED_GROUPED_BY_EMP = {}

with open('assignments.csv') as csv_file: # prompt user for qtr / year
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        SCHED[row.shift] = row.email

for shift, emp in sorted(SCHED.items()):
    SCHED_GROUPED_BY_EMP.setdefault(emp, []).append(shift)

print(RTN())

# output on-call shifts by employee
print('shifts grouped by employee')

print(RTN())

for email, shifts in SCHED_GROUPED_BY_EMP.items():
    print(email)
    for i, shift in enumerate(shifts, 1):
        print(i, shift)
    print(RTN())

# write shifts per employee to individual csvs
