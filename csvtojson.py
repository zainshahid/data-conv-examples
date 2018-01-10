import csv

with open('veggies.csv') as f:
	reader = csv.DictReader (f)
	rows = list(reader)


import json

with open('veggies.json', 'w') as k:
	json.dump(rows,k, indent=2)

