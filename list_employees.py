""" __doc__ """

import employees

RTN = lambda: '\n'

print(RTN())

print('name, first eligible shift')
for emp, first_eligible_shift in employees.EMPLOYEES_FIRST_ELIGIBLE.items():
    print(f'{emp}, {first_eligible_shift}')

print(RTN())
