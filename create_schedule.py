""" __doc__ """

import shifts
import employees
from itertools import cycle

RTN = lambda: "\n"

EMPLOYEES_CYCLED = []
i = 1

for num, employee in enumerate(cycle(employees.employees_dct)):
    if i >= shifts.num_weeks:
        break
    EMPLOYEES_CYCLED.append(employee)
    i += 1

ASSIGNMENTS = dict(zip(shifts.SHIFTS, EMPLOYEES_CYCLED))

print('shift (mon - sun), holiday week, employee')
for shift, emp in ASSIGNMENTS.items():
    print(f'{shift} - {emp}')

print(RTN())

# resolution logic
# while True:
    # if i > 0:
        # break
    # for k, v in dct.items():
        # if k == 'Gene':
            # continue
        # else:
            # print(k, v)
    # for k, v in dct.items():
        # print(k, v)
    # i += 1
