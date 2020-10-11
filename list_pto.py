"""List PTO."""

import functions

PTO_SCHED = {}
EMP_DCT = {}
functions.open_csv(PTO_SCHED)

print(functions.RTN())

print('scheduled pto')
functions.output_pto_sched(PTO_SCHED)

print(functions.RTN())
