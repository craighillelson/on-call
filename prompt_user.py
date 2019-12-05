""" __doc__ """

RTN = lambda: '\n'
print(RTN())

# prompt user for start date
# validate user input
START_DATE = input('Would you like to create a schedule that \n'
                    'a. starts on the next Monday or \n'
                    'b. specify a starting date (YYYY-MM-DD)?\n')

NUM = input('How many weeks into the future would you like to make the '
                'schedule for? ')
