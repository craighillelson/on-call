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
YEAR = today.year

if todays_date.quarter == 4:
    next_qtr = 1
    the_qtr_after = next_qtr + 1
    YEAR = today.year + 1
elif todays_date.quarter == 3:
    the_qtr_after = 1
else:
    next_qtr = todays_date.quarter + 1
    the_qtr_after = todays_date.quarter + 2

while True:
    try:
        starting_qtr = input(f'Would you like to make a schedule for\n'
                             f'a. Q{next_qtr}/{YEAR} or\n'
                             f'b. Q{the_qtr_after}/{YEAR}\n')
        if starting_qtr not in answers:
            print('Please enter \'a\' or \'b\'')
        else:
            break
    except ValueError:
        print('invalid input')

print(RTN())

if starting_qtr == 'a':
    print(f'You selected Q{next_qtr}/{YEAR}')
    starting_qtr = next_qtr
else:
    print(f'You selected Q{the_qtr_after}/{YEAR}')
    starting_qtr = the_qtr_after
