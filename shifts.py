""" __doc__ """

import prompt_user
from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.rrule import MO, SU

RTN = lambda: "\n"

def format_date(a):
    """ formats date """
    return a.strftime('%Y-%m-%d')


def concat_shift(a):
    """ concatenate shift """
    shift = format_date(mon) +' - '+ format_date(sun) +' - '+a
    return shift


def append_shifts():
    """ append the SHIFTS list """
    SHIFTS.append(shift)


TODAY = datetime.now()
MONDAYS = []
SUNDAYS = []
SHIFTS = []
i = 1

num_weeks = int(prompt_user.num) + 1

# populate a list of mondays and a list of sundays
# make mondays tuples?
for i in range(1, num_weeks, 1):
    mon_inc = TODAY + relativedelta(weekday=MO(+i))
    sun_inc = TODAY + relativedelta(weekday=SU(+i+1))
    MONDAYS.append(mon_inc)
    SUNDAYS.append(sun_inc)
    i += 1

# assemble a list of shifts and designate the weeks in which thanksgiving or
# christmas fall
for mon, sun in zip(MONDAYS, SUNDAYS):
    month = mon.month
    day = mon.day
    mon_month_day = (month, day)
    TGIVING_WK_START = (11, 19)
    TGIVING_WK_END = (11, 25)
    XMAS_WK_START = (12, 18)
    XMAS_WK_END = (12, 26)
    if TGIVING_WK_START < mon_month_day <= TGIVING_WK_END or \
    XMAS_WK_START < mon_month_day < XMAS_WK_END:
        shift = concat_shift('yes')
        append_shifts()
    else:
        shift = concat_shift('no')
        append_shifts()
