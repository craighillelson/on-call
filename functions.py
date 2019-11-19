""" __doc__ """

import csv

def print_employee_holiday_week(a, b, c, d):
    if a < date < b or c < date < d:
        print(f"{date.strftime('%Y-%m-%d')}, employee_assigned, - holiday week")
    else:
        print(f"{date.strftime('%Y-%m-%d')}, employee_assigned")


def format_dates(x):
    x = str(year) + '-' + x
    x = imports.datetime.strptime(x, '%Y-%m-%d')
    return x


def write_to_csv(name_of_file, dct):
    """ write dictionary to csv """
    csv_headers = 'date', 'employee'
    with open(name_of_file, 'w') as out_file:
        out_csv = csv.writer(out_file)
        out_csv.writerow(csv_headers)
        for date, employee in dct.items():
            keys_values = (date.strftime('%Y-%m-%d'), employee)
            out_csv.writerow(keys_values)
