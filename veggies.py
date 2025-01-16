vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]


import csv

with open('output/vegetables.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'color', 'length_of_name'])
    for veggie in vegetables:
        name = veggie['name']
        color = veggie['color']
        length_of_name = len(name)
        writer.writerow([name, color, length_of_name])