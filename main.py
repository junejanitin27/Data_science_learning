# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import json
import requests

drink_table = ["Cosmopolitan", "Kamikaze", "Royal Gin Fizz", "Death in the Afternoon", "shots", "Rusty Nail", "Manhattan", "Rum Toddy", "Frisco Sour"]

for x in drink_table:
    r = requests.get('http://www.thecocktaildb.com/api/json/v1/1/search.php?s='+x)
    #parsed = json.loads(r.text)
    drink_dict = json.loads(r.text)
    #print(drink_dict)
    print(drink_dict["drinks"][0]['idDrink'] + ' - ' + drink_dict["drinks"][0]['strDrink'])


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
