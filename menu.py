"""Provide a list of options to the user."""

import functions
import pyinputplus as pyip

options = {
    1: 'add_employees.py',
    2: 'list_employees.py',
    3: 'lunch_roulette.py',
    4: 'remove_employees.py',
}

def switch_case(argument):
    """Switch case statement."""
    options
    return options.get(argument, 'nothing')

while True:
    print('\nMake a selection or press enter to quit')
    for num, option in options.items():
        print(num, option)
    usr_choice = pyip.inputInt('> ', min=1, max=len(options), blank=True)
    if usr_choice != '':
        exec(open(switch_case(usr_choice)).read())
    else:
        print('\nSession complete.\n')
        break
