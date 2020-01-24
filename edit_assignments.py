""" __doc__ """

# imports
import csv
import functions
from collections import namedtuple

# lambda
RTN = lambda: '\n'

# data store
ASSIGNMENTS = {}

# populate ASSIGNMENTS dictionary with contents of existing assignments
with open('Q2-2020_assignments.csv') as csv_file:
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        ASSIGNMENTS[row.shift] = row.employee

for i, (shift, emp) in enumerate(ASSIGNMENTS.items(), 1):
    print(i, shift, emp)

# prompt user
user_selection = input('select a shift (YYYY-MM-DD)\n')

print(ASSIGNMENTS[user_selection])
change_to = input('edit to make\n')
ASSIGNMENTS[user_selection] = change_to

for i, (shift, emp) in enumerate(ASSIGNMENTS.items(), 1):
    print(i, shift, emp)

# write to csv
functions.write_dct_to_csv(['shift', 'employee'], 'Q2-2020_assignments.csv',
                           'shift, emp', ASSIGNMENTS)
