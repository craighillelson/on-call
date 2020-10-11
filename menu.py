"""Provide a list of options to the user."""

import pyinputplus as pyip
from functions import switch_case

options = {
    1: "add_emps.py",
    2: "build_sched.py",
    3: "list_emps.py",
    4: "list_pto.py",
    5: "list_shifts_by_emp.py",
    6: "rem_emps.py",
}

while True:
    print("\nMake a selection or press enter to quit")
    for num, option in options.items():
        print(num, option)
    usr_choice = pyip.inputInt("> ", min=1, max=len(options), blank=True)
    if usr_choice != '':
        exec(open(switch_case(options, usr_choice)).read())
    else:
        print("\nSession complete.\n")
        break
