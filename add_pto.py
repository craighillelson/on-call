""" __doc__ """

import csv
import list_pto
from datetime import datetime

def format_date(a, b, c):
    a = datetime.strptime(b, '%Y-%m-%d')
    c = a.date()
    return c


RTN = lambda: '\n'

NEW_PTO = {}

emp = input('Employee name: \n')

add_start_date = input('Enter start date: \n')
start_date = format_date('start_strptime', add_start_date, 'start_formatted')

add_end_date = input('Enter end date: \n')
end_date = format_date('end_strptime', add_end_date, 'end_formatted')

NEW_PTO[emp] = start_date, end_date

list_pto.PTO.update(NEW_PTO)

HEADERS = 'employee', 'start_date', 'end_date'

with open('pto.csv', 'w') as out_file:
    out_csv = csv.writer(out_file)
    out_csv.writerow(HEADERS)
    for emp, (start_date, end_date) in list_pto.PTO.items():
        keys_values = (emp, start_date, end_date)
        out_csv.writerow(keys_values)

print('PTO added')
print(f'Employee: {emp}')
print(f'PTO start: {start_date}')
print(f'PTO end: {end_date}')

print(RTN())
