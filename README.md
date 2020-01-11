Python 3.8 script to loop through a list of employees and assign them on call shifts

# Requirements
* https://pypi.org/project/python-dateutil/
* https://pandas.pydata.org

# Instructions
1. Save all files to a directory
1. Upload a csv of employees with the following headers: employee,start_date or use the "add_employee.py" script to add employees one at a time
1. In Terminal, type "python3.8 create_schedule.py"

# Files
* add_employee.py - add employee or employees
* add_pto.py - add pto for a given employee to pto.csv
* assignments.csv - stores csv of shifts and assigned employees
* create_schedule.py - imports "employees.csv" and assembles a schedule, matching shifts to employees, and writes the list of shifts to a "shifts.csv"
* employees.csv - stores employee names and start dates
* employees.py - imports contents of "employees.csv" and populates lists and dictionaries
* functions.py - stores functions called by other files
* list_employees.py - lists employees and the first shift for which each is available
* list_pto.py - prints contents of "pto.csv"
* list_shifts_by_emp.py - lists shifts assigned by employee
* prompt_user.py - prompts user to select next quarter or the quarter following as the starting quarter
* pto.csv - stores pto data
* pto.py - populates PTO dictionary with data from "pto.csv"
* remove_employee.py - lists employees and gives user the option to remove an employee
