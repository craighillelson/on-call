""" __doc__ """

def open_file(a):
    """ based on user choice, open file """
    exec(open(a).read())


# prompt user to select one of the options provided
while True:
    print('please make a selection')
    print('a - add employees')
    print('b - build schedule')
    print('c - list employees')
    print('d - list pto')
    print('e - remove employee')
    print('f - quit')
    user_choice = input()
    if user_choice == 'a':
        open_file('add_employees.py')
    elif user_choice == 'b':
        open_file('build_sched.py')
    elif user_choice == 'c':
        open_file('list_employees.py')
    elif user_choice == 'd':
        open_file('list_pto.py')
    elif user_choice == 'e':
        open_file('remove_employee.py')
    else:
        break
