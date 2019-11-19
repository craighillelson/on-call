""" __doc__ """

import csv
from collections import namedtuple

PTO = {}

with open('pto.csv') as f:
    F_CSV = csv.reader(f)
    ROW = namedtuple('ROW', next(F_CSV))
    for r in F_CSV:
        row = ROW(*r)
        PTO[row.shift] = row.employee

for k, v in PTO.items():
    print(k, v)
