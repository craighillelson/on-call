""" __doc__ """

import csv
from collections import namedtuple

EMPLOYEES = []
EMP_START_DATES = []
EMPLOYEES_DCT = {}

with open('employees.csv', 'r') as csv_file:
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        emp = row.employee
        start = row.start_date
        EMPLOYEES.append(emp)
        EMP_START_DATES.append(start)
        EMPLOYEES_DCT[emp] = start
