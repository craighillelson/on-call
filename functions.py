def print_employee_holiday_week(a, b, c, d):
    if a < date < b or c < date < d:
        print(f"{date.strftime('%Y-%m-%d')}, employee_assigned, - holiday week")
    else:
        print(f"{date.strftime('%Y-%m-%d')}, employee_assigned")

def format_dates(x):
    x = str(year) + '-' + x
    x = imports.datetime.strptime(x, '%Y-%m-%d')
    return x
