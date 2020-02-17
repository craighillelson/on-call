""" __doc__ """

import csv
from collections import namedtuple
import calendar
import datetime
from dateutil.relativedelta import relativedelta
from dateutil.rrule import MO

RTN = lambda: '\n'

def calc_dates(a, b, c):
    """ calculate dates """
    a = b + datetime.timedelta(days=-b.weekday(), weeks=c)
    return a


def find_day(a):
    """ determine if the start """
    usr_start_day = datetime.datetime.strptime(a, '%Y-%m-%d').weekday()
    return (calendar.day_name[usr_start_day])


def append_shifts(a, b):
    """ add dates of the next 13 mondays to the shifts list """
    for i in range(0, 14, 1):
        monday = a + datetime.timedelta(days=-a.weekday(), weeks=i)
        b.append(monday)


def find_closest_start_mon(a, b):
    """ based on input from user, find monday before pto start date """
    if a.weekday() == 0:
        b = a
    else:
        b = a + relativedelta(weekday=MO(1))

    return b


def find_closest_end_mon(a, b):
    """ based on input from user, find monday after pto end date  """
    if a.weekday() == 0:
        b = a + relativedelta(weekday=MO(+2))
    else:
        b = a + relativedelta(weekday=MO(+1))

    return b


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
            # a[row.shift] = row.email


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


def output_enum_dct(a):
    """ """
    for i, (shift, email) in enumerate(a.items(), 1):
        print(i, shift, email)


def output_enum_lst(a, b):
    """ """
    for i, a in enumerate(b, 1):
        print(i, a)


def output_unavails(a, b, c, d):
    """ output shifts for which an employee is unavailable """
    print(a)
    for shift in b:
        # k_fmt = fmt_date('k_fmt', k)
        d[shift] = [c]
        # print(shift, c)


def prompt_user_for_pto_start_end(a, b):
    """ """
    print(a)
    b = input()
    return b


def reset_next_emp(a, b):
    """ """
    if a == len(b):
        a = 0
    else:
        pass

    return a
    # else:
    #     pass


def switch_case(a, b):
    """ switch case statement """
    b
    return b.get(a, "nothing")


def write_dct_to_csv(a, b, c, d):
    """ write dictionary to a csv """
    import csv

    HEADERS = a

    with open(b, 'w') as out_file:
        out_csv = csv.writer(out_file)
        out_csv.writerow(HEADERS)
        for c in d.items():
            keys_values = (c)
            out_csv.writerow(keys_values)
