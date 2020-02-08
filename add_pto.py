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

print('employees')
for num, email in EMP_DCT.items():
    print(num, email)

print(f'Please select an employee. ')

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
    PTO[email] = [unavail, avail]

print(functions.RTN())

print('pto to schedule')
for email, pto in PTO.items():
    start = pto[0]
    end = pto[1]
    print(email, start, end)

print(functions.RTN())

functions.output_pto_sched(PTO_SCHED)

print(functions.RTN())

today = date.today()
