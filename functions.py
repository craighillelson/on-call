"""Functions."""

import csv
from collections import namedtuple
import calendar
import datetime
# from dateutil.relativedelta import relativedelta
# from dateutil.rrule import MO

RTN = lambda: '\n'


def calc_dates(a, b):
    """Calculate dates."""
    return a + datetime.timedelta(days=-a.weekday(), weeks=b)


def csv_write(a, b, c, d):
    """Write dictionary to csv."""
    HEADERS = a
    with open(b, 'w') as out_file:
        out_csv = csv.writer(out_file)
        out_csv.writerow(HEADERS)
        for c in d.items():
            keys_values = (c)
            out_csv.writerow(keys_values)


def find_day(a):
    """ determine if the start """
    usr_start_day = datetime.datetime.strptime(a, '%Y-%m-%d').weekday()
    return calendar.day_name[usr_start_day]


def fmt_date(a, b):
    """Format date."""
    a = datetime.datetime.strptime(b, '%Y-%m-%d').date()
    return a


def open_csv(a):
    """Open csv and populate dictionary with its contents."""
    with open('pto.csv') as csv_file:
        F_CSV = csv.reader(csv_file)
        COLUMN_HEADINGS = next(F_CSV)
        CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
        for rows in F_CSV:
            row = CSV_ROW(*rows)
            a[row.shift] = [row.email]


def output_pto_sched(a):
    """Output current pto schedule."""
    for shift, email in a.items():
        for emp in email:
            if email == '':
                print(f"{shift} - no pto booked")
            else:
                print(f'{shift} - {emp}')
        else:
            pass


def prev_subs_shift_lst(a, b, c, d):
    """Find previous or subsequent shift."""
    a = b[c + d]
    return a


def prompt_user_for_pto_start_end(a, b):
    """Prompt user for pto start and end dates."""
    print(a)
    b = input()
    return b


def switch_case(a, b):
    """Switch case statement."""
    return a.get(b, 'nothing')


def update_user(a):
    """Update user regarding an action taken."""
    print(f'\n{a}')
