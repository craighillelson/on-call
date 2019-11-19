""" __doc__ """

RTN = lambda: "\n"

def switch_case(USER_INPUT):
    """ switch case statement """
    switcher = {
        'a': 'view', # view.py
        'b': 'build', # build.py
        'c': 'update', # update.py
        'd': 'view employees', # employees.py
        'e': 'update employees', # update_employees.py
        }
    return switcher.get(USER_INPUT, "nothing")


print(RTN())

print('Please select an option below')

print('a - view the schedule')
print('b - build a schedule')
print('c - update a schedule')
print('d - view employees')
print('e - update employees')

print(RTN())

USER_INPUT = input("What would you like to do? ")

print(RTN())

print(f"You selected {switch_case(USER_INPUT)}")

print(RTN())
