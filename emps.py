"""Import a csv and populate lists and dictionaries."""

import csv
from collections import namedtuple

EMPLOYEES = []
EMP_START_DATES = []
EMPLOYEES_DCT = {}
EMPLOYEES_ENUM = {}

with open("emps.csv", "r") as csv_file:
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        employee = row.email
        start = row.start_date
        EMPLOYEES.append(employee)
        EMP_START_DATES.append(start)
        EMPLOYEES_DCT[employee] = start

for i, employee in enumerate(EMPLOYEES, 1):
    EMPLOYEES_ENUM[i] = employee
