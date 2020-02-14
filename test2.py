""" __doc__ """

import create_shifts
import datetime
import employees
import eligible_emps
import functions
import itertools
import pto
from datetime import date
from itertools import cycle

# data stores
AVAILS = {}
ASSIGNMENTS = {}
CONFLICTS = {}
ELIG_EMPS = []
EMPS_RES = []
INDEXES_CONFLICTS_RESOLVED = []
PTO_LST = []
INDEXES_CONFLICTS = {}
UNFILTERED_ASSIGNMENTS = {}
UPDATED_ASSIGNMENTS = {}

print('pto')
for i, (k, v) in enumerate(pto.PTO.items(), 1):
    PTO_LST.append(v)
    print(i, k, v)

print(functions.RTN())

print('assignments with conflicts identified')
for i, (shift, email, pto_email) in enumerate(zip(create_shifts.SHIFTS,
                                              cycle(eligible_emps.ELIG_EMPS),
                                              PTO_LST), 1):
    if email == pto_email:
        print(f'{i} {shift} {email} {pto_email} '
        f'index: {eligible_emps.ELIG_EMPS.index(email)} - conflict')
        INDEXES_CONFLICTS[i] = [eligible_emps.ELIG_EMPS.index(email), 'conflict']
    else:
        print(f'{i} {shift} {email} {pto_email} '
        f'index: {eligible_emps.ELIG_EMPS.index(email)} - no conflict')
        INDEXES_CONFLICTS[i] = [eligible_emps.ELIG_EMPS.index(email), 'no conflict']

print(functions.RTN())

print('conflict')
for k, v in INDEXES_CONFLICTS.items():
    if 'conflict' in v:
        if v[0] == eligible_emps.ELIG_EMPS[-1]:
            i = 0
            print(f'{k}: {v[1]} current index: {v[0]} new index: {i}')
            INDEXES_CONFLICTS_RESOLVED.append(i)
            break
        else:
            i = v[0]
            i += 1
            print(f'{k}: {v[1]} current index: {v[0]} new index: {i}')
            INDEXES_CONFLICTS_RESOLVED.append(i)
            break
    else:
        if v[0] == eligible_emps.ELIG_EMPS[-1]:
            i = 0
            print(f'{k}: {v[1]} current index: {v[0]}')
            INDEXES_CONFLICTS_RESOLVED.append(i)
        else:
            i = v[0]
            print(f'{k}: {v[1]} current index: {v[0]}')
            INDEXES_CONFLICTS_RESOLVED.append(i)

print(functions.RTN())

for ind in INDEXES_CONFLICTS_RESOLVED:
    print(ind)

print(functions.RTN())

print('number of indexes left')
diff = len(create_shifts.SHIFTS) - len(INDEXES_CONFLICTS_RESOLVED)
print(diff)

print(functions.RTN())

print('value of last element in INDEXES_CONFLICTS_RESOLVED')
num = INDEXES_CONFLICTS_RESOLVED[-1]
print(num)

print(functions.RTN())

print('print number of items in eligible_emps.ELIG_EMPS')
print(len(eligible_emps.ELIG_EMPS) - 1)

print(functions.RTN())

print('determine new indexes')
for i in range(INDEXES_CONFLICTS_RESOLVED[-1], diff, 1): # a - start, n - stop, s - step
    i += 1
    print(i)
