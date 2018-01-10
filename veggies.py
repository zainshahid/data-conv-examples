vegetables = [
 {"name": "eggplant"},
 {"name": "tomato"},
 {"name": "corn"},
 {"name": "potato"},
 {"name": "kale"},
 {"name": "peas"},
 {"name": "carrots"}
]

print vegetables

import csv

with open('veggies.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['name', 'length'])
	for veg in vegetables:
		veg_name=veg['name']
		veg_len=len(veg_name)
		writer.writerow([veg_name, veg_len])