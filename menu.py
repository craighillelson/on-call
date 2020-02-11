""" __doc__ """

while True:
    print('please make a selection')
    print('a - add employees')
    print('b - create schedule')
    print('c - list pto')
    print('d - quit')
    user_choice = input()
    if user_choice == 'a':
        exec(open('add_employees.py').read())
    elif user_choice == 'b':
        exec(open('create_schedule.py').read())
    elif user_choice == 'c':
        exec(open('list_pto.py').read())
    else:
        break
