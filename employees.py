""" __doc__ """

import csv
from collections import namedtuple
from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.rrule import MO

employees_lst = []

with open('employees.csv') as csv_file:
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        date_strptime = datetime.strptime(row.start_date, '%Y-%m-%d')
        first_eligible_shift = date_strptime + relativedelta(weekday=MO(+12))
        first_eligible_shift_form = first_eligible_shift.date()
        emp_first_eligible = row.employee, first_eligible_shift_form
        employees_lst.append(emp_first_eligible)
