import json

# JSON file keys needed to update these key’s values later
number_key = 'numberInInventory'
date_key = 'lastUpdated'
date = '5/21/2167'

# ADD YOUR DICTIONARY CODE HERE (line 10)
monday_rocks = {'nickel': 4, 'olivine': 9, 'feldspar': 5, 'graphite-diamond': 3, 'iron': 19, 'serpentine': 12}

print(monday_rocks)

with open('C:/Users/junej/Downloads/practice.json', ) as json_file:
    data = json.load(json_file)
    # Loop through items to find the mineral key of each item
    # An "item" is each of the JSON files dictionaries

print(data)

for item in data['meteorites']:
    for key in item.keys():
        if item[key] == 'nickel':
            # Update the number of rocks in inventory
            item[number_key] = item[number_key] + monday_rocks['nickel']
            # Update the date
            item[date_key] = date
        if item[key] == 'olivine':
            # Update the number of rocks in inventory
            item[number_key] = item[number_key] + monday_rocks['olivine']
            # Update the date
            item[date_key] = date
        if item[key] == 'feldspar':
            # Update the number of rocks in inventory
            item[number_key] = item[number_key] + monday_rocks['feldspar']
            # Update the date
            item[date_key] = date
        if item[key] == 'graphite-diamond':
            # Update the number of rocks in inventory
            item[number_key] = item[number_key] + monday_rocks['graphite-diamond']
            # Update the date
            item[date_key] = date
        if item[key] == 'iron':
            # Update the number of rocks in inventory
            item[number_key] = item[number_key] + monday_rocks['iron']
            # Update the date
            item[date_key] = date
        if item[key] == 'serpentine':
            # Update the number of rocks in inventory
            item[number_key] = item[number_key] + monday_rocks['serpentine']
            # Update the date
            item[date_key] = date


json_obj = json.dumps(data, indent=4, sort_keys=True)

print(json_obj)
