""" __doc__ """

# import employees
import csv
import functions
import itertools
import pto
import vars
from collections import namedtuple
from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.rrule import MO, SU
from itertools import cycle

RTN = lambda: "\n"

def output_shift_employee(a, b, c):
    a = str(a.strftime('%Y-%m-%d'))
    print(a, b, c)


EMPLOYEES = []

with open('employees.csv') as f:
    F_CSV = csv.reader(f)
    ROW = namedtuple('ROW', next(F_CSV))
    for r in F_CSV:
        row = ROW(*r)
        EMPLOYEES.append(row.employee)

TODAY = datetime.now()
MONDAYS = []
EMPLOYEE_ASSIGNMENTS = []

print(RTN())

NUMBER_OF_WEEKS = input('How many weeks in the future would you like to make \
the schedule for? ')
NUMBER_OF_WEEKS = int(NUMBER_OF_WEEKS) + 1

print(RTN())

# populate a list of mondays
for i in range(1, NUMBER_OF_WEEKS, 1):
    mon_incremented = TODAY + relativedelta(weekday=MO(+i))
    shift = mon_incremented.strftime("%Y-%m-%d")
    MONDAYS.append(shift)
    i = i + 1

for n, employee in enumerate(cycle(EMPLOYEES)):
    EMPLOYEE_ASSIGNMENTS.append(employee)
    if n >= NUMBER_OF_WEEKS:
        break

ASSIGNMENTS = dict(zip(MONDAYS, EMPLOYEE_ASSIGNMENTS))

print('assignments')
for shift, employees in ASSIGNMENTS.items():
    print(shift, employees)

print(RTN())

conflicts = ASSIGNMENTS.items() & pto.PTO.items()
conflicts_dct = dict(ASSIGNMENTS.items() & pto.PTO.items())

print('conflicts')
for shift, employee in sorted(conflicts_dct.items()):
    print(shift, employee)

# make sure that all conflicts are resolved and no employee works consecutive shifts
# keep track of how many shift each employee is scheduled for

print(RTN())

output = str(TODAY.strftime("%Y-%m-%d_%H:%M")) + '_on_call.csv'
functions.write_to_csv(output, ASSIGNMENTS)
print(f'"{output}" has been exported successfully')

print(RTN())
