import csv

with open('fruitcost.csv') as f:
	reader = csv.DictReader(f, delimeter ='\t')
	rows = list(reader)

for row in rows:
    print(row)