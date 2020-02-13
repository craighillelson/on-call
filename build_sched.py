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
CONFLICTS = {}
ELIG_EMPS = []
EMPS_RES =[]
UNFILTERED_ASSIGNMENTS = {}

today = date.today()

print('unfiltered assignments')
for i, (shift, email) in enumerate(zip(create_shifts.SHIFTS,
                                       cycle(eligible_emps.ELIG_EMPS)), 1):
    UNFILTERED_ASSIGNMENTS[shift] = email
    print(i, shift, email)

print(functions.RTN())

# find conflicts
for (k, v), (k2, v2) in zip(UNFILTERED_ASSIGNMENTS.items(), pto.PTO.items()):
    if v != v2:
        AVAILS[k] = v
    else:
        CONFLICTS[k] = v

# resolve conflicts
if CONFLICTS:
    AVAILABLE_EMPS = eligible_emps.ELIG_EMPS
    if len(CONFLICTS) > 1:
        print('multiple conflicts')
        for i, (k, v) in enumerate(CONFLICTS.items(), 1):
            print(f'{i} {k} {v}')
            conflict_index = AVAILABLE_EMPS.index(v)
        del AVAILABLE_EMPS[conflict_index]
        print(functions.RTN())
        if AVAILABLE_EMPS:
            if len(AVAILABLE_EMPS) > 1:
                print('options')
                for i, emp in enumerate(AVAILABLE_EMPS, 1):
                    print(i, emp)
                print(functions.RTN())
            else:
                print('option')
                for emp in AVAILABLE_EMPS:
                    print(emp)
                print(functions.RTN())
        else:
            print(f'there are no employees available to cover the shift '
                  f'starting on {k}')
    else:
        print('one conflict')
        for k, v in CONFLICTS.items():
            print(k, v)
            next_week = k + datetime.timedelta(days=-today.weekday(), weeks=1)
            conflict_index = AVAILABLE_EMPS.index(v)
        del AVAILABLE_EMPS[conflict_index]
        print(functions.RTN())
        if AVAILABLE_EMPS:
            if len(AVAILABLE_EMPS) > 1:
                print('all options')
                for i, emp in enumerate(AVAILABLE_EMPS, 1):
                    print(i, emp)
                print(functions.RTN())
                # find next shift assignment
                print('next shift assignment')
                next_shift_assign = k + datetime.timedelta(days=-k.weekday(),
                                                    weeks=1)
                emp = UNFILTERED_ASSIGNMENTS[next_shift_assign]
                print(emp)
                conflict_index = AVAILABLE_EMPS.index(emp)
                del AVAILABLE_EMPS[conflict_index]
                print(functions.RTN())
                if AVAILABLE_EMPS:
                    if len(AVAILABLE_EMPS) > 1:
                        print('updated options')
                        for emp in AVAILABLE_EMPS:
                            print(emp)
                        print(functions.RTN())
                    else:
                        print('updated option')
                        for emp in AVAILABLE_EMPS:
                            print(emp)
                        print(functions.RTN())
                else:
                    print(f'there are no employees available to cover the '
                          f'shift starting on {k}')
            else:
                print('option')
                for emp in AVAILABLE_EMPS:
                    print(emp)
                print(functions.RTN())
        else:
            print(f'there are no employees available to cover the shift '
                  f'starting on {k}')
else:
    print('no conflicts')
    print(functions.RTN())
