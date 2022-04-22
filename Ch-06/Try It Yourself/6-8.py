# 6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind 
# of animal and the owner's name. Store these dictionaries in a list called pets. Next, loop through your list
# and as you do, print everything you know about each pet.
pets = {
    'itachi': {'type': 'dog',
             'owner': 'charles',
             'location': 'japan',
             },
    'peter': {'type': 'spider',
             'owner': 'mary',
             'location': 'new york',
             },
    'bruce': {'type': 'bat',
              'owner': 'alfred',
              'location': 'gotham',
              },
}
for pet_name, pet_info in pets.items():
    print(f"\nPets name: {pet_name}")
    type = f"{pet_info['type']}"
    location = pet_info['location']

    print(f"\tType of pet: {type.title()}")
    print(f"\tlocation: {location.title()}")
