""" __doc__ """

# remove employee
import employees
import functions

EMP_DCT = {}
nums = []

for i, email in enumerate(employees.EMPLOYEES, 1):
    nums.append(i)
    EMP_DCT[i] = email

print(functions.RTN())

# prompt user to select an employee to remove
print(f'Please select an employee to remove.')
for num, email in EMP_DCT.items():
    print(num, email)

while True:
    user_choice = int(input())
    email = functions.switch_case(user_choice, EMP_DCT)
    if user_choice not in nums:
        print('Not an option. Please select one of the options above. ')
    else:
        print(functions.RTN())
        break

print(f'You selected {email}')

print(functions.RTN())
del employees.EMPLOYEES_DCT[email]

print('updated list of employees')
for k, v in employees.EMPLOYEES_DCT.items():
    print(k, v)

print(functions.RTN())

functions.write_dct_to_csv(['email','start_date'], 'employees.csv', 'k, v',
                           employees.EMPLOYEES_DCT)

# update user
print('"employees.csv" exported successfully')
