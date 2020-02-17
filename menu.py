""" __doc__ """

USER_OPTIONS = {
    'a': 'add_employees.py',
    'b': 'build_sched.py',
    'c': 'edit_sched.py',
    'd': 'list_employees.py',
    'e': 'list_pto.py',
    'f': 'remove_employee.py',
    'g': 'quit',
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
print('please select an option')
for k, v in USER_OPTIONS.items():
    print(k, v)

while True:
    usr_choice = input()
    if usr_choice in KEYS:
        open_file(switch_case(usr_choice))
        break
    else:
        break
