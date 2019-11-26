import csv
from collections import namedtuple

RTN = lambda: "\n"

employees_dct = {}
employees_lst = []

with open('employees.csv') as csv_file:
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        employees_dct[row.employee] = row.start_date
        employees_lst.append(row.employee)

print(RTN())
