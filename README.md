Python 3.8 script to loop through a list of employees to assign them on call shifts that start on Mondays and run for a quarter.

# Requirements
* https://pypi.org/project/python-dateutil/
* https://pandas.pydata.org

# Instructions
1. Save all files to a directory
1. Upload a csv of employees with the following headers: employee,start_date or use the "add_employee.py" script to add employees one at a time
1. In Terminal, type "python3 create_schedule.py"

# Files
* add_employee.py - add employee or employees
* add_pto.py - add pto for a given employee to pto.csv
* assignments.csv - stores csv of shifts and assigned employees
* create_schedule.py - imports "employees.csv" and "shifts.txt" and assembles a schedule, matching shifts to employees
* employees.csv - stores employee names and start dates
* employees.py - imports contents of 'employees.csv' and populates lists and dictionaries
* list_employees.py - lists employees and the first shift for which each is available
* list_pto.py - parses pto.csv and determines next availability
* list_shifts_by_emp.py - lists shifts assigned by employee
* prompt_user.py - prompts user to select next quarter or the quarter following as the starting quarter
* pto.csv - stores pto data
* remove_employee.py - lists employees and gives user the option to remove an employee
* shifts.txt - stores shifts
