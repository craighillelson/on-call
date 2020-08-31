"""Remove employee and write the remaining employees to 'emps.csv'."""

import csv
from collections import namedtuple
import emps
from functions import (csv_write,
                       switch_case,
                       update_user)

nums = []
EMP_DCT = {}
SCHED = {}

for i, email in enumerate(emps.EMPLOYEES, 1):
    nums.append(i)
    EMP_DCT[i] = email

print("\nPlease select an employee to remove.")
for num, email in EMP_DCT.items():
    print(num, email)

while True:
    usr_choice = int(input("> "))
    emp_to_del = switch_case(EMP_DCT, usr_choice)
    if usr_choice not in nums:
        print("Not an option. Please select one of the options above.")
    else:
        break

print(f"\nYou selected {emp_to_del}")

del emps.EMPLOYEES_DCT[emp_to_del]

print("\nupdated list of employees")
for email, start_date in emps.EMPLOYEES_DCT.items():
    print(email, start_date)

csv_write(["email", "start_date"], "emps.csv", "k, v", emps.EMPLOYEES_DCT)

print('\n"emps.csv" exported successfully\n')
print(f"\n{emp_to_del} was scheduled for the following shift\n")

with open("assignments.csv") as csv_file:
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        SCHED[row.shift] = row.email

for shift, email in SCHED.items():
    if emp_to_del in email:
        print(shift, email)

update_user("it is suggested that you edit or rebuild the schedule")
