""" __doc__ """

def num_to_month_day(argument):
    """ switch case statement """
    switcher = {
        '1': ['01-01', '03-31',],
        '2': ['04-01', '06-30',],
        '3': ['07-01', '09-30',],
        '4': ['10-01', '12-31',],
    }
    return switcher.get(argument, 'nothing')


RTN = lambda: '\n'

print(RTN())

# prompt user for start date
# validate user input
# START_DATE = input('Would you like to create a schedule that \n'
                    # 'a. starts on the next Monday or \n'
                    # 'b. specify a starting date (YYYY-MM-DD)?\n')

print('By defualt, schedules created to start on the next Monday and '
      'run for twelve weeks.\nEmployees are eligible for inclusion in the '
      'on-call schedule twelve weeks after their start date.')

NUM = 12
# schedules should be made for an entire quarter at a time

# qtr = input('What quarter would you like the schedule to start? '
            # '(enter a number between 1 and 4\n')
# year = input('In what year (enter in YYYY format)\n')

# month_day = num_to_month_day(qtr)
# start = month_day[0]
# end = month_day[1]
# qtr_start = year + '-' + start
# qtr_end = year + '-' + end
# print(f'Quarter {qtr} - {qtr_start} - {qtr_end}')
