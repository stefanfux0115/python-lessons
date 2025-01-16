import pandas as pd

vegetables = pd.read_csv('output/vegetables.csv')

print(vegetables)

# write vegetables to a new json file called vegetables.json
vegetables.to_json('output/vegetables.json')