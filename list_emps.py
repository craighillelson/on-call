""" __doc__ """

import employees
import functions

EMPS = employees.EMPLOYEES

print(functions.RTN())

print('employees')
if EMPS:
    for i, email in enumerate(EMPS, 1):
        print(i, email)
else:
    print('"employees.csv" is empty')

print(functions.RTN())
