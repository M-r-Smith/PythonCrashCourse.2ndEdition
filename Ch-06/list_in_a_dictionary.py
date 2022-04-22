# IN the following example, two kinds of information are stored for each pizza: a type of crust and a list of toppings.
# The list of toppings is a value associated with the key 'toppings'. To use the items in the list, we give the name of the dictionary and the key 'toppings',
# as we would any value in the dictionary. Instead of returning a single value, we get a list of toppings:
# pizza.py

# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")
    
    
    
# We can nest a list inside of a dictionary anythime we want. If we expand on favorite_languages.py, values, we can make it so people can choose more than one language.
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby,', 'go'],
    'phil': ['python', 'haskell']
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
        


# Inside the dictionary's for loop, we use another for loop to run through the list of languages associated with each person:
# favorite_languages.py
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
        
# Try not to nest so deeply. It becomes difficult to read and there is always a better way.
