""" __doc__ """

import csv

RTN = lambda: "\n"

employees = {
    'Gene':'2019-04-01',
    'Paul':'2019-04-01',
    'Peter':'2019-04-01',
    'Ace':'2019-11-11',
}

add_emp = input("Enter the name of the employee to be added \n")
add_start_date = input("Enter the employee's start date \n")

print(RTN())

print('employee added')
print(f'key: {add_emp}')
print(f'value {add_start_date}')
employees[add_emp] = add_start_date

print(RTN())

print('current employees')
for emp, start_date in employees.items():
    print(emp, start_date)

HEADERS = 'employee', 'start_date'

with open('employees.csv', "w") as out_file:
    out_csv = csv.writer(out_file)
    out_csv.writerow(HEADERS)
    for emp, start_date in employees.items():
        keys_values = (emp, start_date)
        out_csv.writerow(keys_values)
