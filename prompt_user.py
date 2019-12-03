""" __doc__ """

RTN = lambda: '\n'
print(RTN())

# prompt user for start date
# validate user input
START_TODAY = input('Would you like to create a schedule that starts on the '
                    'next Monday? (Y/N) ')

if START_TODAY == 'Y':
    NUM = input('How many weeks into the future would you like to make the '
                'schedule for? ')
else:
    pass
