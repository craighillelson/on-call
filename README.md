Python 3.8 script to loop through a list of employees and assign them on call shifts

# Requirement
* https://pypi.org/project/python-dateutil/

# Instructions
1. Save all files to a directory
1. Upload a csv of employees with the following headers: employee,start_date or navigate to the directory containing the downloaded files and type "pyton3.8 add_employees.py" to add employees one at a time.
1. In Terminal, type "python3.8 create_schedule.py"

# Files
* add_emps.py - add one or more employees
* build_sched.py - imports "employees.csv" and assembles a schedule, matching shifts to employees, and writes the list of shifts to a csv including today's date in the file name
* create_shifts.py - creates thirteen (equivalent to one quarter) on call shifts
* emps.csv - stores employee names and start dates
* empls.py - imports contents of "employees.csv" and populates lists and dictionaries
* functions.py - stores functions called by other files
* list_pto.py - lists shifts and the employees for each shift who will be on pto
* list_emps.py - lists employees
* menu.py - presents user with a list of actions to take, calling
* pto.csv - stores pto data
* pto.py - populates PTO dictionary with data from "pto.csv"
* rem_emps.py - removes employee from "employees.csv," identifies shifts previously assigned to the deleted employee, and encourages the user to edit or rebuild the schedule
