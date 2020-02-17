""" __doc__ """

import csv
import datetime
import functions
from datetime import date

SHIFTS = []

today = date.today()
day = today + datetime.timedelta(days=-today.weekday(), weeks=1)

print(f'Would you like the on-call schedule to start on {day} (y/n)? ')

answers = [
    'y',
    'n'
]

while True:
    usr_choice = input()
    if usr_choice not in answers:
        print(f'Would you like the on-call schedule to start on {day} '
              f'(y/n)? ')
    else:
        break

if usr_choice == 'y':
    sched_start = day
    print(functions.RTN())
    print(f'schedule will start on {sched_start}')
else:
    while True:
        print('please specify a start date for the schedule (YYYY-MM-DD)')
        usr_spec_date = input()
        usr_spec_start = usr_spec_date
        sched_start = functions.fmt_date('sched_start', usr_spec_start)
        if today >= sched_start:
            print('please specify a date in the future')
        else:
            sched_start_day = functions.find_day(str(sched_start))
            if sched_start_day == 'Monday':
                print(sched_start_day)
            else:
                next_mon = sched_start + \
                           datetime.timedelta(days=-sched_start.weekday(),
                                              weeks=1)
                print(functions.RTN())
                print(f'start date: {next_mon}')
            break

print(functions.RTN())

for i in range(0, 13, 1):
    shift = sched_start + datetime.timedelta(days=-sched_start.weekday(),
                                              weeks=i)
    SHIFTS.append(shift)
    i += 1

HEADER = 'shift'

with open('shifts.csv', 'w') as out_file:
    out_csv = csv.writer(out_file)
    out_csv.writerow([HEADER])
    for shift in SHIFTS:
        shift_fmt = shift.strftime('%Y-%m-%d')
        out_csv.writerow([shift_fmt])
