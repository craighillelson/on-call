""" __doc__ """

import csv
from collections import namedtuple

EMPLOYEES = []

with open('employees.csv') as f:
    F_CSV = csv.reader(f)
    ROW = namedtuple('ROW', next(F_CSV))
    for r in F_CSV:
        row = ROW(*r)
        EMPLOYEES.append(row.employee)
