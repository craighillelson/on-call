""" __doc__ """

import pandas as pd

RTN = lambda: '\n'

employees = pd.read_csv('employees.csv', index_col ='employee')

print(RTN())
print(employees)
print(RTN())

employee_rm = input('Please enter a employee\'s name to be deleted. \n')

employees.drop([employee_rm], inplace=True)

print(RTN())
print(employees)
print(RTN())

employees_updated = pd.DataFrame(employees)
employees_updated.to_csv('employees.csv')

print(f'{employee_rm} deleted successfully')
