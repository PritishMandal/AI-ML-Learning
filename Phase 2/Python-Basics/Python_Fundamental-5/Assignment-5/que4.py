# LOGIC:
# 1. Create a dictionary
# 2. Save the dictionary into a JSON file
# 3. Read the JSON file
# 4. Print cities and populations
# 5. Take a new city and population from the user
# 6. Update the JSON file


import json

cities = {
    "Nagpur": 2500000,
    "Pune": 7000000,
    "Mumbai": 12000000
}

with open("cities.json", "w") as f:# ye line cities.json file ko write mode me khol rahi hai
    json.dump(cities, f)#

with open("cities.json", "r") as f:
    data = json.load(f)

for city, population in data.items():#ye line data dictionary ke items ko loop kar rahi hai
    print(city, ":", population)

new_city = input("Enter new city: ")# ye line user se new city ka input le rahi hai
new_population = int(input("Enter population: "))# ye line user se new population ka input le rahi hai

data[new_city] = new_population

with open("cities.json", "w") as f:
    json.dump(data, f)

print("JSON file updated successfully")# ye line print kar rahi hai ki JSON file successfully update ho gayi hai


# QUESTION:
# Q4. Create a Python dictionary of 3 cities and their populations.
# Save it to "cities.json"
# Then load the JSON and print each city and its population.
# Ask the user for a new city & its population - update this info in the json file.