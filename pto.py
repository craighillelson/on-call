""" __doc__ """

# imports
import csv
from collections import namedtuple

PTO = {}

with open('pto.csv') as csv_file:
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        PTO[row.shift] = row.email
