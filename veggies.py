vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

# put above into the csv file and add  length of the name of the vegtable as separate column

import csv

with open('veggies.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'color', 'length_of_name'])
    for veggie in vegetables:
        name = veggie['name']
        color = veggie['color']
        length_of_name = len(name)
        writer.writerow([name, color, length_of_name])