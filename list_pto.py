""" __doc__ """

# imports
import csv
import functions
from collections import namedtuple

PTO_SCHED = {}
EMP_DCT = {}
nums = []

functions.open_csv(PTO_SCHED)

print(functions.RTN())

print('scheduled pto')
for shift, email in PTO_SCHED.items():
    if email != ['']:
        print(shift, email[0])
    else:
        pass

print(functions.RTN())
