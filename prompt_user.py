""" __doc__ """

import pandas as pd
from datetime import date
from dateutil.rrule import MO
from dateutil.relativedelta import relativedelta

answers = [
    'a',
    'b',
]

RTN = lambda: '\n'

print(RTN())

print('By defualt, schedules are created to start on the first Monday of the '
      'next quarter and run for the entire quarter.\n\nEmployees are eligible '
      'for inclusion in the on-call schedule twelve weeks after their start '
      'date.')

print(RTN())

today = date.today()
todays_date = pd.Timestamp(today)
year = today.year

# mon_inc = today + relativedelta(weekday=MO(+2))
# week_from_monday = pd.Timestamp(mon_inc)

if todays_date.quarter == 4:
    next_qtr = 1
    the_qtr_after = next_qtr + 1
    year = today.year + 1
elif todays_date.quarter == 3:
    the_qtr_after = 1
else:
    next_qtr = todays_date.quarter + 1
    the_qtr_after = todays_date.quarter + 2

while True:
    try:
        starting_qtr = input(f'Would you like to make a schedule for\n'
                             f'a. Q{next_qtr}/{year} or\n'
                             f'b. Q{the_qtr_after}/{year}\n')
        if starting_qtr not in answers:
            print('Please enter \'a\' or \'b\'')
        else:
            break
    except ValueError:
        print('invalid input')

print(RTN())

if starting_qtr == 'a':
    print(f'You selected Q{next_qtr}/{year}')
else:
    print(f'You selected Q{the_qtr_after}/{year}')

# print(RTN())
