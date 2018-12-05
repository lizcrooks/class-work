import json

filename = 'favorite_numbers.json'

with open(filename) as file_object:
    favorite_number = json.load(file_object)
    print("I know your favorite number! It's " + favorite_number + "!")