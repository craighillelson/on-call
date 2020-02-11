""" __doc__ """

def open_file(a):
    """ based on user choice, open file """
    exec(open(a).read())


# prompt user to select one of the options provided
while True:
    print('please make a selection')
    print('a - add employees')
    print('b - create schedule')
    print('c - list pto')
    print('d - remove employee')
    print('e - quit')
    user_choice = input()
    if user_choice == 'a':
        open_file('add_employees.py')
    elif user_choice == 'b':
        open_file('create_schedule.py')
    elif user_choice == 'c':
        open_file('list_pto.py')
    elif user_choice == 'd':
        open_file('remove_employee.py')
    else:
        break
