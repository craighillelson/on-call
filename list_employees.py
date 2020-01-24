""" __doc__ """

import employees
import functions
from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.rrule import MO

RTN = lambda: '\n'

print(functions.RTN())

print('name, first eligible shift')
for emp, start_date in employees.EMPLOYEES_DCT.items():
    date = datetime.strptime(start_date, '%Y-%m-%d')
    first_eligible = date.date() + relativedelta(weekday=MO(+12))
    print(f'{emp}, {first_eligible}')

print(functions.RTN())
