"""List employees."""

from emps import EMPLOYEES

print("\nemployees")
if EMPLOYEES:
    for i, email in enumerate(EMPLOYEES, 1):
        print(i, email)
else:
    print('"employees.csv" is empty')
