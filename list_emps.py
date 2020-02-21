""" __doc__ """

import emps
import functions

EMPS = emps.EMPLOYEES

print(functions.RTN())

print('employees')
if EMPS:
    for i, email in enumerate(EMPS, 1):
        print(i, email)
else:
    print('"employees.csv" is empty')

print(functions.RTN())
