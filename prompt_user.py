""" __doc__ """

from datetime import date
from datetime import datetime

def qtr_to_month_day(argument):
    """ switch case statement """
    """ assigns user choice to a list of start and """
    """ end dates for each quarter """
    switcher = {
        1: ['01-01', '03-31',],
        2: ['04-01', '06-30',],
        3: ['07-01', '09-30',],
        4: ['10-01', '12-31',],
    }
    return switcher.get(argument, 'nothing')


def user_selected_year(argument):
    """ switch case statement """
    """ converts user choice into this year or next year """
    switcher = {
        'a': this_year,
        'b': next_year,
    }
    return switcher.get(argument, 'nothing')


RTN = lambda: '\n'

print(RTN())

today = date.today()
this_year = today.year
next_year = this_year + 1

print('By defualt, schedules created to start on the next Monday and '
      'run for twelve weeks.\n\nEmployees are eligible for inclusion in the '
      'on-call schedule twelve weeks after their start date.')

qtrs = [
    1,
    2,
    3,
    4,
]

years = [
    'a',
    'b',
]

while True:
    try:
        qtr = int(input('What quarter would you like the schedule to start? '
                        '(enter a number between 1 and 4)\n'))
        if qtr not in qtrs:
            print(f'please enter a number between 1 and 4')
        else:
            print(RTN())
            break
    except ValueError:
        print('Please enter an integer.')

while True:
    try:
        year = input('Would you like to make the on call schedule for\n'
                     'a. this year or next year\n'
                     'b. next year\n')
        if year not in years:
            print('Please select "a" or "b"')
        else:
            print(RTN())
            break
    except ValueError:
        print('invalid input')

qtr_start_end = qtr_to_month_day(qtr)
on_call_year = user_selected_year(year)
qtr_start = str(on_call_year) + '-' + qtr_start_end[0]
qtr_end = str(on_call_year) + '-' + qtr_start_end[1]

qtr_start_datetime = datetime.strptime(qtr_start, '%Y-%m-%d')
qtr_end_datetime = datetime.strptime(qtr_end, '%Y-%m-%d')

qtr_start_date = qtr_start_datetime.date()
qtr_end_date = qtr_end_datetime.date()
print('date range selected')
print(f'quarter start: {qtr_start_date}')
print(f'quarter end: {qtr_end_date}')
print(RTN())
