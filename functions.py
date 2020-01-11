""" __doc__ """

def start_end_date_str(argument):
    """ switch case statement """
    switcher = {
        1: ['01-01', '03-31'],
        2: ['04-01', '06-30'],
        3: ['07-01', '09-30'],
        4: ['10-01', '12-31'],
        }
    return switcher.get(argument, 'nothing')


def cat_date(a_a, b_b):
    """ concatenates year with start and end dates for each quarter """
    date_ymd = a_a + '-' + b_b
    return date_ymd


def write_to_csv(a_a, b_b, c_c, d_d):
    import csv

    HEADERS = a_a

    with open(b_b, 'w') as out_file:
        OUT_CSV = csv.writer(out_file)
        OUT_CSV.writerow(HEADERS)
        for c_c in d_d:
            OUT_CSV.writerow([c_c])


def append_list(a_a, b_b):
    """ appends var to list """
    a_a.append(b_b)
