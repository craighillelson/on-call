import csv

lines = list()
mem = input('Please enter a member\'s name to be deleted. \n')

with open('employees.csv', 'r') as readFile:
    reader = csv.reader(readFile)
    for row in reader:
        lines.append(row)
        for field in row:
            if field == mem:
                lines.remove(row)

with open('employees.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(lines)

print(f'{mem} deleted successfully')
