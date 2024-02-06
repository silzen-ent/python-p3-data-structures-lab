spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

# D1: Define a function get_names() that takes a list of spicy_foods and returns a list of strings with the names of each spicy food.
def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

print(get_names(spicy_foods))



# D2: Define a function get_spiciest_foods() that takes a list of spicy_foods and returns a list of dictionaries where the heat level of the food is greater than 5.
def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

print(get_spiciest_foods(spicy_foods))



# D3: Define a function print_spicy_foods() that takes a list of spicy_foods and output to the terminal each spicy food in the following format using print(): 
# Buffalo Wings (American) | Heat Level: 🌶🌶🌶.
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: " + "🌶" * food['heat_level'])

print(print_spicy_foods(spicy_foods))



# D4: Define a function get_spicy_food_by_cuisine() that takes a list of spicy_foods and a string representing a cuisine, and returns a single dictionary for the spicy food whose cuisine matches the cuisine being passed to the method.
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
print(get_spicy_food_by_cuisine(spicy_foods, "Thai"))


# D5: Define a function print_spiciest_foods() that takes a list of spicy_foods and outputs to the terminal ONLY the spicy foods that have a heat level greater than 5, in the following format: 
# Buffalo Wings (American) | Heat Level: 🌶🌶🌶.

def print_spiciest_foods(spicy_foods):
#     for food in spicy_foods:
#         if food["heat_level"] > 5:
#             print(f"{food['name']} ({food['cuisine']}) | Heat Level: " + "🌶" * food['heat_level'])

# print(print_spiciest_foods(spicy_foods))

    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)
    
    
# D6: Define a function average_heat_level() that takes a list of spicy_foods and returns an integer representing the average heat level of all the spicy foods in the array. Recall that to derive the average of a collection, you need to calculate the total and divide number of elements in the collection.
def get_average_heat_level(spicy_foods):
    return sum (food["heat_level"] for food in spicy_foods) / len(spicy_foods)

print(get_average_heat_level(spicy_foods))


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

print(create_spicy_food(spicy_foods,
    {
        "name": "Mexican Pizza",
        "cuisine": "Mexican",
        "heat_level": 7,
    }
))