""" __doc__ """

import prompt_user
from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.rrule import MO

RTN = lambda: '\n'

def start_end_date_str(argument):
    """ switch case statement """
    switcher = {
        'a': ['01-01', '03-31'],
        'b': ['04-01', '06-30'],
        'c': ['07-01', '09-30'],
        'd': ['10-01', '12-31'],
        }
    return switcher.get(argument, 'nothing')


def cat_date(a):
    """ concatenates year with start and end dates for each quarter """
    date = year + '-' + a
    return date


def output_date(a, b, c):
    """ outputs first or last day of the quarter """
    print(f'{a} monday of the quarter: {b + relativedelta(weekday=MO(c))}')


qtr_start_end_dates = []
mondays = []
year = str(prompt_user.year)
qtr_start_end = start_end_date_str(prompt_user.starting_qtr)

print(RTN())

for qtr_date in qtr_start_end:
    date_str = cat_date(qtr_date)
    date_fmt = datetime.strptime(date_str, '%Y-%m-%d')
    date = date_fmt.date()
    qtr_start_end_dates.append(date)

qtr_start_date = qtr_start_end_dates[0]
qtr_end_date = qtr_start_end_dates[1]
output_date('first', qtr_start_date, +1)
output_date('last', qtr_end_date, -1)

# count weeks between first and last mondays of the quarter
date_delta = qtr_end_date - qtr_start_date
weeks_between = round(date_delta.days / 7)
print(f'number of weeks between dates: {weeks_between}')

print(RTN())

# make a list of all the mondays in the quarter
for i in range(1, weeks_between + 1, 1):
    mondays.append(qtr_start_date + relativedelta(weekday=MO(+i)))

# for monday in mondays:
#     print(monday)

# print(RTN())

# date = datetime.strptime('2019-09-27', '%Y-%m-%d') # '2019-09-27 is a placeholder'
# print(date.date())

# def format_date(a):
#     """ formats date """
#     return a.strftime('%Y-%m-%d')

# print(prompt_user.year)
# print(prompt_user.starting_qtr)

# print(prompt_user.starting_qtr)

# TODAY = date.today()
# MONDAYS = []
# MONDAYS_TUPLES = []
# SUNDAYS = []
# SHIFTS = []
# i = 1

# num_weeks = int(prompt_user.NUM) + 1

# populate a list of mondays and a list of sundays
# make mondays tuples?
# for i in range(1, 12, 1):
    # mon_inc = TODAY + relativedelta(weekday=MO(+i))
    # sun_inc = TODAY + relativedelta(weekday=SU(+i+1))
    # MONDAYS_TUPLES.append((mon_inc))
    # MONDAYS.append(mon_inc)
    # SUNDAYS.append(sun_inc)
    # i += 1

# assemble a list of shifts and designate the weeks in which thanksgiving or
# christmas fall
# for mon, sun in zip(MONDAYS, SUNDAYS):
    # shift = format_date(mon) +' - '+ format_date(sun)
    # SHIFTS.append(shift)
    # month = mon.month
    # day = mon.day
    # mon_month_day = (month, day)
    # TGIVING_WK_START = (11, 19)
    # TGIVING_WK_END = (11, 25)
    # XMAS_WK_START = (12, 18)
    # XMAS_WK_END = (12, 26)
    # if TGIVING_WK_START < mon_month_day <= TGIVING_WK_END or \
    # XMAS_WK_START < mon_month_day < XMAS_WK_END:
        # shift = concat_shift('yes')
        # append_shifts()
    # else:
        # shift = concat_shift('no')
        # append_shifts()

# for mon in MONDAYS_TUPLES:
    # print(mon)
