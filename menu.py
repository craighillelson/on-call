"""Present user with options."""

import functions

USER_OPTIONS = {
    'a': 'add_emps.py',
    'b': 'build_sched.py',
    'c': 'edit_sched.py',
    'd': 'list_emps.py',
    'e': 'list_pto.py',
    'f': 'list_shifts_by_emp.py',
    'g': 'rem_emps.py',
}

KEYS = list(USER_OPTIONS.keys())

def switch_case(argument):
    """ switch case statement """
    USER_OPTIONS
    return USER_OPTIONS.get(argument, 'nothing')


def open_file(a):
    """ based on user choice, open file """
    exec(open(a).read())


# prompt user to select one of the options provided
print(functions.RTN())
print('please select an option or press return to quit')
for opt, action in USER_OPTIONS.items():
    print(f'{opt} - {action}')

while True:
    usr_choice = input()
    if usr_choice in KEYS:
        open_file(switch_case(usr_choice))
        break
    else:
        break
