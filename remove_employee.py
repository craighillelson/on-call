import csv
from collections import namedtuple

lines = list()
RTN = lambda: '\n'

with open('employees.csv') as csv_file:
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        print(f'{row.employee} {row.start_date}')

employee = input('Please enter a employee\'s name to be deleted. \n')

with open('employees.csv') as csv_file:
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        lines.append(row)
        for field in row:
            if field == employee:
                lines.remove(row)

# fix - include headers

with open('employees.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(lines)

print(RTN())

print(f'{employee} deleted successfully')

print(RTN())
