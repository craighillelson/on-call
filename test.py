""" __doc__ """

import create_shifts
import datetime
import employees
import eligible_emps
import functions
import pto
from datetime import date
from itertools import cycle

# data stores
AVAILS = {}
ASSIGNMENTS = {}
CONFLICTS = {}
ELIG_EMPS = []
EMPS_RES = []
UNFILTERED_ASSIGNMENTS = {}
UPDATED_ASSIGNMENTS = {}

for i, (shift, email) in enumerate(zip(create_shifts.SHIFTS,
                                       cycle(eligible_emps.ELIG_EMPS)), 1):
    UNFILTERED_ASSIGNMENTS[shift] = email

print('assignments - break on conflict')
for (k, v), (k2, v2) in zip(UNFILTERED_ASSIGNMENTS.items(), pto.PTO.items()):
    if v != v2:
        ASSIGNMENTS[k] = v
    else:
        CONFLICTS[k] = v
        emp = v
        break

for i, (k, v) in enumerate(ASSIGNMENTS.items(), 1):
    print(i, k, v)

print(functions.RTN())

conflict_index = eligible_emps.ELIG_EMPS.index(emp)
last_index = len(eligible_emps.ELIG_EMPS) - 1
if conflict_index == last_index:
    j = 0

print('shifts to fill')

range_start = len(ASSIGNMENTS)
range_stop = len(create_shifts.SHIFTS)
REMAINING_SHIFTS = create_shifts.SHIFTS[range_start:range_stop]

for i, shift in enumerate(REMAINING_SHIFTS, 1):
    print(i, shift)

print(functions.RTN())

print('remaining shifts')
for i, (shift, email) in enumerate(zip(REMAINING_SHIFTS,
                                       cycle(eligible_emps.ELIG_EMPS)), 1):
    UPDATED_ASSIGNMENTS[shift] = email
    print(i, shift, email)

print(functions.RTN())

# concatenate dictionaries
d4 = {}
d4.update(ASSIGNMENTS)
d4.update(UPDATED_ASSIGNMENTS)

print('assignments with conflicts resolved')
for i, (k, v) in enumerate(d4.items(), 1):
    print(i, k, v)

print(functions.RTN())

if CONFLICTS:
    if len(CONFLICTS) > 1:
        print('conflicts')
        for i, (k, v) in enumerate(CONFLICTS.items(), 1):
            print(i, k, v)
    else:
        print('one conflict')
        for k, v in CONFLICTS.items():
            print(k, v)
else:
    print('no conflicts')

print(functions.RTN())
