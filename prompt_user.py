RTN = lambda: "\n"
print(RTN())

# prompt user for start date
# validate user input
start_today = input('Would you like to create a schedule that starts on the '
'next Monday? (Y/N) ')

if start_today == 'Y':
    num = input('How many weeks into the future would you like to make the '
    'schedule for? ')
else:
    pass
