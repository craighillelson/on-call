"""Create on-call shifts. Write the results to a csv."""

import csv
import datetime
from datetime import date
import pyinputplus as pyip
import functions

today = date.today()
day = today + datetime.timedelta(days=-today.weekday(), weeks=1)

user_choice = pyip.inputYesNo(f'\nWould you like the on-call schedule to start '
                              f'on {day} (yes/no)?\n> ')

if user_choice == 'yes':
    sched_start = day
    print(f'\nschedule will start on {sched_start}')
else:
    while True:
        print('please specify a start date for the schedule (YYYY-MM-DD)')
        usr_spec_start = input('> ')
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
                print(f'\nstart date: {next_mon}')
            break

SHIFTS = []

for i in range(0, 13, 1):
    shift = sched_start + datetime.timedelta(days=-sched_start.weekday(),
                                             weeks=i)
    SHIFTS.append(shift)
    i += 1

with open('shifts.csv', 'w') as out_file:
    out_csv = csv.writer(out_file)
    out_csv.writerow(['shift'])
    for shift in SHIFTS:
        shift_fmt = shift.strftime('%Y-%m-%d')
        out_csv.writerow([shift_fmt])
