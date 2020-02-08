# imports
import csv
import datetime
import employees
import functions
from collections import namedtuple
from datetime import date

PTO = {}
PTO_SCHED = {}
EMP_DCT = {}
nums = []
functions.open_csv(PTO_SCHED)

print(functions.RTN())

for i, email in enumerate(employees.EMPLOYEES, 1):
    nums.append(i)
    EMP_DCT[i] = email

print(f'Please select an employee.')
for num, email in EMP_DCT.items():
    print(num, email)

while True:
    user_choice = int(input())
    print(functions.RTN())
    email = functions.switch_case(user_choice, EMP_DCT)
    print(email)
    print('start date')
    pto_start = input()
    print('end date')
    pto_end = input()
    print(functions.RTN())
    if user_choice not in nums:
        print('not an option ')
    else:
        break

PTO[email] = [pto_start,pto_end]
for email, pto in PTO.items():
    start = pto[0]
    start_fmt = functions.fmt_date('start_fmt', start)
    end = pto[1]
    end_fmt = functions.fmt_date('end_fmt', end)
    unavail = functions.find_closest_mon(start_fmt, -1, 'unavail')
    avail = functions.find_closest_mon(end_fmt, +1, 'avail')
    date_delta = avail - unavail
    weeks_between = round(date_delta.days / 7) + 1
    PTO[email] = [unavail, avail]

print('unavailable')
for i in range(0, weeks_between - 1, 1):
    print(unavail + datetime.timedelta(days=-unavail.weekday(), weeks=i), email)
    i += 1

print(functions.RTN())

functions.output_pto_sched(PTO_SCHED)

print(functions.RTN())

today = date.today()
