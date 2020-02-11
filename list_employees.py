""" __doc__ """

import employees
import functions

print(functions.RTN())

for i, email in enumerate(employees.EMPLOYEES, 1):
    print(i, email)

print(functions.RTN())
