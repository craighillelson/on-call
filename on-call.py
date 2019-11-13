""" __doc__ """

import csv
import imports
import employees

def print_employee_holiday_week(a, b, c, d):
    if a < date < b or c < date < d:
        print(f"{date.strftime('%Y-%m-%d')} - {employee_assigned}"
        " - holiday week")
    else:
        print(f"{date.strftime('%Y-%m-%d')} - {employee_assigned}")


def format_dates(x):
    x = str(year) + '-' + x
    x = imports.datetime.strptime(x, '%Y-%m-%d')
    return x


def write_to_csv(name_of_file, dct):
    """ write dictionary to csv """
    HEADERS = 'date', 'employee'
    with open(name_of_file, "w") as out_file:
        out_csv = csv.writer(out_file)
        out_csv.writerow(HEADERS)
        for date, employee in dct.items():
            keys_values = (date, employee)
            out_csv.writerow(keys_values)


D = imports.datetime.now()
year = D.year

tgiving_wk_start = '11-22'
tgiving_wk_end = '11-29'
xmas_wk_start = '12-18'
xmas_wk_end = '12-26'

tgiving_wk_start = format_dates(tgiving_wk_start)
tgiving_wk_end = format_dates(tgiving_wk_end)
xmas_wk_start = format_dates(xmas_wk_start)
xmas_wk_end = format_dates(xmas_wk_end)

MONDAYS = []
EMPLOYEE_ASSIGNMENTS = []

number_of_weeks = input("How many weeks in the future would you like to make \
the schedule for? ")
number_of_weeks = int(number_of_weeks) + 1

for i in range(1, number_of_weeks, 1):
    MONDAYS.append(D + imports.relativedelta(weekday=imports.MO(+i)))
    d5 = D + imports.relativedelta(weekday=imports.MO(+i))

for n, employee in enumerate(imports.cycle(employees.EMPLOYEES)):
    EMPLOYEE_ASSIGNMENTS.append(employee)
    if n >= number_of_weeks:
        break

ASSIGNMENTS = dict(zip(MONDAYS, EMPLOYEE_ASSIGNMENTS))

for date, employee_assigned in sorted(ASSIGNMENTS.items()):
    print_employee_holiday_week(tgiving_wk_start, tgiving_wk_end, \
    xmas_wk_start, xmas_wk_end)

write_to_csv('on-call.csv', ASSIGNMENTS)
