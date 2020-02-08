""" __doc__ """

# imports
import csv
import functions
from collections import namedtuple

PTO_SCHED = {}
EMP_DCT = {}
functions.open_csv(PTO_SCHED)

print(functions.RTN())

print('scheduled pto')
for shift, email in PTO_SCHED.items():
    # if email != ['']:
    for emp in email:
        if email == ['']:
            print(f'{shift} - no pto booked')
        else:
            print(f'{shift} - {emp}')
    else:
        pass

print(functions.RTN())
