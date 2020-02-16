""" __doc__ """

def open_file(a):
    """ based on user choice, open file """
    exec(open(a).read())


# prompt user to select one of the options provided
while True:
    print('please make a selection\n')
    print('a - add employees')
    print('b - build schedule')
    print('c - edit schedule')
    print('d - list employees')
    print('e - list pto')
    print('f - remove employee')
    # print('f - review schedule')
    print('g - quit')
    user_choice = input()
    if user_choice == 'a':
        open_file('add_employees.py')
    elif user_choice == 'b':
        open_file('build_sched.py')
    elif user_choice == 'c':
        open_file('edit_sched.py')
    elif user_choice == 'd':
        open_file('list_employees.py')
    elif user_choice == 'e':
        open_file('list_pto.py')
    elif user_choice == 'f':
        open_file('remove_employee.py')
    # elif user_choice == 'f':
    #     cat assignments.csv
    #     open_file('2020-02-12_assignments.csv')
    else:
        break
