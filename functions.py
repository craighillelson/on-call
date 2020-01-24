""" __doc__ """

from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.rrule import MO

def start_end_date_str(a):
    """ switch case statement """
    switcher = {
        1: ['01-01', '03-31'],
        2: ['04-01', '06-30'],
        3: ['07-01', '09-30'],
        4: ['10-01', '12-31'],
        }
    return switcher.get(a, 'nothing')


def cat_date(a_a, b_b):
    """ concatenates year with start and end dates for each quarter """
    date_ymd = a_a + '-' + b_b
    return date_ymd


def write_list_to_csv(a_a, b_b, c_c, d_d):
    """ write to csv """
    import csv

    HEADERS = a_a

    with open(b_b, 'w') as out_file:
        OUT_CSV = csv.writer(out_file)
        OUT_CSV.writerow(HEADERS)
        for c_c in d_d:
            OUT_CSV.writerow([c_c])


def write_dct_to_csv(a, b, c, d, e):
    import csv

    HEADERS = a, b

    with open(c, 'w') as out_file:
        out_csv = csv.writer(out_file)
        out_csv.writerow(HEADERS)
        for d in e.items():
            keys_values = (d)
            out_csv.writerow(keys_values)


def append_list(a_a, b_b):
    """ appends var to list """
    a_a.append(b_b)


def format_date(a, b):
    """ formats dates """
    a = datetime.strptime(b, '%Y-%m-%d').date()
    return a


def output_start_dates(a, b):
    """ output start dates """
    print(f'pto starts: {a}')
    b = a
    print(f'unavailable starting {b}')


def output_rtn_dates(a, b, c):
    """ outputs end dates """
    print(f'pto ends - {a}')
    b = a + relativedelta(weekday=MO(+c))
    print(f'available starting - {b}')
