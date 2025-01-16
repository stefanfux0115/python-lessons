import json
import csv

# Load the JSON file
with open('output/superheroes.json', 'r') as f:
    data = json.load(f)

# Prepare the CSV file
csv_file = 'output/superheroes_flat.csv'

# Define the header
header = ['name', 'age', 'secretIdentity', 'powers', 'squadName', 'homeTown', 'formed', 'secretBase', 'active']

# Open the CSV file for writing
with open(csv_file, 'w', newline='') as f:
    writer = csv.writer(f)
    # Write the header
    writer.writerow(header)

    # Loop through members and write their information
    for member in data['members']:
        for power in member['powers']:
            writer.writerow([
                member['name'],          # name
                member['age'],           # age
                member['secretIdentity'],# secretIdentity
                power,                   # powers (one row per power)
                data['squadName'],       # squadName
                data['homeTown'],        # homeTown
                data['formed'],          # formed
                data['secretBase'],      # secretBase
                data['active']           # active
            ])

print(f"Data has been successfully written to {csv_file}")
