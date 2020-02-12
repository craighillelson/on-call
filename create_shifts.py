""" __doc__ """

import datetime
import functions
from datetime import date

SHIFTS = []

today = date.today()
this_monday = today + datetime.timedelta(days=-today.weekday(), weeks=1)

print(f'Would you like the on-call schedule to start on {this_monday} (y/n)? ')

answers = [
    'y',
    'n'
]

while True:
    usr_choice = input()
    if usr_choice not in answers:
        print(f'Would you like the on-call schedule to start on {this_monday} '
              f'(y/n)? ')
    else:
        break

if usr_choice == 'y':
    sched_start = this_monday
    print(f'schedule will start on {sched_start}')
else:
    print('please specify a start date for the schedule (YYYY-MM-DD)')
    usr_spec_date = input()
    usr_spec_start = usr_spec_date
    sched_start = functions.fmt_date('sched_start', usr_spec_start)

print(functions.RTN())

for i in range(0, 13, 1):
    shift = sched_start + datetime.timedelta(days=-sched_start.weekday(),
                                              weeks=i)
    SHIFTS.append(shift)
    i += 1
