""" __doc__ """

import employees
import functions

print(functions.RTN())

if employees.EMPLOYEES:
    for i, email in enumerate(employees.EMPLOYEES, 1):
        print(i, email)
else:
    print('"employees.csv" is empty')

print(functions.RTN())
