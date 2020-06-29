"""Functions."""

import csv
from collections import namedtuple
import calendar
import datetime
from dateutil.relativedelta import relativedelta
from dateutil.rrule import MO

RTN = lambda: '\n'

def calc_dates(a, b, c):
    """Calculate dates."""
    a = b + datetime.timedelta(days=-b.weekday(), weeks=c)
    return a


def csv_write(a, b, c, d):
    """ write dictionary to csv """
    HEADERS = a
    with open(b, 'w') as out_file:
        out_csv = csv.writer(out_file)
        out_csv.writerow(HEADERS) # define HEADERS before running function
        for c in d.items(): # rename keys and values to make to make them meaningful
            keys_values = (c)
            out_csv.writerow(keys_values)


def find_day(a):
    """ determine if the start """
    usr_start_day = datetime.datetime.strptime(a, '%Y-%m-%d').weekday()
    return (calendar.day_name[usr_start_day])


def fmt_date(a, b):
    """ format date """
    a = datetime.datetime.strptime(b, '%Y-%m-%d').date()
    return a


def open_csv(a):
    """ open csv and populate dictionary with its contents """
    with open('pto.csv') as csv_file:
        F_CSV = csv.reader(csv_file)
        COLUMN_HEADINGS = next(F_CSV)
        CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
        for rows in F_CSV:
            row = CSV_ROW(*rows)
            a[row.shift] = [row.email]


def output_pto_sched(a):
    """ oututs current pto schedule """
    for shift, email in a.items():
        for emp in email:
            if email == '':
                print(f'{shift} - no pto booked')
            else:
                print(f'{shift} - {emp}')
        else:
            pass


def prev_subs_shift_lst(a, b, c, d):
    """ find previous or subsequent shift """
    a = b[c + d]
    return a


def prompt_user_for_pto_start_end(a, b):
    """ prompt user for pto start and end dates """
    print(a)
    b = input()
    return b


def switch_case(a, b):
    """ switch case statement """
    a
    return a.get(b, 'nothing')


def update_user(a):
    """ update user regarding an action taken """
    print(RTN())
    print(a)
    print(RTN())
