""" __doc__ """

def open_file(a):
    exec(open(a).read())


while True:
    print('please make a selection')
    print('a - add employees')
    print('b - create schedule')
    print('c - list pto')
    print('d - quit')
    user_choice = input()
    if user_choice == 'a':
        open_file('add_employees.py')
    elif user_choice == 'b':
        open_file('create_schedule.py')
    elif user_choice == 'c':
        open_file('list_pto.py')
    else:
        break
