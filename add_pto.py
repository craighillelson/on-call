"""Add PTO to 'pto.csv'."""

import csv
from collections import namedtuple
import datetime
import employees
import functions

BOOKED_PTO = {}
EMP_DCT = {}
PTO = {}
NUMS = []

for i, email in enumerate(employees.EMPLOYEES, 1):
    NUMS.append(i)
    EMP_DCT[i] = email

# prompt user to enter start employee's pto start and end dates
print("\nPlease select an employee.")
for num, email in EMP_DCT.items():
    print(num, email)

while True:
    user_choice = int(input())
    print(functions.RTN())
    email = functions.switch_case(user_choice, EMP_DCT)
    print(email)
    pto_start = functions.prompt_user_for_pto_start_end("pto start date",
                                                        "pto_start")
    pto_end = functions.prompt_user_for_pto_start_end("pto end date", "pto_end")
    print(functions.RTN())
    PTO[email] = [pto_start,pto_end]
    if user_choice not in NUMS:
        print("not an option")
    else:
        break

for email, pto in PTO.items():
    pto_start = pto[0]
    pto_end = pto[1]

print(f"{email} will be taking pto from {pto_start} to {pto_end}")

# print(functions.RTN())

print("\nbooked pto")
with open("pto.csv") as csv_file:
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        shift_fmt = functions.fmt_date('shift_fmt', row.shift)
        BOOKED_PTO[shift_fmt] = row.email
        print(shift_fmt, row.email)

print(functions.RTN())

pto_start_fmt = functions.fmt_date("pto_start_fmt", pto_start)
BOOKED_PTO[pto_start_fmt] = email

print('updated pto')
with open('pto.csv', 'w') as out_file:
    out_csv = csv.writer(out_file)
    out_csv.writerow(["shift","email"])
    for shift, email in sorted(BOOKED_PTO.items()):
        keys_values = (shift, email)
        out_csv.writerow(keys_values)
        print(shift, email)

# update user
print('\n"pto.csv" exported successfully\n')
