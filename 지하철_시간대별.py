import csv
f=open('subwaytime.csv')
data = csv.reader(f)

next(data)
next(data)
for row in data:
    row[4:] = map(int, row[4:])
    print(row)