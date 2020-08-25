"""Add employees to emps.csv."""

import functions
import emps

domain = input("What is your domain name?\n")

while True:
    print("Enter the employee's name (or enter nothing to stop.):")
    email_prefix = input()
    email = email_prefix + "@" + domain
    if email_prefix == '':
        break
    print("start date")
    start_date = input()
    emps.EMPLOYEES_DCT[email] = start_date

functions.csv_write(["email", "start_date"], "emps.csv",
                    "email, start_date", emps.EMPLOYEES_DCT)

print("updated list of employees")
print("email, start date")
for email, start_date in emps.EMPLOYEES_DCT.items():
    print(email, start_date)
