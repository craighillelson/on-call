Python 3.8 script to loop through a list of employees to assign them on call shifts that start on Mondays.

# Requirements
* https://pypi.org/project/python-dateutil/
* https://pandas.pydata.org

# Instructions
1. Save "on-call.py" to a directory containing a csv of employees with "employee" as the header.
1. Upload a csv of employees with the following headers: employee,start_date
1. start_date must be formatted as YYYY-MM-DD
1. In Terminal, type "python3 create_schedule.py"

# Files
* add_employee.py - add employee
* add_pto.py - add pto for a given employee to pto.csv
* list_employees.py - lists employees and the first shift that each is available for
* list_pto.py - parses pto.csv and determines next availability
* list_shifts.py - lists shifts assigned by employee
* eligible_employees.py - determines employees eligible to work on-call shifts by comparing the list of shifts with employees' first eligible shift
* prompt_user.py - prompts user to select next quarter or the quarter following as the starting quarter
* pto.csv - stores pto data
* remove_employee.py - lists employees and gives user the option to remove an employee
* shifts.csv - stores on-call shift schedule
* shifts.py - populates a list of dates of consecutive Mondays based on user's response in prompt_user.py
